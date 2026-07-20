# dbo.giftcard_mid

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[giftcard_mid] AS     SELECT [MID] COLLATE Latin1_General_CI_AS AS [MID], [description] COLLATE Latin1_General_CI_AS AS [description], [display] COLLATE Latin1_General_CI_AS AS [display], [localCurrencyCode] COLLATE Latin1_General_CI_AS AS [localCurrencyCode], [isCorporate]     FROM [dbo].[giftcard_mid]
```

