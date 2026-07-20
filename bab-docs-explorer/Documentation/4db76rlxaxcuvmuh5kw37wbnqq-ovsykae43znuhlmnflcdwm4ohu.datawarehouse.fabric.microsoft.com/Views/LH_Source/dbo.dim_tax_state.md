# dbo.dim_tax_state

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_tax_state"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE   VIEW dbo.dim_tax_state AS /* STUB — returns zero rows until upstream lookup replication lands.    Schema is preserved so downstream reports can compile and reference. */ SELECT     CAST(NULL AS int)         AS authority_id,     CAST(NULL AS varchar(2))  AS state_code,     CAST(NULL AS varchar(50)) AS state_name,     CAST(NULL AS varchar(2))  AS country_code,     CAST(NULL AS bit)         AS is_taxable_state WHERE 1 = 0;
```

