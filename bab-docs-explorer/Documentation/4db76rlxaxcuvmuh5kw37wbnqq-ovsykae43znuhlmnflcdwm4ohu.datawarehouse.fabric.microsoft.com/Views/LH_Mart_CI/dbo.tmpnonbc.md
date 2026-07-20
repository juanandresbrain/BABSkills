# dbo.tmpnonbc

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpnonbc"]
    dbo_tmpnonbc(["dbo.tmpnonbc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpnonbc |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpnonbc] AS     SELECT [country] COLLATE Latin1_General_CI_AS AS [country], [PurchaseChannel] COLLATE Latin1_General_CI_AS AS [PurchaseChannel], [transaction_ID], [TransactionDate], [KeyStory] COLLATE Latin1_General_CI_AS AS [KeyStory], [GaapUnits], [GaapSales], [isWeb], [isRetail], [2ndPurchase] COLLATE Latin1_General_CI_AS AS [2ndPurchase], [3rdPurchase] COLLATE Latin1_General_CI_AS AS [3rdPurchase], [4thPurchase] COLLATE Latin1_General_CI_AS AS [4thPurchase]     FROM [dbo].[tmpnonbc]
```

