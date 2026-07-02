# SSIS Package: DW_SalesDimExtracts_CurrencyDim

**Project:** DW_SalesDimExtracts_CurrencyDim  
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
        DW_SalesDimExtracts_CurrencyDim_task["DW_SalesDimExtracts_CurrencyDim"]
        audit_count_task["audit count"]
        DW_SalesDimExtracts_CurrencyDim_task --> audit_count_task
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
        populate_currency_dim_stage_task["populate currency_dim_stage"]
        Process_task --> populate_currency_dim_stage_task
        spMergeCurrencyDim_task["spMergeCurrencyDim"]
        populate_currency_dim_stage_task --> spMergeCurrencyDim_task
        truncate_stage_task["truncate stage"]
        spMergeCurrencyDim_task --> truncate_stage_task
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
| DW_SalesDimExtracts_CurrencyDim | Microsoft.Package |
| audit count | STOCK:SEQUENCE |
| auditDestCount | Microsoft.ExecuteSQLTask |
| auditInvalidCount | Microsoft.ExecuteSQLTask |
| auditSrcCount | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |
| Process | STOCK:SEQUENCE |
| populate currency_dim_stage | Microsoft.Pipeline |
| spMergeCurrencyDim | Microsoft.ExecuteSQLTask |
| truncate stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | SELECT currency_code       ,currency_desc FROM dbo.vwDW_Currency_Dim with (nolock) ORDER BY currency_code |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[currency_dim_stage] |

