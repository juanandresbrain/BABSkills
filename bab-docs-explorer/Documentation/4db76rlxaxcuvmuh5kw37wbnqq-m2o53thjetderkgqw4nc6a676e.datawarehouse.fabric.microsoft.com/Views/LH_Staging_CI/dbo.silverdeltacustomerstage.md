# dbo.silverdeltacustomerstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.silverdeltacustomerstage"]
    dbo_silverdeltacustomerstage(["dbo.silverdeltacustomerstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.silverdeltacustomerstage |

## View Code

```sql
;
CREATE   VIEW [dbo].[silverdeltacustomerstage]
AS
    SELECT [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [SalesforceID] COLLATE Latin1_General_CI_AS AS [SalesforceID]
    FROM LH_Staging.[dbo].[silverdeltacustomerstage]
```

