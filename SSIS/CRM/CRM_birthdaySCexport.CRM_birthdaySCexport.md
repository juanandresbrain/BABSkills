# SSIS Package: CRM_birthdaySCexport

**Project:** CRM_birthdaySCexport  
**Folder:** CRM  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        12M_conn(["12M [CACHE]"])
        18M_conn(["18M [CACHE]"])
        1M_conn(["1M [CACHE]"])
        24M_conn(["24M [CACHE]"])
        3M_conn(["3M [CACHE]"])
        6M_conn(["6M [CACHE]"])
        archive_conn(["archive [FILE]"])
        birthday_export_csv_conn(["birthday_export.csv [FILE]"])
        cDim_conn(["cDim [CACHE]"])
        CRM_conn(["CRM [OLEDB]"])
        delta_conn(["delta [EXCEL]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        Flat_File_Connection_Manager_conn(["Flat File Connection Manager [FLATFILE]"])
        SMTP_conn(["SMTP [SMTP]"])
        STL_SSIS_P_01_IntegrationStaging_conn(["STL-SSIS-P-01.IntegrationStaging [OLEDB]"])
    end
    subgraph ControlFlow
        CRM_birthdaySCexport_task["CRM_birthdaySCexport"]
        Sequence_Container_task["Sequence Container"]
        CRM_birthdaySCexport_task --> Sequence_Container_task
        archive_task["archive"]
        Sequence_Container_task --> archive_task
        bday_stage_task[/"bday_stage"/]
        archive_task --> bday_stage_task
        delete_task["delete"]
        bday_stage_task --> delete_task
        truncate_tmpCrmDe2_SC_task["truncate tmpCrmDe2_SC"]
        delete_task --> truncate_tmpCrmDe2_SC_task
        Send_Mail_Task_task["Send Mail Task"]
        truncate_tmpCrmDe2_SC_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| 12M | CACHE |
| 18M | CACHE |
| 1M | CACHE |
| 24M | CACHE |
| 3M | CACHE |
| 6M | CACHE |
| archive | FILE |
| birthday_export.csv | FILE |
| cDim | CACHE |
| CRM | OLEDB |
| delta | EXCEL |
| DW | OLEDB |
| DWStaging | OLEDB |
| Flat File Connection Manager | FLATFILE |
| SMTP | SMTP |
| STL-SSIS-P-01.IntegrationStaging | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| CRM_birthdaySCexport | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| archive | Microsoft.FileSystemTask |
| bday_stage | Microsoft.Pipeline |
| delete | Microsoft.FileSystemTask |
| truncate tmpCrmDe2_SC | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[tmpCrmDe2_SC] |

