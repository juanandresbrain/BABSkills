# dbo.tmpvlmergesource

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpvlmergesource"]
    dbo_tmpvlmergesource(["dbo.tmpvlmergesource"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpvlmergesource |

## View Code

```sql
; CREATE   VIEW tmpvlmergesource AS SELECT * FROM LH_Staging.dbo.tmpvlmergesource;
```

