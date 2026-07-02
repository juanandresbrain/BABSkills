# dbo.UpdateComment

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateComment"]
    dbo_Comments(["dbo.Comments"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Comments |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateComment]
@Text nvarchar(2048),
@CommentID bigint
AS
BEGIN
    UPDATE
        [Comments]
    SET
        [Text]=@Text,
        [ModifiedDate]=GETDATE()
    WHERE
        [CommentID]=@CommentID
END
```

