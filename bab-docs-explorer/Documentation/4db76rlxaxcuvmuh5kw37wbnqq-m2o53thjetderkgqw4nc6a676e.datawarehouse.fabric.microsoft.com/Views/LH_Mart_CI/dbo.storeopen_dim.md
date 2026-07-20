# dbo.storeopen_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.storeopen_dim"]
    dbo_storeopen_dim(["dbo.storeopen_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.storeopen_dim |

## View Code

```sql
CREATE   VIEW [dbo].[storeopen_dim] AS SELECT recID, store_key, date_key_from, date_key_thru, MDSE_WGHT, INS_DT, UPDT_DT, ETL_LOG_ID, ETL_EVNT_ID FROM LH_Mart.dbo.storeopen_dim;
```

