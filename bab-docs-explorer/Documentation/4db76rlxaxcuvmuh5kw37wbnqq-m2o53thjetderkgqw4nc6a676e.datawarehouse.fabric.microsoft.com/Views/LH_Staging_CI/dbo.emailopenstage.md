# dbo.emailopenstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailopenstage"]
    dbo_emailopenstage(["dbo.emailopenstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailopenstage |

## View Code

```sql
;
CREATE   VIEW [dbo].[emailopenstage]
AS
    SELECT [ClientID], [SendID], [SubscriberKey] COLLATE Latin1_General_CI_AS AS [SubscriberKey], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [OpenDate]
    FROM LH_Staging.[dbo].[emailopenstage]
```

