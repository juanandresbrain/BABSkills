# SSIS Package: DW_SalesDimExtracts_LineObj_Store_Lookup

**Project:** DW_SalesDimExtracts_LineObj_Store_Lookup  
**Folder:** DW  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        ASNCorrections_conn(["ASNCorrections [FLATFILE]"])
        Auditworks_conn(["Auditworks [OLEDB]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        Kodiak_conn(["Kodiak [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        ProductInventory_conn(["ProductInventory [FLATFILE]"])
        SendLog_conn(["SendLog [FLATFILE]"])
        SendLogPIPE_csv_conn(["SendLogPIPE.csv [FILE]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        DW_SalesDimExtracts_LineObj_Store_Lookup_task["DW_SalesDimExtracts_LineObj_Store_Lookup"]
        Process_task["Process"]
        DW_SalesDimExtracts_LineObj_Store_Lookup_task --> Process_task
        populate_LineObj_Store_Lookup_stage_task["populate LineObj_Store_Lookup_stage"]
        Process_task --> populate_LineObj_Store_Lookup_stage_task
        spMergeLineObjStoreLookupDim_task["spMergeLineObjStoreLookupDim"]
        populate_LineObj_Store_Lookup_stage_task --> spMergeLineObjStoreLookupDim_task
        truncate_stage_task["truncate stage"]
        spMergeLineObjStoreLookupDim_task --> truncate_stage_task
        Send_Mail_Task_task["Send Mail Task"]
        truncate_stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| ASNCorrections | FLATFILE |
| Auditworks | OLEDB |
| DW | OLEDB |
| DWStaging | OLEDB |
| IntegrationStaging | OLEDB |
| Kodiak | OLEDB |
| papamart.DWStaging | OLEDB |
| ProductInventory | FLATFILE |
| SendLog | FLATFILE |
| SendLogPIPE.csv | FILE |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| DW_SalesDimExtracts_LineObj_Store_Lookup | Microsoft.Package |
| Process | STOCK:SEQUENCE |
| populate LineObj_Store_Lookup_stage | Microsoft.Pipeline |
| spMergeLineObjStoreLookupDim | Microsoft.ExecuteSQLTask |
| truncate stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | SELECT [STS_line_object]       ,[StoreNo]       ,[Beehive_line_object]   FROM [auditworks].[dbo].[vwDW_LineObj_Store_Lookup]  ORDER BY [STS_line_object], [StoreNo] |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[LineObj_Store_Lookup_stage] |

