# dbo.franchtransimportedpostperiod

**Database:** LH_Staging_CI  
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
CREATE   VIEW [dbo].[franchtransimportedpostperiod]
AS
    SELECT [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [TransactionDate], [ImportDate], [PreviousPeriodCutOffDate], [TransactionPayment], [GrossSales], [GiftCardAmount], [OriginalGrossSales], [OriginalGiftCardAmount], [OriginalInsertDate], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID]
    FROM LH_Staging.[dbo].[franchtransimportedpostperiod]
```

