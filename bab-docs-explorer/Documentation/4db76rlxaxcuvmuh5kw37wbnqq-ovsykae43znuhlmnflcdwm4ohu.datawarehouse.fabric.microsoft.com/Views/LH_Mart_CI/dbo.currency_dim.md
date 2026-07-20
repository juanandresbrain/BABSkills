# dbo.currency_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.currency_dim"]
    dbo_currency_dim(["dbo.currency_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.currency_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[currency_dim] AS     SELECT [currency_key], [currency_code] COLLATE Latin1_General_CI_AS AS [currency_code], [currency_desc] COLLATE Latin1_General_CI_AS AS [currency_desc], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID]     FROM [dbo].[currency_dim]
```

