# dbo.emailfact2023

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailfact2023"]
    dbo_emailfact2023(["dbo.emailfact2023"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailfact2023 |

## View Code

```sql
; CREATE   VIEW emailfact2023 AS SELECT * FROM LH_Mart.dbo.emailfact2023;
```

