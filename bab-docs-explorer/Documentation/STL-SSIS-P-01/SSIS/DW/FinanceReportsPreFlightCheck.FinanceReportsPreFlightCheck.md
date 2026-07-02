# SSIS Package: FinanceReportsPreFlightCheck

**Project:** FinanceReportsPreFlightCheck  
**Folder:** DW  
**Server:** STL-SSIS-P-01  

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

| Name | Type |
|---|---|
| dw | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| FinanceReportsPreFlightCheck | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| PassFail | Microsoft.ExecuteSQLTask |
| RaiseError | Microsoft.ExecuteSQLTask |
| Send Email | Microsoft.ExecuteSQLTask |
| spSQLJobHistory | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

