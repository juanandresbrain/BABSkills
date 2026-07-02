# SSIS Package: ThriveETL

**Project:** ThriveETL  
**Folder:** CRM  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        BABWPartyPlanner_conn(["BABWPartyPlanner [OLEDB]"])
        dw_conn(["dw [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        Flat_File_Connection_Manager_conn(["Flat File Connection Manager [FLATFILE]"])
        PartyRequest_conn(["PartyRequest [OLEDB]"])
        SMTP_EMAIL_conn(["SMTP_EMAIL [SMTP]"])
    end
    subgraph ControlFlow
        ThriveETL_task["ThriveETL"]
        run_once_task["run once"]
        ThriveETL_task --> run_once_task
        daily_file_create_task["daily file create"]
        run_once_task --> daily_file_create_task
        upload_files_task["upload files"]
        daily_file_create_task --> upload_files_task
        daily_file_create_task["daily file create"]
        upload_files_task --> daily_file_create_task
        Foreach_Loop___Move_to_Archive_task["Foreach Loop - Move to Archive"]
        daily_file_create_task --> Foreach_Loop___Move_to_Archive_task
        Archive_File_task["Archive File"]
        Foreach_Loop___Move_to_Archive_task --> Archive_File_task
        FTP_script_task["FTP script"]
        Archive_File_task --> FTP_script_task
        rename_file_task["rename file"]
        FTP_script_task --> rename_file_task
        Send_Email_onError_task["Send Email onError"]
        rename_file_task --> Send_Email_onError_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| BABWPartyPlanner | OLEDB |
| dw | OLEDB |
| DWStaging | OLEDB |
| Flat File Connection Manager | FLATFILE |
| PartyRequest | OLEDB |
| SMTP_EMAIL | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| ThriveETL | Microsoft.Package |
| run once | STOCK:SEQUENCE |
| daily file create | Microsoft.Pipeline |
| upload files | STOCK:SEQUENCE |
| daily file create | Microsoft.Pipeline |
| Foreach Loop - Move to Archive | STOCK:FOREACHLOOP |
| Archive File | Microsoft.FileSystemTask |
| FTP script | Microsoft.ExecuteSQLTask |
| rename file | Microsoft.FileSystemTask |
| Send Email onError | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | ; with tra as ( SELECT DD.actual_date, SD.store_id, SD.store_name, SD.postal_code, SUM(STF.Exits) AS Traffic --INTO #tra FROM DBO.ShopperTrackFact STF WITH (NOLOCK) JOIN DBO.store_dim SD WITH (NOLOCK) ON STF.STOREKEY = SD.STORE_KEY JOIN DBO.date_dim DD WITH (NOLOCK) ON STF.DATEKEY = DD.DATE_KEY --WHERE DD.actual_date between '2019-02-03' and '2022-04-02' where cast(DD.actual_date as date) between  |
|  | ; with tra as ( SELECT DD.actual_date, SD.store_id, SD.store_name, SD.postal_code, SUM(STF.Exits) AS Traffic --INTO #tra FROM DBO.ShopperTrackFact STF WITH (NOLOCK) JOIN DBO.store_dim SD WITH (NOLOCK) ON STF.STOREKEY = SD.STORE_KEY JOIN DBO.date_dim DD WITH (NOLOCK) ON STF.DATEKEY = DD.DATE_KEY --WHERE DD.actual_date between '2019-02-03' and '2022-04-02' where cast(DD.actual_date as date) between  |

## Data Flow: Destinations

_None detected._

