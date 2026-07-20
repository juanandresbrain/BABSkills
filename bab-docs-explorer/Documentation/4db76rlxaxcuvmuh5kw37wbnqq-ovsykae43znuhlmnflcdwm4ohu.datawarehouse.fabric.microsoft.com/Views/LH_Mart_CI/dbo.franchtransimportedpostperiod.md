# dbo.franchtransimportedpostperiod

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[franchtransimportedpostperiod] AS     SELECT [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [TransactionDate], [ImportDate], [PreviousPeriodCutOffDate], [TransactionPayment], [GrossSales], [GiftCardAmount], [OriginalGrossSales], [OriginalGiftCardAmount], [OriginalInsertDate], [InsertDate], [UpdateDate], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID]     FROM [dbo].[franchtransimportedpostperiod]
```

