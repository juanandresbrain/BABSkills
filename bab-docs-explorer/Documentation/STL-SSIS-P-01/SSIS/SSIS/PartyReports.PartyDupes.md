# SSIS Package: PartyDupes

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
        PartyDupes_task["PartyDupes"]
        spRPT_PartyBookingDuplicatesReport_task["spRPT_PartyBookingDuplicatesReport"]
        PartyDupes_task --> spRPT_PartyBookingDuplicatesReport_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| stl-sqlaag-p-01.BABWPartyPlanner | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| PartyDupes | Microsoft.Package |
| spRPT_PartyBookingDuplicatesReport | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

