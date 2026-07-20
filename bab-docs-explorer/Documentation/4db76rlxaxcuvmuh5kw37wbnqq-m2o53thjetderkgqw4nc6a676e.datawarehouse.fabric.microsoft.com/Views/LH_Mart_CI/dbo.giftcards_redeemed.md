# dbo.giftcards_redeemed

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcards_redeemed"]
    dbo_giftcards_redeemed(["dbo.giftcards_redeemed"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcards_redeemed |

## View Code

```sql
;

CREATE VIEW dbo.giftcards_redeemed AS SELECT recID, store_key, transaction_id, date_key, redemption_amount, discount_amount, giftcard_no COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS giftcard_no, currency_key, MID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS MID, daysSinceLastActivation, lift_amount, activation_discount_amount, source COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS source, VLVerified FROM LH_Mart.dbo.giftcards_redeemed;;
```

