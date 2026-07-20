# dbo.actualhoursstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.actualhoursstage"]
    dbo_actualhoursstage(["dbo.actualhoursstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.actualhoursstage |

## View Code

```sql
CREATE   VIEW [dbo].[actualhoursstage]
AS
    SELECT [StoreID], [Year], [Week], [WeekStartDate], [ActualHours]
    FROM LH_Staging.[dbo].[actualhoursstage]
```

