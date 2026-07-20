# dbo.laborcredits

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.laborcredits"]
    dbo_laborcredits(["dbo.laborcredits"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.laborcredits |

## View Code

```sql
; CREATE   VIEW [dbo].[laborcredits] AS     SELECT [DateSubmitted], [StoreNumber], [Month] COLLATE Latin1_General_CI_AS AS [Month], [WeekNumber], [Credit], [Reason] COLLATE Latin1_General_CI_AS AS [Reason], [RequestedBy] COLLATE Latin1_General_CI_AS AS [RequestedBy], [InsertDate], [UpdateDate]     FROM [dbo].[laborcredits]
```

