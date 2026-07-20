# dbo.crmcustomerfrequencyrecencymonetary

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmcustomerfrequencyrecencymonetary"]
    dbo_crmcustomerfrequencyrecencymonetary(["dbo.crmcustomerfrequencyrecencymonetary"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmcustomerfrequencyrecencymonetary |

## View Code

```sql
;

CREATE VIEW dbo.crmcustomerfrequencyrecencymonetary AS SELECT CustomerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CustomerNumber, LifetimeTransactionCount, LifetimeRecencyCount, LifetimeSalesTotal, FirstStoreConcept COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FirstStoreConcept, FirstTransactionDate, Frequency3M, Recency3M, Sales3M, minDaysBetween3M, maxDaysBetween3M, DaysBetween3M, Frequency6M, Recency6M, Sales6M, minDaysBetween6M, maxDaysBetween6M, DaysBetween6M, Frequency12M, Recency12M, Sales12M, minDaysBetween12M, maxDaysBetween12M, DaysBetween12M, Frequency18M, Recency18M, Sales18M, minDaysBetween18M, maxDaysBetween18M, DaysBetween18M, Frequency24M, Recency24M, Sales24M, minDaysBetween24M, maxDaysBetween24M, DaysBetween24M, InsertDate, UpdateDate, Frequency1M, Recency1M, Sales1M, minDaysBetween1M, maxDaysBetween1M, DaysBetween1M, LastTransactionDate, LastTransactionStore COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS LastTransactionStore, Frequency36M, Recency36M, Sales36M, minDaysBetween36M, maxDaysBetween36M, DaysBetween36M FROM LH_Mart.dbo.crmcustomerfrequencyrecencymonetary;;
```

