# dbo.integrationstaging_babw_xrates_daily

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.integrationstaging_babw_xrates_daily"]
    dbo_integrationstaging_babw_xrates_daily(["dbo.integrationstaging_babw_xrates_daily"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.integrationstaging_babw_xrates_daily |

## View Code

```sql
; CREATE   VIEW integrationstaging_babw_xrates_daily AS SELECT * FROM LH_Mart.dbo.integrationstaging_babw_xrates_daily;
```

