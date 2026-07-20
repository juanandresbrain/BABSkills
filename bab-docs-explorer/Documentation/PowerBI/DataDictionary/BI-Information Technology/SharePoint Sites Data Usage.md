# SharePoint Sites Data Usage

**Workspace:** BI-Information Technology  
**Report ID:** adca49d8-2d57-4bd2-b2da-9b3c06c8ceb8  
**Dataset ID:** 4cc5d440-37e8-43f3-8d71-c4396ac2440c  
**Web URL:** https://app.powerbi.com/groups/064e5d9a-9ef2-4ac2-9f6d-f0be736f3b1d/reports/adca49d8-2d57-4bd2-b2da-9b3c06c8ceb8  
**Semantic Model:** [SharePoint Sites Data Usage](../../SemanticModels/BI-Information Technology/SharePoint Sites Data Usage.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["SharePoint Sites Data Usage"]
    SharePoint_Sites__2__SiteName(["SharePoint Sites (2).SiteName"]) --> REPORT
    SharePoint_Sites__2__SiteUrl(["SharePoint Sites (2).SiteUrl"]) --> REPORT
    SharePoint_SiteSnapshots__2__SnapshotDate(["SharePoint SiteSnapshots (2).SnapshotDate"]) --> REPORT
    Sum_SharePoint_SiteSnapshots__2__TotalSpaceUsedMB_(["Sum(SharePoint SiteSnapshots (2).TotalSpaceUsedMB)"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| SharePoint Sites (2).SiteName |
| SharePoint Sites (2).SiteUrl |
| SharePoint SiteSnapshots (2).SnapshotDate |
| Sum(SharePoint SiteSnapshots (2).TotalSpaceUsedMB) |

## Pages

| Page | Visuals |
|---|---|
| Site Storage LIst | 2 |
| Top 10 Site Usage | 1 |
| Heatmap All Sites | 2 |
| Site Storage Over Time | 3 |

## Visuals

### Site Storage LIst

| Visual | Type | Fields |
|---|---|---|
| 147440630dd534565c54 | pivotTable | SharePoint Sites (2).SiteName, SharePoint Sites (2).SiteUrl, SharePoint SiteSnapshots (2).SnapshotDate, Sum(SharePoint SiteSnapshots (2).TotalSpaceUsedMB) |
| 78b33078812fd5d7149c | slicer | SharePoint SiteSnapshots (2).SnapshotDate |

### Top 10 Site Usage

| Visual | Type | Fields |
|---|---|---|
| da152fc4374ab3ce9792 | lineChart | SharePoint SiteSnapshots (2).SnapshotDate, Sum(SharePoint SiteSnapshots (2).TotalSpaceUsedMB), SharePoint Sites (2).SiteName |

### Heatmap All Sites

| Visual | Type | Fields |
|---|---|---|
| a59a9dbd101c6b4e90a7 | treemap | Sum(SharePoint SiteSnapshots (2).TotalSpaceUsedMB), SharePoint Sites (2).SiteName |
| c5f5180d088c008a5a2e | actionButton |  |

### Site Storage Over Time

| Visual | Type | Fields |
|---|---|---|
| 5ae3e4aa501100975ab5 | lineChart | SharePoint SiteSnapshots (2).SnapshotDate, Sum(SharePoint SiteSnapshots (2).TotalSpaceUsedMB), SharePoint Sites (2).SiteName |
| 933a66eb784d42a78e20 | actionButton |  |
| ea0a8a366d872d8826a8 | slicer | SharePoint Sites (2).SiteName |
