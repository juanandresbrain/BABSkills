# dbo.GetDataModelDatasourceForReencryption

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDataModelDatasourceForReencryption"]
    dbo_DataModelDataSource(["dbo.DataModelDataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DataModelDataSource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDataModelDatasourceForReencryption]
@DSID as bigint
AS

SELECT
    [ConnectionString],
    [Username],
    [Password]
FROM [dbo].[DataModelDataSource]
WHERE [DSID] = @DSID
```

