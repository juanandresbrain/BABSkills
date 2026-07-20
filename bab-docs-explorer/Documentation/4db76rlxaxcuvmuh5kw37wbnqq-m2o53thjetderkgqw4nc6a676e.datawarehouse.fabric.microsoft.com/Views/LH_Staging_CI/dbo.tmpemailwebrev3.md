# dbo.tmpemailwebrev3

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpemailwebrev3"]
    dbo_tmpemailwebrev3(["dbo.tmpemailwebrev3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpemailwebrev3 |

## View Code

```sql
;
CREATE   VIEW [dbo].[tmpemailwebrev3]
AS
    SELECT [OpenDate], [emailAddress] COLLATE Latin1_General_CI_AS AS [emailAddress], [rev]
    FROM LH_Staging.[dbo].[tmpemailwebrev3]
```

