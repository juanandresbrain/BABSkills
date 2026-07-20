# dbo.crmtranfact6mstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmtranfact6mstage"]
    dbo_crmtranfact6mstage(["dbo.crmtranfact6mstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmtranfact6mstage |

## View Code

```sql
;
CREATE   VIEW [dbo].[crmtranfact6mstage]
AS
    SELECT [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [MonthRange] COLLATE Latin1_General_CI_AS AS [MonthRange], [TransactionCount], [RecencyCount], [SalesTotal], [minDaysBetween], [maxDaysBetween], [DaysBetween]
    FROM LH_Staging.[dbo].[crmtranfact6mstage]
```

