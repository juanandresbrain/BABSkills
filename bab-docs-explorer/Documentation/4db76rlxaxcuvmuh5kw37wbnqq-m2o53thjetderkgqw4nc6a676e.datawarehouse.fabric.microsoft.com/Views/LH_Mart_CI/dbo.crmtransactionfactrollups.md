# dbo.crmtransactionfactrollups

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmtransactionfactrollups"]
    dbo_crmtransactionfactrollups(["dbo.crmtransactionfactrollups"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmtransactionfactrollups |

## View Code

```sql
;

CREATE VIEW dbo.crmtransactionfactrollups AS SELECT TransactionID, CustomerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS CustomerNumber, TransactionYear, TransacionMonth, TransactionDate, StoreConcept COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS StoreConcept, LifetimeVisitNumber, KeyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS KeyStory, ConsumerGroup COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS ConsumerGroup, Department COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Department, LicensedOrNot, Units, Sales, InsertDate, UpdateDate, StoreNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS StoreNumber, Country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Country, sku COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS sku FROM LH_Mart.dbo.crmtransactionfactrollups;
```

