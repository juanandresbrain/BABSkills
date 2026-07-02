# SSIS Package: AzurePowerBiDataCheck

**Project:** AzurePowerBIDataCheck  
**Folder:** Azure  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        azure_conn(["azure [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
    end
    subgraph ControlFlow
        AzurePowerBiDataCheck_task["AzurePowerBiDataCheck"]
        Azure_Data_Flow_task["Azure Data Flow"]
        AzurePowerBiDataCheck_task --> Azure_Data_Flow_task
        Send_Email_task["Send Email"]
        Azure_Data_Flow_task --> Send_Email_task
        Set_Query_String_task["Set Query String"]
        Send_Email_task --> Set_Query_String_task
        Truncate_Stage_task["Truncate Stage"]
        Set_Query_String_task --> Truncate_Stage_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| azure | OLEDB |
| papamart.DWStaging | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| AzurePowerBiDataCheck | Microsoft.Package |
| Azure Data Flow | Microsoft.Pipeline |
| Send Email | Microsoft.ExecuteSQLTask |
| Set Query String | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | SELECT NON EMPTY { [Measures].[TotalTransactions] } ON COLUMNS, NON EMPTY { ([NewDateDim].[Date_Key].[Date_Key].ALLMEMBERS * [Stores].[TradingGroup].[TradingGroup].ALLMEMBERS ) } DIMENSION PROPERTIES MEMBER_CAPTION, MEMBER_UNIQUE_NAME ON ROWS FROM ( SELECT ( { [NewDateDim].[Date_Key].&[2019-03-03T00:00:00] } ) ON COLUMNS FROM ( SELECT ( { [Stores].[TradingGroup].&[North America], [Stores].[Trading |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [AzureDataCheck] |

