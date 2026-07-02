# SSIS Package: WMS_DynamicsPOReceiptVsAptos

**Project:** WMS_DynamicsPOReceiptVsAptos  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        DW_conn(["DW [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
    end
    subgraph ControlFlow
        WMS_DynamicsPOReceiptVsAptos_task["WMS_DynamicsPOReceiptVsAptos"]
        Data_Flow_Task_task["Data Flow Task"]
        WMS_DynamicsPOReceiptVsAptos_task --> Data_Flow_Task_task
        Truncate_Stage_task["Truncate Stage"]
        Data_Flow_Task_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| DW | OLEDB |
| IntegrationStaging | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| WMS_DynamicsPOReceiptVsAptos | Microsoft.Package |
| Data Flow Task | Microsoft.Pipeline |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | select * from WMS.vwDynamicsPOReceiptVarianceVsAptos |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [Azure].[DynamicsPOReceiptVariances] |

