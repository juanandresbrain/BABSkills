# SSIS Package: PartyReports

**Project:** PartyReports  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        BABWPartyPlanner_conn(["BABWPartyPlanner [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        me_01_conn(["me_01 [OLEDB]"])
    end
    subgraph ControlFlow
        PartyReports_task["PartyReports"]
        Party_Reports_Daily_Emails_task["Party Reports Daily Emails"]
        PartyReports_task --> Party_Reports_Daily_Emails_task
        Girl_Scouts_task["Girl Scouts"]
        Party_Reports_Daily_Emails_task --> Girl_Scouts_task
        UK_task["UK"]
        Girl_Scouts_task --> UK_task
        US_task["US"]
        UK_task --> US_task
        Web_Party_Transfer_Report_task["Web Party Transfer Report"]
        US_task --> Web_Party_Transfer_Report_task
        Send_Email_Summary_task["Send Email Summary"]
        Web_Party_Transfer_Report_task --> Send_Email_Summary_task
        Stage_Report_Data_task["Stage Report Data"]
        Send_Email_Summary_task --> Stage_Report_Data_task
        Truncate_Stage_task["Truncate Stage"]
        Stage_Report_Data_task --> Truncate_Stage_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| BABWPartyPlanner | OLEDB |
| IntegrationStaging | OLEDB |
| me_01 | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| PartyReports | Microsoft.Package |
| Party Reports Daily Emails | STOCK:SEQUENCE |
| Girl Scouts | Microsoft.ExecuteSQLTask |
| UK | Microsoft.ExecuteSQLTask |
| US | Microsoft.ExecuteSQLTask |
| Web Party Transfer Report | STOCK:SEQUENCE |
| Send Email Summary | Microsoft.ExecuteSQLTask |
| Stage Report Data | Microsoft.Pipeline |
| Truncate Stage | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [WEB].[PartyTransferOrdersShipped] |
|  | [WEB].[vwPartyWebOrdersShipped] |

