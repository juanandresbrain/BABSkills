# SSIS Package: Package

**Project:** gpgTest  
**Folder:** HR  
**Server:** STL-SSIS-P-01  

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

_None detected._

## Control Flow Tasks

| Task | Type |
|---|---|
| Package | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| ps1 | Microsoft.ExecuteProcess |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

