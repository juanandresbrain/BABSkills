# SSIS Package: BrickDataNotification

**Project:** BrickDataNotification  
**Folder:** Brick project  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        BrickEngravingCSV_conn(["BrickEngravingCSV [FLATFILE]"])
        SMTP_conn(["SMTP [SMTP]"])
        WebOrderProcessing_conn(["WebOrderProcessing [OLEDB]"])
    end
    subgraph ControlFlow
        BrickDataNotification_task["BrickDataNotification"]
        Sequence_Container_task["Sequence Container"]
        BrickDataNotification_task --> Sequence_Container_task
        Data_Flow_Task_task["Data Flow Task"]
        Sequence_Container_task --> Data_Flow_Task_task
        Foreach_Loop_Container_task["Foreach Loop Container"]
        Data_Flow_Task_task --> Foreach_Loop_Container_task
        Archive_File_task["Archive File"]
        Foreach_Loop_Container_task --> Archive_File_task
        Send_Mail_Task_task["Send Mail Task"]
        Archive_File_task --> Send_Mail_Task_task
        Get_Row_Count_task["Get Row Count"]
        Send_Mail_Task_task --> Get_Row_Count_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| BrickEngravingCSV | FLATFILE |
| SMTP | SMTP |
| WebOrderProcessing | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| BrickDataNotification | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| Foreach Loop Container | STOCK:FOREACHLOOP |
| Archive File | Microsoft.FileSystemTask |
| Send Mail Task | Microsoft.SendMailTask |
| Get Row Count | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | with  CancelledOrders as 	( 		select o.OrderNumber 		from wm.orderstatus os with (nolock) 		join wm.Orders o with (nolock) on os.OrderID=o.OrderID 		where o.SourceSite = 'BABW-US' 		and os.CurrentStatus = 1 		and os.Status='Cancelled' 	) select  DISTINCT 		b.BQBrickID, 		b.OrderNumber, 		replace(b.EngraveLine1,',','') as EngraveLine1, 		replace(b.EngraveLine2,',','') as EngraveLine2, 		replace(b.E |
|  | Update BQ.BrickEngraving Set ExportDate=GetDate() where BQBrickID = ? |

## Data Flow: Destinations

_None detected._

