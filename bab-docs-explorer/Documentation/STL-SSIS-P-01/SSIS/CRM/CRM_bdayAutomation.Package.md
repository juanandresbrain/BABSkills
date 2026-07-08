# SSIS Package: Package

**Project:** CRM_bdayAutomation  
**Folder:** CRM  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| Archive | FILE |  |  |  |
| CA bday gift csv | FLATFILE |  |  |  |
| CRM | OLEDB | stl-crmdb-p-01 | crm | Data Source=stl-crmdb-p-01; Initial Catalog=crm; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| IntegrationStaging | OLEDB | STL-SSIS-p-01 | IntegrationStaging | Data Source=STL-SSIS-p-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| KODIAK | OLEDB | kodiak | DiscountMstrData | Data Source=kodiak; Initial Catalog=DiscountMstrData; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP | SMTP |  |  |  |
| STL-DYNSNC-P-01.DBAUtility | OLEDB | STL-DYNSNC-P-01 | DBAUtility | Data Source=STL-DYNSNC-P-01; Initial Catalog=DBAUtility; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| UK bday gift csv | FLATFILE |  |  |  |
| US bday gift csv | FLATFILE |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| Package | Package |
| 19th estimate for next month CA | SEQUENCE |
| next mo estimate | SendMailTask |
| next month estimate | ExecuteSQLTask |
| 19th estimate for next month UK | SEQUENCE |
| next mo estimate | SendMailTask |
| next month estimate | ExecuteSQLTask |
| 19th estimate for next month US | SEQUENCE |
| next mo estimate | SendMailTask |
| next month estimate | ExecuteSQLTask |
| backup month tables | SEQUENCE |
| Data Flow Task | Pipeline |
| truncate backup | ExecuteSQLTask |
| backup month tables 1 | SEQUENCE |
| Data Flow Task | Pipeline |
| truncate backup | ExecuteSQLTask |
| CA export prep | SEQUENCE |
| assign coupon and export files | SEQUENCE |
| create export tables | ExecuteSQLTask |
| create timestamp file | FileSystemTask |
| remove special char | ExecuteSQLTask |
| set firstDayOfMonth | ExecuteSQLTask |
| stage codes from DM | Pipeline |
| stage cust from CRM | Pipeline |
| update DM detail & produce file | Pipeline |
| update giftSent flag | ExecuteSQLTask |
| CA export prep daily | SEQUENCE |
| assign coupon and export files (daily) | SEQUENCE |
| create export tables | ExecuteSQLTask |
| create timestamp file | FileSystemTask |
| remove special char | ExecuteSQLTask |
| stage codes from DM | Pipeline |
| stage cust from CRM | Pipeline |
| update DM detail & produce file | Pipeline |
| update giftSent flag | ExecuteSQLTask |
| CA success | SendMailTask |
| CA success (daily) | SendMailTask |
| Expression Task | ExpressionTask |
| overwrite vars | ExecuteSQLTask |
| Sequence Container | SEQUENCE |
| coupon check & load | SEQUENCE |
| CA short | SendMailTask |
| count available CA codes | ExecuteSQLTask |
| count available UK codes | ExecuteSQLTask |
| count available US codes | ExecuteSQLTask |
| count CA codes needed | ExecuteSQLTask |
| count UK codes needed | ExecuteSQLTask |
| count US codes needed | ExecuteSQLTask |
| UK short | SendMailTask |
| US short | SendMailTask |
| daily run, initial stage | SEQUENCE |
| CRM_bday_CA_stage | Pipeline |
| CRM_bday_dup_stage | Pipeline |
| CRM_bday_UK_stage | Pipeline |
| CRM_bday_US_stage | Pipeline |
| set month | ExecuteSQLTask |
| merge daily to monthly | SEQUENCE |
| merge CA | ExecuteSQLTask |
| merge UK | ExecuteSQLTask |
| merge US | ExecuteSQLTask |
| overwrite lastDayOfMonth | ExecuteSQLTask |
| truncate daily stages | ExecuteSQLTask |
| Sequence Container 1 | SEQUENCE |
| 1rst of month, initial stage | SEQUENCE |
| CRM_bday_CA_stage | Pipeline |
| CRM_bday_dup_stage | Pipeline |
| CRM_bday_UK_stage | Pipeline |
| CRM_bday_US_stage | Pipeline |
| set month | ExecuteSQLTask |
| coupon check & load | SEQUENCE |
| CA short | SendMailTask |
| count available CA codes | ExecuteSQLTask |
| count available UK codes | ExecuteSQLTask |
| count available US codes | ExecuteSQLTask |
| count CA codes needed | ExecuteSQLTask |
| count UK codes needed | ExecuteSQLTask |
| count US codes needed | ExecuteSQLTask |
| UK short | SendMailTask |
| US short | SendMailTask |
| notification | SendMailTask |
| overwrite lastDayOfMonth | ExecuteSQLTask |
| truncate monthly stages | ExecuteSQLTask |
| Sequence Container 2 | SEQUENCE |
| Foreach Loop - Move to Archive | FOREACHLOOP |
| Archive File | FileSystemTask |
| FTP upload files | ExecuteSQLTask |
| Sequence Container 2 1 | SEQUENCE |
| Foreach Loop - Move to Archive | FOREACHLOOP |
| Archive File | FileSystemTask |
| FTP upload files | ExecuteSQLTask |
| set current dayOfMonth | ExecuteSQLTask |
| set firstDayOfMonth | ExecuteSQLTask |
| set lastDayOfMonth | ExecuteSQLTask |
| UK export prep | SEQUENCE |
| assign coupon and export files | SEQUENCE |
| create export tables | ExecuteSQLTask |
| create timestamp file | FileSystemTask |
| remove special char | ExecuteSQLTask |
| stage codes from DM | Pipeline |
| stage cust from CRM | Pipeline |
| update DM detail & produce file | Pipeline |
| update giftSent flag | ExecuteSQLTask |
| UK export prep daily | SEQUENCE |
| assign coupon and export files (daily) | SEQUENCE |
| create export tables | ExecuteSQLTask |
| create timestamp file | FileSystemTask |
| remove special char | ExecuteSQLTask |
| stage codes from DM | Pipeline |
| stage cust from CRM | Pipeline |
| update DM detail & produce file | Pipeline |
| update giftSent flag | ExecuteSQLTask |
| set current dayOfMonth | ExecuteSQLTask |
| set firstDayOfMonth | ExecuteSQLTask |
| set lastDayOfMonth | ExecuteSQLTask |
| UK success | SendMailTask |
| UK success (daily) | SendMailTask |
| US export prep | SEQUENCE |
| assign coupon and export files | SEQUENCE |
| create export tables | ExecuteSQLTask |
| create timestamp file | FileSystemTask |
| remove special char | ExecuteSQLTask |
| stage codes from DM | Pipeline |
| stage cust from CRM | Pipeline |
| update DM detail & produce file | Pipeline |
| update giftSent flag | ExecuteSQLTask |
| US export prep daily | SEQUENCE |
| assign coupon and export files (daily) | SEQUENCE |
| create export tables | ExecuteSQLTask |
| create timestamp file | FileSystemTask |
| remove special char | ExecuteSQLTask |
| stage codes from DM | Pipeline |
| stage cust from CRM | Pipeline |
| update DM detail & produce file | Pipeline |
| update giftSent flag | ExecuteSQLTask |
| US success | SendMailTask |
| US success (daily) | SendMailTask |
| wait | ExecuteSQLTask |
| wait 1 | ExecuteSQLTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- 19th estimate for next month CA [SEQUENCE]
  - next mo estimate [SendMailTask]
  - next month estimate [ExecuteSQLTask]
- 19th estimate for next month UK [SEQUENCE]
  - next mo estimate [SendMailTask]
  - next month estimate [ExecuteSQLTask]
- 19th estimate for next month US [SEQUENCE]
  - next mo estimate [SendMailTask]
  - next month estimate [ExecuteSQLTask]
- CA export prep [SEQUENCE]
- CA export prep daily [SEQUENCE]
  - assign coupon and export files (daily) [SEQUENCE]
    - create export tables [ExecuteSQLTask]
    - create timestamp file [FileSystemTask]
    - remove special char [ExecuteSQLTask]
    - stage codes from DM [Pipeline]
    - stage cust from CRM [Pipeline]
    - update DM detail & produce file [Pipeline]
    - update giftSent flag [ExecuteSQLTask]
  - assign coupon and export files [SEQUENCE]
    - create export tables [ExecuteSQLTask]
    - create timestamp file [FileSystemTask]
    - remove special char [ExecuteSQLTask]
    - set firstDayOfMonth [ExecuteSQLTask]
    - stage codes from DM [Pipeline]
    - stage cust from CRM [Pipeline]
    - update DM detail & produce file [Pipeline]
    - update giftSent flag [ExecuteSQLTask]
- CA success [SendMailTask]
- CA success (daily) [SendMailTask]
- Expression Task [ExpressionTask]
- Sequence Container [SEQUENCE]
- Sequence Container 1 [SEQUENCE]
  - 1rst of month, initial stage [SEQUENCE]
    - CRM_bday_CA_stage [Pipeline]
    - CRM_bday_UK_stage [Pipeline]
    - CRM_bday_US_stage [Pipeline]
    - CRM_bday_dup_stage [Pipeline]
    - set month [ExecuteSQLTask]
  - coupon check & load [SEQUENCE]
    - CA short [SendMailTask]
    - UK short [SendMailTask]
    - US short [SendMailTask]
    - count CA codes needed [ExecuteSQLTask]
    - count UK codes needed [ExecuteSQLTask]
    - count US codes needed [ExecuteSQLTask]
    - count available CA codes [ExecuteSQLTask]
    - count available UK codes [ExecuteSQLTask]
    - count available US codes [ExecuteSQLTask]
  - notification [SendMailTask]
  - overwrite lastDayOfMonth [ExecuteSQLTask]
  - truncate monthly stages [ExecuteSQLTask]
