# SSIS Package: HR_UltiProValidations

**Project:** HR_UltiProValidations  
**Folder:** HR  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        DW_conn(["DW [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        HR_UltiProValidations_task["HR_UltiProValidations"]
        Delete_Terminated_from_ADEmployee_task["Delete Terminated from ADEmployee"]
        HR_UltiProValidations_task --> Delete_Terminated_from_ADEmployee_task
        StagedButNotInAD_task["StagedButNotInAD"]
        Delete_Terminated_from_ADEmployee_task --> StagedButNotInAD_task
        Send_Mail_Task_task["Send Mail Task"]
        StagedButNotInAD_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| DW | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| HR_UltiProValidations | Microsoft.Package |
| Delete Terminated from ADEmployee | Microsoft.ExecuteSQLTask |
| StagedButNotInAD | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

