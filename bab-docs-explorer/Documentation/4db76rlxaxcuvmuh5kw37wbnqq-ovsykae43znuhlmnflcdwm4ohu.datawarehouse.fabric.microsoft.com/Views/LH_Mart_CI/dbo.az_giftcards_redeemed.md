# dbo.az_giftcards_redeemed

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.az_giftcards_redeemed"]
    dbo_az_giftcards_redeemed(["dbo.az_giftcards_redeemed"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.az_giftcards_redeemed |

## View Code

```sql
; CREATE   VIEW [dbo].[az_giftcards_redeemed] AS    SELECT [store_key]       ,[transaction_id] COLLATE Latin1_General_CI_AS AS [transaction_id]       ,[date_key]       ,[redemption_amount]       ,[discount_amount]       ,[giftcard_no] COLLATE Latin1_General_CI_AS AS [giftcard_no]       ,[currency_key]       ,[MID] COLLATE Latin1_General_CI_AS AS [MID]       ,[daysSinceLastActivation]       ,[lift_amount]       ,[activation_discount_amount]       ,[source] COLLATE Latin1_General_CI_AS AS [source]       ,[VLVerified]   FROM LH_Mart.[dbo].[az_giftcards_redeemed]
```

