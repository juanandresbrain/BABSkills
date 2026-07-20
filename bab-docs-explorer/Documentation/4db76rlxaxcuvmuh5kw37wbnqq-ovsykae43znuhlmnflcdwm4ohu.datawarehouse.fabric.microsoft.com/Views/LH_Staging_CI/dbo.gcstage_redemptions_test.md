# dbo.gcstage_redemptions_test

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.gcstage_redemptions_test"]
    dbo_gcstage_redemptions_test(["dbo.gcstage_redemptions_test"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.gcstage_redemptions_test |

## View Code

```sql
; CREATE   VIEW [dbo].[gcstage_redemptions_test] AS SELECT [recID], [store_key], [transaction_id], [date_key], [redemption_amount], [discount_amount], [giftcard_no] COLLATE Latin1_General_CI_AS AS [giftcard_no], [currency_key], [MID] COLLATE Latin1_General_CI_AS AS [MID], [daysSinceLastActivation], [lift_amount], [activation_discount_amount], [source] COLLATE Latin1_General_CI_AS AS [source], [VLVerified], [register_no], [transaction_no], [postedPhase], [vlLineID] FROM [dbo].[gcstage_redemptions_test]
```

