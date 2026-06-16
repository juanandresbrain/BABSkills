# SSIS Package: CRM_gcRanges

**Project:** CRM_gcRanges  
**Folder:** CRM  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
    end
    subgraph ControlFlow
        CRM_gcRanges_task["CRM_gcRanges"]
        seq1_task["seq1"]
        CRM_gcRanges_task --> seq1_task
        exec_merge_task["exec merge"]
        seq1_task --> exec_merge_task
        exec_proc_task["exec proc"]
        exec_merge_task --> exec_proc_task
        truncate_task["truncate"]
        exec_proc_task --> truncate_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| DW | OLEDB |
| DWStaging | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| CRM_gcRanges | Microsoft.Package |
| seq1 | STOCK:SEQUENCE |
| exec merge | Microsoft.ExecuteSQLTask |
| exec proc | Microsoft.ExecuteSQLTask |
| truncate | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

