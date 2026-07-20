# dbo.storecompdetail_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.storecompdetail_dim"]
    dbo_storecompdetail_dim(["dbo.storecompdetail_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.storecompdetail_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[storecompdetail_dim] AS     SELECT [store_key], [date_key], [isCompTY], [isCompNY], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID], [isShopperTrak], [isShopperTrakCompTY], [isShopperTrakCompNY], [isSOTF], [ShopperTrakStartHour], [ShopperTrakEndHour]     FROM [dbo].[storecompdetail_dim]
```

