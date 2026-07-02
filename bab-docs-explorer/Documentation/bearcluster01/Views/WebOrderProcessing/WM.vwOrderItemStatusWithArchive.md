# WM.vwOrderItemStatusWithArchive

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwOrderItemStatusWithArchive"]
    WM_ItemStatus(["WM.ItemStatus"]) --> VIEW
    WM_ItemStatus_Archive(["WM.ItemStatus_Archive"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ItemStatus |
| WM.ItemStatus_Archive |

## View Code

```sql
CREATE VIEW [WM].[vwOrderItemStatusWithArchive]
AS
SELECT        *
FROM            WM.ItemStatus 
UNION ALL
 SELECT        *
FROM            WM.ItemStatus_Archive
```

