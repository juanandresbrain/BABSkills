# dbo.weborderprocessing_webdemandorderitemsstage

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.weborderprocessing_webdemandorderitemsstage"]
    dbo_weborderprocessing_webdemandorderitemsstage(["dbo.weborderprocessing_webdemandorderitemsstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.weborderprocessing_webdemandorderitemsstage |

## View Code

```sql
; CREATE   VIEW weborderprocessing_webdemandorderitemsstage AS SELECT * FROM LH_Mart.dbo.weborderprocessing_webdemandorderitemsstage;
```

