# SSIS Package: WMS_DynamicsContainer

**Project:** WMS_DynamicsContainer  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_DynamicsContainer_task["WMS_DynamicsContainer"]
        Dynamics_Container_Stage_task["Dynamics Container Stage"]
        WMS_DynamicsContainer_task --> Dynamics_Container_Stage_task
        Container_DataFlow_task["Container DataFlow"]
        Dynamics_Container_Stage_task --> Container_DataFlow_task
        Merge_DynamicsContainer_task["Merge DynamicsContainer"]
        Container_DataFlow_task --> Merge_DynamicsContainer_task
        Truncate_Stage_task["Truncate Stage"]
        Merge_DynamicsContainer_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| Dynamics AX Connection Manager | DynamicsAX |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| WMS_DynamicsContainer | Microsoft.Package |
| Dynamics Container Stage | STOCK:SEQUENCE |
| Container DataFlow | Microsoft.Pipeline |
| Merge DynamicsContainer | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [WMS].[DynamicsContainerStage] |

