# SSIS Package: FlashGaapSales_AzureProcessing

**Project:** FlashGaapSales_AzureProcessing  
**Folder:** Azure  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| AZURE | MSOLAP100 | asazure://northcentralus.asazure.windows.net/azasp01 | FlashGaapSales | Data Source=asazure://northcentralus.asazure.windows.net/azasp01; Initial Catalog=FlashGaapSales; Provider=MSOLAP.7 |

## Control Flow Tasks

| Task | Type |
|---|---|
| FlashGaapSales_AzureProcessing | Package |
| Analysis Services Processing Task | DTSProcessingTask |

## Control Flow Outline

```text
- Analysis Services Processing Task [DTSProcessingTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Analysis_Services_Processing_Task["Analysis Services Processing Task"]
```

## Variables

_None detected._

## Execute SQL Tasks

_None detected._

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._
