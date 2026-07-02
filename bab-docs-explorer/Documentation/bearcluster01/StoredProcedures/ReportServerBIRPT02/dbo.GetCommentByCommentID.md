# dbo.GetCommentByCommentID

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetCommentByCommentID"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_Comments(["dbo.Comments"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.Comments |
| dbo.Users |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetCommentByCommentID]
@CommentID bigint
AS
BEGIN
    SELECT TOP(1)
        C.[CommentID],
        C.[ItemID],
        U.[UserName],
        C.[ThreadID],
        C.[Text],
        C.[CreatedDate],
        C.[ModifiedDate],
        CAI.[Path] AS ItemPath,
        CAA.[Path] AS AttachmentPath,
        CAI.[Name]
    FROM
        [Comments] as C
        INNER JOIN Users as U ON C.[UserID] = U.[UserID]
        INNER JOIN Catalog as CAI ON C.[ItemID] = CAI.[ItemID]
        LEFT JOIN Catalog as CAA ON C.[AttachmentID] = CAA.[ItemID]
    WHERE
        C.[CommentID] = @CommentID
END
```

