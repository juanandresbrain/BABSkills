# SSIS Package: WMS_WholesalePurchaseOrderOnOrderData

**Project:** WMS_WholesalePurchaseOrderOnOrderData  
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
        WMS_WholesalePurchaseOrderOnOrderData_task["WMS_WholesalePurchaseOrderOnOrderData"]
        Sequence_Container_task["Sequence Container"]
        WMS_WholesalePurchaseOrderOnOrderData_task --> Sequence_Container_task
        DataFlow___Download_PO_Lines_task[/"DataFlow - Download PO Lines"/]
        Sequence_Container_task --> DataFlow___Download_PO_Lines_task
        Merge_PO_Lines_task["Merge PO Lines"]
        DataFlow___Download_PO_Lines_task --> Merge_PO_Lines_task
        Truncate_Stage_task["Truncate Stage"]
        Merge_PO_Lines_task --> Truncate_Stage_task
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
| WMS_WholesalePurchaseOrderOnOrderData | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| DataFlow - Download PO Lines | Microsoft.Pipeline |
| Merge PO Lines | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [WMS].[WholesaleOnOrderStage] |

