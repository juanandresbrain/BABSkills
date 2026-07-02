# SSIS Package: MoveWMShippingSpoolFiles

**Project:** WEBMoveWMShippingLabelSpoolFiles  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Archived_conn(["Archived [FILE]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        ShippingLabels_conn(["ShippingLabels [FILE]"])
        SMTP_EMAIL_conn(["SMTP_EMAIL [SMTP]"])
        SpoolFiles_conn(["SpoolFiles [FILE]"])
        SQL_LOG_conn(["SQL_LOG [OLEDB]"])
        wmapptest_RSMonarch_conn(["wmapptest_RSMonarch [FILE]"])
    end
    subgraph ControlFlow
        MoveWMShippingSpoolFiles_task["MoveWMShippingSpoolFiles"]
        Delete_Old_Files_task["Delete Old Files"]
        MoveWMShippingSpoolFiles_task --> Delete_Old_Files_task
        ForeachLoop___Move_Spool_Files_task["ForeachLoop - Move Spool Files"]
        Delete_Old_Files_task --> ForeachLoop___Move_Spool_Files_task
        Archive_File_task["Archive File"]
        ForeachLoop___Move_Spool_Files_task --> Archive_File_task
        Copy_Spool_File_to_CLB_SSRS_P_01_task["Copy Spool File to CLB-SSRS-P-01"]
        Archive_File_task --> Copy_Spool_File_to_CLB_SSRS_P_01_task
        Send_Email_onError_task["Send Email onError"]
        Copy_Spool_File_to_CLB_SSRS_P_01_task --> Send_Email_onError_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| Archived | FILE |
| IntegrationStaging | OLEDB |
| ShippingLabels | FILE |
| SMTP_EMAIL | SMTP |
| SpoolFiles | FILE |
| SQL_LOG | OLEDB |
| wmapptest_RSMonarch | FILE |

## Control Flow Tasks

| Task | Type |
|---|---|
| MoveWMShippingSpoolFiles | Microsoft.Package |
| Delete Old Files | Microsoft.ExecuteSQLTask |
| ForeachLoop - Move Spool Files | STOCK:FOREACHLOOP |
| Archive File | Microsoft.FileSystemTask |
| Copy Spool File to CLB-SSRS-P-01 | Microsoft.FileSystemTask |
| Send Email onError | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

