# dbo.salesplangaap_stage

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.salesplangaap_stage"]
    dbo_salesplangaap_stage(["dbo.salesplangaap_stage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.salesplangaap_stage |

## View Code

```sql
; CREATE   VIEW [dbo].[salesplangaap_stage] AS     SELECT [store], [actual_date], [currency] COLLATE Latin1_General_CI_AS AS [currency], [sales_plan]     FROM [dbo].[salesplangaap_stage]
```

