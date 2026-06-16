# SSIS Package: AzureProcess

**Project:** AzureProcess  
**Folder:** Azure  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        asazure___northcentralus_asazure_windows_net_azasp01_BABW_DW_conn(["asazure://northcentralus.asazure.windows.net/azasp01.BABW-DW [MSOLAP100]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        AzureProcess_task["AzureProcess"]
        Sequence_Container_task["Sequence Container"]
        AzureProcess_task --> Sequence_Container_task
        Analysis_Services_Processing_Task_task["Analysis Services Processing Task"]
        Sequence_Container_task --> Analysis_Services_Processing_Task_task
        Process_Default_task["Process Default"]
        Analysis_Services_Processing_Task_task --> Process_Default_task
        Send_Start_Email_task["Send Start Email"]
        Process_Default_task --> Send_Start_Email_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| asazure://northcentralus.asazure.windows.net/azasp01.BABW-DW | MSOLAP100 |
| DWStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| AzureProcess | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Analysis Services Processing Task | Microsoft.DTSProcessingTask |
| Process Default | Microsoft.ASExecuteDDLTask |
| Send Start Email | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

