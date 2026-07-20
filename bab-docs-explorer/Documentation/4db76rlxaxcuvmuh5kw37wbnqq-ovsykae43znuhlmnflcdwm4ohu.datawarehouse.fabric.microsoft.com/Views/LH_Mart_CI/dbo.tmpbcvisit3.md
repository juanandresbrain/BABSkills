# dbo.tmpbcvisit3

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpbcvisit3"]
    dbo_tmpbcvisit3(["dbo.tmpbcvisit3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpbcvisit3 |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpbcvisit3] AS     SELECT [Country] COLLATE Latin1_General_CI_AS AS [Country], [PurchaseChannel] COLLATE Latin1_General_CI_AS AS [PurchaseChannel], [customerNumber] COLLATE Latin1_General_CI_AS AS [customerNumber], [transactionID], [TransactionDate], [keyStory] COLLATE Latin1_General_CI_AS AS [keyStory], [KeyRankPerTransaction], [KeyRankPerSequenceNewVOldCustomers], [KeyRankPerSequenceGlobal], [KeyStorySales], [KeyStoryUnits], [CustomerFirstTransactionDate], [isFreshCustomer], [isFirstPurchaseChannel], [isFirstPurchase], [isNewCustomer], [isRepeatCustomer], [isWeb], [isRetail], [GaapSalesTranTotal], [KeyStoryPctToTotal] COLLATE Latin1_General_CI_AS AS [KeyStoryPctToTotal], [LifetimeTransactionSequence], [LifetimeVisitSequence], [ParentTransactionID], [ChildTransactionID], [isTopKeyStoryPerTransaction], [isTopKeyStoryNewOrOldGlobal], [isTopKeyStoryGlobal], [hasCountYourCandles], [hasBirthdayGift], [hasHalfBirthday], [hasWinback], [hasOther], [TransactionKey] COLLATE Latin1_General_CI_AS AS [TransactionKey], [firstPurchaseFlag] COLLATE Latin1_General_CI_AS AS [firstPurchaseFlag]     FROM [dbo].[tmpbcvisit3]
```

