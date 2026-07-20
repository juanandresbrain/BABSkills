# dbo.tmpemailretrev3

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpemailretrev3"]
    dbo_tmpemailretrev3(["dbo.tmpemailretrev3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpemailretrev3 |

## View Code

```sql
;
CREATE   VIEW [dbo].[tmpemailretrev3]
AS
    SELECT [OpenDate], [emailAddress] COLLATE Latin1_General_CI_AS AS [emailAddress], [rev]
    FROM LH_Staging.[dbo].[tmpemailretrev3]
```

