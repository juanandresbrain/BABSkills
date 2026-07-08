# dbo.GetDataSourceForUpgrade

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDataSourceForUpgrade"]
    DataSource(["DataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| DataSource |

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

