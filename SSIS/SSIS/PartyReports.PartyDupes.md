# SSIS Package: PartyDupes

**Project:** PartyReports  
**Folder:** SSIS  

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

| Connection Name | Type |
|---|---|
| stl-sqlaag-p-01.BABWPartyPlanner | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| PartyDupes | Microsoft.Package |
| spRPT_PartyBookingDuplicatesReport | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

