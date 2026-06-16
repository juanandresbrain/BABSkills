# SSIS Package: HR_Sage_ETL

**Project:** HR_Sage_ETL  
**Folder:** HR  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        ASNCorrections_conn(["ASNCorrections [FLATFILE]"])
        CRM_conn(["CRM [ADO.NET:SQL]"])
        ESPStaging_conn(["ESPStaging [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        papamart_dw_conn(["papamart.dw [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        papamarttest_dw_conn(["papamarttest.dw [OLEDB]"])
        papamarttest_DWStaging_conn(["papamarttest.DWStaging [OLEDB]"])
        ProductInventory_conn(["ProductInventory [FLATFILE]"])
        SendLog_conn(["SendLog [FLATFILE]"])
        SendLogPIPE_csv_conn(["SendLogPIPE.csv [FILE]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        HR_Sage_ETL_task["HR_Sage_ETL"]
        Sage_to_Buildabear__UK_employees__task["Sage to Buildabear (UK employees)"]
        HR_Sage_ETL_task --> Sage_to_Buildabear__UK_employees__task
        ingest_out_json_task[/"ingest out_json"/]
        Sage_to_Buildabear__UK_employees__task --> ingest_out_json_task
        ingest_out_json_backup_task[/"ingest out_json backup"/]
        ingest_out_json_task --> ingest_out_json_backup_task
        merge_new_records_task["merge new records"]
        ingest_out_json_backup_task --> merge_new_records_task
        name_fix_task["name fix"]
        merge_new_records_task --> name_fix_task
        Truncate_Stage_task["Truncate Stage"]
        name_fix_task --> Truncate_Stage_task
        update_modified_records_task["update modified records"]
        Truncate_Stage_task --> update_modified_records_task
        Sage_to_Buildabear__UK_stores__task["Sage to Buildabear (UK stores)"]
        update_modified_records_task --> Sage_to_Buildabear__UK_stores__task
        ingest_out_json_task[/"ingest out_json"/]
        Sage_to_Buildabear__UK_stores__task --> ingest_out_json_task
        remove_dupes_from_stage_task["remove dupes from stage"]
        ingest_out_json_task --> remove_dupes_from_stage_task
        store_merge_task["store merge"]
        remove_dupes_from_stage_task --> store_merge_task
        Truncate_Stage_task["Truncate Stage"]
        store_merge_task --> Truncate_Stage_task
        Send_Mail_Task_task["Send Mail Task"]
        Truncate_Stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| ASNCorrections | FLATFILE |
| CRM | ADO.NET:SQL |
| ESPStaging | OLEDB |
| IntegrationStaging | OLEDB |
| papamart.dw | OLEDB |
| papamart.DWStaging | OLEDB |
| papamarttest.dw | OLEDB |
| papamarttest.DWStaging | OLEDB |
| ProductInventory | FLATFILE |
| SendLog | FLATFILE |
| SendLogPIPE.csv | FILE |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| HR_Sage_ETL | Microsoft.Package |
| Sage to Buildabear (UK employees) | STOCK:SEQUENCE |
| ingest out_json | Microsoft.Pipeline |
| ingest out_json backup | Microsoft.Pipeline |
| merge new records | Microsoft.ExecuteSQLTask |
| name fix | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| update modified records | Microsoft.ExecuteSQLTask |
| Sage to Buildabear (UK stores) | STOCK:SEQUENCE |
| ingest out_json | Microsoft.Pipeline |
| remove dupes from stage | Microsoft.ExecuteSQLTask |
| store merge | Microsoft.ExecuteSQLTask |
| Truncate Stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[SHCMEmpStage] |
|  | [dbo].[SHCMEmpStage] |
|  | [dbo].[SHCMStoreStage] |

