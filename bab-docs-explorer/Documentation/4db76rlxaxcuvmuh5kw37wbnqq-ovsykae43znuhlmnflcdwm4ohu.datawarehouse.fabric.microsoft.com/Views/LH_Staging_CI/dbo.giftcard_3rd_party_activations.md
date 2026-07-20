# dbo.giftcard_3rd_party_activations

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_3rd_party_activations"]
    dbo_giftcard_3rd_party_activations(["dbo.giftcard_3rd_party_activations"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_3rd_party_activations |

## View Code

```sql
; CREATE   VIEW [dbo].[giftcard_3rd_party_activations] AS SELECT [SoldThru] COLLATE Latin1_General_CI_AS AS [SoldThru], [Promo] COLLATE Latin1_General_CI_AS AS [Promo], [Date], [Qty], [StartCardNumber] COLLATE Latin1_General_CI_AS AS [StartCardNumber], [EndCardNumber] COLLATE Latin1_General_CI_AS AS [EndCardNumber], [#_Cards] FROM [dbo].[giftcard_3rd_party_activations]
```

