# SSIS Package: Package

**Project:** HR_UltiproADphoneExt  
**Folder:** HR  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Active_Directory_Connection_Manager_1_conn(["Active Directory Connection Manager 1 [ActiveDirectory]"])
        Active_Directory_Connection_Manager_2_conn(["Active Directory Connection Manager 2 [ActiveDirectory]"])
        Auditworks_conn(["Auditworks [OLEDB]"])
        Azure_Service_Bus_conn(["Azure Service Bus [Azure Service Bus (KingswaySoft)]"])
        CRM_conn(["CRM [OLEDB]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        empIDs_conn(["empIDs [FLATFILE]"])
        empNoID_conn(["empNoID [FLATFILE]"])
        HTTP_Connection_Manager_conn(["HTTP Connection Manager [HTTP (KingswaySoft)]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        ME_01_conn(["ME_01 [OLEDB]"])
        namedAndNumbered_conn(["namedAndNumbered [FLATFILE]"])
        papamart_dw1_conn(["papamart.dw1 [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
        UltiProImportPhoneCSV_conn(["UltiProImportPhoneCSV [FLATFILE]"])
    end
    subgraph ControlFlow
        Package_task["Package"]
        create_file_to_update_work_phone_and_extensions_in_Ultipro_task["create file to update work phone and extensions in Ultipro"]
        Package_task --> create_file_to_update_work_phone_and_extensions_in_Ultipro_task
        SEQ___Generate_BABWWorkPhone_CSV_File_and_upload_task["SEQ - Generate BABWWorkPhone CSV File and upload"]
        create_file_to_update_work_phone_and_extensions_in_Ultipro_task --> SEQ___Generate_BABWWorkPhone_CSV_File_and_upload_task
        Foreach_Loop____CSV_task["Foreach Loop -  CSV"]
        SEQ___Generate_BABWWorkPhone_CSV_File_and_upload_task --> Foreach_Loop____CSV_task
        Archive_File_task["Archive File"]
        Foreach_Loop____CSV_task --> Archive_File_task
        SEQ___SamAccountCSV_task["SEQ - SamAccountCSV"]
        Archive_File_task --> SEQ___SamAccountCSV_task
        Generate_UltiPro_Import_Phone_CSV_task["Generate UltiPro Import Phone CSV"]
        SEQ___SamAccountCSV_task --> Generate_UltiPro_Import_Phone_CSV_task
        sFTP_Upload_task["sFTP Upload"]
        Generate_UltiPro_Import_Phone_CSV_task --> sFTP_Upload_task
        Send_Mail_Task_task["Send Mail Task"]
        sFTP_Upload_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| Active Directory Connection Manager 1 | ActiveDirectory |
| Active Directory Connection Manager 2 | ActiveDirectory |
| Auditworks | OLEDB |
| Azure Service Bus | Azure Service Bus (KingswaySoft) |
| CRM | OLEDB |
| DW | OLEDB |
| DWStaging | OLEDB |
| empIDs | FLATFILE |
| empNoID | FLATFILE |
| HTTP Connection Manager | HTTP (KingswaySoft) |
| IntegrationStaging | OLEDB |
| ME_01 | OLEDB |
| namedAndNumbered | FLATFILE |
| papamart.dw1 | OLEDB |
| SMTP | SMTP |
| UltiProImportPhoneCSV | FLATFILE |

## Control Flow Tasks

| Task | Type |
|---|---|
| Package | Microsoft.Package |
| create file to update work phone and extensions in Ultipro | STOCK:SEQUENCE |
| SEQ - Generate BABWWorkPhone CSV File and upload | STOCK:SEQUENCE |
| Foreach Loop -  CSV | STOCK:FOREACHLOOP |
| Archive File | Microsoft.FileSystemTask |
| SEQ - SamAccountCSV | STOCK:SEQUENCE |
| Generate UltiPro Import Phone CSV | Microsoft.Pipeline |
| sFTP Upload | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | SELECT [Company],[Effective Date],[emp #],[phone number],[ext] FROM [dbo].[vwUHCMUltiproFromADphoneExt] --where [emp #] = '0063553' |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[vwUltiProNeedsSamAccount] |

