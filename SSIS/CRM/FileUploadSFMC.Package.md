# SSIS Package: Package

**Project:** FileUploadSFMC  
**Folder:** CRM  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Archive_APP_conn(["Archive APP [FILE]"])
        Archive_DB_conn(["Archive DB [FILE]"])
        FTP_SFMC_APP_conn(["FTP_SFMC APP [FILE]"])
        FTP_SFMC_DB_conn(["FTP_SFMC DB [FILE]"])
        STL_CRMDB_P_01_crm_conn(["STL-CRMDB-P-01.crm [OLEDB]"])
    end
    subgraph ControlFlow
        Package_task["Package"]
        File_Upload_to_SFMC_task["File Upload to SFMC"]
        Package_task --> File_Upload_to_SFMC_task
        Move_txt_file_to_DB_server_task["Move txt file to DB server"]
        File_Upload_to_SFMC_task --> Move_txt_file_to_DB_server_task
        Archive_Files_task["Archive Files"]
        Move_txt_file_to_DB_server_task --> Archive_Files_task
        Copy_Files_task["Copy Files"]
        Archive_Files_task --> Copy_Files_task
        Move_Uploaded_txt_Files_to_Archive_DB_task["Move Uploaded txt Files to Archive DB"]
        Copy_Files_task --> Move_Uploaded_txt_Files_to_Archive_DB_task
        Execute_sp_to_upload_files_to_SFMC_task["Execute sp to upload files to SFMC"]
        Move_Uploaded_txt_Files_to_Archive_DB_task --> Execute_sp_to_upload_files_to_SFMC_task
        File_System_Task_task["File System Task"]
        Execute_sp_to_upload_files_to_SFMC_task --> File_System_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Archive APP | FILE |
| Archive DB | FILE |
| FTP_SFMC APP | FILE |
| FTP_SFMC DB | FILE |
| STL-CRMDB-P-01.crm | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| Package | Microsoft.Package |
| File Upload to SFMC | STOCK:SEQUENCE |
| Move txt file to DB server | STOCK:FOREACHLOOP |
| Archive Files | Microsoft.FileSystemTask |
| Copy Files | Microsoft.FileSystemTask |
| Move Uploaded txt Files to Archive DB | STOCK:FOREACHLOOP |
| Execute sp to upload files to SFMC | Microsoft.ExecuteSQLTask |
| File System Task | Microsoft.FileSystemTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

