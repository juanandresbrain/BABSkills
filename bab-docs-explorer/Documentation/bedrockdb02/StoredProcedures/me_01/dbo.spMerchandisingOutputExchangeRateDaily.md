# dbo.spMerchandisingOutputExchangeRateDaily

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputExchangeRateDaily"]
    dbo_exchange_rate_facts(["dbo.exchange_rate_facts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.exchange_rate_facts |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputExchangeRateDaily]

as

-- =====================================================================================================
-- Name: spMerchandisingOutputExchangeRateDaily
--
-- Description:	Creates tab delimited file that contain daily exchange rate from Papamart which is getting it from ERP D365 Dynamics
------The pipeline file must be formatted as follows:
--------•	Record Type – CC (Currency Conversion Rate)
--------•	Action Type – A (Add)
--------•	Currency Conversion Type – 1 (Purchasing Conversion) or 2 (Pricing Conversion)
--------•	From Currency Code – USD
--------•	To Currency Code – Foreign Currency
--------•	Effective From Date – The 1st day upon which this currency conversion rate becomes effective
--------•	Exchange Rate – The amount of USD required to purchase 1 unit of the foreign currency
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Lee		08/20/2018		Created proc.	
--		Lizzy Timm		09/21/2018		Replaced -f 65001 with -u to make unicode
--		Lizzy Timm		10/02/2018		Changed rate source from fiscal_month_ave_rate to bbw_rate
--		Lizzy Timm						Pointed towards production pipeline
-- =====================================================================================================

set nocount on


if (object_id('tempdb..##exchange_rates') is not null) drop table ##exchange_rates


select	'CC' as "Record Type",
		'A' as "Action Type",
		'1' as "Currency Conversion Type",
		'USD' as "From Currency Code",
		to_currency_code as "To Currency Code",
		convert(varchar,actual_date, 101) as "Effective From Date",
		cast(1/bbw_rate as decimal(10,6)) as "Exchange Rate"
into	##exchange_rates
from	Papamart.dw.dbo.exchange_rate_facts 
where	convert(varchar,actual_date,101) = convert(varchar,getdate(),101)
and		from_currency_code = 'USD'
and		to_currency_code in ('CAD','DKK','EUR', 'GBP', 'CNY')
and		fiscal_month_ave_rate is not null
and		fiscal_month_ave_rate > 0.00000000

union all

select	'CC' as "Record Type",
		'A' as "Action Type",
		'2' as "Currency Conversion Type",
		'USD' as "From Currency Code",
		to_currency_code as "To Currency Code",
		convert(varchar,actual_date, 101) as "Effective From Date",
		cast(1/bbw_rate as decimal(10,6)) as "Exchange Rate"
from	Papamart.dw.dbo.exchange_rate_facts 
where	convert(varchar,actual_date,101) = convert(varchar,getdate(),101)
and		from_currency_code = 'USD'
and		to_currency_code in ('CAD','DKK','EUR', 'GBP', 'CNY')
and		fiscal_month_ave_rate is not null
and		fiscal_month_ave_rate > 0.00000000
order by to_currency_code, 3

begin

	declare @query varchar(1000),
			@date varchar(20),
			@filename varchar(100),
			@filelocation varchar(100),
			@server varchar(20),
			@database varchar(20),
			@sqlcmd varchar(1000),
			@query_text varchar(1000)

	select @query = 'set nocount on select * from ##exchange_rates'
	select @date = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(hh, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar) + cast(datepart(ss, getdate()) as varchar) 
	select @filelocation = '\\pipetestapp01\Company01\Text File to EDM & PROD Import Tables - Imp Master Entities\'
	select @filename = 'EXCHANGE_RATE_' + @date + '.GO'
	select @server = 'bedrockdb02'
	select @database = 'me_01'
	select @sqlcmd = 'sqlcmd -S' + @server + ' -d' + @database + ' -Q' + '"' + @query + '"' + ' -o' + '"' + @filelocation + @filename + '"' + ' -s"	" -W -h-1 -u ' 
	-- (-W removes extra blank line)
	-- (-h-1 removes headers, both coulmn names and dashed lines) 
	-- (-u sets to unicode (for chinese characters))
	exec master..xp_cmdshell @sqlcmd

end
```

