# dbo.emailsendjobs

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailsendjobs"]
    dbo_emailsendjobs(["dbo.emailsendjobs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailsendjobs |

## View Code

```sql
;
CREATE   VIEW [dbo].[emailsendjobs]
AS
    SELECT [ClientID], [SendID], [Subject] COLLATE Latin1_General_CI_AS AS [Subject], [EmailName] COLLATE Latin1_General_CI_AS AS [EmailName], [EventDate]
    FROM LH_Staging.[dbo].[emailsendjobs]
```

