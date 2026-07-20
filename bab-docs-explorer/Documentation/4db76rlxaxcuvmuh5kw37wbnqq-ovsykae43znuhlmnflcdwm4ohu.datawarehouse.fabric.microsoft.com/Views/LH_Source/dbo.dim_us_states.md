# dbo.dim_us_states

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_us_states"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE   VIEW dbo.dim_us_states AS /* STUB — returns zero rows until upstream replication lands. */ SELECT     CAST(NULL AS char(2))      AS state_code,     CAST(NULL AS varchar(50))  AS state_name,     CAST(NULL AS varchar(20))  AS region,     CAST(NULL AS bit)          AS is_us_territory,     CAST(NULL AS bit)          AS is_active_for_es WHERE 1 = 0;
```

