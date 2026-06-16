# SSIS Package: PartyGiftCardBalancing

**Project:** PartyReports  
**Folder:** SSIS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        stl_sqlaag_p_01_BABWPartyPlanner_conn(["stl-sqlaag-p-01.BABWPartyPlanner [OLEDB]"])
    end
    subgraph ControlFlow
        PartyGiftCardBalancing_task["PartyGiftCardBalancing"]
        spRPT_PartyGCBalancingReport_task["spRPT_PartyGCBalancingReport"]
        PartyGiftCardBalancing_task --> spRPT_PartyGCBalancingReport_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| stl-sqlaag-p-01.BABWPartyPlanner | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| PartyGiftCardBalancing | Microsoft.Package |
| spRPT_PartyGCBalancingReport | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

