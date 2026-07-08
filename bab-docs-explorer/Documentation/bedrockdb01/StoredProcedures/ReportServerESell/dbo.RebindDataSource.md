# dbo.RebindDataSource

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RebindDataSource"]
    DataSource(["DataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| DataSource |

## Stored Procedure Code

```sql
-- Republishing generates new DSID and stores those in the object model, 
-- in order to resolve the data sources we need to rebind the old 
-- data source definition to the current DSID
CREATE PROCEDURE [dbo].[RebindDataSource]
@ItemId		uniqueidentifier, 
@Name		nvarchar(260), 
@NewDSID	uniqueidentifier
AS
UPDATE DataSource
SET DSID = @NewDSID
WHERE ItemID = @ItemId AND [Name] = @Name
```

