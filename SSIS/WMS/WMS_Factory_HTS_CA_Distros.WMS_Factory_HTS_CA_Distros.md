# SSIS Package: WMS_Factory_HTS_CA_Distros

**Project:** WMS_Factory_HTS_CA_Distros  
**Folder:** WMS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Cache___SalesOrderItems_conn(["Cache - SalesOrderItems [CACHE]"])
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_Factory_HTS_CA_Distros_task["WMS_Factory_HTS_CA_Distros"]
        Sequence_Container_task["Sequence Container"]
        WMS_Factory_HTS_CA_Distros_task --> Sequence_Container_task
        Cache_Order_Items_task[/"Cache Order Items"/]
        Sequence_Container_task --> Cache_Order_Items_task
        Generate_CSV_task[/"Generate CSV"/]
        Cache_Order_Items_task --> Generate_CSV_task
        Send_Mail_Task_task["Send Mail Task"]
        Generate_CSV_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Cache - SalesOrderItems | CACHE |
| Dynamics AX Connection Manager | DynamicsAX |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WMS_Factory_HTS_CA_Distros | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Cache Order Items | Microsoft.Pipeline |
| Generate CSV | Microsoft.Pipeline |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select ProductNumber, ProductName, HarmonizedSystemCode, CountryOfOrigin from [WMS].[vwItemsWithoutHTS_COO_Factory] where isnull(HarmonizedSystemCode,'')='' or isnull(CountryOfOrigin,'') ='' |

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

