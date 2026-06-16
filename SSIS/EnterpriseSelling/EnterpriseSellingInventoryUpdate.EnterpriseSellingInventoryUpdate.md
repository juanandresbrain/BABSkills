# SSIS Package: EnterpriseSellingInventoryUpdate

**Project:** EnterpriseSellingInventoryUpdate  
**Folder:** EnterpriseSelling  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        esell_conn(["esell [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
        WebOrderProcessing_conn(["WebOrderProcessing [OLEDB]"])
    end
    subgraph ControlFlow
        EnterpriseSellingInventoryUpdate_task["EnterpriseSellingInventoryUpdate"]
        SEQ___task["SEQ -"]
        EnterpriseSellingInventoryUpdate_task --> SEQ___task
        DataFlow___Load_StoreOrderQtyStage_task[/"DataFlow - Load StoreOrderQtyStage"/]
        SEQ___task --> DataFlow___Load_StoreOrderQtyStage_task
        spMergeEnterpriseSellingStoreOrderQty_task["spMergeEnterpriseSellingStoreOrderQty"]
        DataFlow___Load_StoreOrderQtyStage_task --> spMergeEnterpriseSellingStoreOrderQty_task
        spUpdateDigitalSoundsInfiniteInventory_task["spUpdateDigitalSoundsInfiniteInventory"]
        spMergeEnterpriseSellingStoreOrderQty_task --> spUpdateDigitalSoundsInfiniteInventory_task
        Truncate_Stage_task["Truncate Stage"]
        spUpdateDigitalSoundsInfiniteInventory_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| esell | OLEDB |
| SMTP | SMTP |
| WebOrderProcessing | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| EnterpriseSellingInventoryUpdate | Microsoft.Package |
| SEQ - | STOCK:SEQUENCE |
| DataFlow - Load StoreOrderQtyStage | Microsoft.Pipeline |
| spMergeEnterpriseSellingStoreOrderQty | Microsoft.ExecuteSQLTask |
| spUpdateDigitalSoundsInfiniteInventory | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select  	o.PickUpStore, 	oi.sku ItemNumber, 	sum(oi.qty) ItemQty from wm.Orders o with (nolock) join wm.OrderStatus os with (nolock)  	on o.OrderID=os.OrderID 	and os.CurrentStatus=1 	and os.[Status] not in ('Cancelled', 'Complete', 'Shipped')  join wm.OrderItems oi with (nolock)  	on o.OrderID=oi.OrderID where 1=1 and isnull(o.PickUpStore,'') not in ('', '2013','0013') and len(oi.sku) = 6 group b |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[StoreOrderQtyStage] |

