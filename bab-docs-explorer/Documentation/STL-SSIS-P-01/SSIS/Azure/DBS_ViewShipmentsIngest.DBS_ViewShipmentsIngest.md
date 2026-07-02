# SSIS Package: DBS_ViewShipmentsIngest

**Project:** DBS_ViewShipmentsIngest  
**Folder:** Azure  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        FTP_Connection_Manager_conn(["FTP Connection Manager [FTP]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        DBS_ViewShipmentsIngest_task["DBS_ViewShipmentsIngest"]
        Foreach_Loop___Ingest_File_task["Foreach Loop - Ingest File"]
        DBS_ViewShipmentsIngest_task --> Foreach_Loop___Ingest_File_task
        Data_Flow_Task_task["Data Flow Task"]
        Foreach_Loop___Ingest_File_task --> Data_Flow_Task_task
        Truncate_Stage_task["Truncate Stage"]
        Data_Flow_Task_task --> Truncate_Stage_task
        FTP_Task_task["FTP Task"]
        Truncate_Stage_task --> FTP_Task_task
        Send_Mail_Task_task["Send Mail Task"]
        FTP_Task_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| FTP Connection Manager | FTP |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| DBS_ViewShipmentsIngest | Microsoft.Package |
| Foreach Loop - Ingest File | STOCK:FOREACHLOOP |
| Data Flow Task | Microsoft.Pipeline |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| FTP Task | Microsoft.FtpTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [DBS_ViewShipmentsStage] |

