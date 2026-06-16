# SSIS Package: WEB_StoreInventoryBuffers

**Project:** WEB_StoreInventoryBuffers  
**Folder:** WEB  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        BuffersCSV_conn(["BuffersCSV [FLATFILE]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WEB_StoreInventoryBuffers_task["WEB_StoreInventoryBuffers"]
        SEQ___Stage_Buffer_Data_task["SEQ - Stage Buffer Data"]
        WEB_StoreInventoryBuffers_task --> SEQ___Stage_Buffer_Data_task
        Foreach_Loop_Container_task["Foreach Loop Container"]
        SEQ___Stage_Buffer_Data_task --> Foreach_Loop_Container_task
        DataFlow___Load_Buffers_task[/"DataFlow - Load Buffers"/]
        Foreach_Loop_Container_task --> DataFlow___Load_Buffers_task
        Merge_StoreInventoryBuffers_task["Merge StoreInventoryBuffers"]
        DataFlow___Load_Buffers_task --> Merge_StoreInventoryBuffers_task
        Truncate_Stage_task["Truncate Stage"]
        Merge_StoreInventoryBuffers_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| BuffersCSV | FLATFILE |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WEB_StoreInventoryBuffers | Microsoft.Package |
| SEQ - Stage Buffer Data | STOCK:SEQUENCE |
| Foreach Loop Container | STOCK:FOREACHLOOP |
| DataFlow - Load Buffers | Microsoft.Pipeline |
| Merge StoreInventoryBuffers | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [WEB].[StoreInventoryBuffersStage] |

