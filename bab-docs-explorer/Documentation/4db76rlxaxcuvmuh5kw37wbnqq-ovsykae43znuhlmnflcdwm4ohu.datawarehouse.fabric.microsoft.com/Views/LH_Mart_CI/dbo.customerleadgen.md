# dbo.customerleadgen

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.customerleadgen"]
    dbo_customerleadgen(["dbo.customerleadgen"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.customerleadgen |

## View Code

```sql
; CREATE   VIEW [dbo].[customerleadgen] AS     SELECT [EntryDate], [CountryCode] COLLATE Latin1_General_CI_AS AS [CountryCode], [Campaign] COLLATE Latin1_General_CI_AS AS [Campaign], [Source] COLLATE Latin1_General_CI_AS AS [Source], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [FileDate], [FileName] COLLATE Latin1_General_CI_AS AS [FileName], [InsertDate], [UpdateDate]     FROM [dbo].[customerleadgen]
```

