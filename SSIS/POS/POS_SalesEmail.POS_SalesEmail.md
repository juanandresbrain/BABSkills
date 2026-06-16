# SSIS Package: POS_SalesEmail

**Project:** POS_SalesEmail  
**Folder:** POS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        DW_conn(["DW [OLEDB]"])
        SMTP_Connection_Manager_conn(["SMTP Connection Manager [SMTP]"])
    end
    subgraph ControlFlow
        POS_SalesEmail_task["POS_SalesEmail"]
        Foreach_Loop_Container_task["Foreach Loop Container"]
        POS_SalesEmail_task --> Foreach_Loop_Container_task
        Send_Mail_Task_task["Send Mail Task"]
        Foreach_Loop_Container_task --> Send_Mail_Task_task
        Load_Sales_Into_Memory_task["Load Sales Into Memory"]
        Send_Mail_Task_task --> Load_Sales_Into_Memory_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| DW | OLEDB |
| SMTP Connection Manager | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| POS_SalesEmail | Microsoft.Package |
| Foreach Loop Container | STOCK:FOREACHLOOP |
| Send Mail Task | Microsoft.SendMailTask |
| Load Sales Into Memory | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

