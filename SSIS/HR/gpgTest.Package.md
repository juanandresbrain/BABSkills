# SSIS Package: Package

**Project:** gpgTest  
**Folder:** HR  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph ControlFlow
        Package_task["Package"]
        Sequence_Container_task["Sequence Container"]
        Package_task --> Sequence_Container_task
        ps1_task["ps1"]
        Sequence_Container_task --> ps1_task
    end
```

## Connection Managers

_No connections found._

## Control Flow Tasks

| Task Name | Type |
|---|---|
| Package | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| ps1 | Microsoft.ExecuteProcess |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

