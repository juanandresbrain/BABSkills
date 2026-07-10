# dbo.vwPOSActiveJumpMindStores

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSActiveJumpMindStores"]
    JMC_sls_trans(["JMC_sls_trans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| JMC_sls_trans |

## View Code

```sql
CREATE view [dbo].[vwPOSActiveJumpMindStores] 


as



select 
	case 
			when left(business_unit_id,1)='2 '
				then business_unit_id
			else cast(right((cast('0000' as varchar) + cast(right(business_unit_id,3) as varchar)),4) as int)
	end as StoreID,
	min(business_date) FirstJumpMindDate,
	business_unit_id
from dw..JMC_sls_trans with (nolock)
where 
	case 
			when left(business_unit_id,1)='2 '
				then business_unit_id
			else cast(right((cast('0000' as varchar) + cast(right(business_unit_id,3) as varchar)),4) as int)
	end not in ('0013','2013')

	--and not ( ---trying to exclude 119 from this list because they were JM but switched back to Aptos
	--		case 
	--				when left(business_unit_id,1)='2 '
	--					then business_unit_id
	--				else cast(right((cast('0000' as varchar) + cast(right(business_unit_id,3) as varchar)),4) as int)
	--		end='119'
	--		and cast(getdate() as date) < '2024-01-15'
	--	)

group by 
	case 
			when left(business_unit_id,1)='2 '
				then business_unit_id
			else cast(right((cast('0000' as varchar) + cast(right(business_unit_id,3) as varchar)),4) as int)
	end,
	business_unit_id
having max(cast(business_date as date)) >'2023-04-15'--- first jump mind store went live around 4/10
```

