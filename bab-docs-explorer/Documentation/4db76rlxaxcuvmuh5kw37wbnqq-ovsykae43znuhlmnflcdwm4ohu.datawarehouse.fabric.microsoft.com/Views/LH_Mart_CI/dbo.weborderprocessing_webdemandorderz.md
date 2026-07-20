# dbo.weborderprocessing_webdemandorderz

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.weborderprocessing_webdemandorderz"]
    dbo_weborderprocessing_webdemandorderz(["dbo.weborderprocessing_webdemandorderz"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.weborderprocessing_webdemandorderz |

## View Code

```sql
; CREATE   VIEW weborderprocessing_webdemandorderz AS SELECT * FROM LH_Mart.dbo.weborderprocessing_webdemandorderz;
```

