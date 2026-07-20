# dbo.store_sotf_open_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.store_sotf_open_dim"]
    dbo_store_sotf_open_dim(["dbo.store_sotf_open_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_sotf_open_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[store_sotf_open_dim] AS     SELECT [recID], [store_key], [date_key_from], [date_key_thru], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID]     FROM [dbo].[store_sotf_open_dim]
```

