# SSIS Package: PricingData

**Project:** PricingData  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

_None detected._

## Control Flow Tasks

| Task | Type |
|---|---|
| PricingData | SSIS.Package.3 |
| Execute SQL Task | SqlServer.Dts.Tasks.ExecuteSQLTask.ExecuteSQLTask, SqlServer.SQLTask, Version=11.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91 |
| Merchandising_Data | SSIS.Pipeline.3 |
| PLM | SSIS.Pipeline.3 |

## Control Flow Outline

```text
- PricingData [SSIS.Package.3]
- Execute SQL Task [SqlServer.Dts.Tasks.ExecuteSQLTask.ExecuteSQLTask, SqlServer.SQLTask, Version=11.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91]
- Merchandising_Data [SSIS.Pipeline.3]
- PLM [SSIS.Pipeline.3]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package["PricingData"]
    n_Package_Execute_SQL_Task["Execute SQL Task"]
    n_Package_Merchandising_Data["Merchandising_Data"]
    n_Package_PLM["PLM"]
    n_Package_Execute_SQL_Task --> n_Package_PLM
    n_Package_PLM --> n_Package_Merchandising_Data
```

## Variables

_None detected._

## Execute SQL Tasks

_None detected._

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._
