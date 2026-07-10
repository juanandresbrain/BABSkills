# dbo.vwPOSSalesTotalByDayByTransaction_BAK20230814

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSSalesTotalByDayByTransaction_BAK20230814"]
    JMC_sls_trans(["JMC_sls_trans"]) --> VIEW
    jmc_sls_trans_units(["jmc_sls_trans_units"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| JMC_sls_trans |
| jmc_sls_trans_units |

## View Code

```sql
create view [dbo].[vwPOSSalesTotalByDayByTransaction_BAK20230814]


as

with 
Units as
	(
		select 
			cast(business_date as date) BusinessDate,
			business_unit_id as StoreNumber,
			case 
				when left(business_unit_id,1)='2 '
					then business_unit_id
				else cast(right((cast('0000' as varchar) + cast(right(business_unit_id,3) as varchar)),4) as int)
			end as StoreID,
			cast(right(device_id,3) as int) as RegisterNumber,
			trans_nbr TransactionNumber,
			sum(line_item_Count) Units
		from jmc_sls_trans_units with (nolock)
		group by 
			cast(business_date as date) ,
			business_unit_id , 
			right(device_id,3),
			trans_nbr
	),
Sales as
	(
		select 
			cast(s.business_date as date) as BusinessDate,
			case 
				when left(s.business_unit_id,1)='2 '
					then s.business_unit_id
				else cast(right((cast('0000' as varchar) + cast(right(s.business_unit_id,3) as varchar)),4) as int)
			end as StoreID,
			cast(right(s.device_id,2) as int) as RegisterNumber,
			s.trans_nbr TransactionNumber,
			sum(s.total) Sales
		from JMC_sls_trans s with (nolock) 
		where 
			(
				cast(business_date as date) >='2023-04-12' --first day of new POs
				--and datediff(dd, business_date, getdate())<=7
			)
		and 
			case 
				when left(s.business_unit_id,1)='2 '
					then s.business_unit_id
				else cast(right((cast('0000' as varchar) + cast(right(s.business_unit_id,3) as varchar)),4) as int)
			end not in ('13', '2013') ---excluding endless aisle??
		group by
			cast(s.business_date as date),
			business_unit_id,
			s.device_id,
			s.trans_nbr
	)
select 
	s.StoreID,
	s.BusinessDate,
	s.RegisterNumber,
	s.TransactionNumber,
	sum(s.Sales) Sales,
	sum(u.Units) Units
from Sales s
join Units u on 
	s.BusinessDate=u.BusinessDate
	and s.StoreID=u.StoreID
	and s.RegisterNumber=u.RegisterNumber
	and s.TransactionNumber=u.TransactionNumber
group by 
	s.StoreID,
	s.BusinessDate,
	s.RegisterNumber,
	s.TransactionNumber
```

