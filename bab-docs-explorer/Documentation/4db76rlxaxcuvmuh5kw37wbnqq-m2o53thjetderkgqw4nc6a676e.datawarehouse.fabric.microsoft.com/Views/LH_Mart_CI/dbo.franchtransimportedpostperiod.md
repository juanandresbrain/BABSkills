# dbo.franchtransimportedpostperiod

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchtransimportedpostperiod"]
    dbo_franchtransimportedpostperiod(["dbo.franchtransimportedpostperiod"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchtransimportedpostperiod |

## View Code

```sql
;

CREATE VIEW dbo.franchtransimportedpostperiod AS SELECT Franchisee COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Franchisee, TransactionID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS TransactionID, TransactionDate, ImportDate, PreviousPeriodCutOffDate, TransactionPayment, GrossSales, GiftCardAmount, OriginalGrossSales, OriginalGiftCardAmount, OriginalInsertDate, InsertDate, UpdateDate, StoreID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS StoreID FROM LH_Mart.dbo.franchtransimportedpostperiod;;
```

