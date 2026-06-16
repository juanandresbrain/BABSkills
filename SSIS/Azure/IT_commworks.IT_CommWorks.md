# SSIS Package: IT_CommWorks

**Project:** IT_commworks  
**Folder:** Azure  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        CommWorks_conn(["CommWorks [HTTP (KingswaySoft)]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        IT_CommWorks_task["IT_CommWorks"]
        CommWorks_API_data_flow_task[/"CommWorks API data flow"/]
        IT_CommWorks_task --> CommWorks_API_data_flow_task
        merge_task["merge"]
        CommWorks_API_data_flow_task --> merge_task
        truncate_table_task["truncate table"]
        merge_task --> truncate_table_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| CommWorks | HTTP (KingswaySoft) |
| DW | OLEDB |
| DWStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| IT_CommWorks | Microsoft.Package |
| CommWorks API data flow | Microsoft.Pipeline |
| merge | Microsoft.ExecuteSQLTask |
| truncate table | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[IT_commworks_stage] |

