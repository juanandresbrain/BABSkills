# WMS.spPrintInventoryAdjustments

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spPrintInventoryAdjustments"]
    WMS_InventoryAdjustments(["WMS.InventoryAdjustments"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.InventoryAdjustments |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spPrintInventoryAdjustments]
@FilePath varchar(1000)

as
----------------------------------------------------------------------------------------------------------------------------
--	Dan Tweedie	2019-07-17	Created proc to generate pipeline file for Merch to post inventory adjustments from Dynamics
----------------------------------------------------------------------------------------------------------------------------

set nocount on 

declare @Count int

select @Count = count(*) from WMS.InventoryAdjustments where Warehouse='9980' and TransmittedToAptos is NULL

if @Count > 0


begin
		declare 
			@query varchar(1000),
			@file_name varchar(100),
			@file_location varchar(100),
			@osql varchar(1000),
			@username varchar(52),
			@password varchar(52),
			@server varchar(52),
			@database varchar(52)

		set @query = 'exec IntegrationStaging.WMS.spSelectInventoryAdjustments'
		set @file_location = @FilePath 
		set @file_name = 'STSIMSA.WM.' + convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())) + convert(varchar, datepart(ss, getdate())) + '.GO'
		--set @server = 'wmdb01'
		--set @database = 'wmprod'
		--set @osql = 'osql -E ' + ' -S' + @server + ' -d' + @database + ' -Q' + '"' + @query + '"' + ' -o' + '"' + @file_location + @file_name + '"' + ' -w1000'
		set @osql = 'osql -E ' + ' -Q' + '"' + @query + '"' + ' -o' + '"' + @file_location + @file_name + '"' + ' -w1000'
		exec master..xp_cmdshell @osql
end
```

