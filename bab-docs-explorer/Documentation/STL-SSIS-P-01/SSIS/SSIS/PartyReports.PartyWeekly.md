# SSIS Package: PartyWeekly

**Project:** PartyReports  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        stl_sqlaag_p_01_BABWPartyPlanner_conn(["stl-sqlaag-p-01.BABWPartyPlanner [OLEDB]"])
    end
    subgraph ControlFlow
        PartyWeekly_task["PartyWeekly"]
        spRPT_PartyBookingWeeklySummary___UK_task["spRPT_PartyBookingWeeklySummary - UK"]
        PartyWeekly_task --> spRPT_PartyBookingWeeklySummary___UK_task
        spRPT_PartyBookingWeeklySummary___US_task["spRPT_PartyBookingWeeklySummary - US"]
        spRPT_PartyBookingWeeklySummary___UK_task --> spRPT_PartyBookingWeeklySummary___US_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| stl-sqlaag-p-01.BABWPartyPlanner | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| PartyWeekly | Microsoft.Package |
| spRPT_PartyBookingWeeklySummary - UK | Microsoft.ExecuteSQLTask |
| spRPT_PartyBookingWeeklySummary - US | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

