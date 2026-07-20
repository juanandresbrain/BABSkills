# dbo.emailfact2024

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailfact2024"]
    dbo_emailfact2024(["dbo.emailfact2024"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailfact2024 |

## View Code

```sql
; CREATE   VIEW emailfact2024 AS SELECT * FROM LH_Mart.dbo.emailfact2024;
```

