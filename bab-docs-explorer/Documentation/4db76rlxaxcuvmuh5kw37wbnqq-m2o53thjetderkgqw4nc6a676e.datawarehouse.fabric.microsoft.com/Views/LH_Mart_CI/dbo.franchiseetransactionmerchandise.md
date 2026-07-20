# dbo.franchiseetransactionmerchandise

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionmerchandise"]
    dbo_franchiseetransactionmerchandise(["dbo.franchiseetransactionmerchandise"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionmerchandise |

## View Code

```sql
;

CREATE VIEW dbo.franchiseetransactionmerchandise AS SELECT FranchiseeTransactionHeaderID, FranchiseeTransactionMerchandiseID, Style COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Style, Units, Cost, GrossSales, Discount, VAT, InsertDate, BatchID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS BatchID, product_key, updateDate, OriginalDiscount FROM LH_Mart.dbo.franchiseetransactionmerchandise;
```

