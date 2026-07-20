# dbo.laborcreditsstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.laborcreditsstage"]
    dbo_laborcreditsstage(["dbo.laborcreditsstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.laborcreditsstage |

## View Code

```sql
; CREATE   VIEW [dbo].[laborcreditsstage] AS SELECT [DateSubmitted], [StoreNumber], [Month] COLLATE Latin1_General_CI_AS AS [Month], [WeekNumber], [Credit], [Reason] COLLATE Latin1_General_CI_AS AS [Reason], [RequestedBy] COLLATE Latin1_General_CI_AS AS [RequestedBy] FROM [dbo].[laborcreditsstage]
```

