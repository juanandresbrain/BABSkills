# dbo.DeleteDataSources

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteDataSources"]
    dbo_DataSource(["dbo.DataSource"]) --> SP
    dbo_TempDataSources(["dbo.TempDataSources"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DataSource |
| dbo.TempDataSources |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteDataSources]
@ItemID [uniqueidentifier]
AS

DELETE
FROM [DataSource]
WHERE [ItemID] = @ItemID or [SubscriptionID] = @ItemID
DELETE
FROM [ReportServerBIRPT02TempDB].dbo.TempDataSources
WHERE [ItemID] = @ItemID
```

