# dbo.vwDW_GiftCard_GetFilesToPull

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_GiftCard_GetFilesToPull"]
    dbo_GiftCard_FilesToPull(["dbo.GiftCard_FilesToPull"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GiftCard_FilesToPull |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_GiftCard_GetFilesToPull]
AS
SELECT     FTP_Server, FTP_FileName, MustPullFile, DropDirectory, GroupCode, FileType, ISNULL(GroupID, '') AS GroupID
FROM         dbo.GiftCard_FilesToPull
WHERE     (Active = 1)
```

