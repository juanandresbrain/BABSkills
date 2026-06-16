# SSIS Package: WMS_WebSalesOrderDownloadFromDynamics

**Project:** WMS_WebSalesOrderDownloadFromDynamics  
**Folder:** WMS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        BEARCLUSTER01_SQL_BUILDABEAR_COM_WebOrderProcessing_conn(["BEARCLUSTER01.SQL.BUILDABEAR.COM.WebOrderProcessing [OLEDB]"])
        Cache_OrderLine_conn(["Cache OrderLine [CACHE]"])
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_WebSalesOrderDownloadFromDynamics_task["WMS_WebSalesOrderDownloadFromDynamics"]
        SEQ___Data_Extract_task["SEQ - Data Extract"]
        WMS_WebSalesOrderDownloadFromDynamics_task --> SEQ___Data_Extract_task
        DataFlow___Order_Data_Extract_task[/"DataFlow - Order Data Extract"/]
        SEQ___Data_Extract_task --> DataFlow___Order_Data_Extract_task
        Merge_AgedWebOrdersInDynamics_task["Merge AgedWebOrdersInDynamics"]
        DataFlow___Order_Data_Extract_task --> Merge_AgedWebOrdersInDynamics_task
        Truncate_Stage_task["Truncate Stage"]
        Merge_AgedWebOrdersInDynamics_task --> Truncate_Stage_task
        SEQ___Dupes_task["SEQ - Dupes"]
        Truncate_Stage_task --> SEQ___Dupes_task
        DataFlow___Order_Data_Extract_task[/"DataFlow - Order Data Extract"/]
        SEQ___Dupes_task --> DataFlow___Order_Data_Extract_task
        Send_Mail_Task_task["Send Mail Task"]
        DataFlow___Order_Data_Extract_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| BEARCLUSTER01.SQL.BUILDABEAR.COM.WebOrderProcessing | OLEDB |
| Cache OrderLine | CACHE |
| Dynamics AX Connection Manager | DynamicsAX |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WMS_WebSalesOrderDownloadFromDynamics | Microsoft.Package |
| SEQ - Data Extract | STOCK:SEQUENCE |
| DataFlow - Order Data Extract | Microsoft.Pipeline |
| Merge AgedWebOrdersInDynamics | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| SEQ - Dupes | STOCK:SEQUENCE |
| DataFlow - Order Data Extract | Microsoft.Pipeline |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select OrderDate, cast(OrderNum as nvarchar(10)) as OrderNum from wm.Orders |
|  |  | with  DeckStatuses as 	( 		select  			OrderNumber as DeckOrderNumber, 			case  				when CurrentItemStatus='Cancelled' or Cancelled is not null  					then 'Cancelled' 				when CurrentItemStatus='Shipped' or isnull(isnull(shipped,StoreShipped),GiftCardProcessed) is not null 					then 'Shipped' 			end as OrderStatus 		from wm.vwDeckOrderItemStatusPivot 		where  			( 				CurrentItemStatus in ('Cancell |
|  |  | select cast(OrderNum as nvarchar) as OrderNum from wms.SalesOrderStatusUpdateShipped with (nolock) group by cast(OrderNum as nvarchar) |
|  |  | select  	cast(wo.SalesOrderNumber as nvarchar) SalesOrderNumber, 	wo.WebOrderNumber  from wms.vwWebOrderSalesOrderLookup wo group by  cast(wo.SalesOrderNumber as nvarchar), wo.WebOrderNumber |
|  |  | with MaxWave as 	( 		select 			OrderNum, max(WaveID) as WaveID 		from WMS.SalesOrderStatusUpdateWaved with (nolock) 		group by OrderNum 	) select  	wa.WaveID, 	wa.ReleasedDateAndTime, 	wa.ContainerID, 	wa.WorkID, 	cast(wa.OrderNum as nvarchar) as OrderNum, 	wa.ItemID from WMS.SalesOrderStatusUpdateWaved wa with (nolock) --join MaxWave mw on wa.WaveID=mw.WaveID where exists (select mw.WaveID from M |
|  |  | select  	cast(wo.SalesOrderNumber as nvarchar) SalesOrderNumber, 	wo.WebOrderNumber  from wms.vwWebOrderSalesOrderLookup wo group by  cast(wo.SalesOrderNumber as nvarchar), wo.WebOrderNumber |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [WMS].[AgedWebOrdersInDynamicsStage] |

