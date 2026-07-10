# dbo.vwPOS_JMC_SLS

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOS_JMC_SLS"]
    JMC_sls_trans(["JMC_sls_trans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| JMC_sls_trans |

## View Code

```sql
CREATE view [dbo].[vwPOS_JMC_SLS]

as

select DISTINCT
	device_id,
	cast(business_date as date) as BusinessDate,
	--cast (create_time as date) as BusinessDate,
	case 
		when left(business_unit_id,1)='2'
			then business_unit_id
		else cast(right((cast('0000' as varchar) + cast(right(business_unit_id,3) as varchar)),4) as int)
	end as StoreID,
	cast(right(device_id,3) as int) as RegisterNumber,
	trans_nbr,
	total,
	trans_type,
	trans_status,
	loyalty_card_number,
	customer_id,
	username as Employee
from dw..JMC_sls_trans
where 1=1
and isnumeric(right(device_id,2))=1
and 
	(
		cast(business_date as date) >='2023-04-12' --first day of new POs -- 
		--and datediff(dd, business_date, getdate())<=7
	)
```

