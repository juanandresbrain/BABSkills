# dbo.webtransactions

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webtransactions"]
    dbo_webtransactions(["dbo.webtransactions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webtransactions |

## View Code

```sql
;

CREATE VIEW dbo.webtransactions AS SELECT TransactionID, TransactionNum COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS TransactionNum, TransactionDateTime, TaxAmount, TaxJurisdiction COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS TaxJurisdiction, InsertDate, UpdateDate FROM LH_Mart.dbo.webtransactions;;
```

