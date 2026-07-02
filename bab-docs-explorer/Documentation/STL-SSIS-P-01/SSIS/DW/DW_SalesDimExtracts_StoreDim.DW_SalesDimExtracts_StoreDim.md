# SSIS Package: DW_SalesDimExtracts_StoreDim

**Project:** DW_SalesDimExtracts_StoreDim  
**Folder:** DW  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        ASNCorrections_conn(["ASNCorrections [FLATFILE]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        Kodiak_conn(["Kodiak [OLEDB]"])
        ME_01_conn(["ME_01 [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        ProductInventory_conn(["ProductInventory [FLATFILE]"])
        SendLog_conn(["SendLog [FLATFILE]"])
        SendLogPIPE_csv_conn(["SendLogPIPE.csv [FILE]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        DW_SalesDimExtracts_StoreDim_task["DW_SalesDimExtracts_StoreDim"]
        audit_count_task["audit count"]
        DW_SalesDimExtracts_StoreDim_task --> audit_count_task
        auditDestCount_task["auditDestCount"]
        audit_count_task --> auditDestCount_task
        auditInvalidCount_task["auditInvalidCount"]
        auditDestCount_task --> auditInvalidCount_task
        auditSrcCount_task["auditSrcCount"]
        auditInvalidCount_task --> auditSrcCount_task
        Send_Mail_Task_task["Send Mail Task"]
        auditSrcCount_task --> Send_Mail_Task_task
        Process_task["Process"]
        Send_Mail_Task_task --> Process_task
        populate_StoreDim_Stage_task["populate StoreDim_Stage"]
        Process_task --> populate_StoreDim_Stage_task
        spMergeStoreDim_task["spMergeStoreDim"]
        populate_StoreDim_Stage_task --> spMergeStoreDim_task
        truncate_stage_task["truncate stage"]
        spMergeStoreDim_task --> truncate_stage_task
        Send_Mail_Task_task["Send Mail Task"]
        truncate_stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| ASNCorrections | FLATFILE |
| DW | OLEDB |
| DWStaging | OLEDB |
| IntegrationStaging | OLEDB |
| Kodiak | OLEDB |
| ME_01 | OLEDB |
| papamart.DWStaging | OLEDB |
| ProductInventory | FLATFILE |
| SendLog | FLATFILE |
| SendLogPIPE.csv | FILE |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| DW_SalesDimExtracts_StoreDim | Microsoft.Package |
| audit count | STOCK:SEQUENCE |
| auditDestCount | Microsoft.ExecuteSQLTask |
| auditInvalidCount | Microsoft.ExecuteSQLTask |
| auditSrcCount | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |
| Process | STOCK:SEQUENCE |
| populate StoreDim_Stage | Microsoft.Pipeline |
| spMergeStoreDim | Microsoft.ExecuteSQLTask |
| truncate stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | EXEC dbo.spDW_DataWarehouseSource_From_MDM_and_Merch |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[StoreDim_Stage] |

