# SSIS Package: PartyMonthly

**Project:** PartyReports  
**Folder:** SSIS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        dw_conn(["dw [OLEDB]"])
        stl_sqlaag_p_01_BABWPartyPlanner_conn(["stl-sqlaag-p-01.BABWPartyPlanner [OLEDB]"])
    end
    subgraph ControlFlow
        PartyMonthly_task["PartyMonthly"]
        GoNoGo_task["GoNoGo"]
        PartyMonthly_task --> GoNoGo_task
        Sequence_Container_task["Sequence Container"]
        GoNoGo_task --> Sequence_Container_task
        MonthlySummary_UK_task["MonthlySummary-UK"]
        Sequence_Container_task --> MonthlySummary_UK_task
        MonthlySummary_US_task["MonthlySummary-US"]
        MonthlySummary_UK_task --> MonthlySummary_US_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| dw | OLEDB |
| stl-sqlaag-p-01.BABWPartyPlanner | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| PartyMonthly | Microsoft.Package |
| GoNoGo | Microsoft.ExecuteSQLTask |
| Sequence Container | STOCK:SEQUENCE |
| MonthlySummary-UK | Microsoft.ExecuteSQLTask |
| MonthlySummary-US | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

