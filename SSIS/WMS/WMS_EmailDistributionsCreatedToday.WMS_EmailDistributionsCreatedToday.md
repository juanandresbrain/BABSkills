# SSIS Package: WMS_EmailDistributionsCreatedToday

**Project:** WMS_EmailDistributionsCreatedToday  
**Folder:** WMS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Cache___OrderItems_conn(["Cache - OrderItems [CACHE]"])
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        me_01_conn(["me_01 [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_EmailDistributionsCreatedToday_task["WMS_EmailDistributionsCreatedToday"]
        Sequence_Container_task["Sequence Container"]
        WMS_EmailDistributionsCreatedToday_task --> Sequence_Container_task
        Cache_Order_Items_task[/"Cache Order Items"/]
        Sequence_Container_task --> Cache_Order_Items_task
        Emails_task["Emails"]
        Cache_Order_Items_task --> Emails_task
        Order_DataFlow_task[/"Order DataFlow"/]
        Emails_task --> Order_DataFlow_task
        Truncate_Stage_task["Truncate Stage"]
        Order_DataFlow_task --> Truncate_Stage_task
        Truncate_Stage_me_01_task["Truncate Stage me_01"]
        Truncate_Stage_task --> Truncate_Stage_me_01_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Cache - OrderItems | CACHE |
| Dynamics AX Connection Manager | DynamicsAX |
| IntegrationStaging | OLEDB |
| me_01 | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WMS_EmailDistributionsCreatedToday | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Cache Order Items | Microsoft.Pipeline |
| Emails | Microsoft.ExecuteSQLTask |
| Order DataFlow | Microsoft.Pipeline |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Truncate Stage me_01 | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select  	im.ItemNumber,  	coalesce( 				case when p.ProductName='' then Null else p.ProductName end, 				case when p.ProductSearchName='' then Null else p.ProductSearchName end, 				case when p.ProductDescription='' then Null else p.ProductDescription end 			) as ProductDescription from WMS.ItemMaster im with (nolock) join wms.ItemMasterProducts p with (nolock) on im.ItemNumber=p.ProductNumber whe |
|  |  | select  --	WarehouseID, 	LocationCode, 	PrimaryAddressDescription from erp.vwWarehouseIDToLocationCode where Entity=1100 |
|  |  | select  cast(WarehouseID as nvarchar) as WarehouseID,  	LocationCode from erp.vwWarehouseIDToLocationCode  where Entity=1100 |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [tmpDynamicsOrderItems] |
|  | [dbo].[tmpDynamicsOrderItems] |
|  | [tmpSupplyOrdersStaged] |

