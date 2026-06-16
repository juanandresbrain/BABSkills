# SSIS Package: WMS_WarehouseMaster

**Project:** WMS_WarehouseMaster  
**Folder:** WMS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_WarehouseMaster_task["WMS_WarehouseMaster"]
        SEQ___WarehouseMaster_task["SEQ - WarehouseMaster"]
        WMS_WarehouseMaster_task --> SEQ___WarehouseMaster_task
        Merge_WarehouseMaster_task["Merge WarehouseMaster"]
        SEQ___WarehouseMaster_task --> Merge_WarehouseMaster_task
        Truncate_Stage_task["Truncate Stage"]
        Merge_WarehouseMaster_task --> Truncate_Stage_task
        WarehouseMaster_task[/"WarehouseMaster"/]
        Truncate_Stage_task --> WarehouseMaster_task
        Send_Mail_Task_task["Send Mail Task"]
        WarehouseMaster_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Dynamics AX Connection Manager | DynamicsAX |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WMS_WarehouseMaster | Microsoft.Package |
| SEQ - WarehouseMaster | STOCK:SEQUENCE |
| Merge WarehouseMaster | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| WarehouseMaster | Microsoft.Pipeline |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [ERP].[WarehouseMasterStage] |
|  | [WMS].[WarehouseMasterFail] |

