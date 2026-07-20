# dbo.shoppertrackfact

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.shoppertrackfact"]
    dbo_shoppertrackfact(["dbo.shoppertrackfact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.shoppertrackfact |

## View Code

```sql
;

CREATE VIEW dbo.shoppertrackfact AS SELECT ShopperTrackFactKey, ShopperTrakOrgId, StoreKey, DateKey, TimeKey, Enters, Exits, DataIndicatorName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS DataIndicatorName, InsertDate, UpdateDate FROM LH_Mart.dbo.shoppertrackfact;
```

