# dbo.tmpshoppertrack

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpshoppertrack"]
    dbo_tmpshoppertrack(["dbo.tmpshoppertrack"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpshoppertrack |

## View Code

```sql
; CREATE   VIEW tmpshoppertrack AS SELECT * FROM LH_Mart.dbo.tmpshoppertrack;
```

