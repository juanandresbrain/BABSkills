# dbo.webdemandordersuk

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webdemandordersuk"]
    dbo_webdemandordersuk(["dbo.webdemandordersuk"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webdemandordersuk |

## View Code

```sql
; CREATE   VIEW webdemandordersuk AS SELECT * FROM LH_Mart.dbo.webdemandordersuk;
```

