# SSIS Package: GiftCard_Validation

**Project:** GiftCard_Validation  
**Folder:** DW  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        ASNCorrections_conn(["ASNCorrections [FLATFILE]"])
        currentGCfile_conn(["currentGCfile [FLATFILE]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        Flat_File_Connection_Manager_conn(["Flat File Connection Manager [FLATFILE]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        ProductInventory_conn(["ProductInventory [FLATFILE]"])
        SendLog_conn(["SendLog [FLATFILE]"])
        SendLogPIPE_csv_conn(["SendLogPIPE.csv [FILE]"])
        SMTP_conn(["SMTP [SMTP]"])
        STL_SQL_P_04_SQL2008R2_ReportServer_birpt01_conn(["STL-SQL-P-04\SQL2008R2.ReportServer_birpt01 [OLEDB]"])
    end
    subgraph ControlFlow
        GiftCard_Validation_task["GiftCard_Validation"]
        Validation_task["Validation"]
        GiftCard_Validation_task --> Validation_task
        1____SKIPPED_STEP____task["1 -- SKIPPED STEP --"]
        Validation_task --> 1____SKIPPED_STEP____task
        2___Generate_any_missing_Mids_task["2 - Generate any missing Mids"]
        1____SKIPPED_STEP____task --> 2___Generate_any_missing_Mids_task
        3____3rd_party_GC_into_DW_task["3 -- 3rd party GC into DW"]
        2___Generate_any_missing_Mids_task --> 3____3rd_party_GC_into_DW_task
        4___Exec_validation_stored_proc_task["4 - Exec validation stored proc"]
        3____3rd_party_GC_into_DW_task --> 4___Exec_validation_stored_proc_task
        5___Generate_Validation_Reports_task["5 - Generate Validation Reports"]
        4___Exec_validation_stored_proc_task --> 5___Generate_Validation_Reports_task
        Send_Mail_Task_task["Send Mail Task"]
        5___Generate_Validation_Reports_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| ASNCorrections | FLATFILE |
| currentGCfile | FLATFILE |
| DW | OLEDB |
| DWStaging | OLEDB |
| Flat File Connection Manager | FLATFILE |
| IntegrationStaging | OLEDB |
| ProductInventory | FLATFILE |
| SendLog | FLATFILE |
| SendLogPIPE.csv | FILE |
| SMTP | SMTP |
| STL-SQL-P-04\SQL2008R2.ReportServer_birpt01 | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| GiftCard_Validation | Microsoft.Package |
| Validation | STOCK:SEQUENCE |
| 1 -- SKIPPED STEP -- | Microsoft.ExecuteSQLTask |
| 2 - Generate any missing Mids | Microsoft.ExecuteSQLTask |
| 3 -- 3rd party GC into DW | Microsoft.ExecuteSQLTask |
| 4 - Exec validation stored proc | Microsoft.ExecuteSQLTask |
| 5 - Generate Validation Reports | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

