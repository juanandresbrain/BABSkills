# SSIS Package: AzurePartitionsMetaDownload

**Project:** AzurePartitionsMetaDownload  
**Folder:** Azure  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        AzureQuery_conn(["AzureQuery [ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
    end
    subgraph ControlFlow
        AzurePartitionsMetaDownload_task["AzurePartitionsMetaDownload"]
        SEQ___Stage_Table_Meta___1_task["SEQ - Stage Table Meta - 1"]
        AzurePartitionsMetaDownload_task --> SEQ___Stage_Table_Meta___1_task
        Dataflow___Stage_Table_Meta_task["Dataflow - Stage Table Meta"]
        SEQ___Stage_Table_Meta___1_task --> Dataflow___Stage_Table_Meta_task
        spAzurePartitionGroupDerive_task["spAzurePartitionGroupDerive"]
        Dataflow___Stage_Table_Meta_task --> spAzurePartitionGroupDerive_task
        Truncate_Stage_task["Truncate Stage"]
        spAzurePartitionGroupDerive_task --> Truncate_Stage_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| AzureQuery | ADO.NET:System.Data.OleDb.OleDbConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089 |
| DWStaging | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| AzurePartitionsMetaDownload | Microsoft.Package |
| SEQ - Stage Table Meta - 1 | STOCK:SEQUENCE |
| Dataflow - Stage Table Meta | Microsoft.Pipeline |
| spAzurePartitionGroupDerive | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[AzureTableMeta] |

