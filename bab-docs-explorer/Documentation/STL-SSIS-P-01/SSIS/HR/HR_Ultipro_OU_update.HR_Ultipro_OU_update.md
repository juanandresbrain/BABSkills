# SSIS Package: HR_Ultipro_OU_update

**Project:** HR_Ultipro_OU_update  
**Folder:** HR  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| Active Directory Connection Manager 1 | ActiveDirectory |  |  |  |
| Active Directory Connection Manager 2 | ActiveDirectory |  |  |  |
| Auditworks | OLEDB | bedrocktestdb01 | auditworks | Data Source=bedrocktestdb01; Initial Catalog=auditworks; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| Azure Service Bus | Azure Service Bus (KingswaySoft) |  |  |  |
| CRM | OLEDB | stl-crmdb-p-01 | crm | Data Source=stl-crmdb-p-01; Initial Catalog=crm; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| DW | OLEDB | papamart | dw | Data Source=papamart; Initial Catalog=dw; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| DWStaging | OLEDB | papamart | DWStaging | Data Source=papamart; Initial Catalog=DWStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| HTTP Connection Manager | HTTP (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-t-01 | IntegrationStaging | Data Source=STL-SSIS-t-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| ME_01 | OLEDB | bedrocktestdb02 | me_01 | Data Source=bedrocktestdb02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP | SMTP |  |  |  |
| UltiProImportEmailCSV | FLATFILE |  |  |  |
| UltiProImportSamAccountCSV | FLATFILE |  |  |  |
| coredb01 | OLEDB | coredb01 | AIMSConfig | Data Source=coredb01; Initial Catalog=AIMSConfig; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| empIDs | FLATFILE |  |  |  |
| empNoID | FLATFILE |  |  |  |
| namedAndNumbered | FLATFILE |  |  |  |
| papamart.dw1 | OLEDB | papamart | dw | Data Source=papamart; Initial Catalog=dw; Provider=SQLOLEDB.1; Integrated Security=SSPI; Application Name=SSIS-Package-{3AE9F320-D541-4496-80AB-31E67461FEC7}papamart.dw1; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| HR_Ultipro_OU_update | Package |
| create file to reset samaccount and email in Ultipro ONE EMPLOYEE | SEQUENCE |
| SEQ - Generate SamAccountName CSV Files | SEQUENCE |
| Foreach Loop -  CSV | FOREACHLOOP |
| Archive File | FileSystemTask |
| SEQ - EmailCSV | SEQUENCE |
| PrimaryEmail CSV | Pipeline |
| SEQ - SamAccountCSV | SEQUENCE |
| SamAccount CSV | Pipeline |
| sFTP Upload | ExecuteSQLTask |
| CWM display name & DL update | SEQUENCE |
| DL updates | SEQUENCE |
| remove CWM from group | Pipeline |
| update CWM email group | Pipeline |
| truncate DL reject stage | ExecuteSQLTask |
| update CWM display name | Pipeline |
| update CWM display name w email | Pipeline |
| OU update | SEQUENCE |
| count OU moves | ExecuteSQLTask |
| Sequence Container | SEQUENCE |
| AD extract Loop | FOREACHLOOP |
| Data Flow - memberOf | Pipeline |
| load ADemployeeStage | ExecuteSQLTask |
| Script - ADExtract | ScriptTask |
| Script - ADextract | ScriptTask |
| Merge ADEmployee | ExecuteSQLTask |
| stage employee ID | ExecuteSQLTask |
| truncate stage | ExecuteSQLTask |
| update OU | Pipeline |
| update OU one time | Pipeline |
| wait | ExecuteSQLTask |
| retrieve AD attributes | Pipeline |
| store demotion | SEQUENCE |
| count OU demotes | ExecuteSQLTask |
| create file to reset samaccount and email in Ultipro | SEQUENCE |
| SEQ - Generate SamAccountName CSV Files | SEQUENCE |
| Foreach Loop -  CSV | FOREACHLOOP |
| Archive File | FileSystemTask |
| SEQ - EmailCSV | SEQUENCE |
| PrimaryEmail CSV | Pipeline |
| SEQ - SamAccountCSV | SEQUENCE |
| SamAccount CSV | Pipeline |
| sFTP Upload | ExecuteSQLTask |
| send to AD | Pipeline |
| send to AD 1 | Pipeline |
| send to AD 2 | Pipeline |
| Sequence Container | SEQUENCE |
| AD extract Loop | FOREACHLOOP |
| Data Flow - memberOf | Pipeline |
| load ADemployeeStage | ExecuteSQLTask |
| Script - ADExtract | ScriptTask |
| Merge ADEmployee | ExecuteSQLTask |
| stage employee ID | ExecuteSQLTask |
| truncate stage | ExecuteSQLTask |
| Sequence Container 1 | SEQUENCE |
| add to Store Users DL | Pipeline |
| remove from CWM DL | Pipeline |
| update UHCMemp table | Pipeline |
| wait | ExecuteSQLTask |
| store promotion | SEQUENCE |
| count OU promotes | ExecuteSQLTask |
| create file to reset samaccount and email in Ultipro | SEQUENCE |
| SEQ - Generate SamAccountName CSV Files | SEQUENCE |
| Foreach Loop -  CSV | FOREACHLOOP |
| Archive File | FileSystemTask |
| SEQ - EmailCSV | SEQUENCE |
| PrimaryEmail CSV | Pipeline |
| SEQ - SamAccountCSV | SEQUENCE |
| SamAccount CSV | Pipeline |
| sFTP Upload | ExecuteSQLTask |
| send C to dataLoaderStaging | Pipeline |
| send RN to dataLoaderStaging | Pipeline |
| Sequence Container | SEQUENCE |
| AD extract Loop | FOREACHLOOP |
| Data Flow - memberOf | Pipeline |
| load ADemployeeStage | ExecuteSQLTask |
| Script - ADExtract | ScriptTask |
| Merge ADEmployee | ExecuteSQLTask |
| stage employee ID | ExecuteSQLTask |
| truncate stage | ExecuteSQLTask |
| update UHCMemp table | Pipeline |
| wait | ExecuteSQLTask |
| test update attribute | Pipeline |
| update ActiveDirectoryDataStage table | SEQUENCE |
| SEQ - refresh ActiveDirectoryDataStage table | SEQUENCE |
| DataFlow - ActiveDirectoryDataStage | Pipeline |
| Truncate ActiveDirectoryDataStage | ExecuteSQLTask |
| update all CWM display names | Pipeline |
| update ExtensionAttribute5 | Pipeline |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- CWM display name & DL update [SEQUENCE]
  - DL updates [SEQUENCE]
    - remove CWM from group [Pipeline]
    - update CWM email group [Pipeline]
  - truncate DL reject stage [ExecuteSQLTask]
  - update CWM display name [Pipeline]
  - update CWM display name w email [Pipeline]
- OU update [SEQUENCE]
  - Sequence Container [SEQUENCE]
    - AD extract Loop [FOREACHLOOP]
      - Data Flow - memberOf [Pipeline]
      - Script - ADExtract [ScriptTask]
      - Script - ADextract [ScriptTask]
      - load ADemployeeStage [ExecuteSQLTask]
    - Merge ADEmployee [ExecuteSQLTask]
    - stage employee ID [ExecuteSQLTask]
    - truncate stage [ExecuteSQLTask]
  - count OU moves [ExecuteSQLTask]
  - update OU [Pipeline]
  - update OU one time [Pipeline]
  - wait [ExecuteSQLTask]
- create file to reset samaccount and email in Ultipro ONE EMPLOYEE [SEQUENCE]
  - SEQ - Generate SamAccountName CSV Files [SEQUENCE]
    - Foreach Loop -  CSV [FOREACHLOOP]
      - Archive File [FileSystemTask]
    - SEQ - EmailCSV [SEQUENCE]
      - PrimaryEmail CSV [Pipeline]
    - SEQ - SamAccountCSV [SEQUENCE]
      - SamAccount CSV [Pipeline]
    - sFTP Upload [ExecuteSQLTask]
- retrieve AD attributes [Pipeline]
- store demotion [SEQUENCE]
  - Sequence Container [SEQUENCE]
  - Sequence Container 1 [SEQUENCE]
    - add to Store Users DL [Pipeline]
    - remove from CWM DL [Pipeline]
    - AD extract Loop [FOREACHLOOP]
      - Data Flow - memberOf [Pipeline]
      - Script - ADExtract [ScriptTask]
      - load ADemployeeStage [ExecuteSQLTask]
    - Merge ADEmployee [ExecuteSQLTask]
    - stage employee ID [ExecuteSQLTask]
    - truncate stage [ExecuteSQLTask]
  - count OU demotes [ExecuteSQLTask]
  - create file to reset samaccount and email in Ultipro [SEQUENCE]
    - SEQ - Generate SamAccountName CSV Files [SEQUENCE]
      - Foreach Loop -  CSV [FOREACHLOOP]
        - Archive File [FileSystemTask]
      - SEQ - EmailCSV [SEQUENCE]
        - PrimaryEmail CSV [Pipeline]
      - SEQ - SamAccountCSV [SEQUENCE]
        - SamAccount CSV [Pipeline]
      - sFTP Upload [ExecuteSQLTask]
  - send to AD [Pipeline]
  - send to AD 1 [Pipeline]
  - send to AD 2 [Pipeline]
  - update UHCMemp table [Pipeline]
  - wait [ExecuteSQLTask]
- store promotion [SEQUENCE]
  - Sequence Container [SEQUENCE]
    - AD extract Loop [FOREACHLOOP]
      - Data Flow - memberOf [Pipeline]
      - Script - ADExtract [ScriptTask]
      - load ADemployeeStage [ExecuteSQLTask]
    - Merge ADEmployee [ExecuteSQLTask]
    - stage employee ID [ExecuteSQLTask]
    - truncate stage [ExecuteSQLTask]
  - count OU promotes [ExecuteSQLTask]
  - create file to reset samaccount and email in Ultipro [SEQUENCE]
    - SEQ - Generate SamAccountName CSV Files [SEQUENCE]
      - Foreach Loop -  CSV [FOREACHLOOP]
        - Archive File [FileSystemTask]
      - SEQ - EmailCSV [SEQUENCE]
        - PrimaryEmail CSV [Pipeline]
      - SEQ - SamAccountCSV [SEQUENCE]
        - SamAccount CSV [Pipeline]
      - sFTP Upload [ExecuteSQLTask]
  - send C to dataLoaderStaging [Pipeline]
  - send RN to dataLoaderStaging [Pipeline]
  - update UHCMemp table [Pipeline]
  - wait [ExecuteSQLTask]
- test update attribute [Pipeline]
- update ActiveDirectoryDataStage table [SEQUENCE]
  - SEQ - refresh ActiveDirectoryDataStage table [SEQUENCE]
    - DataFlow - ActiveDirectoryDataStage [Pipeline]
    - Truncate ActiveDirectoryDataStage [ExecuteSQLTask]
- update ExtensionAttribute5 [Pipeline]
- update all CWM display names [Pipeline]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE["create file to reset samaccount and email in Ultipro ONE EMPLOYEE"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files["SEQ - Generate SamAccountName CSV Files"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV["Foreach Loop -  CSV"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV_Archive_File["Archive File"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV["SEQ - EmailCSV"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV_PrimaryEmail_CSV["PrimaryEmail CSV"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV["SEQ - SamAccountCSV"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV_SamAccount_CSV["SamAccount CSV"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload["sFTP Upload"]
    n_Package_CWM_display_name___DL_update["CWM display name & DL update"]
    n_Package_CWM_display_name___DL_update_DL_updates["DL updates"]
    n_Package_CWM_display_name___DL_update_DL_updates_remove_CWM_from_group["remove CWM from group"]
    n_Package_CWM_display_name___DL_update_DL_updates_update_CWM_email_group["update CWM email group"]
    n_Package_CWM_display_name___DL_update_truncate_DL_reject_stage["truncate DL reject stage"]
    n_Package_CWM_display_name___DL_update_update_CWM_display_name["update CWM display name"]
    n_Package_CWM_display_name___DL_update_update_CWM_display_name_w_email["update CWM display name w email"]
    n_Package_OU_update["OU update"]
    n_Package_OU_update_count_OU_moves["count OU moves"]
    n_Package_OU_update_Sequence_Container["Sequence Container"]
    n_Package_OU_update_Sequence_Container_AD_extract_Loop["AD extract Loop"]
    n_Package_OU_update_Sequence_Container_AD_extract_Loop_Data_Flow___memberOf["Data Flow - memberOf"]
    n_Package_OU_update_Sequence_Container_AD_extract_Loop_load_ADemployeeStage["load ADemployeeStage"]
    n_Package_OU_update_Sequence_Container_AD_extract_Loop_Script___ADExtract["Script - ADExtract"]
    n_Package_OU_update_Sequence_Container_AD_extract_Loop_Script___ADextract["Script - ADextract"]
    n_Package_OU_update_Sequence_Container_Merge_ADEmployee["Merge ADEmployee"]
    n_Package_OU_update_Sequence_Container_stage_employee_ID["stage employee ID"]
    n_Package_OU_update_Sequence_Container_truncate_stage["truncate stage"]
    n_Package_OU_update_update_OU["update OU"]
    n_Package_OU_update_update_OU_one_time["update OU one time"]
    n_Package_OU_update_wait["wait"]
    n_Package_retrieve_AD_attributes["retrieve AD attributes"]
    n_Package_store_demotion["store demotion"]
    n_Package_store_demotion_count_OU_demotes["count OU demotes"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro["create file to reset samaccount and email in Ultipro"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files["SEQ - Generate SamAccountName CSV Files"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV["Foreach Loop -  CSV"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV_Archive_File["Archive File"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV["SEQ - EmailCSV"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV_PrimaryEmail_CSV["PrimaryEmail CSV"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV["SEQ - SamAccountCSV"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV_SamAccount_CSV["SamAccount CSV"]
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload["sFTP Upload"]
    n_Package_store_demotion_send_to_AD["send to AD"]
    n_Package_store_demotion_send_to_AD_1["send to AD 1"]
    n_Package_store_demotion_send_to_AD_2["send to AD 2"]
    n_Package_store_demotion_Sequence_Container["Sequence Container"]
    n_Package_store_demotion_Sequence_Container_AD_extract_Loop["AD extract Loop"]
    n_Package_store_demotion_Sequence_Container_AD_extract_Loop_Data_Flow___memberOf["Data Flow - memberOf"]
    n_Package_store_demotion_Sequence_Container_AD_extract_Loop_load_ADemployeeStage["load ADemployeeStage"]
    n_Package_store_demotion_Sequence_Container_AD_extract_Loop_Script___ADExtract["Script - ADExtract"]
    n_Package_store_demotion_Sequence_Container_Merge_ADEmployee["Merge ADEmployee"]
    n_Package_store_demotion_Sequence_Container_stage_employee_ID["stage employee ID"]
    n_Package_store_demotion_Sequence_Container_truncate_stage["truncate stage"]
    n_Package_store_demotion_Sequence_Container_1["Sequence Container 1"]
    n_Package_store_demotion_Sequence_Container_1_add_to_Store_Users_DL["add to Store Users DL"]
    n_Package_store_demotion_Sequence_Container_1_remove_from_CWM_DL["remove from CWM DL"]
    n_Package_store_demotion_update_UHCMemp_table["update UHCMemp table"]
    n_Package_store_demotion_wait["wait"]
    n_Package_store_promotion["store promotion"]
    n_Package_store_promotion_count_OU_promotes["count OU promotes"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro["create file to reset samaccount and email in Ultipro"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files["SEQ - Generate SamAccountName CSV Files"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV["Foreach Loop -  CSV"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV_Archive_File["Archive File"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV["SEQ - EmailCSV"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV_PrimaryEmail_CSV["PrimaryEmail CSV"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV["SEQ - SamAccountCSV"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV_SamAccount_CSV["SamAccount CSV"]
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload["sFTP Upload"]
    n_Package_store_promotion_send_C_to_dataLoaderStaging["send C to dataLoaderStaging"]
    n_Package_store_promotion_send_RN_to_dataLoaderStaging["send RN to dataLoaderStaging"]
    n_Package_store_promotion_Sequence_Container["Sequence Container"]
    n_Package_store_promotion_Sequence_Container_AD_extract_Loop["AD extract Loop"]
    n_Package_store_promotion_Sequence_Container_AD_extract_Loop_Data_Flow___memberOf["Data Flow - memberOf"]
    n_Package_store_promotion_Sequence_Container_AD_extract_Loop_load_ADemployeeStage["load ADemployeeStage"]
    n_Package_store_promotion_Sequence_Container_AD_extract_Loop_Script___ADExtract["Script - ADExtract"]
    n_Package_store_promotion_Sequence_Container_Merge_ADEmployee["Merge ADEmployee"]
    n_Package_store_promotion_Sequence_Container_stage_employee_ID["stage employee ID"]
    n_Package_store_promotion_Sequence_Container_truncate_stage["truncate stage"]
    n_Package_store_promotion_update_UHCMemp_table["update UHCMemp table"]
    n_Package_store_promotion_wait["wait"]
    n_Package_test_update_attribute["test update attribute"]
    n_Package_update_ActiveDirectoryDataStage_table["update ActiveDirectoryDataStage table"]
    n_Package_update_ActiveDirectoryDataStage_table_SEQ___refresh_ActiveDirectoryDataStage_table["SEQ - refresh ActiveDirectoryDataStage table"]
    n_Package_update_ActiveDirectoryDataStage_table_SEQ___refresh_ActiveDirectoryDataStage_table_DataFlow___ActiveDirectoryDataStage["DataFlow - ActiveDirectoryDataStage"]
    n_Package_update_ActiveDirectoryDataStage_table_SEQ___refresh_ActiveDirectoryDataStage_table_Truncate_ActiveDirectoryDataStage["Truncate ActiveDirectoryDataStage"]
    n_Package_update_all_CWM_display_names["update all CWM display names"]
    n_Package_update_ExtensionAttribute5["update ExtensionAttribute5"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV --> n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV --> n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload
    n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload --> n_Package_create_file_to_reset_samaccount_and_email_in_Ultipro_ONE_EMPLOYEE_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV
    n_Package_CWM_display_name___DL_update_DL_updates_update_CWM_email_group --> n_Package_CWM_display_name___DL_update_DL_updates_remove_CWM_from_group
    n_Package_CWM_display_name___DL_update_update_CWM_display_name --> n_Package_CWM_display_name___DL_update_truncate_DL_reject_stage
    n_Package_CWM_display_name___DL_update_truncate_DL_reject_stage --> n_Package_CWM_display_name___DL_update_DL_updates
    n_Package_OU_update_Sequence_Container_AD_extract_Loop_Script___ADExtract --> n_Package_OU_update_Sequence_Container_AD_extract_Loop_load_ADemployeeStage
    n_Package_OU_update_Sequence_Container_AD_extract_Loop_load_ADemployeeStage --> n_Package_OU_update_Sequence_Container_AD_extract_Loop_Data_Flow___memberOf
    n_Package_OU_update_Sequence_Container_truncate_stage --> n_Package_OU_update_Sequence_Container_stage_employee_ID
    n_Package_OU_update_Sequence_Container_stage_employee_ID --> n_Package_OU_update_Sequence_Container_AD_extract_Loop
    n_Package_OU_update_Sequence_Container_AD_extract_Loop --> n_Package_OU_update_Sequence_Container_Merge_ADEmployee
    n_Package_OU_update_count_OU_moves --> n_Package_OU_update_update_OU
    n_Package_OU_update_update_OU --> n_Package_OU_update_wait
    n_Package_OU_update_wait --> n_Package_OU_update_Sequence_Container
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV --> n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV --> n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload --> n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV
    n_Package_store_demotion_Sequence_Container_AD_extract_Loop_Script___ADExtract --> n_Package_store_demotion_Sequence_Container_AD_extract_Loop_load_ADemployeeStage
    n_Package_store_demotion_Sequence_Container_AD_extract_Loop_load_ADemployeeStage --> n_Package_store_demotion_Sequence_Container_AD_extract_Loop_Data_Flow___memberOf
    n_Package_store_demotion_Sequence_Container_truncate_stage --> n_Package_store_demotion_Sequence_Container_stage_employee_ID
    n_Package_store_demotion_Sequence_Container_stage_employee_ID --> n_Package_store_demotion_Sequence_Container_AD_extract_Loop
    n_Package_store_demotion_Sequence_Container_AD_extract_Loop --> n_Package_store_demotion_Sequence_Container_Merge_ADEmployee
    n_Package_store_demotion_Sequence_Container_1_remove_from_CWM_DL --> n_Package_store_demotion_Sequence_Container_1_add_to_Store_Users_DL
    n_Package_store_demotion_count_OU_demotes --> n_Package_store_demotion_send_to_AD
    n_Package_store_demotion_send_to_AD --> n_Package_store_demotion_Sequence_Container_1
    n_Package_store_demotion_wait --> n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro
    n_Package_store_demotion_Sequence_Container_1 --> n_Package_store_demotion_wait
    n_Package_store_demotion_create_file_to_reset_samaccount_and_email_in_Ultipro --> n_Package_store_demotion_Sequence_Container
    n_Package_store_demotion_Sequence_Container --> n_Package_store_demotion_update_UHCMemp_table
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___EmailCSV --> n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_SEQ___SamAccountCSV --> n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_sFTP_Upload --> n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro_SEQ___Generate_SamAccountName_CSV_Files_Foreach_Loop____CSV
    n_Package_store_promotion_Sequence_Container_AD_extract_Loop_Script___ADExtract --> n_Package_store_promotion_Sequence_Container_AD_extract_Loop_load_ADemployeeStage
    n_Package_store_promotion_Sequence_Container_AD_extract_Loop_load_ADemployeeStage --> n_Package_store_promotion_Sequence_Container_AD_extract_Loop_Data_Flow___memberOf
    n_Package_store_promotion_Sequence_Container_truncate_stage --> n_Package_store_promotion_Sequence_Container_stage_employee_ID
    n_Package_store_promotion_Sequence_Container_stage_employee_ID --> n_Package_store_promotion_Sequence_Container_AD_extract_Loop
    n_Package_store_promotion_Sequence_Container_AD_extract_Loop --> n_Package_store_promotion_Sequence_Container_Merge_ADEmployee
    n_Package_store_promotion_count_OU_promotes --> n_Package_store_promotion_send_RN_to_dataLoaderStaging
    n_Package_store_promotion_send_RN_to_dataLoaderStaging --> n_Package_store_promotion_update_UHCMemp_table
    n_Package_store_promotion_wait --> n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro
    n_Package_store_promotion_create_file_to_reset_samaccount_and_email_in_Ultipro --> n_Package_store_promotion_Sequence_Container
    n_Package_store_promotion_update_UHCMemp_table --> n_Package_store_promotion_wait
    n_Package_update_ActiveDirectoryDataStage_table_SEQ___refresh_ActiveDirectoryDataStage_table_Truncate_ActiveDirectoryDataStage --> n_Package_update_ActiveDirectoryDataStage_table_SEQ___refresh_ActiveDirectoryDataStage_table_DataFlow___ActiveDirectoryDataStage
    n_Package_OU_update --> n_Package_store_promotion
    n_Package_store_promotion --> n_Package_store_demotion
    n_Package_store_demotion --> n_Package_CWM_display_name___DL_update
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | DateTimeStamp | Yes |
| User | EmployeeIDStage | No |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | SQL_MemberOfQuery | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | UltiProImportEmailCSVFileName | Yes |
| User | UltiProImportFilePreStagePath | Yes |
| User | UltiProImportFiles | No |
| User | UltiProImportSamAccountCSVConnectionString | Yes |
| User | UltiProImportSamAccountCSVFileName | Yes |
| User | UltiproImportArchive | Yes |
| User | UltiproImportEmailCSVConnectionString | Yes |
| User | ad_EmployeeID | No |
| User | ad_cn | No |
| User | ad_company | No |
| User | ad_department | No |
| User | ad_description | No |
| User | ad_displayName | No |
| User | ad_givenname | No |
| User | ad_mail | No |
| User | ad_manager | No |
| User | ad_memberOf | No |
| User | ad_samaccountName | No |
| User | ad_sn | No |
| User | ad_title | No |
| User | empDemoteCount | No |
| User | empMoveCount | No |
| User | empPromoteCount | No |

### Expression-bound variable values

#### User::DateTimeStamp

**Expression:**

```sql
(DT_WSTR,4)DATEPART("yyyy",GetDate()) 
+ (DT_WSTR,4)DATEPART("mm",GetDate()) 
+ (DT_WSTR,4)DATEPART("dd",GetDate()) 
+ (DT_WSTR,4)DATEPART("hh",GetDate()) 
+ (DT_WSTR,4)DATEPART("mi",GetDate()) 
+ (DT_WSTR,4)DATEPART("ss",GetDate()) 
+ (DT_WSTR,4)DATEPART("ms",GetDate())
```

**Evaluated value:**

```sql
202654131248397
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
5/4/2026
```

#### User::EndDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::EndDate])  + "-" + 
(DT_WSTR, 2) datepart("mm", @[User::EndDate])  + "-" + 
(DT_WSTR, 2) datepart("dd",  @[User::EndDate])
```

**Evaluated value:**

```sql
2026-5-4
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
5/4/2026
```

#### User::GetDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::GetDate])  + "-" + 
(DT_WSTR, 2) datepart("mm", @[User::GetDate])  + "-" + 
(DT_WSTR, 2) datepart("dd",  @[User::GetDate])
```

**Evaluated value:**

```sql
2026-5-4
```

#### User::SQL_MemberOfQuery

**Expression:**

```sql
"
SELECT cast('" + @[User::ad_EmployeeID] + "' as nvarchar(7))  as EmployeeID, cast(replace(ADsPath, 'LDAP://', '') as nvarchar(4000)) as memberOf 
FROM OPENQUERY
	(
		ADSI, 
            'SELECT * FROM ''LDAP://DC=buildabear,DC=com'' 
             WHERE employeeID = ''" + @[User::ad_EmployeeID] + "'''
	)  
"
```

**Evaluated value:**

```sql

SELECT cast('' as nvarchar(7))  as EmployeeID, cast(replace(ADsPath, 'LDAP://', '') as nvarchar(4000)) as memberOf 
FROM OPENQUERY
	(
		ADSI, 
            'SELECT * FROM ''LDAP://DC=buildabear,DC=com'' 
             WHERE employeeID = '''''
	)  

```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
5/3/2026
```

#### User::StartDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::StartDate])  + "-" + 
(DT_WSTR, 2) datepart("mm", @[User::StartDate])  + "-" + 
(DT_WSTR, 2) datepart("dd",  @[User::StartDate])
```

**Evaluated value:**

```sql
2026-5-3
```

#### User::UltiProImportEmailCSVFileName

**Expression:**

```sql
"UPEmail" +  @[User::DateTimeStamp] + ".csv"
```

**Evaluated value:**

```sql
UPEmail202654131248403.csv
```

#### User::UltiProImportFilePreStagePath

**Expression:**

```sql
"\\\\stl-ssis-p-01\\IntegrationStaging\\HR\\UltiProTermSamaccount\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\HR\UltiProTermSamaccount\
```

#### User::UltiProImportSamAccountCSVConnectionString

**Expression:**

```sql
@[$Package::UltiProFileStagePath_SamAccountEmail] +  @[User::UltiProImportSamAccountCSVFileName]
```

**Evaluated value:**

```sql
\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\UPSamAccount202654131248407.csv
```

#### User::UltiProImportSamAccountCSVFileName

**Expression:**

```sql
"UPSamAccount" +  @[User::DateTimeStamp] + ".csv"
```

**Evaluated value:**

```sql
UPSamAccount202654131248407.csv
```

#### User::UltiproImportArchive

**Expression:**

```sql
@[User::UltiProImportFilePreStagePath]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\HR\UltiProTermSamaccount\Archive\
```

#### User::UltiproImportEmailCSVConnectionString

**Expression:**

```sql
@[$Package::UltiProFileStagePath_SamAccountEmail] +  @[User::UltiProImportEmailCSVFileName]
```

**Evaluated value:**

```sql
\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\UPEmail202654131248403.csv
```

## Execute SQL Tasks

### truncate DL reject stage

**Path:** `Package\CWM display name & DL update\truncate DL reject stage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
TRUNCATE TABLE ADattributesGroupRejects
```

### load ADemployeeStage

**Path:** `Package\OU update\Sequence Container\AD extract Loop\load ADemployeeStage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
with stage as 
(
select 
? as EmployeeID, 
? as cn, 
? as company, 
? as description, 
? as displayName, 
? as mail, 
? as manager, 
? as samaccountName, 
? as sn,
? as Department,
? as givenname,
? as memberOf,
? as Title
)

insert ADEmployeeStage 
select *
from Stage
/*
where 
 (
  samaccountName is not NULL
  and samaccountName <> ''
  and len(samaccountName) > 0
  and samaccountName <> 'no data'
 )
OR
 (
  mail is not NULL
  and mail <> ''
  and len(mail) > 0
  and mail <> 'no data'
  and mail like '@buildabear%'
 )
*/
```

### Merge ADEmployee

**Path:** `Package\OU update\Sequence Container\Merge ADEmployee`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec spMergeADEmployee
```

### stage employee ID

**Path:** `Package\OU update\Sequence Container\stage employee ID`  
**Connection:** DW (papamart/dw)  

```sql
select EepEEID from  [dbo].[vwUHCMUltiproToADouMove]

```

### truncate stage

**Path:** `Package\OU update\Sequence Container\truncate stage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
TRUNCATE TABLE ADEmployeeStage
```

### count OU moves

**Path:** `Package\OU update\count OU moves`  
**Connection:** DW (papamart/dw)  

```sql
select count(*)  from [dbo].[vwUHCMUltiproToADouMove]
```

### wait

**Path:** `Package\OU update\wait`  
**Connection:** DW (papamart/dw)  

```sql
WAITFOR DELAY '00:00:22';
```

### sFTP Upload

**Path:** `Package\create file to reset samaccount and email in Ultipro ONE EMPLOYEE\SEQ - Generate SamAccountName CSV Files\sFTP Upload`  
**Connection:** IntegrationStaging (STL-SSIS-t-01/IntegrationStaging)  

```sql
declare
@winSCP varchar(1000),
@script varchar(1000),
@log varchar(1000),
@FTP varchar(4000),
@Log_query varchar(1000),
@Log_filename varchar(100),
@Log_file_location varchar(100),
@Log_bcp varchar(1000),
@body varchar(4000)

select 
@winSCP = '"\\stl-ssis-p-01\C$\Program Files (x86)\WinSCP\WinSCP.exe"',
@script = ' /script=\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\FTP\sFTPuploadScript.txt',
@log = ' /log=\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\FTP\FTPUpload.log',
@FTP = (@winSCP + @script + @log)

exec master..xp_cmdshell @FTP
--exec master..xp_cmdshell 'move \\STL-SSIS-P-01\integrationStaging\HR\UltiProTermSamaccount\*.csv \\STL-SSIS-P-01\integrationStaging\HR\UltiProTermSamaccount\Archive'
```

### load ADemployeeStage

**Path:** `Package\store demotion\Sequence Container\AD extract Loop\load ADemployeeStage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
with stage as 
(
select 
? as EmployeeID, 
? as cn, 
? as company, 
? as description, 
? as displayName, 
? as mail, 
? as manager, 
? as samaccountName, 
? as sn,
? as Department,
? as givenname,
? as memberOf,
? as Title
)

insert ADEmployeeStage 
select *
from Stage
/*
where 
 (
  samaccountName is not NULL
  and samaccountName <> ''
  and len(samaccountName) > 0
  and samaccountName <> 'no data'
 )
OR
 (
  mail is not NULL
  and mail <> ''
  and len(mail) > 0
  and mail <> 'no data'
  and mail like '@buildabear%'
 )
*/
```

### Merge ADEmployee

**Path:** `Package\store demotion\Sequence Container\Merge ADEmployee`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec spMergeADEmployee
```

### stage employee ID

**Path:** `Package\store demotion\Sequence Container\stage employee ID`  
**Connection:** DW (papamart/dw)  

```sql
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADdemote]

```

### truncate stage

**Path:** `Package\store demotion\Sequence Container\truncate stage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
TRUNCATE TABLE ADEmployeeStage
```

### count OU demotes

**Path:** `Package\store demotion\count OU demotes`  
**Connection:** DW (papamart/dw)  

```sql
select count(*)  from [dbo].[vwUHCMUltiproToADdemote]
```

### sFTP Upload

**Path:** `Package\store demotion\create file to reset samaccount and email in Ultipro\SEQ - Generate SamAccountName CSV Files\sFTP Upload`  
**Connection:** IntegrationStaging (STL-SSIS-t-01/IntegrationStaging)  

```sql
declare
@winSCP varchar(1000),
@script varchar(1000),
@log varchar(1000),
@FTP varchar(4000),
@Log_query varchar(1000),
@Log_filename varchar(100),
@Log_file_location varchar(100),
@Log_bcp varchar(1000),
@body varchar(4000)

select 
@winSCP = '"\\stl-ssis-p-01\C$\Program Files (x86)\WinSCP\WinSCP.exe"',
@script = ' /script=\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\FTP\sFTPuploadScript.txt',
@log = ' /log=\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\FTP\FTPUpload.log',
@FTP = (@winSCP + @script + @log)

exec master..xp_cmdshell @FTP
--exec master..xp_cmdshell 'move \\STL-SSIS-P-01\integrationStaging\HR\UltiProTermSamaccount\*.csv \\STL-SSIS-P-01\integrationStaging\HR\UltiProTermSamaccount\Archive'
```

### wait

**Path:** `Package\store demotion\wait`  
**Connection:** DW (papamart/dw)  

```sql
WAITFOR DELAY '00:00:22';
```

### load ADemployeeStage

**Path:** `Package\store promotion\Sequence Container\AD extract Loop\load ADemployeeStage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
with stage as 
(
select 
? as EmployeeID, 
? as cn, 
? as company, 
? as description, 
? as displayName, 
? as mail, 
? as manager, 
? as samaccountName, 
? as sn,
? as Department,
? as givenname,
? as memberOf,
? as Title
)

insert ADEmployeeStage 
select *
from Stage
/*
where 
 (
  samaccountName is not NULL
  and samaccountName <> ''
  and len(samaccountName) > 0
  and samaccountName <> 'no data'
 )
OR
 (
  mail is not NULL
  and mail <> ''
  and len(mail) > 0
  and mail <> 'no data'
  and mail like '@buildabear%'
 )
*/
```

### Merge ADEmployee

**Path:** `Package\store promotion\Sequence Container\Merge ADEmployee`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec spMergeADEmployee
```

### stage employee ID

**Path:** `Package\store promotion\Sequence Container\stage employee ID`  
**Connection:** DW (papamart/dw)  

```sql
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADpromote]
/*
select EepEEID from UHCMemp where EepEEID in (0059821,0059277)
*/
```

### truncate stage

**Path:** `Package\store promotion\Sequence Container\truncate stage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
TRUNCATE TABLE ADEmployeeStage
```

### count OU promotes

**Path:** `Package\store promotion\count OU promotes`  
**Connection:** DW (papamart/dw)  

```sql
select count(*)  from [dbo].[vwUHCMUltiproToADpromote]
```

### sFTP Upload

**Path:** `Package\store promotion\create file to reset samaccount and email in Ultipro\SEQ - Generate SamAccountName CSV Files\sFTP Upload`  
**Connection:** IntegrationStaging (STL-SSIS-t-01/IntegrationStaging)  

```sql
declare
@winSCP varchar(1000),
@script varchar(1000),
@log varchar(1000),
@FTP varchar(4000),
@Log_query varchar(1000),
@Log_filename varchar(100),
@Log_file_location varchar(100),
@Log_bcp varchar(1000),
@body varchar(4000)

select 
@winSCP = '"\\stl-ssis-p-01\C$\Program Files (x86)\WinSCP\WinSCP.exe"',
@script = ' /script=\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\FTP\sFTPuploadScript.txt',
@log = ' /log=\\STL-SSIs-p-01\integrationStaging\HR\UltiProTermSamaccount\FTP\FTPUpload.log',
@FTP = (@winSCP + @script + @log)

exec master..xp_cmdshell @FTP
--exec master..xp_cmdshell 'move \\STL-SSIS-P-01\integrationStaging\HR\UltiProTermSamaccount\*.csv \\STL-SSIS-P-01\integrationStaging\HR\UltiProTermSamaccount\Archive'
```

### wait

**Path:** `Package\store promotion\wait`  
**Connection:** DW (papamart/dw)  

```sql
WAITFOR DELAY '00:00:22';
```

### Truncate ActiveDirectoryDataStage

**Path:** `Package\update ActiveDirectoryDataStage table\SEQ - refresh ActiveDirectoryDataStage table\Truncate ActiveDirectoryDataStage`  
**Connection:** DW (papamart/dw)  

```sql
Truncate Table ActiveDirectoryDataStage
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| SQL |  | OLEDBSource | PrimaryEmail CSV | DW | SqlCommand |
| SQL |  | OLEDBSource | SamAccount CSV | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | remove CWM from group | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | update CWM email group | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | update CWM display name | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | update CWM display name w email | DW | SqlCommand |
| LDAP |  | OLEDBSource | Data Flow - memberOf | DW |  |
| OLE DB Source |  | OLEDBSource | update OU | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | update OU one time | DW | SqlCommand |
| SQL |  | OLEDBSource | PrimaryEmail CSV | DW | SqlCommand |
| SQL |  | OLEDBSource | SamAccount CSV | DW | SqlCommand |
| OLE DB Source 1 |  | OLEDBSource | send to AD | papamart.dw1 | SqlCommand |
| OLE DB Source 1 |  | OLEDBSource | send to AD 1 | papamart.dw1 | SqlCommand |
| OLE DB Source 1 |  | OLEDBSource | send to AD 2 | papamart.dw1 | SqlCommand |
| LDAP |  | OLEDBSource | Data Flow - memberOf | DW |  |
| OLE DB Source |  | OLEDBSource | add to Store Users DL | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | remove from CWM DL | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | update UHCMemp table | papamart.dw1 | SqlCommand |
| SQL |  | OLEDBSource | PrimaryEmail CSV | DW | SqlCommand |
| SQL |  | OLEDBSource | SamAccount CSV | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | send C to dataLoaderStaging | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | send RN to dataLoaderStaging | DW | SqlCommand |
| LDAP |  | OLEDBSource | Data Flow - memberOf | DW |  |
| OLE DB Source |  | OLEDBSource | update UHCMemp table | papamart.dw1 | SqlCommand |
| OLE DB Source |  | OLEDBSource | test update attribute | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | update all CWM display names | DW | SqlCommand |
| OLE DB Source |  | OLEDBSource | update ExtensionAttribute5 | DW | SqlCommand |

#### SQL — SqlCommand

```sql
with 
distinctEmpPromote
as
(
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADpromote]
union 
select '0081763'
)

select e.eepCompanyCode, convert(varchar, getdate(), 101) as EffectiveDate, vP.EepEEID, 'EmilyFe@buildabear.com' as PrimaryEmail   -- '^' as PrimaryEmail 
from distinctEmpPromote vP
join [dbo].[UHCMEmp] e on e.EepEEID = vP.EepEEID
where e.eepCompanyCode <> 'BABUK'
```

#### SQL — SqlCommand

```sql
with 
distinctEmpPromote
as
(
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADpromote]
union 
select '0081763'
)

select e.eepCompanyCode, convert(varchar, getdate(), 101) as EffectiveDate, vP.EepEEID, 'EmilyFe' as SamAccountname 
from distinctEmpPromote vP
join [dbo].[UHCMEmp] e on e.EepEEID = vP.EepEEID
where e.eepCompanyCode <> 'BABUK'
```

#### OLE DB Source — SqlCommand

```sql
select * from [dbo].[vwUHCMUltiproToADdlMove] where JbcJobCode <> 'DCWM'  and currentStoreDistributionList is not null
```

#### OLE DB Source — SqlCommand

```sql
select * from [dbo].[vwUHCMUltiproToADdlMove]
```

#### OLE DB Source — SqlCommand

```sql
select n.* from [dbo].[vwUHCMUltiproToADdisplayNames] n 
join [dbo].[UHCMEmp] u on n.EepEEID = u.EepEEID 
where 1=1 
and n.JbcJobCode in ('CWM','CNCWM','GWM','DCWM','DCWMTMP','CNGWM','CWMTMP','CNDCWM') 
and (u.InsertDate > getdate()-7 or u.UpdateDate > getdate()-7)
and u.Samaccountname is not null
```

#### OLE DB Source — SqlCommand

```sql
select n.* from [dbo].[vwUHCMUltiproToADdisplayNames] n 
join [dbo].[UHCMEmp] u on n.EepEEID = u.EepEEID 
where n.JbcJobCode in ('CWM','CNCWM','GWM','DCWM','DCWMTMP','CNGWM','CWMTMP','CNDCWM') 
and (u.InsertDate > getdate()-7 or u.UpdateDate > getdate()-7)
and u.Samaccountname is not null
```

#### OLE DB Source — SqlCommand

```sql
select * from [dbo].[vwUHCMUltiproToADouMove]
```

#### OLE DB Source — SqlCommand

```sql
select * from [dbo].[vwUHCMUltiproToADouMove2]
```

#### SQL — SqlCommand

```sql
with 
distinctEmpDemote
as
(
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADdemote]
--select '0044063' as 'EepEEID'
)

select e.eepCompanyCode, convert(varchar, getdate(), 101) as EffectiveDate, vP.EepEEID, '^' as PrimaryEmail 
from distinctEmpDemote vP
join [dbo].[UHCMEmp] e on e.EepEEID = vP.EepEEID
where e.eepCompanyCode <> 'BABUK'
```

#### SQL — SqlCommand

```sql
with 
distinctEmpDemote
as
(
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADdemote]
--select '0044063' as 'EepEEID'
)

select e.eepCompanyCode, convert(varchar, getdate(), 101) as EffectiveDate, vP.EepEEID
, vP.EepEEID as SamAccountname 
--, '^' as SamAccountname
from distinctEmpDemote vP
join [dbo].[UHCMEmp] e on e.EepEEID = vP.EepEEID
where e.eepCompanyCode <> 'BABUK'
```

#### OLE DB Source 1 — SqlCommand

```sql
SELECT [EecLocation]
      ,[EepEEID]
      ,[EepNameFirst]
      ,[EepNamePreferred]
      ,[EepNameLast]
      ,[LocDesc]
      ,[JbcJobCode]
      ,[EecOrgLvl1Code]
      ,[samaccountname]
      ,[newAdsPath]
      ,[objectToMove] as 'AdsPath'
      ,[EmployeeADGroup]
      ,[AD_Department]
      ,[UserPrincipalName]
	  ,EepEEID + '@buildabear.com' as 'NewUserPrincipalName'

  FROM [dbo].[vwUHCMUltiproToADdemote]
```

#### OLE DB Source — SqlCommand

```sql
select * from [dbo].[vwUHCMUltiproToADdlMove2] where EepEEID in
(
 select EepEEID from [dbo].[vwUHCMUltiproToADdemote]
)
and newGroupName is not null
```

#### OLE DB Source — SqlCommand

```sql
select * from [dbo].[vwUHCMUltiproToADdlMove2] where EepEEID in
(
 select EepEEID from [dbo].[vwUHCMUltiproToADdemote]
)
and currentStoreDIstributionList is not null
```

#### OLE DB Source — SqlCommand

```sql
select distinct(EepEEID), EecLocation,EepNameFirst,EepNameLast,JbcJobCode,EecOrgLvl1Code,samaccountname from [dbo].[vwUHCMUltiproToADdemote]
```

#### SQL — SqlCommand

```sql
with 
distinctEmpPromote
as
(
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADpromote]
)

select e.eepCompanyCode, convert(varchar, getdate(), 101) as EffectiveDate, vP.EepEEID, '^' as PrimaryEmail 
from distinctEmpPromote vP
join [dbo].[UHCMEmp] e on e.EepEEID = vP.EepEEID
where e.eepCompanyCode <> 'BABUK'
```

#### SQL — SqlCommand

```sql
with 
distinctEmpPromote
as
(
select distinct(EepEEID)  from [dbo].[vwUHCMUltiproToADpromote]
)

select e.eepCompanyCode, convert(varchar, getdate(), 101) as EffectiveDate, vP.EepEEID, '^' as SamAccountname 
from distinctEmpPromote vP
join [dbo].[UHCMEmp] e on e.EepEEID = vP.EepEEID
where e.eepCompanyCode <> 'BABUK'
```

#### OLE DB Source — SqlCommand

```sql
Select 
	ISNULL(e.UpdateDate, e.InsertDate) as [UpdatedTimeStamp],
	Cast(e.EecDateOfLastHire as datetime) as [StartDate],
	Cast(e.TerminatedEffectiveDate as datetime) as [EndDate],
	'C' as [ProvisioningEvent],
	Cast('' as Nvarchar) as [ProvisioningValue(s)],
	Cast(Case
		When e.JbcJobCode in ( 'BB', 'ASM', 'SL', 'CNBB', 'CNSL', 'CNASM', 'SLTMP', 'AWM', 'CNAWM') THEN 'US Bear Builder'
		When e.JbcJobCode in  ('CWM', 'CNCWM') THEN 'US Chief Workshop Manager'
		When e.LocDesc = m.LocCodeDescription THEN m.UserProvisioningRole 
		When m.UserProvisioningRole is null then  'BQ General'
		else m.UserProvisioningRole 
	END as Nvarchar) as [UserProvisioningRole],
	Cast(isnull(e.eepNamePreferred, e.EepNameFirst) as NVarChar) as [FirstName],
	Cast(e.EepNameMiddle as Nvarchar) as [MiddleName],
	Cast(e.EepNameLast as Nvarchar) as [LastName],
	Cast('' as Nvarchar) as [ContainerOU],
	Cast('' as datetime) as [AccountExpiration],
	Cast(e.JbcLongDesc as Nvarchar) as [Title],
	Cast(Case 
		When d.AD_Department is null  then 'BQ' 
		else d.AD_Department 
	END as Nvarchar) as [Department],
	Cast('' as Nvarchar) as [Office],
	Cast('' as Nvarchar) as [Street],
	Cast('' as Nvarchar) as [City],
	Cast('' as Nvarchar) as [State],
	Cast('' as Nvarchar) as [Zip/PostalCode],
	Cast('' as Nvarchar) as [Country],
	Cast('' as Nvarchar) as [Business],
	Cast('' as Nvarchar) as [Fax],
	Cast('' as Nvarchar) as [Mobile],
	Cast('' as Nvarchar) as [Pager],
	Cast('' as Nvarchar) as [Home],
	Cast(e.EepEEID as Nvarchar) as [EmployeeID],
	Cast('' as Nvarchar) as [EmployeeNumber],
	Cast('' as Nvarchar) as [AccountingCode],
	Cast(e.SupervisorID as Nvarchar) as [ManagerEmployeeID],
	Cast('' as Nvarchar) as [ManagerEmployeeNumber],
	Cast('' as Nvarchar) as [ManagerEmail],
	Cast('' as Nvarchar) as [ManagerFirstName],
	Cast('' as Nvarchar) as [ManagerMiddleName],
	Cast('' as Nvarchar) as [ManagerLastName],
	Cast('' as Nvarchar) as [Description], 
	Cast('' as Nvarchar) as [UserPassword], 
	Cast(e.EfoPhoneNumber as Nvarchar) as [Extension Attribute 1],
	Cast('' as Nvarchar) as [Extension Attribute 2],
	Cast('' as Nvarchar) as [Extension Attribute 3],
	Cast('' as Nvarchar) as [Extension Attribute 4],
	Cast('' as Nvarchar) as [Extension Attribute 5],
	Cast('' as Nvarchar) as [Extension Attribute 6],
	Cast('' as Nvarchar) as [Extension Attribute 7],
	Cast('' as Nvarchar) as [Extension Attribute 8],
	Cast('' as Nvarchar) as [Extension Attribute 9],
	Cast('' as Nvarchar) as [Extension Attribute 10],
	Cast('' as Nvarchar) as [Extension Attribute 11],
	Cast('' as Nvarchar) as [Extension Attribute 12],
	Cast('' as Nvarchar) as [Extension Attribute 13],
	Cast('' as Nvarchar) as [Extension Attribute 14],
	Cast('' as Nvarchar) as [Extension Attribute 15],
	Cast(e.sAMAccountName  as Nvarchar) as [User Logon Name (Pre-Windows 2000)],
	Cast('' as Nvarchar) as [User Logon Name],
	Cast('' as Nvarchar) as [Full Name],
	Cast(isnull(e.eepNamePreferred, e.EepNameFirst) + ' ' + e.EepNameLast as Nvarchar) as [Display Name],
	Cast('' as Nvarchar) as [Email],
	Cast('' as Nvarchar) as [Exchange Alias],
	Cast('' as Nvarchar) as [Exchange Display Name],
	Dateadd(minute, 30, getdate()) as InsertDate,
	Dateadd(minute, 30, getdate())as DateUpdated

	From UHCMEMP e with (nolock)
	left join UHCMRoleMap m 
		On e.LocDesc = m.LocCodeDescription
	left Join ADEmployee ad with (nolock)
		On ad.EmployeeID = e.SupervisorID
	Left Join UHCMDepartmentMap d with (nolock)
		On e.EecLocation = d.EecLocation
	left join vwADEmployee a with (nolock)
			On a.EmployeeID = e.EepEEID
	Where 1=1
	and e.EecLocation <> 'UKBQ'   
	and e.EecLocation not like '2%'
	
	--and Cast(Case
	--	When ((e.TerminatedFlag = 'Y' or e.EecEmplStatus = 'Terminated') and e.TermEmailSentFlag is null) THEN 'T'
	--	When a.EmployeeID is null and e.TerminatedFlag is null and e.sAMAccountName is NULL and e.EecEmplStatus <> 'Terminated' THEN 'H'
	--	When (a.EmployeeADGroup <> d.AD_Department) and e.EecEmplStatus <> 'Terminated' THEN 'C'
	--	Else 'P'
	--End as nvarchar) <> 'C'
	and e.EepEEID in (select EepEEID from [dbo].[vwUHCMUltiproToADpromote])
```

#### OLE DB Source — SqlCommand

```sql
Select 
	ISNULL(e.UpdateDate, e.InsertDate) as [UpdatedTimeStamp],
	Cast(e.EecDateOfLastHire as datetime) as [StartDate],
	Cast(e.TerminatedEffectiveDate as datetime) as [EndDate],
	'RN' as [ProvisioningEvent],
	Cast('' as Nvarchar) as [ProvisioningValue(s)],
	--Cast(Case
	--	When e.JbcJobCode in ( 'BB', 'ASM', 'SL', 'CNBB', 'CNSL', 'CNASM', 'SLTMP', 'AWM', 'CNAWM') THEN 'US Bear Builder'
	--	When e.JbcJobCode in  ('CWM', 'CNCWM','CWMTMP','CNCWMTMP') THEN 'US Chief Workshop Manager'
	--	When e.LocDesc = m.LocCodeDescription THEN m.UserProvisioningRole 
	--	When m.UserProvisioningRole is null then  'BQ General'
	--	else m.UserProvisioningRole 
	--END as Nvarchar) as [UserProvisioningRole],

		----***************************************************** new logic for new store roles added in Nov 2022
				[UserProvisioningRole] = CASE WHEN e.EepCompanyCode in ('BABW','BABCN','BABR') and e.EecOrgLvl1Code <> 'BRHS' THEN
					Cast(Case
						When e.JbcJobCode in ( 'BB', 'CNBB', 'XPOPBB') THEN 'US Bear Builder'
						When e.JbcJobCode in ( 'SL', 'CNSL', 'SLTMP',  'CNSLTMP', 'XPOPSL') THEN 'US Sales Lead'
						When e.JbcJobCode in ( 'ASM',  'CNAWM', 'AWM', 'CNAWM',  'AWMTMP', 'XPOPAWM') THEN 'US Assistant Manager'
						When e.JbcJobCode in  ('CWM', 'CNCWM','CWMTMP', 'CNCWMTMP', 'CNDCWM', 'DCWM', 'DCWMTMP', 'XPOPCWM','GWM') THEN 'US Chief Workshop Manager'
						When e.LocDesc = m.LocCodeDescription THEN m.UserProvisioningRole 
						When m.UserProvisioningRole is null then  'BQ General'
						else m.UserProvisioningRole 
					END as Nvarchar) 
					WHEN e.EepCompanyCode in ('BABW','BABCN','BABR') and e.EecOrgLvl1Code = 'BRHS' THEN
						Cast(Case
						When e.JbcJobCode in ('BHRECPT','BHWRKI','BHWRKII','WEBBBI','WEBBBII') THEN 'Bear House - WHSE'
						When e.JbcJobCode in ('ITBRHSSU','BHCLEAN', 'BHHRAD', 'BHHRASST', 'BHSHIPSP', 'BHWRKIII','DXBRHS','LOGWHOCO','LXBH',
                          -- 'LXWEB','MNTTCH','MNTTCH2','MXBHHR','MXBHMNT','MXBHOPS','MXGMBH','SMXOPSEC','SXBH','SXWEB','SXWEBAST','SXWHOCOR') THEN 'Bear House – General'
						    'LXWEB','MNTTCH','MNTTCH2','MXBHHR','MXBHMNT','MXBHOPS','MXGMBH','SMXOPSEC','SXBH','SXWEB','SXWEBAST','SXWHOCOR') THEN 'Bear House - General'
						--else 'Bear House – WHSE'
						else 'Bear House - WHSE'
					END as Nvarchar) 
			      WHEN e.EepCompanyCode = 'BABUK' THEN
					Cast(Case
						When  e.JbcJobCode in ('Bear Builder','Bearbuilder','IrelandBear Builder4','UKBear Builder4') THEN 'UK Bear Builder'
						
						When e.JbcJobCode in ('Assistant Workshop Manager','IrelandAssistant Workshop Manager30','IrelandAssistant Workshop Manager35','UKAssistant Workshop Manager20',
						  'UKAssistant Workshop Manager25','UKAssistant Workshop Manager30','UKAssistant Workshop Manager35','UKAssistant Workshop Manager40') THEN 'UK Assistant Manager'
						
						When e.JbcJobCode in (
						  'IrelandSales Lead Hourly12','IrelandSales Lead Hourly20','Sales Lead',
						  'Sales Lead Hourly','Sales Lead(Annual Salary)','Sales Lead(Hourly)','UKSales Lead Hourly12',
						  'UKSales Lead Hourly20','UKSales Lead Hourly4','IrelandSales Lead Hourly4') THEN 'UK Sales Lead'
						
						When e.JbcJobCode in  ('IrelandChief Workshop Manager40','Dual Site Chief Workshop Manager','Chief Workshop Manager',
							'UKChief Workshop Manager35','UKChief Workshop Manager40','UKDual Site Chief Workshop Manager35',
							'UKDual Site Chief Workshop Manager40') THEN 'UK Chief Workshop Manager'
						When e.JbcJobCode = m2.JbcJobCode THEN m2.UserProvisioningRole 
						When m2.UserProvisioningRole is null then  'UK BQ General'
						else m2.UserProvisioningRole 
					END as Nvarchar)
				ELSE m.UserProvisioningRole END,
				----*****************************************************




	Cast(coalesce (nullif (e.eepNamePreferred, ''), e.EepNameFirst) as NVarChar) as [FirstName],
	Cast(e.EepNameMiddle as Nvarchar) as [MiddleName],
	Cast(e.EepNameLast as Nvarchar) as [LastName],
	Cast('' as Nvarchar) as [ContainerOU],
	Cast('' as datetime) as [AccountExpiration],
	Cast(e.JbcLongDesc as Nvarchar) as [Title],
	Cast(Case 
		When d.AD_Department is null  then 'BQ' 
		else d.AD_Department 
	END as Nvarchar) as [Department],
	Cast('' as Nvarchar) as [Office],
	Cast('' as Nvarchar) as [Street],
	Cast('' as Nvarchar) as [City],
	Cast('' as Nvarchar) as [State],
	Cast('' as Nvarchar) as [Zip/PostalCode],
	Cast('' as Nvarchar) as [Country],
	Cast('' as Nvarchar) as [Business],
	Cast('' as Nvarchar) as [Fax],
	Cast('' as Nvarchar) as [Mobile],
	Cast('' as Nvarchar) as [Pager],
	Cast('' as Nvarchar) as [Home],
	Cast(e.EepEEID as Nvarchar) as [EmployeeID],
	Cast('' as Nvarchar) as [EmployeeNumber],
	Cast('' as Nvarchar) as [AccountingCode],
	Cast(e.SupervisorID as Nvarchar) as [ManagerEmployeeID],
	Cast('' as Nvarchar) as [ManagerEmployeeNumber],
	Cast('' as Nvarchar) as [ManagerEmail],
	Cast('' as Nvarchar) as [ManagerFirstName],
	Cast('' as Nvarchar) as [ManagerMiddleName],
	Cast('' as Nvarchar) as [ManagerLastName],
	Cast('' as Nvarchar) as [Description], 
	Cast('' as Nvarchar) as [UserPassword], 
	--Cast(e.EfoPhoneNumber as Nvarchar) as [Extension Attribute 1],
	--Cast('' as Nvarchar) as [Extension Attribute 2],
	--Cast('' as Nvarchar) as [Extension Attribute 3],
	--Cast('' as Nvarchar) as [Extension Attribute 4],
	--Cast('' as Nvarchar) as [Extension Attribute 5],
	[Extension Attribute 1] = 
        case 
            when e.EfoPhoneNumber is NULL and e.DateOfBirth is null then Cast(e.EepEEID as Nvarchar) 

            WHEN e.EepCompanyCode in ('BABW','BABCN','BABR') THEN Cast(e.EfoPhoneNumber as Nvarchar)
             WHEN e.EepCompanyCode = 'BABUK' THEN Cast(e.DateOfBirth as Nvarchar)    
        end,
	Cast('' as Nvarchar) as [Extension Attribute 2],
	Cast('' as Nvarchar) as [Extension Attribute 3],
	Cast('' as Nvarchar) as [Extension Attribute 4],
	Cast(e.JbcJobCode as Nvarchar) as [Extension Attribute 5],	
                   Cast('' as Nvarchar) as [Extension Attribute 6],
	Cast('' as Nvarchar) as [Extension Attribute 7],
	Cast('' as Nvarchar) as [Extension Attribute 8],
	Cast('' as Nvarchar) as [Extension Attribute 9],
	Cast('' as Nvarchar) as [Extension Attribute 10],
	Cast('' as Nvarchar) as [Extension Attribute 11],
	Cast('' as Nvarchar) as [Extension Attribute 12],
	Cast('' as Nvarchar) as [Extension Attribute 13],
	Cast('' as Nvarchar) as [Extension Attribute 14],
	Cast('' as Nvarchar) as [Extension Attribute 15],
	Cast(e.sAMAccountName  as Nvarchar) as [User Logon Name (Pre-Windows 2000)],
	Cast('' as Nvarchar) as [User Logon Name],
	Cast('' as Nvarchar) as [Full Name],
	Cast(isnull(e.eepNamePreferred, e.EepNameFirst) + ' ' + e.EepNameLast as Nvarchar) as [Display Name],
	Cast('' as Nvarchar) as [Email],
	Cast('' as Nvarchar) as [Exchange Alias],
	Cast('' as Nvarchar) as [Exchange Display Name],
	Dateadd(minute, 10, getdate()) as InsertDate,
	Dateadd(minute, 10, getdate())as DateUpdated

	From UHCMEMP e with (nolock)
	left join UHCMRoleMap m 
		On e.LocDesc = m.LocCodeDescription
	left join SHCMRoleMap m2
		On e.JbcJobCode = m2.JbcJobCode
	left Join ADEmployee ad with (nolock)
		On ad.EmployeeID = e.SupervisorID
	Left Join UHCMDepartmentMap d with (nolock)
		On e.EecLocation = d.EecLocation
	left join vwADEmployee a with (nolock)
			On a.EmployeeID = e.EepEEID
	Where 1=1
	and e.EecLocation <> 'UKBQ'   
	--and e.EecLocation not like '2%'
	
	--and Cast(Case
	--	When ((e.TerminatedFlag = 'Y' or e.EecEmplStatus = 'Terminated') and e.TermEmailSentFlag is null) THEN 'T'
	--	When a.EmployeeID is null and e.TerminatedFlag is null and e.sAMAccountName is NULL and e.EecEmplStatus <> 'Terminated' THEN 'H'
	--	When (a.EmployeeADGroup <> d.AD_Department) and e.EecEmplStatus <> 'Terminated' THEN 'C'
	--	Else 'P'
	--End as nvarchar) <> 'C'
	and e.EepEEID in (select EepEEID from [dbo].[vwUHCMUltiproToADpromote])
	and e.EepEEID not in (select EmployeeID from [coredb01].[AIMSconfig].[dbo].[DataLoaderStaging] where ProvisioningEvent = 'RN' and  (datediff(hh, UpdatedTimeStamp, getdate()) <= 2))
```

#### OLE DB Source — SqlCommand

```sql
select distinct(EepEEID), EecLocation,
'EepNameFirst' = CASE when EepNamePreferred is null then EepNameFirst
when EepNamePreferred = '' then  EepNameFirst
else EepNamePreferred end
,EepNameLast,JbcJobCode,EecOrgLvl1Code,samaccountname from [dbo].[vwUHCMUltiproToADpromote]
```

#### OLE DB Source — SqlCommand

```sql
select EecLocation, EepEEID, EepNameFirst, EepNamePreferred, EepNameLast, JbcJobCode, EecOrgLvl1Code
,samaccountname, 'IanW@buildabear.com' as UserPrincipleName, 'Ian Wallace' as NewDisplayName, samaccountname as MailNickname
from  [dbo].[UHCMEmp] where EepEEID = '0073834'
```

#### OLE DB Source — SqlCommand

```sql
select n.* from [dbo].[vwUHCMUltiproToADdisplayNames] n 
join [dbo].[UHCMEmp] u on n.EepEEID = u.EepEEID 
where n.JbcJobCode in ('CWM','CNCWM','GWM','DCWM')
--and u.EepEEID = '0000021'
--and (u.InsertDate > getdate()-1 or u.UpdateDate > getdate()-1)
```

#### OLE DB Source — SqlCommand

```sql
select EecLocation, EepEEID, EepNameFirst, EepNamePreferred, EepNameLast, JbcJobCode, JbcLongDesc, JbcLongDesc as title, EecOrgLvl1Code
,samaccountname,  EepEEID + '@buildabear.com' as UserPrincipleName, '' as NewDisplayName, samaccountname as MailNickname
from  [dbo].[UHCMEmp] where EepEEID in 
('0048804','0056997','0057974','0060667','0064358','0066410''0066561',
'0066841','0067095','0067984','0070136','0070322',
'0071569','0072498','0072685','0072907','0073072','0073373',
'0073563','0073759','0073811','0074018','0074497','0075176')
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| UP CSV |  | FlatFileDestination | PrimaryEmail CSV | UltiProImportEmailCSV |  |
| UP CSV |  | FlatFileDestination | SamAccount CSV | UltiProImportSamAccountCSV |  |
| OLE DB Destination |  | OLEDBDestination | update CWM email group | DWStaging |  |
| UP CSV |  | FlatFileDestination | PrimaryEmail CSV | UltiProImportEmailCSV |  |
| UP CSV |  | FlatFileDestination | SamAccount CSV | UltiProImportSamAccountCSV |  |
| OLE DB Destination |  | OLEDBDestination | remove from CWM DL | DWStaging |  |
| UP CSV |  | FlatFileDestination | PrimaryEmail CSV | UltiProImportEmailCSV |  |
| UP CSV |  | FlatFileDestination | SamAccount CSV | UltiProImportSamAccountCSV |  |
| OLE DB Destination |  | OLEDBDestination | send C to dataLoaderStaging | coredb01 |  |
| OLE DB Destination |  | OLEDBDestination | send RN to dataLoaderStaging | coredb01 |  |
| ActiveDirectoryDataStage |  | OLEDBDestination | DataFlow - ActiveDirectoryDataStage | DW |  |
