# SSIS Package: FinanceReportsPreFlightCheck

**Project:** FinanceReportsPreFlightCheck  
**Folder:** DW  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        dw_conn(["dw [OLEDB]"])
    end
    subgraph ControlFlow
        FinanceReportsPreFlightCheck_task["FinanceReportsPreFlightCheck"]
        Sequence_Container_task["Sequence Container"]
        FinanceReportsPreFlightCheck_task --> Sequence_Container_task
        PassFail_task["PassFail"]
        Sequence_Container_task --> PassFail_task
        RaiseError_task["RaiseError"]
        PassFail_task --> RaiseError_task
        Send_Email_task["Send Email"]
        RaiseError_task --> Send_Email_task
        spSQLJobHistory_task["spSQLJobHistory"]
        Send_Email_task --> spSQLJobHistory_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| dw | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| FinanceReportsPreFlightCheck | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| PassFail | Microsoft.ExecuteSQLTask |
| RaiseError | Microsoft.ExecuteSQLTask |
| Send Email | Microsoft.ExecuteSQLTask |
| spSQLJobHistory | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

