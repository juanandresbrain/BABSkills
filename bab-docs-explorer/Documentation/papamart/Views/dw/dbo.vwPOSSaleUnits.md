# dbo.vwPOSSaleUnits

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSSaleUnits"]
    jmc_sls_trans_units(["jmc_sls_trans_units"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| jmc_sls_trans_units |

## View Code

```sql
create view vwPOSSaleUnits

as

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
	sum(line_item_Count) UnitCount
from jmc_sls_trans_units 
where business_unit_id='1521'
group by 
	cast(business_date as date) ,
	business_unit_id , 
	right(device_id,3),
	trans_nbr
```

