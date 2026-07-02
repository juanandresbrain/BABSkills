# SSIS Package: CRM_surveyETL

**Project:** CRM_SurveyETL  
**Folder:** CRM  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        ASNCorrections_conn(["ASNCorrections [FLATFILE]"])
        CRM_conn(["CRM [ADO.NET:SQL]"])
        Data_xlsx_conn(["Data.xlsx [FILE]"])
        ESPStaging_conn(["ESPStaging [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        ProductInventory_conn(["ProductInventory [FLATFILE]"])
        SendLog_conn(["SendLog [FLATFILE]"])
        SendLogPIPE_csv_conn(["SendLogPIPE.csv [FILE]"])
        SMTP_conn(["SMTP [SMTP]"])
        surveyDestination_conn(["surveyDestination [FILE]"])
    end
    subgraph ControlFlow
        CRM_surveyETL_task["CRM_surveyETL"]
        Sequence_Container_1_task["Sequence Container 1"]
        CRM_surveyETL_task --> Sequence_Container_1_task
        archive_file_task["archive file"]
        Sequence_Container_1_task --> archive_file_task
        copy_xlsx_task["copy xlsx"]
        archive_file_task --> copy_xlsx_task
        copy_to_p_01_task["copy to p-01"]
        copy_xlsx_task --> copy_to_p_01_task
        Execute_SQL_Task_task["Execute SQL Task"]
        copy_to_p_01_task --> Execute_SQL_Task_task
        retreive_files_task["retreive files"]
        Execute_SQL_Task_task --> retreive_files_task
        retreive_files_task["retreive files"]
        retreive_files_task --> retreive_files_task
        stage_files_task["stage files"]
        retreive_files_task --> stage_files_task
        archive_file_task["archive file"]
        stage_files_task --> archive_file_task
        delete_file_task["delete file"]
        archive_file_task --> delete_file_task
        merge_data_task["merge data"]
        delete_file_task --> merge_data_task
        rename_file_task["rename file"]
        merge_data_task --> rename_file_task
        stage_data_task["stage data"]
        rename_file_task --> stage_data_task
        truncate_stage_task["truncate stage"]
        stage_data_task --> truncate_stage_task
        unzip_files_task["unzip files"]
        truncate_stage_task --> unzip_files_task
        Execute_Process_Task_task["Execute Process Task"]
        unzip_files_task --> Execute_Process_Task_task
        File_System_Task_task["File System Task"]
        Execute_Process_Task_task --> File_System_Task_task
        File_System_Task_1_task["File System Task 1"]
        File_System_Task_task --> File_System_Task_1_task
        Send_Mail_Task_task["Send Mail Task"]
        File_System_Task_1_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| ASNCorrections | FLATFILE |
| CRM | ADO.NET:SQL |
| Data.xlsx | FILE |
| ESPStaging | OLEDB |
| IntegrationStaging | OLEDB |
| papamart.DWStaging | OLEDB |
| ProductInventory | FLATFILE |
| SendLog | FLATFILE |
| SendLogPIPE.csv | FILE |
| SMTP | SMTP |
| surveyDestination | FILE |

## Control Flow Tasks

| Task | Type |
|---|---|
| CRM_surveyETL | Microsoft.Package |
| Sequence Container 1 | STOCK:SEQUENCE |
| archive file | Microsoft.FileSystemTask |
| copy xlsx | STOCK:FOREACHLOOP |
| copy to p-01 | Microsoft.FileSystemTask |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| retreive files | STOCK:FOREACHLOOP |
| retreive files | Microsoft.FileSystemTask |
| stage files | STOCK:FOREACHLOOP |
| archive file | Microsoft.FileSystemTask |
| delete file | Microsoft.FileSystemTask |
| merge data | Microsoft.ExecuteSQLTask |
| rename file | Microsoft.FileSystemTask |
| stage data | Microsoft.Pipeline |
| truncate stage | Microsoft.ExecuteSQLTask |
| unzip files | STOCK:FOREACHLOOP |
| Execute Process Task | Microsoft.ExecuteProcess |
| File System Task | Microsoft.FileSystemTask |
| File System Task 1 | Microsoft.FileSystemTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[CRM_surveyStage] |

