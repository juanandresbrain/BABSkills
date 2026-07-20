# dbo.store_shoppertrak_open_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.store_shoppertrak_open_dim"]
    dbo_store_shoppertrak_open_dim(["dbo.store_shoppertrak_open_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_shoppertrak_open_dim |

## View Code

```sql
CREATE   VIEW [dbo].[store_shoppertrak_open_dim] AS SELECT recID, store_key, date_key_from, date_key_thru, hour_day_start, hour_day_end, INS_DT, UPDT_DT, ETL_LOG_ID, ETL_EVNT_ID FROM LH_Mart.dbo.store_shoppertrak_open_dim;
```

