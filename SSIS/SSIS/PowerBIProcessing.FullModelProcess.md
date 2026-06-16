# SSIS Package: FullModelProcess

**Project:** PowerBIProcessing  
**Folder:** SSIS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph ControlFlow
        FullModelProcess_task["FullModelProcess"]
        Analysis_Services_Processing_Task_task["Analysis Services Processing Task"]
        FullModelProcess_task --> Analysis_Services_Processing_Task_task
        Send_Mail_Task_task["Send Mail Task"]
        Analysis_Services_Processing_Task_task --> Send_Mail_Task_task
    end
```

## Connection Managers

_No connections found._

## Control Flow Tasks

| Task Name | Type |
|---|---|
| FullModelProcess | Microsoft.Package |
| Analysis Services Processing Task | Microsoft.DTSProcessingTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

