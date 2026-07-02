# SSIS Package: PCHealthChecks

**Project:** PCHealthChecks  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Azure_conn(["Azure [MSOLAP100]"])
        DW_conn(["DW [OLEDB]"])
        KODIAK_conn(["KODIAK [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        PCHealthChecks_task["PCHealthChecks"]
        Analysis_Services_Processing_Task___Reload_PC_Health_Checks_Table_in_Azure_task["Analysis Services Processing Task - Reload PC Health Checks Table in Azure"]
        PCHealthChecks_task --> Analysis_Services_Processing_Task___Reload_PC_Health_Checks_Table_in_Azure_task
        Sequence_Container_task["Sequence Container"]
        Analysis_Services_Processing_Task___Reload_PC_Health_Checks_Table_in_Azure_task --> Sequence_Container_task
        Load_StoreStation_Data_to_DW_task["Load StoreStation Data to DW"]
        Sequence_Container_task --> Load_StoreStation_Data_to_DW_task
        Truncate_PCHealthChecks_Table_in_DW_task["Truncate PCHealthChecks Table in DW"]
        Load_StoreStation_Data_to_DW_task --> Truncate_PCHealthChecks_Table_in_DW_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_PCHealthChecks_Table_in_DW_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| Azure | MSOLAP100 |
| DW | OLEDB |
| KODIAK | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| PCHealthChecks | Microsoft.Package |
| Analysis Services Processing Task - Reload PC Health Checks Table in Azure | Microsoft.DTSProcessingTask |
| Sequence Container | STOCK:SEQUENCE |
| Load StoreStation Data to DW | Microsoft.Pipeline |
| Truncate PCHealthChecks Table in DW | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | select Hostname, isnull(Store,SUBSTRING(Hostname,4,4))as Store,  Role, Model, GoPostReportErrors, GoPostReportWarnings, (Select top 1 Description from OsdStatusMessages where OsdStatusMessages.HostID=StoreStations.id order by Date desc) Description, (Select top 1 Status from OsdStatusMessages where OsdStatusMessages.HostID=StoreStations.id order by Date desc) Status, (Select top 1 Date from OsdSta |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [Azure].[PCHealthChecks] |

