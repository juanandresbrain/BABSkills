# dbo.storecomp_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.storecomp_dim"]
    dbo_storecomp_dim(["dbo.storecomp_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.storecomp_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[storecomp_dim] AS     SELECT [recID], [store_key], [date_key_from], [date_key_thru], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID]     FROM [dbo].[storecomp_dim]
```

