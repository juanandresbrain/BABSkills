# dbo.franchiseetransactiongiftcard

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactiongiftcard"]
    dbo_franchiseetransactiongiftcard(["dbo.franchiseetransactiongiftcard"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactiongiftcard |

## View Code

```sql
;

CREATE VIEW dbo.franchiseetransactiongiftcard AS SELECT FranchiseeTransactionHeaderID, FranchiseeTransactionGiftCardID, Units, GiftCardAmount, Discount, InsertDate, BatchID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BatchID, UpdateDate FROM LH_Mart.dbo.franchiseetransactiongiftcard;;
```

