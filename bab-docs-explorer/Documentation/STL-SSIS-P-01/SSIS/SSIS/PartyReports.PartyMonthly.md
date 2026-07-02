# SSIS Package: PartyMonthly

**Project:** PartyReports  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

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

| Name | Type |
|---|---|
| dw | OLEDB |
| stl-sqlaag-p-01.BABWPartyPlanner | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| PartyMonthly | Microsoft.Package |
| GoNoGo | Microsoft.ExecuteSQLTask |
| Sequence Container | STOCK:SEQUENCE |
| MonthlySummary-UK | Microsoft.ExecuteSQLTask |
| MonthlySummary-US | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