- Sequence Container 2 [SEQUENCE]
- Sequence Container 2 1 [SEQUENCE]
  - FTP upload files [ExecuteSQLTask]
  - Foreach Loop - Move to Archive [FOREACHLOOP]
    - Archive File [FileSystemTask]
  - FTP upload files [ExecuteSQLTask]
  - Foreach Loop - Move to Archive [FOREACHLOOP]
    - Archive File [FileSystemTask]
  - coupon check & load [SEQUENCE]
    - CA short [SendMailTask]
    - UK short [SendMailTask]
    - US short [SendMailTask]
    - count CA codes needed [ExecuteSQLTask]
    - count UK codes needed [ExecuteSQLTask]
    - count US codes needed [ExecuteSQLTask]
    - count available CA codes [ExecuteSQLTask]
    - count available UK codes [ExecuteSQLTask]
    - count available US codes [ExecuteSQLTask]
  - daily run, initial stage [SEQUENCE]
    - CRM_bday_CA_stage [Pipeline]
    - CRM_bday_UK_stage [Pipeline]
    - CRM_bday_US_stage [Pipeline]
    - CRM_bday_dup_stage [Pipeline]
    - set month [ExecuteSQLTask]
  - merge daily to monthly [SEQUENCE]
    - merge CA [ExecuteSQLTask]
    - merge UK [ExecuteSQLTask]
    - merge US [ExecuteSQLTask]
  - overwrite lastDayOfMonth [ExecuteSQLTask]
  - truncate daily stages [ExecuteSQLTask]
- UK export prep [SEQUENCE]
- UK export prep daily [SEQUENCE]
  - assign coupon and export files (daily) [SEQUENCE]
    - create export tables [ExecuteSQLTask]
    - create timestamp file [FileSystemTask]
    - remove special char [ExecuteSQLTask]
    - stage codes from DM [Pipeline]
    - stage cust from CRM [Pipeline]
    - update DM detail & produce file [Pipeline]
    - update giftSent flag [ExecuteSQLTask]
  - set current dayOfMonth [ExecuteSQLTask]
  - set firstDayOfMonth [ExecuteSQLTask]
  - set lastDayOfMonth [ExecuteSQLTask]
  - assign coupon and export files [SEQUENCE]
    - create export tables [ExecuteSQLTask]
    - create timestamp file [FileSystemTask]
    - remove special char [ExecuteSQLTask]
    - stage codes from DM [Pipeline]
    - stage cust from CRM [Pipeline]
    - update DM detail & produce file [Pipeline]
    - update giftSent flag [ExecuteSQLTask]
- UK success [SendMailTask]
- UK success (daily) [SendMailTask]
- US export prep [SEQUENCE]
- US export prep daily [SEQUENCE]
  - assign coupon and export files (daily) [SEQUENCE]
    - create export tables [ExecuteSQLTask]
    - create timestamp file [FileSystemTask]
    - remove special char [ExecuteSQLTask]
    - stage codes from DM [Pipeline]
    - stage cust from CRM [Pipeline]
    - update DM detail & produce file [Pipeline]
    - update giftSent flag [ExecuteSQLTask]
  - assign coupon and export files [SEQUENCE]
    - create export tables [ExecuteSQLTask]
    - create timestamp file [FileSystemTask]
    - remove special char [ExecuteSQLTask]
    - stage codes from DM [Pipeline]
    - stage cust from CRM [Pipeline]
    - update DM detail & produce file [Pipeline]
    - update giftSent flag [ExecuteSQLTask]
- US success [SendMailTask]
- US success (daily) [SendMailTask]
- backup month tables [SEQUENCE]
- backup month tables 1 [SEQUENCE]
  - Data Flow Task [Pipeline]
  - truncate backup [ExecuteSQLTask]
  - Data Flow Task [Pipeline]
  - truncate backup [ExecuteSQLTask]
