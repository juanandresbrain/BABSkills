# SSIS Package: FlashGaapSales_AzureProcessing

**Project:** FlashGaapSales_AzureProcessing  
**Folder:** Azure  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        AZURE_conn(["AZURE [MSOLAP100]"])
    end
    subgraph ControlFlow
        FlashGaapSales_AzureProcessing_task["FlashGaapSales_AzureProcessing"]
        Analysis_Services_Processing_Task_task["Analysis Services Processing Task"]
        FlashGaapSales_AzureProcessing_task --> Analysis_Services_Processing_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| AZURE | MSOLAP100 |

## Control Flow Tasks

| Task | Type |
|---|---|
| FlashGaapSales_AzureProcessing | Microsoft.Package |
| Analysis Services Processing Task | Microsoft.DTSProcessingTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

