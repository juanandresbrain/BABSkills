# dbo.webdemandordersus

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webdemandordersus"]
    dbo_webdemandordersus(["dbo.webdemandordersus"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webdemandordersus |

## View Code

```sql
; CREATE   VIEW webdemandordersus AS SELECT * FROM LH_Mart.dbo.webdemandordersus;
```

