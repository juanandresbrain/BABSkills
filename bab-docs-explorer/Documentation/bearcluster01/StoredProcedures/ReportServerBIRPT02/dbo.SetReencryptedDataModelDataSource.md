# dbo.SetReencryptedDataModelDataSource

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetReencryptedDataModelDataSource"]
    dbo_DataModelDataSource(["dbo.DataModelDataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DataModelDataSource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetReencryptedDataModelDataSource]
    @DSID bigint,
    @ConnectionString varbinary(max) = null,
    @Username varbinary(max) = null,
    @Password varbinary(max) = null
AS

UPDATE [dbo].[DataModelDataSource]
SET
    [ConnectionString] = @ConnectionString,
    [Username] = @Username,
    [Password] = @Password
WHERE [DSID] = @DSID
```

