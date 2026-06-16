# SSIS Package: HR_Sage_ETL_2

**Project:** HR_Sage_ETL2  
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
        HR_Sage_ETL_2_task["HR_Sage_ETL_2"]
        archive_csv_files_task["archive csv files"]
        HR_Sage_ETL_2_task --> archive_csv_files_task
        archive_files_task["archive files"]
        archive_csv_files_task --> archive_files_task
        archive_json_files_task["archive json files"]
        archive_files_task --> archive_json_files_task
        archive_files_task["archive files"]
        archive_json_files_task --> archive_files_task
        Buildabear_back_to_Sage_task["Buildabear back to Sage"]
        archive_files_task --> Buildabear_back_to_Sage_task
        generate_in_json_task[/"generate in_json"/]
        Buildabear_back_to_Sage_task --> generate_in_json_task
        generate_in_json_OLD_task[/"generate in_json OLD"/]
        generate_in_json_task --> generate_in_json_OLD_task
        Send_Mail_Task_task["Send Mail Task"]
        generate_in_json_OLD_task --> Send_Mail_Task_task
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
| HR_Sage_ETL_2 | Microsoft.Package |
| archive csv files | STOCK:FOREACHLOOP |
| archive files | Microsoft.FileSystemTask |
| archive json files | STOCK:FOREACHLOOP |
| archive files | Microsoft.FileSystemTask |
| Buildabear back to Sage | STOCK:SEQUENCE |
| generate in_json | Microsoft.Pipeline |
| generate in_json OLD | Microsoft.Pipeline |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | SELECT u.EecLocation,u.EepEEID,u.JbcJobCode,u.JbcLongDesc,u.EecOrgLvl1Code,u.EecOrgLvl1Description,u.LocDesc,u.EecEmplStatus,u.EepNameFirst,u.EepNameLast,u.EepNameMiddle,u.EepAddressEMail,u.EepAddressEMail2 ,u.WorkPhoneNumber,u.efoPhoneExtension,u.EecSalaryOrHourly,u.EepNamePreferred,u.EecDateOfOriginalHire,u.EepCompanyCode,u.TerminationDate, --u.sAMAccountName isnull(a.SamAccountName,'') as sAMAc |
|  |  | SELECT u.EecLocation,u.EepEEID,u.JbcJobCode,u.JbcLongDesc,u.EecOrgLvl1Code,u.EecOrgLvl1Description,u.LocDesc,u.EecEmplStatus,u.EepNameFirst,u.EepNameLast,u.EepNameMiddle,u.EepAddressEMail ,u.WorkPhoneNumber,u.efoPhoneExtension,u.EecSalaryOrHourly,u.EepNamePreferred,u.EecDateOfOriginalHire,u.EepCompanyCode,u.TerminationDate, --u.sAMAccountName isnull(a.SamAccountName,'') as sAMAccountName --sAMAcco |

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

