# SSIS Package: WMS_VendorMaster

**Project:** WMS_VendorMaster  
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
        WMS_VendorMaster_task["WMS_VendorMaster"]
        Seq___Download_and_Merge_task["Seq - Download and Merge"]
        WMS_VendorMaster_task --> Seq___Download_and_Merge_task
        Dataflow___VendorMaster_task[/"Dataflow - VendorMaster"/]
        Seq___Download_and_Merge_task --> Dataflow___VendorMaster_task
        Merge_VendorMaster_task["Merge VendorMaster"]
        Dataflow___VendorMaster_task --> Merge_VendorMaster_task
        Truncate_Stage_task["Truncate Stage"]
        Merge_VendorMaster_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
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
| WMS_VendorMaster | Microsoft.Package |
| Seq - Download and Merge | STOCK:SEQUENCE |
| Dataflow - VendorMaster | Microsoft.Pipeline |
| Merge VendorMaster | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [ERP].[VendorMasterStage] |

