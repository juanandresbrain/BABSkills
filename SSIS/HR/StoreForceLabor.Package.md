# SSIS Package: Package

**Project:** StoreForceLabor  
**Folder:** HR  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Auditworks_conn(["Auditworks [OLEDB]"])
        CRM_conn(["CRM [OLEDB]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        Excel_Connection_Manager_conn(["Excel Connection Manager [EXCEL]"])
        Excel_Connection_Manager_1_conn(["Excel Connection Manager 1 [EXCEL]"])
        Flat_File_Connection_Manager_conn(["Flat File Connection Manager [FLATFILE]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        ME_01_conn(["ME_01 [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        Package_task["Package"]
        Foreach_Loop_Archive_task["Foreach Loop Archive"]
        Package_task --> Foreach_Loop_Archive_task
        Archive_File_task["Archive File"]
        Foreach_Loop_Archive_task --> Archive_File_task
        Generate_CSV_task[/"Generate CSV"/]
        Archive_File_task --> Generate_CSV_task
        sFTP_Upload_task["sFTP Upload"]
        Generate_CSV_task --> sFTP_Upload_task
        Send_Mail_Task_task["Send Mail Task"]
        sFTP_Upload_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Auditworks | OLEDB |
| CRM | OLEDB |
| DW | OLEDB |
| DWStaging | OLEDB |
| Excel Connection Manager | EXCEL |
| Excel Connection Manager 1 | EXCEL |
| Flat File Connection Manager | FLATFILE |
| IntegrationStaging | OLEDB |
| ME_01 | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| Package | Microsoft.Package |
| Foreach Loop Archive | STOCK:FOREACHLOOP |
| Archive File | Microsoft.FileSystemTask |
| Generate CSV | Microsoft.Pipeline |
| sFTP Upload | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | With Dates as ( select Max(StartDate) as StartDate, Max(EndDate) as EndDate from PayPeriodDates Where StartDate < GetDate()  --and datediff(dd, StartDate, Getdate()) >= 14 and EndDate < GetDate() )  select *  from vwStoreForceLabor vw Join Dates d On vw.WorkDate between d.StartDate and d.EndDate |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [Azure].[DailyInvAvailToDist] |

