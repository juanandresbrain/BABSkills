# dbo.vw_FA_tmpItemCoSell_Single

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_FA_tmpItemCoSell_Single"]
    dbo_vw_FA_tmpItemCoSell(["dbo.vw_FA_tmpItemCoSell"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vw_FA_tmpItemCoSell |

## View Code

```sql
create view dbo.vw_FA_tmpItemCoSell_Single --WITH SCHEMABINDING
as


select  a.transaction_id,
	a.store_key,
	a.date_key
--into dbo.#tmpItemCoSell_Single
from dbo.vw_FA_tmpItemCoSell a 
where a.department IN ('unstuffed','dolls','Animals','Uk-Unstuffed')  --('dolls')
or (a.department = 'sports licensing' and a.subclass = 'skins') 
 group by a.transaction_id,
	 a.store_key,
	 a.date_key
having sum(a.units) = 1
```

