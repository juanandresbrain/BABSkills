# dbo.customerleadgenstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.customerleadgenstage"]
    dbo_customerleadgenstage(["dbo.customerleadgenstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.customerleadgenstage |

## View Code

```sql
; CREATE   VIEW [dbo].[customerleadgenstage] AS SELECT [EntryDate], [CountryCode] COLLATE Latin1_General_CI_AS AS [CountryCode], [Campaign] COLLATE Latin1_General_CI_AS AS [Campaign], [Source] COLLATE Latin1_General_CI_AS AS [Source], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [FileDate], [FileName] COLLATE Latin1_General_CI_AS AS [FileName] FROM [dbo].[customerleadgenstage]
```

