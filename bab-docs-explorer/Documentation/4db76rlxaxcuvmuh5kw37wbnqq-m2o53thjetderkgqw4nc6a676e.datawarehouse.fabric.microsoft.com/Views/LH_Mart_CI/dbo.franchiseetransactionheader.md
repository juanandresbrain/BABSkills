# dbo.franchiseetransactionheader

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionheader"]
    dbo_franchiseetransactionheader(["dbo.franchiseetransactionheader"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionheader |

## View Code

```sql
;

CREATE VIEW dbo.franchiseetransactionheader AS SELECT FranchiseeTransactionHeaderID, Franchisee COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Franchisee, TransactionID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS TransactionID, TransactionDateTime, StoreID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS StoreID, InsertDate, BatchID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS BatchID, store_key, date_key, time_key, UpdateDate FROM LH_Mart.dbo.franchiseetransactionheader;
```

