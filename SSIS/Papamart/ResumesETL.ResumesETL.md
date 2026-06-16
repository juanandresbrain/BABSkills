# SSIS Package: ResumesETL

**Project:** ResumesETL  
**Folder:** Papamart  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        BABWMstrData_conn(["BABWMstrData [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        Locations_conn(["Locations [OLEDB]"])
    end
    subgraph ControlFlow
        ResumesETL_task["ResumesETL"]
        Merge_Resume_Data_task["Merge Resume Data"]
        ResumesETL_task --> Merge_Resume_Data_task
        Stage_ContactEmails_task[/"Stage ContactEmails"/]
        Merge_Resume_Data_task --> Stage_ContactEmails_task
        Stage_Resume_Data_task[/"Stage Resume Data"/]
        Stage_ContactEmails_task --> Stage_Resume_Data_task
        Truncate_Stage_task["Truncate Stage"]
        Stage_Resume_Data_task --> Truncate_Stage_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| BABWMstrData | OLEDB |
| DWStaging | OLEDB |
| Locations | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| ResumesETL | Microsoft.Package |
| Merge Resume Data | Microsoft.ExecuteSQLTask |
| Stage ContactEmails | Microsoft.Pipeline |
| Stage Resume Data | Microsoft.Pipeline |
| Truncate Stage | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[vwContactEmails] |
|  | [ContactEmailStage] |
|  | [dbo].[ResumeStage] |

