# dbo.RebindDataSet

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RebindDataSet"]
    DataSets(["DataSets"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| DataSets |

## Stored Procedure Code

```sql
-- Republishing generates new ID and stores those in the object model, 
-- in order to resolve the data sets we need to rebind the old 
-- data set definition to the current ID
CREATE PROCEDURE [dbo].[RebindDataSet]
@ItemId		uniqueidentifier, 
@Name		nvarchar(260), 
@NewID	uniqueidentifier
AS
UPDATE DataSets
SET ID = @NewID
WHERE ItemID = @ItemId AND [Name] = @Name
```

