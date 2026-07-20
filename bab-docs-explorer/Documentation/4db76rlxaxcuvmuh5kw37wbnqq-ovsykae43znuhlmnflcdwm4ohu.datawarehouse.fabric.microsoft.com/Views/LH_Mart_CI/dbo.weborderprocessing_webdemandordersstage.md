# dbo.weborderprocessing_webdemandordersstage

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.weborderprocessing_webdemandordersstage"]
    dbo_weborderprocessing_webdemandordersstage(["dbo.weborderprocessing_webdemandordersstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.weborderprocessing_webdemandordersstage |

## View Code

```sql
; CREATE   VIEW weborderprocessing_webdemandordersstage AS SELECT * FROM LH_Mart.dbo.weborderprocessing_webdemandordersstage;
```

