# SSIS Package: WM_MoveInventoryFromProdToTest

**Project:** WM_MoveInventoryFromProdToTest  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        WMProd_conn(["WMProd [OLEDB]"])
        WMTest_conn(["WMTest [OLEDB]"])
    end
    subgraph ControlFlow
        WM_MoveInventoryFromProdToTest_task["WM_MoveInventoryFromProdToTest"]
        WM_Case_Detail_task["WM Case Detail"]
        WM_MoveInventoryFromProdToTest_task --> WM_Case_Detail_task
        WM_Case_Header_task["WM Case Header"]
        WM_Case_Detail_task --> WM_Case_Header_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| WMProd | OLEDB |
| WMTest | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| WM_MoveInventoryFromProdToTest | Microsoft.Package |
| WM Case Detail | Microsoft.Pipeline |
| WM Case Header | Microsoft.Pipeline |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | select case_nbr  from case_dtl with (nolock) |
|  | select cd.* from case_dtl cd with (nolock) join case_hdr ch with (nolock) on cd.case_nbr = ch.case_nbr join locn_hdr lh with (nolock) on ch.locn_id = lh.locn_id  and (lh.work_grp <> 'web' or lh.work_grp is null) where ch.stat_code = 30 |
|  | select case_nbr  from case_hdr with (nolock) |
|  | select ch.* from case_hdr ch with (nolock)  join locn_hdr lh with (nolock) on ch.locn_id = lh.locn_id  and (lh.work_grp <> 'web' or lh.work_grp is null) where ch.stat_code = 30 |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[CASE_DTL] |
|  | [dbo].[CASE_HDR] |

