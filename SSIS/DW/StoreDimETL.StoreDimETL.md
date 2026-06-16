# SSIS Package: StoreDimETL

**Project:** StoreDimETL  
**Folder:** DW  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        BABWMstrData_conn(["BABWMstrData [OLEDB]"])
        Bearhouse_conn(["Bearhouse [OLEDB]"])
        BearwebDB_conn(["BearwebDB [OLEDB]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        Kodiak_conn(["Kodiak [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
        WebCart_Commerce_conn(["WebCart_Commerce [OLEDB]"])
    end
    subgraph ControlFlow
        StoreDimETL_task["StoreDimETL"]
        Copy_Store_Dim_task["Copy Store Dim"]
        StoreDimETL_task --> Copy_Store_Dim_task
        Merge_StoreDim_Sequence_task["Merge StoreDim Sequence"]
        Copy_Store_Dim_task --> Merge_StoreDim_Sequence_task
        Merge_StoreDim___BearData_task["Merge StoreDim - BearData"]
        Merge_StoreDim_Sequence_task --> Merge_StoreDim___BearData_task
        Merge_StoreDim___BearHouse_task["Merge StoreDim - BearHouse"]
        Merge_StoreDim___BearData_task --> Merge_StoreDim___BearHouse_task
        Merge_StoreDim___Locations_task["Merge StoreDim - Locations"]
        Merge_StoreDim___BearHouse_task --> Merge_StoreDim___Locations_task
        Merge_StoreDim___WebCartCommerce_task["Merge StoreDim - WebCartCommerce"]
        Merge_StoreDim___Locations_task --> Merge_StoreDim___WebCartCommerce_task
        StoreDimStage_task[/"StoreDimStage"/]
        Merge_StoreDim___WebCartCommerce_task --> StoreDimStage_task
        Truncate_Stage_Sequence_task["Truncate Stage Sequence"]
        StoreDimStage_task --> Truncate_Stage_Sequence_task
        Truncate_Stage_BearwebDB_task["Truncate Stage BearwebDB"]
        Truncate_Stage_Sequence_task --> Truncate_Stage_BearwebDB_task
        Truncate_Stage_Kodiak_task["Truncate Stage Kodiak"]
        Truncate_Stage_BearwebDB_task --> Truncate_Stage_Kodiak_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_Kodiak_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| BABWMstrData | OLEDB |
| Bearhouse | OLEDB |
| BearwebDB | OLEDB |
| DW | OLEDB |
| DWStaging | OLEDB |
| IntegrationStaging | OLEDB |
| Kodiak | OLEDB |
| SMTP | SMTP |
| WebCart_Commerce | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| StoreDimETL | Microsoft.Package |
| Copy Store Dim | STOCK:SEQUENCE |
| Merge StoreDim Sequence | STOCK:SEQUENCE |
| Merge StoreDim - BearData | Microsoft.ExecuteSQLTask |
| Merge StoreDim - BearHouse | Microsoft.ExecuteSQLTask |
| Merge StoreDim - Locations | Microsoft.ExecuteSQLTask |
| Merge StoreDim - WebCartCommerce | Microsoft.ExecuteSQLTask |
| StoreDimStage | Microsoft.Pipeline |
| Truncate Stage Sequence | STOCK:SEQUENCE |
| Truncate Stage BearwebDB | Microsoft.ExecuteSQLTask |
| Truncate Stage Kodiak | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[store_dim] |
|  | [dbo].[StoreDimStage] |
|  | [dbo].[StoreDimStage] |
|  | [dbo].[StoreDimStage] |

