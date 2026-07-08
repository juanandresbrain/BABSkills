# SSIS Package: PartyGiftCardBalancing

**Project:** PartyReports  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| stl-sqlaag-p-01.BABWPartyPlanner | OLEDB | stl-sqlaag-p-01 | BABWPartyPlanner | Data Source=stl-sqlaag-p-01; Initial Catalog=BABWPartyPlanner; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| PartyGiftCardBalancing | Package |
| spRPT_PartyGCBalancingReport | ExecuteSQLTask |

## Control Flow Outline

```text
- spRPT_PartyGCBalancingReport [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_spRPT_PartyGCBalancingReport["spRPT_PartyGCBalancingReport"]
```

## Variables

_None detected._

## Execute SQL Tasks

### spRPT_PartyGCBalancingReport

**Path:** `Package\spRPT_PartyGCBalancingReport`  
**Connection:** stl-sqlaag-p-01.BABWPartyPlanner (stl-sqlaag-p-01/BABWPartyPlanner)  

```sql
exec spRPT_PartyGCBalancingReport @ac_recipients = 'kevinpa@buildabear.com;ArtH@buildabear.com;SheelaA@buildabear.com;'
```

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._
