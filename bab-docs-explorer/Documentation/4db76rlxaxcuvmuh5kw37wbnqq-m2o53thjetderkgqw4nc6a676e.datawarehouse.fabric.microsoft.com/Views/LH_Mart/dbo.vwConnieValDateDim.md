# dbo.vwConnieValDateDim

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwConnieValDateDim"]
    date_dim(["date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |

## View Code

```sql
create view vwConnieValDateDim
as
select 
	count(*) RowKount,
	cast(min(actual_date) as date) MinDate,
	cast(max(actual_date) as date) MaxDate
from date_dim
```

