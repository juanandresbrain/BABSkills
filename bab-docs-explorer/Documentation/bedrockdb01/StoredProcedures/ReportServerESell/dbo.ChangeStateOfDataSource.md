# dbo.ChangeStateOfDataSource

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ChangeStateOfDataSource"]
    DataSource(["DataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| DataSource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ChangeStateOfDataSource]
@ItemID [uniqueidentifier],
@Enable bit
AS
IF @Enable != 0 BEGIN
   UPDATE [DataSource]
      SET
         [Flags] = [Flags] | 1
   WHERE [ItemID] = @ItemID
END
ELSE
BEGIN
   UPDATE [DataSource]
      SET
         [Flags] = [Flags] & 0x7FFFFFFE
   WHERE [ItemID] = @ItemID
END
```

