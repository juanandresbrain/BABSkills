# dbo.crmtranfact36mstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmtranfact36mstage"]
    dbo_crmtranfact36mstage(["dbo.crmtranfact36mstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmtranfact36mstage |

## View Code

```sql
;
CREATE   VIEW [dbo].[crmtranfact36mstage]
AS
    SELECT [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [MonthRange] COLLATE Latin1_General_CI_AS AS [MonthRange], [TransactionCount], [RecencyCount], [SalesTotal], [minDaysBetween], [maxDaysBetween], [DaysBetween]
    FROM LH_Staging.[dbo].[crmtranfact36mstage]
```

