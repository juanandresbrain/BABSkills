# SSIS Package: DiscountResultsETL

**Project:** DiscountResultsETL  
**Folder:** DW  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        DiscountMstrData_conn(["DiscountMstrData [OLEDB]"])
        dw_conn(["dw [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        DiscountResultsETL_task["DiscountResultsETL"]
        Sequence_Container_task["Sequence Container"]
        DiscountResultsETL_task --> Sequence_Container_task
        Merge_DiscountResults_task["Merge DiscountResults"]
        Sequence_Container_task --> Merge_DiscountResults_task
        Prestage_DiscountResults_for_Merge_task["Prestage DiscountResults for Merge"]
        Merge_DiscountResults_task --> Prestage_DiscountResults_for_Merge_task
        PreStage_DiscountResults_to_DW_task["PreStage DiscountResults to DW"]
        Prestage_DiscountResults_for_Merge_task --> PreStage_DiscountResults_to_DW_task
        Truncate_Stage_task["Truncate Stage"]
        PreStage_DiscountResults_to_DW_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| DiscountMstrData | OLEDB |
| dw | OLEDB |
| DWStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| DiscountResultsETL | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Merge DiscountResults | Microsoft.ExecuteSQLTask |
| Prestage DiscountResults for Merge | Microsoft.Pipeline |
| PreStage DiscountResults to DW | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | SELECT        countryID, Abbrv FROM            dbo.Country |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[vwDM_Discount_Results] |
|  | [OutboundDiscountResultsStage] |

