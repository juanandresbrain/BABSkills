# dbo.vw_FA_tmpItemCoSell

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_FA_tmpItemCoSell"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
create view dbo.vw_FA_tmpItemCoSell --WITH SCHEMABINDING
as

select 	a.transaction_id,
	a.store_key,
	a.date_key,
	a.actual_date,
	t.units,
	p.sku,
	p.product_desc,
	p.department,
	p.subclass
from
(select transaction_id,store_key,date_key,sku,actual_date from dbo.vw_FA_tmpItemCoSell_1) a
join dbo.transaction_detail_facts t (index=idxN_U_transaction_detail_facts_transaction_id)
	on a.transaction_id = t.transaction_id
	and a.store_key = t.store_key
	and a.date_key = t.date_key
join dbo.product_dim p on p.product_key = t.product_key 
where t.transaction_line_seq >=0
```

