# dbo.AddDataModelDataSource

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddDataModelDataSource"]
    dbo_DataModelDataSource(["dbo.DataModelDataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DataModelDataSource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[AddDataModelDataSource]
    @ItemID uniqueidentifier,
    @DSType int = 0,
    @DSKind int = 0,
    @AuthType int = 0,
    @ConnectionString varbinary(max) = null,
    @Username varbinary(max) = null,
    @Password varbinary(max) = null
AS
BEGIN
INSERT
    INTO DataModelDataSource
        ([ItemID],
        [DSType],
        [DSKind],
        [AuthType],
        [ConnectionString],
        [Username],
        [Password])
    VALUES
        (@ItemID,
        @DSType,
        @DSKind,
        @AuthType,
        @ConnectionString,
        @Username,
        @Password)
END
```

