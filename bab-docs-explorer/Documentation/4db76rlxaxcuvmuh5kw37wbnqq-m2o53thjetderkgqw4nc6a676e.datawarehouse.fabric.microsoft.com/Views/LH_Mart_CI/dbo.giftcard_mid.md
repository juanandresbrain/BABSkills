# dbo.giftcard_mid

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_mid"]
    dbo_giftcard_mid(["dbo.giftcard_mid"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_mid |

## View Code

```sql
;

CREATE VIEW dbo.giftcard_mid AS SELECT MID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS MID, description COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS description, display COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS display, localCurrencyCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS localCurrencyCode, isCorporate FROM LH_Mart.dbo.giftcard_mid;
```

