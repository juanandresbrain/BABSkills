# dbo.discountdestage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.discountdestage"]
    dbo_discountdestage(["dbo.discountdestage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.discountdestage |

## View Code

```sql
;
CREATE   VIEW [dbo].[discountdestage]
AS
    SELECT [Category] COLLATE Latin1_General_CI_AS AS [Category], [certificateNumber] COLLATE Latin1_General_CI_AS AS [certificateNumber], [coupon_desc] COLLATE Latin1_General_CI_AS AS [coupon_desc], [couponNumber] COLLATE Latin1_General_CI_AS AS [couponNumber], [DiscountAmountPerLine], [DiscountTransactionLineNumber], [event_name] COLLATE Latin1_General_CI_AS AS [event_name], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [UnitGrossAmount], [customerNumber] COLLATE Latin1_General_CI_AS AS [customerNumber], [TransactionDate]
    FROM LH_Staging.[dbo].[discountdestage]
```

