# SSIS Package: Package

**Project:** GenerateTnAReportsForStores  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        KODIAK_BABWTimeAndAttendance_conn(["KODIAK.BABWTimeAndAttendance [OLEDB]"])
        SMTP_EMAIL_conn(["SMTP_EMAIL [SMTP]"])
        SQL_LOG_conn(["SQL_LOG [OLEDB]"])
        STL_SSIS_P_01_IntegrationStaging_conn(["STL-SSIS-P-01.IntegrationStaging [OLEDB]"])
        StoreDataFile_conn(["StoreDataFile [FLATFILE]"])
    end
    subgraph ControlFlow
        Package_task["Package"]
        Foreach_Loop_Container_task["Foreach Loop Container"]
        Package_task --> Foreach_Loop_Container_task
        Export_Data_File_For_Store_task["Export Data File For Store"]
        Foreach_Loop_Container_task --> Export_Data_File_For_Store_task
        Get_list_of_distinct_stores_task["Get list of distinct stores"]
        Export_Data_File_For_Store_task --> Get_list_of_distinct_stores_task
        Move_the_yesterdays_data_to_staging_task["Move the yesterdays data to staging"]
        Get_list_of_distinct_stores_task --> Move_the_yesterdays_data_to_staging_task
        Truncate_Staging_Tables_task["Truncate Staging Tables"]
        Move_the_yesterdays_data_to_staging_task --> Truncate_Staging_Tables_task
        Send_Email_onError_task["Send Email onError"]
        Truncate_Staging_Tables_task --> Send_Email_onError_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| KODIAK.BABWTimeAndAttendance | OLEDB |
| SMTP_EMAIL | SMTP |
| SQL_LOG | OLEDB |
| STL-SSIS-P-01.IntegrationStaging | OLEDB |
| StoreDataFile | FLATFILE |

## Control Flow Tasks

| Task | Type |
|---|---|
| Package | Microsoft.Package |
| Foreach Loop Container | STOCK:FOREACHLOOP |
| Export Data File For Store | Microsoft.Pipeline |
| Get list of distinct stores | Microsoft.ExecuteSQLTask |
| Move the yesterdays data to staging | Microsoft.Pipeline |
| Truncate Staging Tables | Microsoft.ExecuteSQLTask |
| Send Email onError | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | SELECT        StoreId, POSCode, PunchInTime, PunchOutTime, JobCodeName, Status FROM            BABW_TnA_Staging WHERE        (StoreId = ?) |
|  | EXEC [dbo].[sp_GenerateDailyTimeAndAttendanceReport] @ReportStartDate = ?, @ReportEndDate = ? |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [BABW_TnA_Staging] |

