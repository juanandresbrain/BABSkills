# dbo.tmpbcvisit1

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpbcvisit1"]
    dbo_tmpbcvisit1(["dbo.tmpbcvisit1"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpbcvisit1 |

## View Code

```sql
;

CREATE VIEW dbo.tmpbcvisit1 AS SELECT Country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Country, PurchaseChannel COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PurchaseChannel, customerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS customerNumber, transactionID, TransactionDate, keyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS keyStory, KeyRankPerTransaction, KeyRankPerSequenceNewVOldCustomers, KeyRankPerSequenceGlobal, KeyStorySales, KeyStoryUnits, CustomerFirstTransactionDate, isFreshCustomer, isFirstPurchaseChannel, isFirstPurchase, isNewCustomer, isRepeatCustomer, isWeb, isRetail, GaapSalesTranTotal, KeyStoryPctToTotal COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS KeyStoryPctToTotal, LifetimeTransactionSequence, LifetimeVisitSequence, ParentTransactionID, ChildTransactionID, isTopKeyStoryPerTransaction, isTopKeyStoryNewOrOldGlobal, isTopKeyStoryGlobal, hasCountYourCandles, hasBirthdayGift, hasHalfBirthday, hasWinback, hasOther, TransactionKey COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS TransactionKey, firstPurchaseFlag COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS firstPurchaseFlag FROM LH_Mart.dbo.tmpbcvisit1;;
```

