# dbo.giftcards_activated

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcards_activated"]
    dbo_giftcards_activated(["dbo.giftcards_activated"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcards_activated |

## View Code

```sql
;

CREATE VIEW dbo.giftcards_activated AS SELECT recID, store_key, transaction_id, date_key, activated_amount, discount_amount, giftcard_no COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS giftcard_no, currency_key, MID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS MID, Source COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Source, VLVerified FROM LH_Mart.dbo.giftcards_activated;
```