- overwrite vars [ExecuteSQLTask]
- set current dayOfMonth [ExecuteSQLTask]
- set firstDayOfMonth [ExecuteSQLTask]
- set lastDayOfMonth [ExecuteSQLTask]
- wait [ExecuteSQLTask]
- wait 1 [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_19th_estimate_for_next_month_CA["19th estimate for next month CA"]
    n_Package_19th_estimate_for_next_month_CA_next_mo_estimate["next mo estimate"]
    n_Package_19th_estimate_for_next_month_CA_next_month_estimate["next month estimate"]
    n_Package_19th_estimate_for_next_month_UK["19th estimate for next month UK"]
    n_Package_19th_estimate_for_next_month_UK_next_mo_estimate["next mo estimate"]
    n_Package_19th_estimate_for_next_month_UK_next_month_estimate["next month estimate"]
    n_Package_19th_estimate_for_next_month_US["19th estimate for next month US"]
    n_Package_19th_estimate_for_next_month_US_next_mo_estimate["next mo estimate"]
    n_Package_19th_estimate_for_next_month_US_next_month_estimate["next month estimate"]
    n_Package_backup_month_tables["backup month tables"]
    n_Package_backup_month_tables_Data_Flow_Task["Data Flow Task"]
    n_Package_backup_month_tables_truncate_backup["truncate backup"]
    n_Package_backup_month_tables_1["backup month tables 1"]
    n_Package_backup_month_tables_1_Data_Flow_Task["Data Flow Task"]
    n_Package_backup_month_tables_1_truncate_backup["truncate backup"]
    n_Package_CA_export_prep["CA export prep"]
    n_Package_CA_export_prep_assign_coupon_and_export_files["assign coupon and export files"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_create_export_tables["create export tables"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_create_timestamp_file["create timestamp file"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_remove_special_char["remove special char"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_set_firstDayOfMonth["set firstDayOfMonth"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_stage_codes_from_DM["stage codes from DM"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM["stage cust from CRM"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file["update DM detail & produce file"]
    n_Package_CA_export_prep_assign_coupon_and_export_files_update_giftSent_flag["update giftSent flag"]
    n_Package_CA_export_prep_daily["CA export prep daily"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily_["assign coupon and export files (daily)"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__create_export_tables["create export tables"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__create_timestamp_file["create timestamp file"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char["remove special char"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM["stage codes from DM"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM["stage cust from CRM"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file["update DM detail & produce file"]
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag["update giftSent flag"]
    n_Package_CA_success["CA success"]
    n_Package_CA_success__daily_["CA success (daily)"]
    n_Package_Expression_Task["Expression Task"]
    n_Package_overwrite_vars["overwrite vars"]
    n_Package_Sequence_Container["Sequence Container"]
    n_Package_Sequence_Container_coupon_check___load["coupon check & load"]
    n_Package_Sequence_Container_coupon_check___load_CA_short["CA short"]
    n_Package_Sequence_Container_coupon_check___load_count_available_CA_codes["count available CA codes"]
    n_Package_Sequence_Container_coupon_check___load_count_available_UK_codes["count available UK codes"]
    n_Package_Sequence_Container_coupon_check___load_count_available_US_codes["count available US codes"]
    n_Package_Sequence_Container_coupon_check___load_count_CA_codes_needed["count CA codes needed"]
    n_Package_Sequence_Container_coupon_check___load_count_UK_codes_needed["count UK codes needed"]
    n_Package_Sequence_Container_coupon_check___load_count_US_codes_needed["count US codes needed"]
    n_Package_Sequence_Container_coupon_check___load_UK_short["UK short"]
    n_Package_Sequence_Container_coupon_check___load_US_short["US short"]
    n_Package_Sequence_Container_daily_run__initial_stage["daily run, initial stage"]
    n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_CA_stage["CRM_bday_CA_stage"]
    n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_dup_stage["CRM_bday_dup_stage"]
    n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_UK_stage["CRM_bday_UK_stage"]
    n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_US_stage["CRM_bday_US_stage"]
    n_Package_Sequence_Container_daily_run__initial_stage_set_month["set month"]
    n_Package_Sequence_Container_merge_daily_to_monthly["merge daily to monthly"]
    n_Package_Sequence_Container_merge_daily_to_monthly_merge_CA["merge CA"]
    n_Package_Sequence_Container_merge_daily_to_monthly_merge_UK["merge UK"]
    n_Package_Sequence_Container_merge_daily_to_monthly_merge_US["merge US"]
    n_Package_Sequence_Container_overwrite_lastDayOfMonth["overwrite lastDayOfMonth"]
    n_Package_Sequence_Container_truncate_daily_stages["truncate daily stages"]
    n_Package_Sequence_Container_1["Sequence Container 1"]
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage["1rst of month, initial stage"]
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_CA_stage["CRM_bday_CA_stage"]
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_dup_stage["CRM_bday_dup_stage"]
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_UK_stage["CRM_bday_UK_stage"]
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_US_stage["CRM_bday_US_stage"]
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_set_month["set month"]
    n_Package_Sequence_Container_1_coupon_check___load["coupon check & load"]
    n_Package_Sequence_Container_1_coupon_check___load_CA_short["CA short"]
    n_Package_Sequence_Container_1_coupon_check___load_count_available_CA_codes["count available CA codes"]
    n_Package_Sequence_Container_1_coupon_check___load_count_available_UK_codes["count available UK codes"]
    n_Package_Sequence_Container_1_coupon_check___load_count_available_US_codes["count available US codes"]
    n_Package_Sequence_Container_1_coupon_check___load_count_CA_codes_needed["count CA codes needed"]
    n_Package_Sequence_Container_1_coupon_check___load_count_UK_codes_needed["count UK codes needed"]
    n_Package_Sequence_Container_1_coupon_check___load_count_US_codes_needed["count US codes needed"]
    n_Package_Sequence_Container_1_coupon_check___load_UK_short["UK short"]
    n_Package_Sequence_Container_1_coupon_check___load_US_short["US short"]
    n_Package_Sequence_Container_1_notification["notification"]
    n_Package_Sequence_Container_1_overwrite_lastDayOfMonth["overwrite lastDayOfMonth"]
    n_Package_Sequence_Container_1_truncate_monthly_stages["truncate monthly stages"]
    n_Package_Sequence_Container_2["Sequence Container 2"]
    n_Package_Sequence_Container_2_Foreach_Loop___Move_to_Archive["Foreach Loop - Move to Archive"]
    n_Package_Sequence_Container_2_Foreach_Loop___Move_to_Archive_Archive_File["Archive File"]
    n_Package_Sequence_Container_2_FTP_upload_files["FTP upload files"]
    n_Package_Sequence_Container_2_1["Sequence Container 2 1"]
    n_Package_Sequence_Container_2_1_Foreach_Loop___Move_to_Archive["Foreach Loop - Move to Archive"]
    n_Package_Sequence_Container_2_1_Foreach_Loop___Move_to_Archive_Archive_File["Archive File"]
    n_Package_Sequence_Container_2_1_FTP_upload_files["FTP upload files"]
    n_Package_set_current_dayOfMonth["set current dayOfMonth"]
    n_Package_set_firstDayOfMonth["set firstDayOfMonth"]
    n_Package_set_lastDayOfMonth["set lastDayOfMonth"]
    n_Package_UK_export_prep["UK export prep"]
    n_Package_UK_export_prep_assign_coupon_and_export_files["assign coupon and export files"]
    n_Package_UK_export_prep_assign_coupon_and_export_files_create_export_tables["create export tables"]
    n_Package_UK_export_prep_assign_coupon_and_export_files_create_timestamp_file["create timestamp file"]
    n_Package_UK_export_prep_assign_coupon_and_export_files_remove_special_char["remove special char"]
    n_Package_UK_export_prep_assign_coupon_and_export_files_stage_codes_from_DM["stage codes from DM"]
    n_Package_UK_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM["stage cust from CRM"]
    n_Package_UK_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file["update DM detail & produce file"]
    n_Package_UK_export_prep_assign_coupon_and_export_files_update_giftSent_flag["update giftSent flag"]
    n_Package_UK_export_prep_daily["UK export prep daily"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily_["assign coupon and export files (daily)"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__create_export_tables["create export tables"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__create_timestamp_file["create timestamp file"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char["remove special char"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM["stage codes from DM"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM["stage cust from CRM"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file["update DM detail & produce file"]
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag["update giftSent flag"]
    n_Package_UK_export_prep_daily_set_current_dayOfMonth["set current dayOfMonth"]
    n_Package_UK_export_prep_daily_set_firstDayOfMonth["set firstDayOfMonth"]
    n_Package_UK_export_prep_daily_set_lastDayOfMonth["set lastDayOfMonth"]
    n_Package_UK_success["UK success"]
    n_Package_UK_success__daily_["UK success (daily)"]
    n_Package_US_export_prep["US export prep"]
    n_Package_US_export_prep_assign_coupon_and_export_files["assign coupon and export files"]
    n_Package_US_export_prep_assign_coupon_and_export_files_create_export_tables["create export tables"]
    n_Package_US_export_prep_assign_coupon_and_export_files_create_timestamp_file["create timestamp file"]
    n_Package_US_export_prep_assign_coupon_and_export_files_remove_special_char["remove special char"]
    n_Package_US_export_prep_assign_coupon_and_export_files_stage_codes_from_DM["stage codes from DM"]
    n_Package_US_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM["stage cust from CRM"]
    n_Package_US_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file["update DM detail & produce file"]
    n_Package_US_export_prep_assign_coupon_and_export_files_update_giftSent_flag["update giftSent flag"]
    n_Package_US_export_prep_daily["US export prep daily"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily_["assign coupon and export files (daily)"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__create_export_tables["create export tables"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__create_timestamp_file["create timestamp file"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char["remove special char"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM["stage codes from DM"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM["stage cust from CRM"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file["update DM detail & produce file"]
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag["update giftSent flag"]
    n_Package_US_success["US success"]
    n_Package_US_success__daily_["US success (daily)"]
    n_Package_wait["wait"]
    n_Package_wait_1["wait 1"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_19th_estimate_for_next_month_CA_next_month_estimate --> n_Package_19th_estimate_for_next_month_CA_next_mo_estimate
    n_Package_19th_estimate_for_next_month_UK_next_month_estimate --> n_Package_19th_estimate_for_next_month_UK_next_mo_estimate
    n_Package_19th_estimate_for_next_month_US_next_month_estimate --> n_Package_19th_estimate_for_next_month_US_next_mo_estimate
    n_Package_backup_month_tables_truncate_backup --> n_Package_backup_month_tables_Data_Flow_Task
    n_Package_backup_month_tables_1_truncate_backup --> n_Package_backup_month_tables_1_Data_Flow_Task
    n_Package_CA_export_prep_assign_coupon_and_export_files_create_export_tables --> n_Package_CA_export_prep_assign_coupon_and_export_files_stage_codes_from_DM
    n_Package_CA_export_prep_assign_coupon_and_export_files_stage_codes_from_DM --> n_Package_CA_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM
    n_Package_CA_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM --> n_Package_CA_export_prep_assign_coupon_and_export_files_update_giftSent_flag
    n_Package_CA_export_prep_assign_coupon_and_export_files_remove_special_char --> n_Package_CA_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file
    n_Package_CA_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file --> n_Package_CA_export_prep_assign_coupon_and_export_files_create_timestamp_file
    n_Package_CA_export_prep_assign_coupon_and_export_files_update_giftSent_flag --> n_Package_CA_export_prep_assign_coupon_and_export_files_remove_special_char
    n_Package_CA_export_prep_assign_coupon_and_export_files_set_firstDayOfMonth --> n_Package_CA_export_prep_assign_coupon_and_export_files_create_export_tables
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__create_export_tables --> n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM --> n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM --> n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char --> n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file --> n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__create_timestamp_file
    n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag --> n_Package_CA_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char
    n_Package_Sequence_Container_coupon_check___load_count_available_US_codes --> n_Package_Sequence_Container_coupon_check___load_count_US_codes_needed
    n_Package_Sequence_Container_coupon_check___load_count_available_CA_codes --> n_Package_Sequence_Container_coupon_check___load_count_CA_codes_needed
    n_Package_Sequence_Container_coupon_check___load_count_available_UK_codes --> n_Package_Sequence_Container_coupon_check___load_count_UK_codes_needed
    n_Package_Sequence_Container_coupon_check___load_count_UK_codes_needed --> n_Package_Sequence_Container_coupon_check___load_UK_short
    n_Package_Sequence_Container_coupon_check___load_count_CA_codes_needed --> n_Package_Sequence_Container_coupon_check___load_CA_short
    n_Package_Sequence_Container_coupon_check___load_count_US_codes_needed --> n_Package_Sequence_Container_coupon_check___load_US_short
    n_Package_Sequence_Container_daily_run__initial_stage_set_month --> n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_dup_stage
    n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_dup_stage --> n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_US_stage
    n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_US_stage --> n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_CA_stage
    n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_CA_stage --> n_Package_Sequence_Container_daily_run__initial_stage_CRM_bday_UK_stage
    n_Package_Sequence_Container_merge_daily_to_monthly_merge_US --> n_Package_Sequence_Container_merge_daily_to_monthly_merge_CA
    n_Package_Sequence_Container_merge_daily_to_monthly_merge_CA --> n_Package_Sequence_Container_merge_daily_to_monthly_merge_UK
    n_Package_Sequence_Container_truncate_daily_stages --> n_Package_Sequence_Container_daily_run__initial_stage
    n_Package_Sequence_Container_daily_run__initial_stage --> n_Package_Sequence_Container_merge_daily_to_monthly
    n_Package_Sequence_Container_merge_daily_to_monthly --> n_Package_Sequence_Container_coupon_check___load
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_set_month --> n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_dup_stage
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_dup_stage --> n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_US_stage
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_US_stage --> n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_CA_stage
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_CA_stage --> n_Package_Sequence_Container_1_1rst_of_month__initial_stage_CRM_bday_UK_stage
    n_Package_Sequence_Container_1_coupon_check___load_count_available_US_codes --> n_Package_Sequence_Container_1_coupon_check___load_count_US_codes_needed
    n_Package_Sequence_Container_1_coupon_check___load_count_available_CA_codes --> n_Package_Sequence_Container_1_coupon_check___load_count_CA_codes_needed
    n_Package_Sequence_Container_1_coupon_check___load_count_available_UK_codes --> n_Package_Sequence_Container_1_coupon_check___load_count_UK_codes_needed
    n_Package_Sequence_Container_1_coupon_check___load_count_US_codes_needed --> n_Package_Sequence_Container_1_coupon_check___load_US_short
    n_Package_Sequence_Container_1_coupon_check___load_count_UK_codes_needed --> n_Package_Sequence_Container_1_coupon_check___load_UK_short
    n_Package_Sequence_Container_1_coupon_check___load_count_CA_codes_needed --> n_Package_Sequence_Container_1_coupon_check___load_CA_short
    n_Package_Sequence_Container_1_truncate_monthly_stages --> n_Package_Sequence_Container_1_notification
    n_Package_Sequence_Container_1_1rst_of_month__initial_stage --> n_Package_Sequence_Container_1_coupon_check___load
    n_Package_Sequence_Container_1_notification --> n_Package_Sequence_Container_1_1rst_of_month__initial_stage
    n_Package_Sequence_Container_2_FTP_upload_files --> n_Package_Sequence_Container_2_Foreach_Loop___Move_to_Archive
    n_Package_Sequence_Container_2_1_FTP_upload_files --> n_Package_Sequence_Container_2_1_Foreach_Loop___Move_to_Archive
    n_Package_UK_export_prep_assign_coupon_and_export_files_create_export_tables --> n_Package_UK_export_prep_assign_coupon_and_export_files_stage_codes_from_DM
    n_Package_UK_export_prep_assign_coupon_and_export_files_stage_codes_from_DM --> n_Package_UK_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM
    n_Package_UK_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM --> n_Package_UK_export_prep_assign_coupon_and_export_files_update_giftSent_flag
    n_Package_UK_export_prep_assign_coupon_and_export_files_remove_special_char --> n_Package_UK_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file
    n_Package_UK_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file --> n_Package_UK_export_prep_assign_coupon_and_export_files_create_timestamp_file
    n_Package_UK_export_prep_assign_coupon_and_export_files_update_giftSent_flag --> n_Package_UK_export_prep_assign_coupon_and_export_files_remove_special_char
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__create_export_tables --> n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM --> n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM --> n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char --> n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file --> n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__create_timestamp_file
    n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag --> n_Package_UK_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char
    n_Package_UK_export_prep_daily_set_lastDayOfMonth --> n_Package_UK_export_prep_daily_set_current_dayOfMonth
    n_Package_UK_export_prep_daily_set_firstDayOfMonth --> n_Package_UK_export_prep_daily_set_lastDayOfMonth
    n_Package_US_export_prep_assign_coupon_and_export_files_create_export_tables --> n_Package_US_export_prep_assign_coupon_and_export_files_stage_codes_from_DM
    n_Package_US_export_prep_assign_coupon_and_export_files_stage_codes_from_DM --> n_Package_US_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM
    n_Package_US_export_prep_assign_coupon_and_export_files_stage_cust_from_CRM --> n_Package_US_export_prep_assign_coupon_and_export_files_update_giftSent_flag
    n_Package_US_export_prep_assign_coupon_and_export_files_remove_special_char --> n_Package_US_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file
    n_Package_US_export_prep_assign_coupon_and_export_files_update_DM_detail___produce_file --> n_Package_US_export_prep_assign_coupon_and_export_files_create_timestamp_file
    n_Package_US_export_prep_assign_coupon_and_export_files_update_giftSent_flag --> n_Package_US_export_prep_assign_coupon_and_export_files_remove_special_char
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__create_export_tables --> n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__stage_codes_from_DM --> n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__stage_cust_from_CRM --> n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char --> n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__update_DM_detail___produce_file --> n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__create_timestamp_file
    n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__update_giftSent_flag --> n_Package_US_export_prep_daily_assign_coupon_and_export_files__daily__remove_special_char
    n_Package_set_current_dayOfMonth --> n_Package_Sequence_Container
    n_Package_set_lastDayOfMonth --> n_Package_set_current_dayOfMonth
    n_Package_UK_success --> n_Package_wait
    n_Package_Sequence_Container --> n_Package_US_export_prep_daily
    n_Package_Sequence_Container_1 --> n_Package_UK_export_prep
    n_Package_Sequence_Container --> n_Package_CA_export_prep_daily
    n_Package_Sequence_Container --> n_Package_UK_export_prep_daily
    n_Package_backup_month_tables --> n_Package_Expression_Task
    n_Package_US_success__daily_ --> n_Package_wait_1
    n_Package_US_export_prep_daily --> n_Package_US_success__daily_
    n_Package_CA_export_prep_daily --> n_Package_CA_success__daily_
    n_Package_UK_export_prep_daily --> n_Package_UK_success__daily_
    n_Package_set_current_dayOfMonth --> n_Package_Sequence_Container_1
    n_Package_set_firstDayOfMonth --> n_Package_set_lastDayOfMonth
    n_Package_CA_success__daily_ --> n_Package_wait_1
    n_Package_UK_success__daily_ --> n_Package_wait_1
    n_Package_Sequence_Container_2_1 --> n_Package_backup_month_tables
    n_Package_Sequence_Container_2 --> n_Package_backup_month_tables_1
    n_Package_Expression_Task --> n_Package_19th_estimate_for_next_month_US
    n_Package_Expression_Task --> n_Package_19th_estimate_for_next_month_CA
    n_Package_Expression_Task --> n_Package_19th_estimate_for_next_month_UK
    n_Package_wait --> n_Package_Sequence_Container_2
    n_Package_wait_1 --> n_Package_Sequence_Container_2_1
    n_Package_US_export_prep --> n_Package_US_success
    n_Package_Sequence_Container_1 --> n_Package_CA_export_prep
    n_Package_CA_export_prep --> n_Package_CA_success
    n_Package_UK_export_prep --> n_Package_UK_success
    n_Package_US_success --> n_Package_wait
    n_Package_Sequence_Container_1 --> n_Package_US_export_prep
    n_Package_CA_success --> n_Package_wait
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | DateTimeStamp | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | varAvailableCAcodes | No |
| User | varAvailableUKcodes | No |
| User | varAvailableUScodes | No |
| User | varCAestimateMessage | Yes |
| User | varCAfile | No |
| User | varCAsuccessMessage | Yes |
| User | varCodeQuery | No |
| User | varDateStamp | Yes |
| User | varDayCount | No |
| User | varExt | No |
| User | varFileToArchive | No |
| User | varFirstofMonth | No |
| User | varFirstofMonthDate | No |
| User | varLastofMonth | No |
| User | varLastofMonthDate | No |
| User | varMonthCount | No |
| User | varMonthCount2 | No |
| User | varNeededCAcodes | No |
| User | varNeededUKcodes | No |
| User | varNeededUScodes | No |
| User | varNewCAfilename | Yes |
| User | varNewUKfilename | Yes |
| User | varNewUSfilename | Yes |
| User | varNextMonthEstimateCA | No |
| User | varNextMonthEstimateUK | No |
| User | varNextMonthEstimateUS | No |
| User | varOriginalCAfilename | Yes |
| User | varOriginalUKfilename | Yes |
| User | varOriginalUSfilename | Yes |
| User | varRemainingCAcodes | No |
| User | varRemainingUKcodes | No |
| User | varRemainingUScodes | No |
| User | varStageFolder | No |
| User | varUKestimateMessage | Yes |
| User | varUKfile | No |
| User | varUKsuccessMessage | Yes |
| User | varUSestimateMessage | Yes |
| User | varUSfile | No |
| User | varUSsuccessMessage | Yes |

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
2021630102125737
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
6/30/2021
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
2021-6-30
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
6/30/2021
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
2021-6-30
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
6/29/2021
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
2021-6-29
```

#### User::varCAestimateMessage

**Expression:**

```sql
"Coupons estimated for CA next month (15% added): " + (DT_WSTR, 10)@[User::varNextMonthEstimateCA]
```

**Evaluated value:**

```sql
Coupons estimated for CA next month (15% added): 0
```

#### User::varCAsuccessMessage

**Expression:**

```sql
"Coupons created for CA: " + "Needed codes: " + (DT_WSTR, 10)@[User::varNeededCAcodes] + ", Available codes: " + (DT_WSTR, 10)@[User::varAvailableCAcodes]
```

**Evaluated value:**

```sql
Coupons created for CA: Needed codes: 0, Available codes: 0
```

#### User::varDateStamp

**Expression:**

```sql
(DT_WSTR, 4)DATEPART("yyyy",GETDATE()) 
+ RIGHT("0" + (DT_WSTR, 2) DATEPART("mm",GETDATE()),2) 
+ RIGHT("0" + (DT_WSTR, 2) DATEPART("dd",GETDATE()),2)
```

**Evaluated value:**

```sql
20210630
```

#### User::varNewCAfilename

**Expression:**

```sql
@[User::varStageFolder] + @[User::varCAfile] +  "_" + @[User::varDateStamp] + @[User::varExt]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\CRM\CA_BirthdayGift_20210630.csv
```

#### User::varNewUKfilename

**Expression:**

```sql
@[User::varStageFolder] + @[User::varUKfile] +  "_" + @[User::varDateStamp] + @[User::varExt]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\CRM\UK_BirthdayGift_20210630.csv
```

#### User::varNewUSfilename

**Expression:**

```sql
@[User::varStageFolder] + @[User::varUSfile] +  "_" + @[User::varDateStamp] + @[User::varExt]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\CRM\US_BirthdayGift_20210630.csv
```

#### User::varOriginalCAfilename

**Expression:**

```sql
@[User::varStageFolder] + @[User::varCAfile] +  @[User::varExt]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\CRM\CA_BirthdayGift.csv
```

#### User::varOriginalUKfilename

**Expression:**

```sql
@[User::varStageFolder] + @[User::varUKfile] +  @[User::varExt]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\CRM\UK_BirthdayGift.csv
```

#### User::varOriginalUSfilename

**Expression:**

```sql
@[User::varStageFolder] + @[User::varUSfile] +  @[User::varExt]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\CRM\US_BirthdayGift.csv
```

#### User::varUKestimateMessage

**Expression:**

```sql
"Coupons estimated for UK next month (15% added): " + (DT_WSTR, 10)@[User::varNextMonthEstimateUK]
```

**Evaluated value:**

```sql
Coupons estimated for UK next month (15% added): 0
```

#### User::varUKsuccessMessage

**Expression:**

```sql
"Coupons created for UK: " + "Needed codes: " + (DT_WSTR, 10)@[User::varNeededUKcodes] + ", Available codes: " + (DT_WSTR, 10)@[User::varAvailableUKcodes]
```

**Evaluated value:**

```sql
Coupons created for UK: Needed codes: 0, Available codes: 0
```

#### User::varUSestimateMessage

**Expression:**

```sql
"Coupons estimated for US next month (15% added): " + (DT_WSTR, 10)@[User::varNextMonthEstimateUS]
```

**Evaluated value:**

```sql
Coupons estimated for US next month (15% added): 0
```

#### User::varUSsuccessMessage

**Expression:**

```sql
"Coupons created for US: " + "Needed codes: " + (DT_WSTR, 10)@[User::varNeededUScodes] + ", Available codes: " + (DT_WSTR, 10)@[User::varAvailableUScodes]
```

**Evaluated value:**

```sql
Coupons created for US: Needed codes: 0, Available codes: 0
```

## Execute SQL Tasks

### next month estimate

**Path:** `Package\19th estimate for next month CA\next month estimate`  
**Connection:** CRM (stl-crmdb-p-01/crm)  

```sql

 with nextMonthEstimateCA as
(
select 
 distinct
 cast(c.customer_no as varchar) as subscriberkey,
 e.email_address,
 ca.attribute_code,
 ca.attribute_comment,
 ca.attribute_value
 
from [stl-crmdb-p-01].crm.dbo.customer c
 join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
 join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
 join [stl-crmdb-p-01].crm.dbo.customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
 join [stl-crmdb-p-01].crm.dbo.email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
 join [stl-crmdb-p-01].crm.dbo.email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
 join [stl-crmdb-p-01].crm.dbo.address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
 right(ca.attribute_value,2)*1=?

 and a.country_code='CAN'
 and e.email_indicator in (0,9)
 and ed.email_opt_in_flag=1
 
 )

select cast(count(*)*1.13 as int) as 'estimateCA' from nextMonthEstimateCA
```

### next month estimate

**Path:** `Package\19th estimate for next month UK\next month estimate`  
**Connection:** CRM (stl-crmdb-p-01/crm)  

```sql

 with nextMonthEstimateUK as
(
select 
 distinct
 cast(c.customer_no as varchar) as subscriberkey,
 e.email_address,
 ca.attribute_code,
 ca.attribute_comment,
 ca.attribute_value
 
from [stl-crmdb-p-01].crm.dbo.customer c
 join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
 join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
 join [stl-crmdb-p-01].crm.dbo.customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
 join [stl-crmdb-p-01].crm.dbo.email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
 join [stl-crmdb-p-01].crm.dbo.email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
 join [stl-crmdb-p-01].crm.dbo.address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
 right(ca.attribute_value,2)*1=?

 and a.country_code='GBR'
 and e.email_indicator in (0,9)
 and ed.email_opt_in_flag=1
 
 )

select cast(count(*)*1.13 as int) as 'estimateUK' from nextMonthEstimateUK
```

### next month estimate

**Path:** `Package\19th estimate for next month US\next month estimate`  
**Connection:** CRM (stl-crmdb-p-01/crm)  

```sql

 with nextMonthEstimateUS as
(
select 
	distinct
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value
	
from [stl-crmdb-p-01].crm.dbo.customer c
	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join [stl-crmdb-p-01].crm.dbo.email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join [stl-crmdb-p-01].crm.dbo.address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	right(ca.attribute_value,2)*1=?

	and a.country_code='USA'
	and e.email_indicator in (0,9)
	and ed.email_opt_in_flag=1
	
	)

select cast(count(*)*1.13 as int) as 'estimateUS' from nextMonthEstimateUS
```

### create export tables

**Path:** `Package\CA export prep daily\assign coupon and export files (daily)\create export tables`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
IF OBJECT_ID('[dbo].[CRM_bday_CA_guest_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_CA_guest_export]

CREATE TABLE [CRM_bday_CA_guest_export]
(
  [tmpId] int identity(1,1) primary key,
  [emailAddress] [nvarchar](254) NOT NULL,
  [subscriberKey] [varchar](50) NOT NULL,
  [firstName] [nvarchar](255) NULL,
  [lastName] [nvarchar](255) NULL,
  [address] [nvarchar](255) NULL,
  [address2] [nvarchar](255) NULL,
  [city] [nvarchar](255) NULL,
  [state] [nvarchar](255) NULL,
  [zipCode] [nvarchar](20) NULL,
  [carrierRoute] [nvarchar](10) NULL
)

IF OBJECT_ID('[dbo].[CRM_bday_CA_code_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_CA_code_export]

CREATE TABLE [dbo].[CRM_bday_CA_code_export]
(
  [tmpId] int identity(1,1) primary key,
  [giftCodeID] int,
  [giftCode] [varchar](50)
)


```

### remove special char

**Path:** `Package\CA export prep daily\assign coupon and export files (daily)\remove special char`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql

update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set firstName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(firstName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set lastName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(lastName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set address = LTRIM(RTRIM(REPLACE(REPLACE(CAST(address AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set address2 = LTRIM(RTRIM(REPLACE(REPLACE(CAST(address2 AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set city = LTRIM(RTRIM(REPLACE(REPLACE(CAST(city AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set state = LTRIM(RTRIM(REPLACE(REPLACE(CAST(state AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set zipCode = LTRIM(RTRIM(REPLACE(REPLACE(CAST(zipCode AS VARCHAR(MAX)),'?',''),'  ',' ')))


```

### update giftSent flag

**Path:** `Package\CA export prep daily\assign coupon and export files (daily)\update giftSent flag`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
update u
SET u.giftSent = 1
from [CRM_bday_CA_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?

```

### create export tables

**Path:** `Package\CA export prep\assign coupon and export files\create export tables`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
IF OBJECT_ID('[dbo].[CRM_bday_CA_guest_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_CA_guest_export]

CREATE TABLE [CRM_bday_CA_guest_export]
(
 [tmpId] int identity(1,1) primary key,
 [emailAddress] [nvarchar](254) NOT NULL,
 [subscriberKey] [varchar](50) NOT NULL,
  [firstName] [nvarchar](255) NULL,
  [lastName] [nvarchar](255) NULL,
  [address] [nvarchar](255) NULL,
  [address2] [nvarchar](255) NULL,
  [city] [nvarchar](255) NULL,
  [state] [nvarchar](255) NULL,
  [zipCode] [nvarchar](20) NULL,
  [carrierRoute] [nvarchar](10) NULL
)

IF OBJECT_ID('[dbo].[CRM_bday_CA_code_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_CA_code_export]

CREATE TABLE [dbo].[CRM_bday_CA_code_export]
(
  [tmpId] int identity(1,1) primary key,
  [giftCodeID] int,
  [giftCode] [varchar](50)
)


```

### remove special char

**Path:** `Package\CA export prep\assign coupon and export files\remove special char`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql

update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set firstName = replace(firstName,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set firstName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(firstName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set lastName = replace(lastName,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set lastName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(lastName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address = replace(address,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set address2 = replace(address2,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set city = replace(city,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set state = replace(state,'''',' ') 

update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'@',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'&',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'(',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,')',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,',',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'~',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'#',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'$',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'%',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'|',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'\',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'/',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'*',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'^',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'+',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'{',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'}',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'<',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'>',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'-',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'"',' ') 
update [dbo].[CRM_bday_CA_guest_export] set zipCode = replace(zipCode,'''',' ') 


```

### set firstDayOfMonth

**Path:** `Package\CA export prep\assign coupon and export files\set firstDayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
SELECT CONVERT(varchar(10), DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),126) as 'firstDayOfMonth'
```

### update giftSent flag

**Path:** `Package\CA export prep\assign coupon and export files\update giftSent flag`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
update u
SET u.giftSent = 1
from [CRM_bday_CA_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?

```

### set month

**Path:** `Package\Sequence Container 1\1rst of month, initial stage\set month`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select month(getdate()) as 'monthNum'
```

### count CA codes needed

**Path:** `Package\Sequence Container 1\coupon check & load\count CA codes needed`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select count(*) as 'CAneeded' from [CRM_bday_CA_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.giftSent is null

```

### count UK codes needed

**Path:** `Package\Sequence Container 1\coupon check & load\count UK codes needed`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select count(*) as 'UKneeded' from [CRM_bday_UK_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.giftSent is null

```

### count US codes needed

**Path:** `Package\Sequence Container 1\coupon check & load\count US codes needed`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select count(*) as 'USneeded' from [CRM_bday_US_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.giftSent is null

```

### count available CA codes

**Path:** `Package\Sequence Container 1\coupon check & load\count available CA codes`  
**Connection:** KODIAK (kodiak/DiscountMstrData)  

```sql
select count(*) as 'CAcount' from [dbo].[SerializationDiscountDetail] where serializationID in
(select serializationID from [dbo].[Discount] d
join [dbo].[SerializationDiscount] sd on d.discountID = sd.discountID
where d.startDate =? 
--and d.endingDate = ? 
and d.countryID = 2
and sd.serializationFileTypeID = 2) and isPoolAvailable = 1 and len(customerNumber) < 1 

```

### count available UK codes

**Path:** `Package\Sequence Container 1\coupon check & load\count available UK codes`  
**Connection:** KODIAK (kodiak/DiscountMstrData)  

```sql
select count(*) as 'UKcount' from [dbo].[SerializationDiscountDetail] where serializationID in
(select serializationID from [dbo].[Discount] d
join [dbo].[SerializationDiscount] sd on d.discountID = sd.discountID
where d.startDate =? 
--and d.endingDate = ? 
and d.countryID = 3
and sd.serializationFileTypeID = 2) and isPoolAvailable = 1 and len(customerNumber) < 1 

```

### count available US codes

**Path:** `Package\Sequence Container 1\coupon check & load\count available US codes`  
**Connection:** KODIAK (kodiak/DiscountMstrData)  

```sql
select count(*) as 'UScount' from [dbo].[SerializationDiscountDetail] where serializationID in
(select serializationID from [dbo].[Discount] d
join [dbo].[SerializationDiscount] sd on d.discountID = sd.discountID
where d.startDate = ? 
--and d.endingDate = ? 
and d.countryID = 1
and sd.serializationFileTypeID = 2) and isPoolAvailable = 1 and len(customerNumber) < 1 

```

### overwrite lastDayOfMonth

**Path:** `Package\Sequence Container 1\overwrite lastDayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select 'lastDayOfMonth' = '2020-12-01'
```

### truncate monthly stages

**Path:** `Package\Sequence Container 1\truncate monthly stages`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [CRM_bday_US_month_stage]
TRUNCATE TABLE [CRM_bday_CA_month_stage]
TRUNCATE TABLE [CRM_bday_UK_month_stage]
TRUNCATE TABLE [CRM_bday_dup_stage]

```

### FTP upload files

**Path:** `Package\Sequence Container 2 1\FTP upload files`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

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
 @script = ' /script=\\stl-ssis-p-01\IntegrationStaging\CRM\FTP\sFTPuploadScript.txt',
 @log = ' /log=\\stl-ssis-p-01\IntegrationStaging\CRM\FTP\upload.log',
 @FTP = (@winSCP + @script + @log)
   
   
exec master..xp_cmdshell @FTP
```

### FTP upload files

**Path:** `Package\Sequence Container 2\FTP upload files`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

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
 @script = ' /script=\\stl-ssis-p-01\IntegrationStaging\CRM\FTP\sFTPuploadScript.txt',
 @log = ' /log=\\stl-ssis-p-01\IntegrationStaging\CRM\FTP\upload.log',
 @FTP = (@winSCP + @script + @log)
   
   
exec master..xp_cmdshell @FTP
```

### count CA codes needed

**Path:** `Package\Sequence Container\coupon check & load\count CA codes needed`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select count(*) as 'CAneeded' from [CRM_bday_CA_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?
and u.giftSent is null

```

### count UK codes needed

**Path:** `Package\Sequence Container\coupon check & load\count UK codes needed`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select count(*) as 'UKneeded' from [CRM_bday_UK_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?
and u.giftSent is null

```

### count US codes needed

**Path:** `Package\Sequence Container\coupon check & load\count US codes needed`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select count(*) as 'USneeded' from [CRM_bday_US_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null 
and u.dayOfMonthAdded = ?
and u.giftSent is null

```

### count available CA codes

**Path:** `Package\Sequence Container\coupon check & load\count available CA codes`  
**Connection:** KODIAK (kodiak/DiscountMstrData)  

```sql
select count(*) as 'CAcount' from [dbo].[SerializationDiscountDetail] where serializationID in
(select serializationID from [dbo].[Discount] d
join [dbo].[SerializationDiscount] sd on d.discountID = sd.discountID
where d.startDate = ? 
--and d.endingDate = ? 
and d.countryID = 2
and sd.serializationFileTypeID = 2) and isPoolAvailable = 1 and len(customerNumber) < 1
```

### count available UK codes

**Path:** `Package\Sequence Container\coupon check & load\count available UK codes`  
**Connection:** KODIAK (kodiak/DiscountMstrData)  

```sql
select count(*) as 'UKcount' from [dbo].[SerializationDiscountDetail] where serializationID in
(select serializationID from [dbo].[Discount] d
join [dbo].[SerializationDiscount] sd on d.discountID = sd.discountID
where d.startDate = ? 
--and d.endingDate = ? 
and d.countryID = 3
and sd.serializationFileTypeID = 2) and isPoolAvailable = 1 and len(customerNumber) < 1

```

### count available US codes

**Path:** `Package\Sequence Container\coupon check & load\count available US codes`  
**Connection:** KODIAK (kodiak/DiscountMstrData)  

```sql
select count(*) as 'UScount' from [dbo].[SerializationDiscountDetail] where serializationID in
(select serializationID from [dbo].[Discount] d
join [dbo].[SerializationDiscount] sd on d.discountID = sd.discountID
where d.startDate = ? 
--and d.endingDate = ? 
and d.countryID = 1
and sd.serializationFileTypeID = 2) and isPoolAvailable = 1 and len(customerNumber) < 1
```

### set month

**Path:** `Package\Sequence Container\daily run, initial stage\set month`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select month(getdate()) as 'monthNum'
```

### merge CA

**Path:** `Package\Sequence Container\merge daily to monthly\merge CA`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
merge into [dbo].[CRM_bday_CA_month_stage] as target
using [dbo].[CRM_bday_CA_daily_stage] as source 
on 
 (
  target.subscriberKey=source.subscriberKey
  AND
  target.attributeCode=source.attributeCode
  AND
  target.attributeValue = source.attributeValue
 )
when not matched by target 
 then insert 
  (
   emailAddress,
   subscriberKey,
   attributeCode,
   attributeComment,
   attributeValue,
   dayOfMonthAdded
  )
 values
  (
   source.emailAddress,
   source.subscriberKey,
   source.attributeCode,
   source.attributeComment,
   source.attributeValue,
   ?  
  )
;
```

### merge UK

**Path:** `Package\Sequence Container\merge daily to monthly\merge UK`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
merge into [dbo].[CRM_bday_UK_month_stage] as target
using [dbo].[CRM_bday_UK_daily_stage] as source 
on 
 (
  target.subscriberKey=source.subscriberKey
  AND
  target.attributeCode=source.attributeCode
  AND
  target.attributeValue = source.attributeValue
 )
when not matched by target 
 then insert 
  (
   emailAddress,
   subscriberKey,
   attributeCode,
   attributeComment,
   attributeValue,
   dayOfMonthAdded
  )
 values
  (
   source.emailAddress,
   source.subscriberKey,
   source.attributeCode,
   source.attributeComment,
   source.attributeValue,
   ?  
  )
;
```

### merge US

**Path:** `Package\Sequence Container\merge daily to monthly\merge US`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
merge into [dbo].[CRM_bday_US_month_stage] as target
using [dbo].[CRM_bday_US_daily_stage] as source 
on 
	(
		target.subscriberKey=source.subscriberKey
		AND
		target.attributeCode=source.attributeCode
		AND
		target.attributeValue = source.attributeValue
	)
when not matched by target 
	then insert 
		(
			emailAddress,
			subscriberKey,
			attributeCode,
			attributeComment,
			attributeValue,
			firstName,
			lastName,
			address,
			address2,
			city,
			state,
			zipCode,
			dayOfMonthAdded
		)
	values
		(
			source.emailAddress,
			source.subscriberKey,
			source.attributeCode,
			source.attributeComment,
			source.attributeValue,
			source.firstName,
			source.lastName,
			source.address,
			source.address2,
			source.city,
			source.state,
			source.zipCode,
			?	 
		)
;
```

### overwrite lastDayOfMonth

**Path:** `Package\Sequence Container\overwrite lastDayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select 'lastDayOfMonth' = '2020-12-01'
```

### truncate daily stages

**Path:** `Package\Sequence Container\truncate daily stages`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [CRM_bday_US_daily_stage]
TRUNCATE TABLE [CRM_bday_CA_daily_stage]
TRUNCATE TABLE [CRM_bday_UK_daily_stage]
TRUNCATE TABLE [CRM_bday_dup_stage]

```

### create export tables

**Path:** `Package\UK export prep daily\assign coupon and export files (daily)\create export tables`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
IF OBJECT_ID('[dbo].[CRM_bday_UK_guest_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_UK_guest_export]

CREATE TABLE [CRM_bday_UK_guest_export]
(
[tmpId] int identity(1,1) primary key,
 [emailAddress] [nvarchar](254) NOT NULL,
 [subscriberKey] [varchar](50) NOT NULL,
  [firstName] [nvarchar](255) NULL,
  [lastName] [nvarchar](255) NULL,
  [address] [nvarchar](255) NULL,
  [address2] [nvarchar](255) NULL,
  [city] [nvarchar](255) NULL,
  [state] [nvarchar](255) NULL,
  [zipCode] [nvarchar](20) NULL,
  [carrierRoute] [nvarchar](10) NULL
)

IF OBJECT_ID('[dbo].[CRM_bday_UK_code_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_UK_code_export]

CREATE TABLE [dbo].[CRM_bday_UK_code_export]
(
  [tmpId] int identity(1,1) primary key,
  [giftCodeID] int,
  [giftCode] [varchar](50)
)



```

### remove special char

**Path:** `Package\UK export prep daily\assign coupon and export files (daily)\remove special char`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql

update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set firstName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(firstName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set lastName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(lastName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set address = LTRIM(RTRIM(REPLACE(REPLACE(CAST(address AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set address2 = LTRIM(RTRIM(REPLACE(REPLACE(CAST(address2 AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set city = LTRIM(RTRIM(REPLACE(REPLACE(CAST(city AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set state = LTRIM(RTRIM(REPLACE(REPLACE(CAST(state AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set zipCode = LTRIM(RTRIM(REPLACE(REPLACE(CAST(zipCode AS VARCHAR(MAX)),'?',''),'  ',' ')))

```

### update giftSent flag

**Path:** `Package\UK export prep daily\assign coupon and export files (daily)\update giftSent flag`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
update u
SET u.giftSent = 1
from [CRM_bday_UK_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?

```

### set current dayOfMonth

**Path:** `Package\UK export prep daily\set current dayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select day(getdate()-1) as 'dayOfMonth'
```

### set firstDayOfMonth

**Path:** `Package\UK export prep daily\set firstDayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
SELECT CONVERT(varchar(10), DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),126) as 'firstDayOfMonth'
```

### set lastDayOfMonth

**Path:** `Package\UK export prep daily\set lastDayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
SELECT CONVERT(varchar(10), DATEADD (dd, -1, DATEADD(mm, DATEDIFF(mm, 0, GETDATE()) + 1 , 0)),126) as 'lastDayOfMonth'
```

### create export tables

**Path:** `Package\UK export prep\assign coupon and export files\create export tables`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
IF OBJECT_ID('[dbo].[CRM_bday_UK_guest_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_UK_guest_export]

CREATE TABLE [CRM_bday_UK_guest_export]
(
[tmpId] int identity(1,1) primary key,
 [emailAddress] [nvarchar](254) NOT NULL,
 [subscriberKey] [varchar](50) NOT NULL,
  [firstName] [nvarchar](255) NULL,
  [lastName] [nvarchar](255) NULL,
  [address] [nvarchar](255) NULL,
  [address2] [nvarchar](255) NULL,
  [city] [nvarchar](255) NULL,
  [state] [nvarchar](255) NULL,
  [zipCode] [nvarchar](20) NULL,
  [carrierRoute] [nvarchar](10) NULL
)

IF OBJECT_ID('[dbo].[CRM_bday_UK_code_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_UK_code_export]

CREATE TABLE [dbo].[CRM_bday_UK_code_export]
(
  [tmpId] int identity(1,1) primary key,
  [giftCodeID] int,
  [giftCode] [varchar](50)
)



```

### remove special char

**Path:** `Package\UK export prep\assign coupon and export files\remove special char`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql

update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set firstName = replace(firstName,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set firstName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(firstName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set lastName = replace(lastName,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set lastName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(lastName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address = replace(address,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set address2 = replace(address2,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set city = replace(city,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set state = replace(state,'''',' ') 

update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'@',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'&',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'(',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,')',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,',',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'~',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'#',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'$',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'%',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'|',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'\',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'/',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'*',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'^',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'+',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'{',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'}',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'<',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'>',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'-',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'"',' ') 
update [dbo].[CRM_bday_UK_guest_export] set zipCode = replace(zipCode,'''',' ') 



```

### update giftSent flag

**Path:** `Package\UK export prep\assign coupon and export files\update giftSent flag`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
update u
SET u.giftSent = 1
from [CRM_bday_UK_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?

```

### create export tables

**Path:** `Package\US export prep daily\assign coupon and export files (daily)\create export tables`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
IF OBJECT_ID('[dbo].[CRM_bday_US_guest_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_US_guest_export]

CREATE TABLE [CRM_bday_US_guest_export]
(
	[tmpId] int identity(1,1) primary key,
	[emailAddress] [nvarchar](254) NOT NULL,
	[subscriberKey] [varchar](50) NOT NULL,
	[customerNumber] [nvarchar](20) NULL,
	[firstName] [nvarchar](255) NULL,
	[lastName] [nvarchar](255) NULL,
	[address] [nvarchar](255) NULL,
	[address2] [nvarchar](255) NULL,
	[city] [nvarchar](255) NULL,
	[state] [nvarchar](255) NULL,
	[zipCode] [nvarchar](20) NULL,
	[carrierRoute] [nvarchar](10) NULL
)

IF OBJECT_ID('[dbo].[CRM_bday_US_code_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_US_code_export]

CREATE TABLE [dbo].[CRM_bday_US_code_export]
(
		[tmpId] int identity(1,1) primary key,
		[giftCodeID] int,
		[giftCode] [varchar](50)
)


```

### remove special char

**Path:** `Package\US export prep daily\assign coupon and export files (daily)\remove special char`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql

update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'''',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = LTRIM(RTRIM(firstName))

update [dbo].[CRM_bday_US_guest_export] set firstName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(firstName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'''',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = LTRIM(RTRIM(lastName))

update [dbo].[CRM_bday_US_guest_export] set lastName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(lastName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set address = LTRIM(RTRIM(REPLACE(REPLACE(CAST(address AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set address2 = LTRIM(RTRIM(REPLACE(REPLACE(CAST(address2 AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set city = LTRIM(RTRIM(REPLACE(REPLACE(CAST(city AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set state = LTRIM(RTRIM(REPLACE(REPLACE(CAST(state AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set zipCode = LTRIM(RTRIM(REPLACE(REPLACE(CAST(zipCode AS VARCHAR(MAX)),'?',''),'  ',' ')))

```

### update giftSent flag

**Path:** `Package\US export prep daily\assign coupon and export files (daily)\update giftSent flag`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
update u
SET u.giftSent = 1
from [CRM_bday_US_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?

```

### create export tables

**Path:** `Package\US export prep\assign coupon and export files\create export tables`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql

IF OBJECT_ID('[dbo].[CRM_bday_US_guest_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_US_guest_export]

CREATE TABLE [CRM_bday_US_guest_export]
(
	[tmpId] int identity(1,1) primary key,
	[emailAddress] [nvarchar](254) NOT NULL,
	[subscriberKey] [varchar](50) NOT NULL,
	[firstName] [nvarchar](255) NULL,
	[lastName] [nvarchar](255) NULL,
	[address] [nvarchar](255) NULL,
	[address2] [nvarchar](255) NULL,
	[city] [nvarchar](255) NULL,
	[state] [nvarchar](255) NULL,
	[zipCode] [nvarchar](20) NULL,
	[carrierRoute] [nvarchar](10) NULL
)

IF OBJECT_ID('[dbo].[CRM_bday_US_code_export]', 'U') IS NOT NULL DROP TABLE [dbo].[CRM_bday_US_code_export]

CREATE TABLE [dbo].[CRM_bday_US_code_export]
(
		[tmpId] int identity(1,1) primary key,
		[giftCodeID] int,
		[giftCode] [varchar](50)
)


```

### remove special char

**Path:** `Package\US export prep\assign coupon and export files\remove special char`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql

update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = replace(firstName,'''',' ') 
update [dbo].[CRM_bday_US_guest_export] set firstName = LTRIM(RTRIM(firstName))

update [dbo].[CRM_bday_US_guest_export] set firstName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(firstName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = replace(lastName,'''',' ') 
update [dbo].[CRM_bday_US_guest_export] set lastName = LTRIM(RTRIM(lastName))

update [dbo].[CRM_bday_US_guest_export] set lastName = LTRIM(RTRIM(REPLACE(REPLACE(CAST(lastName AS VARCHAR(MAX)),'?',''),'  ',' ')))

update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set address = replace(address,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set address2 = replace(address2,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set city = replace(city,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set state = replace(state,'''',' ') 

update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'@',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'&',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'(',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,')',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,',',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'~',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'#',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'$',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'%',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'|',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'\',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'/',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'*',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'^',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'+',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'{',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'}',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'<',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'>',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'-',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'"',' ') 
update [dbo].[CRM_bday_US_guest_export] set zipCode = replace(zipCode,'''',' ') 



```

### update giftSent flag

**Path:** `Package\US export prep\assign coupon and export files\update giftSent flag`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
update u
SET u.giftSent = 1
from [CRM_bday_US_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?

```

### truncate backup

**Path:** `Package\backup month tables 1\truncate backup`  
**Connection:** STL-DYNSNC-P-01.DBAUtility (STL-DYNSNC-P-01/DBAUtility)  

```sql
TRUNCATE TABLE [CRM_bday_US_month_stage]
TRUNCATE TABLE [CRM_bday_CA_month_stage]
TRUNCATE TABLE [CRM_bday_UK_month_stage]
```

### truncate backup

**Path:** `Package\backup month tables\truncate backup`  
**Connection:** STL-DYNSNC-P-01.DBAUtility (STL-DYNSNC-P-01/DBAUtility)  

```sql
TRUNCATE TABLE [CRM_bday_US_month_stage]
TRUNCATE TABLE [CRM_bday_CA_month_stage]
TRUNCATE TABLE [CRM_bday_UK_month_stage]
```

### overwrite vars

**Path:** `Package\overwrite vars`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select 'dayOfMonth' = 2, 'firstDayOfMonth' = '2019-11-01' , 'lastDayOfMonth' = '2019-11-30'
```

### set current dayOfMonth

**Path:** `Package\set current dayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
select day(getdate()) as 'dayOfMonth'
```

### set firstDayOfMonth

**Path:** `Package\set firstDayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
SELECT CONVERT(varchar(10), DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),126) as 'firstDayOfMonth'
```

### set lastDayOfMonth

**Path:** `Package\set lastDayOfMonth`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
SELECT CONVERT(varchar(10), DATEADD (dd, -1, DATEADD(mm, DATEDIFF(mm, 0, GETDATE()) + 1 , 0)),126) as 'lastDayOfMonth'
```

### wait

**Path:** `Package\wait`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
WAITFOR DELAY '00:45:00';
```

### wait 1

**Path:** `Package\wait 1`  
**Connection:** IntegrationStaging (STL-SSIS-p-01/IntegrationStaging)  

```sql
WAITFOR DELAY '00:05:00';
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| CA month |  | OLEDBSource | Data Flow Task | IntegrationStaging |  |
| UK month |  | OLEDBSource | Data Flow Task | IntegrationStaging |  |
| US month |  | OLEDBSource | Data Flow Task | IntegrationStaging |  |
| CA month |  | OLEDBSource | Data Flow Task | IntegrationStaging |  |
| UK month |  | OLEDBSource | Data Flow Task | IntegrationStaging |  |
| US month |  | OLEDBSource | Data Flow Task | IntegrationStaging |  |
| Kodiak DM |  | OLEDBSource | stage codes from DM | KODIAK | SqlCommand |
| month stage bday customers |  | OLEDBSource | stage cust from CRM | IntegrationStaging | SqlCommand |
| code and guest staged results |  | OLEDBSource | update DM detail & produce file | IntegrationStaging | SqlCommand |
| Kodiak DM |  | OLEDBSource | stage codes from DM | KODIAK | SqlCommand |
| month stage bday customers |  | OLEDBSource | stage cust from CRM | IntegrationStaging | SqlCommand |
| code and guest staged results |  | OLEDBSource | update DM detail & produce file | IntegrationStaging | SqlCommand |
| crm CA stage |  | OLEDBSource | CRM_bday_CA_stage | CRM | SqlCommand |
| crm CYC duplicates |  | OLEDBSource | CRM_bday_dup_stage | CRM | SqlCommand |
| crm UK stage |  | OLEDBSource | CRM_bday_UK_stage | CRM | SqlCommand |
| crm US bday customers |  | OLEDBSource | CRM_bday_US_stage | CRM | SqlCommand |
| crm CA stage |  | OLEDBSource | CRM_bday_CA_stage | CRM | SqlCommand |
| crm CYC duplicates |  | OLEDBSource | CRM_bday_dup_stage | CRM | SqlCommand |
| crm UK stage |  | OLEDBSource | CRM_bday_UK_stage | CRM | SqlCommand |
| crm US bday customers |  | OLEDBSource | CRM_bday_US_stage | CRM | SqlCommand |
| Kodiak DM |  | OLEDBSource | stage codes from DM | KODIAK | SqlCommand |
| month stage bday customers |  | OLEDBSource | stage cust from CRM | IntegrationStaging | SqlCommand |
| code and guest staged results |  | OLEDBSource | update DM detail & produce file | IntegrationStaging | SqlCommand |
| Kodiak DM |  | OLEDBSource | stage codes from DM | KODIAK | SqlCommand |
| month stage bday customers |  | OLEDBSource | stage cust from CRM | IntegrationStaging | SqlCommand |
| code and guest staged results |  | OLEDBSource | update DM detail & produce file | IntegrationStaging | SqlCommand |
| Kodiak DM |  | OLEDBSource | stage codes from DM | KODIAK | SqlCommand |
| month stage bday customers |  | OLEDBSource | stage cust from CRM | IntegrationStaging | SqlCommand |
| code and guest staged results |  | OLEDBSource | update DM detail & produce file | IntegrationStaging | SqlCommand |
| Kodiak DM |  | OLEDBSource | stage codes from DM | KODIAK | SqlCommand |
| month stage bday customers |  | OLEDBSource | stage cust from CRM | IntegrationStaging | SqlCommand |
| code and guest staged results |  | OLEDBSource | update DM detail & produce file | IntegrationStaging | SqlCommand |

#### Kodiak DM — SqlCommand

```sql
select sdd.serializationDiscountDetailID, sdd.serializedNum  
from [dbo].[SerializationDiscountDetail] sdd
join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID
join [dbo].[Discount] d on sd.discountID = d.discountID 
where d.startDate = ?  
--and d.endingDate  = ?
and d.countryID = 2 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNumber) < 1
```

#### month stage bday customers — SqlCommand

```sql
SELECT u.emailAddress, u.subscriberkey,
u.firstName,u.lastName,u.address,u.address2,u.city,
u.state,u.zipCode,u.carrierRoute
from [CRM_bday_CA_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
order by u.subscriberKey asc
```

#### code and guest staged results — SqlCommand

```sql
with assignedGift as
(
select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey
,g.firstName
,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode
from [dbo].[CRM_bday_CA_code_export] c
join [dbo].[CRM_bday_CA_guest_export] g on c.tmpId = g.tmpId
)

select * from assignedGift
```

#### month stage bday customers — SqlCommand

```sql
SELECT u.emailAddress, u.subscriberkey,u.dayOfMonthAdded,
u.firstName,u.lastName,u.address,u.address2,u.city,
u.state,u.zipCode,u.carrierRoute
from [CRM_bday_CA_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?
and u.giftSent is null
order by u.subscriberKey asc
```

#### code and guest staged results — SqlCommand

```sql
with assignedGift as
(
select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName
,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode
from [dbo].[CRM_bday_CA_code_export] c
join [dbo].[CRM_bday_CA_guest_export] g on c.tmpId = g.tmpId
)

select * from assignedGift
```

#### crm CA stage — SqlCommand

```sql
select 
	distinct
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value,
  c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route
from customer c
	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	right(ca.attribute_value,2)*1=?
	and a.country_code='CAN'
	and e.email_indicator in (0,9)
	and ed.email_opt_in_flag=1
order by 1
```

#### crm CYC duplicates — SqlCommand

```sql
select 
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value
from customer c
	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	(ca.attribute_code like '%CYC%' and ca2.attribute_code like '%KID%' and ca.attribute_value=ca2.attribute_value)
order by 1
```

#### crm UK stage — SqlCommand

```sql
select 
	distinct
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value,
  c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route
from customer c
	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join customer_attribute ca3 with (nolock) on cd.customer_id=ca3.customer_id and ca3.attribute_grouping_code='GDPR' and ca3.attribute_code='OPTIN' and ca3.attribute_value=1
	join email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	right(ca.attribute_value,2)*1=?
	and a.country_code='GBR'
	and e.email_indicator in (0,9)
	and ed.email_opt_in_flag=1
order by 1
```

#### crm US bday customers — SqlCommand

```sql
select 
	distinct
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value,
                   c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route
from customer c
	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	right(ca.attribute_value,2)*1=?
	and a.country_code='USA'
	and e.email_indicator in (0,9)
	and ed.email_opt_in_flag=1
order by 1
```

#### crm CA stage — SqlCommand

```sql
select 
	distinct
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value,
c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route
from [stl-crmdb-p-01].crm.dbo.customer c
	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join [stl-crmdb-p-01].crm.dbo.email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join [stl-crmdb-p-01].crm.dbo.address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	right(ca.attribute_value,2)*1=?
	and a.country_code='CAN'
	and e.email_indicator in (0,9)
	and ed.email_opt_in_flag=1
order by 1
```

#### crm CYC duplicates — SqlCommand

```sql
select 
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value
from [stl-crmdb-p-01].crm.dbo.customer c
	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join [stl-crmdb-p-01].crm.dbo.email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join [stl-crmdb-p-01].crm.dbo.address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	(ca.attribute_code like '%CYC%' and ca2.attribute_code like '%KID%' and ca.attribute_value=ca2.attribute_value)
order by 1
```

#### crm UK stage — SqlCommand

```sql
select 
	distinct
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value,
c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route
from [stl-crmdb-p-01].crm.dbo.customer c
	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca3 with (nolock) on cd.customer_id=ca3.customer_id and ca3.attribute_grouping_code='GDPR' and ca3.attribute_code='OPTIN' and ca3.attribute_value=1
	join [stl-crmdb-p-01].crm.dbo.email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join [stl-crmdb-p-01].crm.dbo.email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join [stl-crmdb-p-01].crm.dbo.address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	right(ca.attribute_value,2)*1=?
	and a.country_code='GBR'
	and e.email_indicator in (0,9)
	and ed.email_opt_in_flag=1
order by 1
```

#### crm US bday customers — SqlCommand

```sql
select 
	distinct
	cast(c.customer_no as varchar) as subscriberkey,
	e.email_address,
	ca.attribute_code,
	ca.attribute_comment,
	ca.attribute_value,
                   c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route
from [stl-crmdb-p-01].crm.dbo.customer c
	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89)
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca2 with (nolock) on cd.customer_id=ca2.customer_id and ca2.attribute_grouping_code  ='BDAY'
	join [stl-crmdb-p-01].crm.dbo.email e with (nolock) on cd.customer_id=e.customer_id and cd.primary_email_id=e.email_id
	join [stl-crmdb-p-01].crm.dbo.email_division ed with (nolock) on cd.customer_id=ed.customer_id and cd.primary_email_id=ed.email_id
	join [stl-crmdb-p-01].crm.dbo.address a with (nolock) on cd.customer_id=a.customer_id and cd.primary_address_id=a.address_id
where 
	right(ca.attribute_value,2)*1=?
	and a.country_code='USA'
	and e.email_indicator in (0,9)
	and ed.email_opt_in_flag=1
order by 1
```

#### Kodiak DM — SqlCommand

```sql
select sdd.serializationDiscountDetailID, sdd.serializedNum  
from [dbo].[SerializationDiscountDetail] sdd
join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID
join [dbo].[Discount] d on sd.discountID = d.discountID 
where d.startDate = ?  
--and d.endingDate  = ?
and d.countryID = 3 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNumber) < 1
```

#### month stage bday customers — SqlCommand

```sql
SELECT u.emailAddress, u.subscriberkey,
u.firstName,u.lastName,u.address,u.address2,u.city,
u.state,u.zipCode,u.carrierRoute
from [CRM_bday_UK_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
order by u.subscriberKey asc
```

#### code and guest staged results — SqlCommand

```sql
with assignedGift as
(
select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey
,g.firstName
,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode
from [dbo].[CRM_bday_UK_code_export] c
join [dbo].[CRM_bday_UK_guest_export] g on c.tmpId = g.tmpId
)

select * from assignedGift
```

#### month stage bday customers — SqlCommand

```sql
SELECT u.emailAddress, u.subscriberkey,u.dayOfMonthAdded,
u.firstName,u.lastName,u.address,u.address2,u.city,
u.state,u.zipCode,u.carrierRoute
from [CRM_bday_UK_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?
and u.giftSent is null
order by u.subscriberKey asc
```

#### code and guest staged results — SqlCommand

```sql
with assignedGift as
(
select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName
,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode
from [dbo].[CRM_bday_UK_code_export] c
join [dbo].[CRM_bday_UK_guest_export] g on c.tmpId = g.tmpId
)

select * from assignedGift
```

#### Kodiak DM — SqlCommand

```sql
select sdd.serializationDiscountDetailID, sdd.serializedNum  
from [dbo].[SerializationDiscountDetail] sdd
join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID
join [dbo].[Discount] d on sd.discountID = d.discountID 
where d.startDate = ?  
--and d.endingDate  = ?
and d.countryID = 1 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNumber) < 1
```

#### month stage bday customers — SqlCommand

```sql
SELECT u.emailAddress, u.subscriberkey,
u.firstName,u.lastName,u.address,u.address2,u.city,
u.state,u.zipCode,u.carrierRoute
from [CRM_bday_US_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
order by u.subscriberKey asc
```

#### code and guest staged results — SqlCommand

```sql
with assignedGift as
(
select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey
,g.firstName
,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode
from [dbo].[CRM_bday_US_code_export] c
join [dbo].[CRM_bday_US_guest_export] g on c.tmpId = g.tmpId
--where g.tmpID in (5490,1234,4277,2589,6251,12310,73616,49164,45389,5094)
)

select * from assignedGift
```

#### month stage bday customers — SqlCommand

```sql
SELECT u.emailAddress, u.subscriberkey,u.dayOfMonthAdded,
u.firstName,u.lastName,u.address,u.address2,u.city,
u.state,u.zipCode,u.carrierRoute
from [CRM_bday_US_month_stage] u 
left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode
where n.attributeCode is null
and u.dayOfMonthAdded = ?
and u.giftSent is null
order by u.subscriberKey asc
```

#### code and guest staged results — SqlCommand

```sql
with assignedGift as
(
select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName
,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode
from [dbo].[CRM_bday_US_code_export] c
join [dbo].[CRM_bday_US_guest_export] g on c.tmpId = g.tmpId
)

select * from assignedGift
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| CA month backup |  | OLEDBDestination | Data Flow Task | STL-DYNSNC-P-01.DBAUtility |  |
| UK month backup |  | OLEDBDestination | Data Flow Task | STL-DYNSNC-P-01.DBAUtility |  |
| US month backup |  | OLEDBDestination | Data Flow Task | STL-DYNSNC-P-01.DBAUtility |  |
| CA month backup |  | OLEDBDestination | Data Flow Task | STL-DYNSNC-P-01.DBAUtility |  |
| UK month backup |  | OLEDBDestination | Data Flow Task | STL-DYNSNC-P-01.DBAUtility |  |
| US month backup |  | OLEDBDestination | Data Flow Task | STL-DYNSNC-P-01.DBAUtility |  |
| IntegrationStaging |  | OLEDBDestination | stage codes from DM | IntegrationStaging |  |
| export stage customers |  | OLEDBDestination | stage cust from CRM | IntegrationStaging |  |
| CA bday gift csv |  | FlatFileDestination | update DM detail & produce file | CA bday gift csv |  |
| IntegrationStaging |  | OLEDBDestination | stage codes from DM | IntegrationStaging |  |
| export stage customers |  | OLEDBDestination | stage cust from CRM | IntegrationStaging |  |
| CA bday gift csv |  | FlatFileDestination | update DM detail & produce file | CA bday gift csv |  |
| CRM_bday_CA_stage |  | OLEDBDestination | CRM_bday_CA_stage | IntegrationStaging |  |
| CRM_bday_DUP_stage |  | OLEDBDestination | CRM_bday_dup_stage | IntegrationStaging |  |
| CRM_bday_UK_stage |  | OLEDBDestination | CRM_bday_UK_stage | IntegrationStaging |  |
| CRM_bday_US_stage |  | OLEDBDestination | CRM_bday_US_stage | IntegrationStaging |  |
| CRM_bday_CA_stage |  | OLEDBDestination | CRM_bday_CA_stage | IntegrationStaging |  |
| CRM_bday_dup_stage |  | OLEDBDestination | CRM_bday_dup_stage | IntegrationStaging |  |
| CRM_bday_UK_stage |  | OLEDBDestination | CRM_bday_UK_stage | IntegrationStaging |  |
| CRM_bday_US_stage |  | OLEDBDestination | CRM_bday_US_stage | IntegrationStaging |  |
| IntegrationStaging |  | OLEDBDestination | stage codes from DM | IntegrationStaging |  |
| export stage customers |  | OLEDBDestination | stage cust from CRM | IntegrationStaging |  |
| UK bday gift csv |  | FlatFileDestination | update DM detail & produce file | UK bday gift csv |  |
| IntegrationStaging |  | OLEDBDestination | stage codes from DM | IntegrationStaging |  |
| export stage customers |  | OLEDBDestination | stage cust from CRM | IntegrationStaging |  |
| UK bday gift csv |  | FlatFileDestination | update DM detail & produce file | UK bday gift csv |  |
| IntegrationStaging |  | OLEDBDestination | stage codes from DM | IntegrationStaging |  |
| export stage customers |  | OLEDBDestination | stage cust from CRM | IntegrationStaging |  |
| US bday gift csv |  | FlatFileDestination | update DM detail & produce file | US bday gift csv |  |
| IntegrationStaging |  | OLEDBDestination | stage codes from DM | IntegrationStaging |  |
| export stage customers |  | OLEDBDestination | stage cust from CRM | IntegrationStaging |  |
| US bday gift csv |  | FlatFileDestination | update DM detail & produce file | US bday gift csv |  |
