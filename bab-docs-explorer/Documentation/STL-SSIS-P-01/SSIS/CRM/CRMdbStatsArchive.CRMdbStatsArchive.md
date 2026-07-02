# SSIS Package: CRMdbStatsArchive

**Project:** CRMdbStatsArchive  
**Folder:** CRM  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        a0_conn(["a0 [ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]"])
        a1_conn(["a1 [ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]"])
        a2_conn(["a2 [ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]"])
        CDS_ALL_conn(["CDS_ALL [Excel (KingswaySoft)]"])
        CDS_UK_IE_conn(["CDS_UK_IE [Excel (KingswaySoft)]"])
        CDS_US_CA_conn(["CDS_US_CA [Excel (KingswaySoft)]"])
        CRM_DB_Stats_conn(["CRM_DB_Stats [Excel (KingswaySoft)]"])
        DW_conn(["DW [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        CRMdbStatsArchive_task["CRMdbStatsArchive"]
        is_first_Sunday_of_new_period__task["is first Sunday of new period?"]
        CRMdbStatsArchive_task --> is_first_Sunday_of_new_period__task
        Send_Mail_Task_task["Send Mail Task"]
        is_first_Sunday_of_new_period__task --> Send_Mail_Task_task
        Sequence_Container_task["Sequence Container"]
        Send_Mail_Task_task --> Sequence_Container_task
        5_second_pause_1_1_task["5 second pause 1 1"]
        Sequence_Container_task --> 5_second_pause_1_1_task
        5_second_pause_1_1_1_task["5 second pause 1 1 1"]
        5_second_pause_1_1_task --> 5_second_pause_1_1_1_task
        send_file_to_sharebear_task["send file to sharebear"]
        5_second_pause_1_1_1_task --> send_file_to_sharebear_task
        Sequence_Container_task["Sequence Container"]
        send_file_to_sharebear_task --> Sequence_Container_task
        total_sheet_task["total sheet"]
        Sequence_Container_task --> total_sheet_task
        Sequence_Container_1_task["Sequence Container 1"]
        total_sheet_task --> Sequence_Container_1_task
        US_CA_sheet_task["US_CA sheet"]
        Sequence_Container_1_task --> US_CA_sheet_task
        Sequence_Container_1_1_task["Sequence Container 1 1"]
        US_CA_sheet_task --> Sequence_Container_1_1_task
        UK_IE_sheet_task["UK_IE sheet"]
        Sequence_Container_1_1_task --> UK_IE_sheet_task
        Send_Mail_Task_task["Send Mail Task"]
        UK_IE_sheet_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| a0 | ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089 |
| a1 | ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089 |
| a2 | ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089 |
| CDS_ALL | Excel (KingswaySoft) |
| CDS_UK_IE | Excel (KingswaySoft) |
| CDS_US_CA | Excel (KingswaySoft) |
| CRM_DB_Stats | Excel (KingswaySoft) |
| DW | OLEDB |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| CRMdbStatsArchive | Microsoft.Package |
| is first Sunday of new period? | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |
| Sequence Container | STOCK:SEQUENCE |
| 5 second pause 1 1 | STOCK:FORLOOP |
| 5 second pause 1 1 1 | STOCK:FORLOOP |
| send file to sharebear | Microsoft.FileSystemTask |
| Sequence Container | STOCK:SEQUENCE |
| total sheet | Microsoft.Pipeline |
| Sequence Container 1 | STOCK:SEQUENCE |
| US_CA sheet | Microsoft.Pipeline |
| Sequence Container 1 1 | STOCK:SEQUENCE |
| UK_IE sheet | Microsoft.Pipeline |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

