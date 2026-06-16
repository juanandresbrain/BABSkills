# SSIS Package: OMSCustomOrderExportImport

**Project:** WebOrderProcessing  
**Folder:** SSIS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        OMSCustomOrderExport_conn(["OMSCustomOrderExport [FLATFILE]"])
        OMSTransactionDetailReport_v2_conn(["OMSTransactionDetailReport_v2 [FLATFILE]"])
        SMTP_EMAIL_conn(["SMTP_EMAIL [SMTP]"])
        SQL_LOG_conn(["SQL_LOG [OLEDB]"])
    end
    subgraph ControlFlow
        OMSCustomOrderExportImport_task["OMSCustomOrderExportImport"]
        Sequence_Container_task["Sequence Container"]
        OMSCustomOrderExportImport_task --> Sequence_Container_task
        Foreach_Loop___Move_Source_Files_to_Stage_task["Foreach Loop - Move Source Files to Stage"]
        Sequence_Container_task --> Foreach_Loop___Move_Source_Files_to_Stage_task
        Move_Files_to_Stage_task["Move Files to Stage"]
        Foreach_Loop___Move_Source_Files_to_Stage_task --> Move_Files_to_Stage_task
        Foreach_Loop_Container_task["Foreach Loop Container"]
        Move_Files_to_Stage_task --> Foreach_Loop_Container_task
        DFT___Process_Custom_Order_Export_task[/"DFT - Process Custom Order Export"/]
        Foreach_Loop_Container_task --> DFT___Process_Custom_Order_Export_task
        File_System_Task_task["File System Task"]
        DFT___Process_Custom_Order_Export_task --> File_System_Task_task
        Send_Email_onError_task["Send Email onError"]
        File_System_Task_task --> Send_Email_onError_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| OMSCustomOrderExport | FLATFILE |
| OMSTransactionDetailReport_v2 | FLATFILE |
| SMTP_EMAIL | SMTP |
| SQL_LOG | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| OMSCustomOrderExportImport | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Foreach Loop - Move Source Files to Stage | STOCK:FOREACHLOOP |
| Move Files to Stage | Microsoft.FileSystemTask |
| Foreach Loop Container | STOCK:FOREACHLOOP |
| DFT - Process Custom Order Export | Microsoft.Pipeline |
| File System Task | Microsoft.FileSystemTask |
| Send Email onError | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | SELECT [TransactionID]       ,[TransactionNum]   FROM [WebOrderProcessing].[WM].[Transactions] |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [WM].[OMSCustomOrderExport] |

