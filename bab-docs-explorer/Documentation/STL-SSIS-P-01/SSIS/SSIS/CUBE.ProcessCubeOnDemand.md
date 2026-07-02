# SSIS Package: ProcessCubeOnDemand

**Project:** CUBE  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        biapp01_BAB_DW_conn(["biapp01.BAB DW [MSOLAP100]"])
        SMTP_EMAIL_conn(["SMTP_EMAIL [SMTP]"])
        SQL_LOG_conn(["SQL_LOG [OLEDB]"])
    end
    subgraph ControlFlow
        ProcessCubeOnDemand_task["ProcessCubeOnDemand"]
        Process_Transactions_Partition_task["Process Transactions Partition"]
        ProcessCubeOnDemand_task --> Process_Transactions_Partition_task
        Send_Email_onError_task["Send Email onError"]
        Process_Transactions_Partition_task --> Send_Email_onError_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| biapp01.BAB DW | MSOLAP100 |
| SMTP_EMAIL | SMTP |
| SQL_LOG | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| ProcessCubeOnDemand | Microsoft.Package |
| Process Transactions Partition | Microsoft.DTSProcessingTask |
| Send Email onError | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

