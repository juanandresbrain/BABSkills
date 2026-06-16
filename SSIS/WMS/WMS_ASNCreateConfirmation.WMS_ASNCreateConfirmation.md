# SSIS Package: WMS_ASNCreateConfirmation

**Project:** WMS_ASNCreateConfirmation  
**Folder:** WMS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Azure_Service_Bus_conn(["Azure Service Bus [Azure Service Bus (KingswaySoft)]"])
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_ASNCreateConfirmation_task["WMS_ASNCreateConfirmation"]
        Sequence_Container_task["Sequence Container"]
        WMS_ASNCreateConfirmation_task --> Sequence_Container_task
        Capture__Service_Bus_Messages_task[/"Capture  Service Bus Messages"/]
        Sequence_Container_task --> Capture__Service_Bus_Messages_task
        spMergeASNCreateConfirmation_task["spMergeASNCreateConfirmation"]
        Capture__Service_Bus_Messages_task --> spMergeASNCreateConfirmation_task
        Truncate_Stage_task["Truncate Stage"]
        spMergeASNCreateConfirmation_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Azure Service Bus | Azure Service Bus (KingswaySoft) |
| Dynamics AX Connection Manager | DynamicsAX |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WMS_ASNCreateConfirmation | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Capture  Service Bus Messages | Microsoft.Pipeline |
| spMergeASNCreateConfirmation | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [WMS].[ASN_CreateConfirmationStage] |

