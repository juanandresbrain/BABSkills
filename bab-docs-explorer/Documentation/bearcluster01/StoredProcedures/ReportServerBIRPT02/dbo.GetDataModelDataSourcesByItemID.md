# dbo.GetDataModelDataSourcesByItemID

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDataModelDataSourcesByItemID"]
    dbo_DataModelDataSource(["dbo.DataModelDataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DataModelDataSource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDataModelDataSourcesByItemID]
    @ItemID uniqueidentifier
AS
    SELECT
        D.DSID,
        D.ItemId,
        D.DSType,
        D.DSKind,
        D.AuthType,
        D.ConnectionString,
        D.Username,
        D.Password
    FROM
        [DataModelDataSource] as D
    WHERE
        D.[ItemID] = @ItemID
```

