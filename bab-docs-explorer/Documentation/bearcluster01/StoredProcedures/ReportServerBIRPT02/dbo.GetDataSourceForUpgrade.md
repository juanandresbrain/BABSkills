# dbo.GetDataSourceForUpgrade

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDataSourceForUpgrade"]
    dbo_DataSource(["dbo.DataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DataSource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDataSourceForUpgrade]
@CurrentVersion int
AS
SELECT
    [DSID]
FROM
    [DataSource]
WHERE
    [Version] != @CurrentVersion
```

