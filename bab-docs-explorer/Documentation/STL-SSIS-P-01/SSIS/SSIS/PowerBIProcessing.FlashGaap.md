# SSIS Package: FlashGaap

**Project:** PowerBIProcessing  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

_None detected._

## Control Flow Tasks

| Task | Type |
|---|---|
| FlashGaap | Package |
| Analysis Services Processing Task | DTSProcessingTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- Analysis Services Processing Task [DTSProcessingTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Analysis_Services_Processing_Task["Analysis Services Processing Task"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |

## Execute SQL Tasks

_None detected._

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._
