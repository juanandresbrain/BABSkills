# SSIS Package: Package

**Project:** CRM_bdayAutomation  
**Folder:** CRM  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Archive_conn(["Archive [FILE]"])
        CA_bday_gift_csv_conn(["CA bday gift csv [FLATFILE]"])
        CRM_conn(["CRM [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        KODIAK_conn(["KODIAK [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
        STL_DYNSNC_P_01_DBAUtility_conn(["STL-DYNSNC-P-01.DBAUtility [OLEDB]"])
        UK_bday_gift_csv_conn(["UK bday gift csv [FLATFILE]"])
        US_bday_gift_csv_conn(["US bday gift csv [FLATFILE]"])
    end
    subgraph ControlFlow
        Package_task["Package"]
        19th_estimate_for_next_month_CA_task["19th estimate for next month CA"]
        Package_task --> 19th_estimate_for_next_month_CA_task
        next_mo_estimate_task["next mo estimate"]
        19th_estimate_for_next_month_CA_task --> next_mo_estimate_task
        next_month_estimate_task["next month estimate"]
        next_mo_estimate_task --> next_month_estimate_task
        19th_estimate_for_next_month_UK_task["19th estimate for next month UK"]
        next_month_estimate_task --> 19th_estimate_for_next_month_UK_task
        next_mo_estimate_task["next mo estimate"]
        19th_estimate_for_next_month_UK_task --> next_mo_estimate_task
        next_month_estimate_task["next month estimate"]
        next_mo_estimate_task --> next_month_estimate_task
        19th_estimate_for_next_month_US_task["19th estimate for next month US"]
        next_month_estimate_task --> 19th_estimate_for_next_month_US_task
        next_mo_estimate_task["next mo estimate"]
        19th_estimate_for_next_month_US_task --> next_mo_estimate_task
        next_month_estimate_task["next month estimate"]
        next_mo_estimate_task --> next_month_estimate_task
        backup_month_tables_task["backup month tables"]
        next_month_estimate_task --> backup_month_tables_task
        Data_Flow_Task_task["Data Flow Task"]
        backup_month_tables_task --> Data_Flow_Task_task
        truncate_backup_task["truncate backup"]
        Data_Flow_Task_task --> truncate_backup_task
        backup_month_tables_1_task["backup month tables 1"]
        truncate_backup_task --> backup_month_tables_1_task
        Data_Flow_Task_task["Data Flow Task"]
        backup_month_tables_1_task --> Data_Flow_Task_task
        truncate_backup_task["truncate backup"]
        Data_Flow_Task_task --> truncate_backup_task
        CA_export_prep_task["CA export prep"]
        truncate_backup_task --> CA_export_prep_task
        assign_coupon_and_export_files_task["assign coupon and export files"]
        CA_export_prep_task --> assign_coupon_and_export_files_task
        create_export_tables_task["create export tables"]
        assign_coupon_and_export_files_task --> create_export_tables_task
        create_timestamp_file_task["create timestamp file"]
        create_export_tables_task --> create_timestamp_file_task
        remove_special_char_task["remove special char"]
        create_timestamp_file_task --> remove_special_char_task
        set_firstDayOfMonth_task["set firstDayOfMonth"]
        remove_special_char_task --> set_firstDayOfMonth_task
        stage_codes_from_DM_task["stage codes from DM"]
        set_firstDayOfMonth_task --> stage_codes_from_DM_task
        stage_cust_from_CRM_task["stage cust from CRM"]
        stage_codes_from_DM_task --> stage_cust_from_CRM_task
        update_DM_detail___produce_file_task["update DM detail & produce file"]
        stage_cust_from_CRM_task --> update_DM_detail___produce_file_task
        update_giftSent_flag_task["update giftSent flag"]
        update_DM_detail___produce_file_task --> update_giftSent_flag_task
        CA_export_prep_daily_task["CA export prep daily"]
        update_giftSent_flag_task --> CA_export_prep_daily_task
        assign_coupon_and_export_files__daily__task["assign coupon and export files (daily)"]
        CA_export_prep_daily_task --> assign_coupon_and_export_files__daily__task
        create_export_tables_task["create export tables"]
        assign_coupon_and_export_files__daily__task --> create_export_tables_task
        create_timestamp_file_task["create timestamp file"]
        create_export_tables_task --> create_timestamp_file_task
        remove_special_char_task["remove special char"]
        create_timestamp_file_task --> remove_special_char_task
        stage_codes_from_DM_task["stage codes from DM"]
        remove_special_char_task --> stage_codes_from_DM_task
        stage_cust_from_CRM_task["stage cust from CRM"]
        stage_codes_from_DM_task --> stage_cust_from_CRM_task
        update_DM_detail___produce_file_task["update DM detail & produce file"]
        stage_cust_from_CRM_task --> update_DM_detail___produce_file_task
        update_giftSent_flag_task["update giftSent flag"]
        update_DM_detail___produce_file_task --> update_giftSent_flag_task
        CA_success_task["CA success"]
        update_giftSent_flag_task --> CA_success_task
        CA_success__daily__task["CA success (daily)"]
        CA_success_task --> CA_success__daily__task
        Expression_Task_task["Expression Task"]
        CA_success__daily__task --> Expression_Task_task
        overwrite_vars_task["overwrite vars"]
        Expression_Task_task --> overwrite_vars_task
        Sequence_Container_task["Sequence Container"]
        overwrite_vars_task --> Sequence_Container_task
        coupon_check___load_task["coupon check & load"]
        Sequence_Container_task --> coupon_check___load_task
        CA_short_task["CA short"]
        coupon_check___load_task --> CA_short_task
        count_available_CA_codes_task["count available CA codes"]
        CA_short_task --> count_available_CA_codes_task
        count_available_UK_codes_task["count available UK codes"]
        count_available_CA_codes_task --> count_available_UK_codes_task
        count_available_US_codes_task["count available US codes"]
        count_available_UK_codes_task --> count_available_US_codes_task
        count_CA_codes_needed_task["count CA codes needed"]
        count_available_US_codes_task --> count_CA_codes_needed_task
        count_UK_codes_needed_task["count UK codes needed"]
        count_CA_codes_needed_task --> count_UK_codes_needed_task
        count_US_codes_needed_task["count US codes needed"]
        count_UK_codes_needed_task --> count_US_codes_needed_task
        UK_short_task["UK short"]
        count_US_codes_needed_task --> UK_short_task
        US_short_task["US short"]
        UK_short_task --> US_short_task
        daily_run__initial_stage_task["daily run, initial stage"]
        US_short_task --> daily_run__initial_stage_task
        CRM_bday_CA_stage_task["CRM_bday_CA_stage"]
        daily_run__initial_stage_task --> CRM_bday_CA_stage_task
        CRM_bday_dup_stage_task["CRM_bday_dup_stage"]
        CRM_bday_CA_stage_task --> CRM_bday_dup_stage_task
        CRM_bday_UK_stage_task["CRM_bday_UK_stage"]
        CRM_bday_dup_stage_task --> CRM_bday_UK_stage_task
        CRM_bday_US_stage_task["CRM_bday_US_stage"]
        CRM_bday_UK_stage_task --> CRM_bday_US_stage_task
        set_month_task["set month"]
        CRM_bday_US_stage_task --> set_month_task
        merge_daily_to_monthly_task["merge daily to monthly"]
        set_month_task --> merge_daily_to_monthly_task
        merge_CA_task["merge CA"]
        merge_daily_to_monthly_task --> merge_CA_task
        merge_UK_task["merge UK"]
        merge_CA_task --> merge_UK_task
        merge_US_task["merge US"]
        merge_UK_task --> merge_US_task
        overwrite_lastDayOfMonth_task["overwrite lastDayOfMonth"]
        merge_US_task --> overwrite_lastDayOfMonth_task
        truncate_daily_stages_task["truncate daily stages"]
        overwrite_lastDayOfMonth_task --> truncate_daily_stages_task
        Sequence_Container_1_task["Sequence Container 1"]
        truncate_daily_stages_task --> Sequence_Container_1_task
        1rst_of_month__initial_stage_task["1rst of month, initial stage"]
        Sequence_Container_1_task --> 1rst_of_month__initial_stage_task
        CRM_bday_CA_stage_task["CRM_bday_CA_stage"]
        1rst_of_month__initial_stage_task --> CRM_bday_CA_stage_task
        CRM_bday_dup_stage_task["CRM_bday_dup_stage"]
        CRM_bday_CA_stage_task --> CRM_bday_dup_stage_task
        CRM_bday_UK_stage_task["CRM_bday_UK_stage"]
        CRM_bday_dup_stage_task --> CRM_bday_UK_stage_task
        CRM_bday_US_stage_task["CRM_bday_US_stage"]
        CRM_bday_UK_stage_task --> CRM_bday_US_stage_task
        set_month_task["set month"]
        CRM_bday_US_stage_task --> set_month_task
        coupon_check___load_task["coupon check & load"]
        set_month_task --> coupon_check___load_task
        CA_short_task["CA short"]
        coupon_check___load_task --> CA_short_task
        count_available_CA_codes_task["count available CA codes"]
        CA_short_task --> count_available_CA_codes_task
        count_available_UK_codes_task["count available UK codes"]
        count_available_CA_codes_task --> count_available_UK_codes_task
        count_available_US_codes_task["count available US codes"]
        count_available_UK_codes_task --> count_available_US_codes_task
        count_CA_codes_needed_task["count CA codes needed"]
        count_available_US_codes_task --> count_CA_codes_needed_task
        count_UK_codes_needed_task["count UK codes needed"]
        count_CA_codes_needed_task --> count_UK_codes_needed_task
        count_US_codes_needed_task["count US codes needed"]
        count_UK_codes_needed_task --> count_US_codes_needed_task
        UK_short_task["UK short"]
        count_US_codes_needed_task --> UK_short_task
        US_short_task["US short"]
        UK_short_task --> US_short_task
        notification_task["notification"]
        US_short_task --> notification_task
        overwrite_lastDayOfMonth_task["overwrite lastDayOfMonth"]
        notification_task --> overwrite_lastDayOfMonth_task
        truncate_monthly_stages_task["truncate monthly stages"]
        overwrite_lastDayOfMonth_task --> truncate_monthly_stages_task
        Sequence_Container_2_task["Sequence Container 2"]
        truncate_monthly_stages_task --> Sequence_Container_2_task
        Foreach_Loop___Move_to_Archive_task["Foreach Loop - Move to Archive"]
        Sequence_Container_2_task --> Foreach_Loop___Move_to_Archive_task
        Archive_File_task["Archive File"]
        Foreach_Loop___Move_to_Archive_task --> Archive_File_task
        FTP_upload_files_task["FTP upload files"]
        Archive_File_task --> FTP_upload_files_task
        Sequence_Container_2_1_task["Sequence Container 2 1"]
        FTP_upload_files_task --> Sequence_Container_2_1_task
        Foreach_Loop___Move_to_Archive_task["Foreach Loop - Move to Archive"]
        Sequence_Container_2_1_task --> Foreach_Loop___Move_to_Archive_task
        Archive_File_task["Archive File"]
        Foreach_Loop___Move_to_Archive_task --> Archive_File_task
        FTP_upload_files_task["FTP upload files"]
        Archive_File_task --> FTP_upload_files_task
        set_current_dayOfMonth_task["set current dayOfMonth"]
        FTP_upload_files_task --> set_current_dayOfMonth_task
        set_firstDayOfMonth_task["set firstDayOfMonth"]
        set_current_dayOfMonth_task --> set_firstDayOfMonth_task
        set_lastDayOfMonth_task["set lastDayOfMonth"]
        set_firstDayOfMonth_task --> set_lastDayOfMonth_task
        UK_export_prep_task["UK export prep"]
        set_lastDayOfMonth_task --> UK_export_prep_task
        assign_coupon_and_export_files_task["assign coupon and export files"]
        UK_export_prep_task --> assign_coupon_and_export_files_task
        create_export_tables_task["create export tables"]
        assign_coupon_and_export_files_task --> create_export_tables_task
        create_timestamp_file_task["create timestamp file"]
        create_export_tables_task --> create_timestamp_file_task
        remove_special_char_task["remove special char"]
        create_timestamp_file_task --> remove_special_char_task
        stage_codes_from_DM_task["stage codes from DM"]
        remove_special_char_task --> stage_codes_from_DM_task
        stage_cust_from_CRM_task["stage cust from CRM"]
        stage_codes_from_DM_task --> stage_cust_from_CRM_task
        update_DM_detail___produce_file_task["update DM detail & produce file"]
        stage_cust_from_CRM_task --> update_DM_detail___produce_file_task
        update_giftSent_flag_task["update giftSent flag"]
        update_DM_detail___produce_file_task --> update_giftSent_flag_task
        UK_export_prep_daily_task["UK export prep daily"]
        update_giftSent_flag_task --> UK_export_prep_daily_task
        assign_coupon_and_export_files__daily__task["assign coupon and export files (daily)"]
        UK_export_prep_daily_task --> assign_coupon_and_export_files__daily__task
        create_export_tables_task["create export tables"]
        assign_coupon_and_export_files__daily__task --> create_export_tables_task
        create_timestamp_file_task["create timestamp file"]
        create_export_tables_task --> create_timestamp_file_task
        remove_special_char_task["remove special char"]
        create_timestamp_file_task --> remove_special_char_task
        stage_codes_from_DM_task["stage codes from DM"]
        remove_special_char_task --> stage_codes_from_DM_task
        stage_cust_from_CRM_task["stage cust from CRM"]
        stage_codes_from_DM_task --> stage_cust_from_CRM_task
        update_DM_detail___produce_file_task["update DM detail & produce file"]
        stage_cust_from_CRM_task --> update_DM_detail___produce_file_task
        update_giftSent_flag_task["update giftSent flag"]
        update_DM_detail___produce_file_task --> update_giftSent_flag_task
        set_current_dayOfMonth_task["set current dayOfMonth"]
        update_giftSent_flag_task --> set_current_dayOfMonth_task
        set_firstDayOfMonth_task["set firstDayOfMonth"]
        set_current_dayOfMonth_task --> set_firstDayOfMonth_task
        set_lastDayOfMonth_task["set lastDayOfMonth"]
        set_firstDayOfMonth_task --> set_lastDayOfMonth_task
        UK_success_task["UK success"]
        set_lastDayOfMonth_task --> UK_success_task
        UK_success__daily__task["UK success (daily)"]
        UK_success_task --> UK_success__daily__task
        US_export_prep_task["US export prep"]
        UK_success__daily__task --> US_export_prep_task
        assign_coupon_and_export_files_task["assign coupon and export files"]
        US_export_prep_task --> assign_coupon_and_export_files_task
        create_export_tables_task["create export tables"]
        assign_coupon_and_export_files_task --> create_export_tables_task
        create_timestamp_file_task["create timestamp file"]
        create_export_tables_task --> create_timestamp_file_task
        remove_special_char_task["remove special char"]
        create_timestamp_file_task --> remove_special_char_task
        stage_codes_from_DM_task["stage codes from DM"]
        remove_special_char_task --> stage_codes_from_DM_task
        stage_cust_from_CRM_task["stage cust from CRM"]
        stage_codes_from_DM_task --> stage_cust_from_CRM_task
        update_DM_detail___produce_file_task["update DM detail & produce file"]
        stage_cust_from_CRM_task --> update_DM_detail___produce_file_task
        update_giftSent_flag_task["update giftSent flag"]
        update_DM_detail___produce_file_task --> update_giftSent_flag_task
        US_export_prep_daily_task["US export prep daily"]
        update_giftSent_flag_task --> US_export_prep_daily_task
        assign_coupon_and_export_files__daily__task["assign coupon and export files (daily)"]
        US_export_prep_daily_task --> assign_coupon_and_export_files__daily__task
        create_export_tables_task["create export tables"]
        assign_coupon_and_export_files__daily__task --> create_export_tables_task
        create_timestamp_file_task["create timestamp file"]
        create_export_tables_task --> create_timestamp_file_task
        remove_special_char_task["remove special char"]
        create_timestamp_file_task --> remove_special_char_task
        stage_codes_from_DM_task["stage codes from DM"]
        remove_special_char_task --> stage_codes_from_DM_task
        stage_cust_from_CRM_task["stage cust from CRM"]
        stage_codes_from_DM_task --> stage_cust_from_CRM_task
        update_DM_detail___produce_file_task["update DM detail & produce file"]
        stage_cust_from_CRM_task --> update_DM_detail___produce_file_task
        update_giftSent_flag_task["update giftSent flag"]
        update_DM_detail___produce_file_task --> update_giftSent_flag_task
        US_success_task["US success"]
        update_giftSent_flag_task --> US_success_task
        US_success__daily__task["US success (daily)"]
        US_success_task --> US_success__daily__task
        wait_task["wait"]
        US_success__daily__task --> wait_task
        wait_1_task["wait 1"]
        wait_task --> wait_1_task
        Send_Mail_Task_task["Send Mail Task"]
        wait_1_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| Archive | FILE |
| CA bday gift csv | FLATFILE |
| CRM | OLEDB |
| IntegrationStaging | OLEDB |
| KODIAK | OLEDB |
| SMTP | SMTP |
| STL-DYNSNC-P-01.DBAUtility | OLEDB |
| UK bday gift csv | FLATFILE |
| US bday gift csv | FLATFILE |

## Control Flow Tasks

| Task | Type |
|---|---|
| Package | Microsoft.Package |
| 19th estimate for next month CA | STOCK:SEQUENCE |
| next mo estimate | Microsoft.SendMailTask |
| next month estimate | Microsoft.ExecuteSQLTask |
| 19th estimate for next month UK | STOCK:SEQUENCE |
| next mo estimate | Microsoft.SendMailTask |
| next month estimate | Microsoft.ExecuteSQLTask |
| 19th estimate for next month US | STOCK:SEQUENCE |
| next mo estimate | Microsoft.SendMailTask |
| next month estimate | Microsoft.ExecuteSQLTask |
| backup month tables | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| truncate backup | Microsoft.ExecuteSQLTask |
| backup month tables 1 | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| truncate backup | Microsoft.ExecuteSQLTask |
| CA export prep | STOCK:SEQUENCE |
| assign coupon and export files | STOCK:SEQUENCE |
| create export tables | Microsoft.ExecuteSQLTask |
| create timestamp file | Microsoft.FileSystemTask |
| remove special char | Microsoft.ExecuteSQLTask |
| set firstDayOfMonth | Microsoft.ExecuteSQLTask |
| stage codes from DM | Microsoft.Pipeline |
| stage cust from CRM | Microsoft.Pipeline |
| update DM detail & produce file | Microsoft.Pipeline |
| update giftSent flag | Microsoft.ExecuteSQLTask |
| CA export prep daily | STOCK:SEQUENCE |
| assign coupon and export files (daily) | STOCK:SEQUENCE |
| create export tables | Microsoft.ExecuteSQLTask |
| create timestamp file | Microsoft.FileSystemTask |
| remove special char | Microsoft.ExecuteSQLTask |
| stage codes from DM | Microsoft.Pipeline |
| stage cust from CRM | Microsoft.Pipeline |
| update DM detail & produce file | Microsoft.Pipeline |
| update giftSent flag | Microsoft.ExecuteSQLTask |
| CA success | Microsoft.SendMailTask |
| CA success (daily) | Microsoft.SendMailTask |
| Expression Task | Microsoft.ExpressionTask |
| overwrite vars | Microsoft.ExecuteSQLTask |
| Sequence Container | STOCK:SEQUENCE |
| coupon check & load | STOCK:SEQUENCE |
| CA short | Microsoft.SendMailTask |
| count available CA codes | Microsoft.ExecuteSQLTask |
| count available UK codes | Microsoft.ExecuteSQLTask |
| count available US codes | Microsoft.ExecuteSQLTask |
| count CA codes needed | Microsoft.ExecuteSQLTask |
| count UK codes needed | Microsoft.ExecuteSQLTask |
| count US codes needed | Microsoft.ExecuteSQLTask |
| UK short | Microsoft.SendMailTask |
| US short | Microsoft.SendMailTask |
| daily run, initial stage | STOCK:SEQUENCE |
| CRM_bday_CA_stage | Microsoft.Pipeline |
| CRM_bday_dup_stage | Microsoft.Pipeline |
| CRM_bday_UK_stage | Microsoft.Pipeline |
| CRM_bday_US_stage | Microsoft.Pipeline |
| set month | Microsoft.ExecuteSQLTask |
| merge daily to monthly | STOCK:SEQUENCE |
| merge CA | Microsoft.ExecuteSQLTask |
| merge UK | Microsoft.ExecuteSQLTask |
| merge US | Microsoft.ExecuteSQLTask |
| overwrite lastDayOfMonth | Microsoft.ExecuteSQLTask |
| truncate daily stages | Microsoft.ExecuteSQLTask |
| Sequence Container 1 | STOCK:SEQUENCE |
| 1rst of month, initial stage | STOCK:SEQUENCE |
| CRM_bday_CA_stage | Microsoft.Pipeline |
| CRM_bday_dup_stage | Microsoft.Pipeline |
| CRM_bday_UK_stage | Microsoft.Pipeline |
| CRM_bday_US_stage | Microsoft.Pipeline |
| set month | Microsoft.ExecuteSQLTask |
| coupon check & load | STOCK:SEQUENCE |
| CA short | Microsoft.SendMailTask |
| count available CA codes | Microsoft.ExecuteSQLTask |
| count available UK codes | Microsoft.ExecuteSQLTask |
| count available US codes | Microsoft.ExecuteSQLTask |
| count CA codes needed | Microsoft.ExecuteSQLTask |
| count UK codes needed | Microsoft.ExecuteSQLTask |
| count US codes needed | Microsoft.ExecuteSQLTask |
| UK short | Microsoft.SendMailTask |
| US short | Microsoft.SendMailTask |
| notification | Microsoft.SendMailTask |
| overwrite lastDayOfMonth | Microsoft.ExecuteSQLTask |
| truncate monthly stages | Microsoft.ExecuteSQLTask |
| Sequence Container 2 | STOCK:SEQUENCE |
| Foreach Loop - Move to Archive | STOCK:FOREACHLOOP |
| Archive File | Microsoft.FileSystemTask |
| FTP upload files | Microsoft.ExecuteSQLTask |
| Sequence Container 2 1 | STOCK:SEQUENCE |
| Foreach Loop - Move to Archive | STOCK:FOREACHLOOP |
| Archive File | Microsoft.FileSystemTask |
| FTP upload files | Microsoft.ExecuteSQLTask |
| set current dayOfMonth | Microsoft.ExecuteSQLTask |
| set firstDayOfMonth | Microsoft.ExecuteSQLTask |
| set lastDayOfMonth | Microsoft.ExecuteSQLTask |
| UK export prep | STOCK:SEQUENCE |
| assign coupon and export files | STOCK:SEQUENCE |
| create export tables | Microsoft.ExecuteSQLTask |
| create timestamp file | Microsoft.FileSystemTask |
| remove special char | Microsoft.ExecuteSQLTask |
| stage codes from DM | Microsoft.Pipeline |
| stage cust from CRM | Microsoft.Pipeline |
| update DM detail & produce file | Microsoft.Pipeline |
| update giftSent flag | Microsoft.ExecuteSQLTask |
| UK export prep daily | STOCK:SEQUENCE |
| assign coupon and export files (daily) | STOCK:SEQUENCE |
| create export tables | Microsoft.ExecuteSQLTask |
| create timestamp file | Microsoft.FileSystemTask |
| remove special char | Microsoft.ExecuteSQLTask |
| stage codes from DM | Microsoft.Pipeline |
| stage cust from CRM | Microsoft.Pipeline |
| update DM detail & produce file | Microsoft.Pipeline |
| update giftSent flag | Microsoft.ExecuteSQLTask |
| set current dayOfMonth | Microsoft.ExecuteSQLTask |
| set firstDayOfMonth | Microsoft.ExecuteSQLTask |
| set lastDayOfMonth | Microsoft.ExecuteSQLTask |
| UK success | Microsoft.SendMailTask |
| UK success (daily) | Microsoft.SendMailTask |
| US export prep | STOCK:SEQUENCE |
| assign coupon and export files | STOCK:SEQUENCE |
| create export tables | Microsoft.ExecuteSQLTask |
| create timestamp file | Microsoft.FileSystemTask |
| remove special char | Microsoft.ExecuteSQLTask |
| stage codes from DM | Microsoft.Pipeline |
| stage cust from CRM | Microsoft.Pipeline |
| update DM detail & produce file | Microsoft.Pipeline |
| update giftSent flag | Microsoft.ExecuteSQLTask |
| US export prep daily | STOCK:SEQUENCE |
| assign coupon and export files (daily) | STOCK:SEQUENCE |
| create export tables | Microsoft.ExecuteSQLTask |
| create timestamp file | Microsoft.FileSystemTask |
| remove special char | Microsoft.ExecuteSQLTask |
| stage codes from DM | Microsoft.Pipeline |
| stage cust from CRM | Microsoft.Pipeline |
| update DM detail & produce file | Microsoft.Pipeline |
| update giftSent flag | Microsoft.ExecuteSQLTask |
| US success | Microsoft.SendMailTask |
| US success (daily) | Microsoft.SendMailTask |
| wait | Microsoft.ExecuteSQLTask |
| wait 1 | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | select sdd.serializationDiscountDetailID, sdd.serializedNum   from [dbo].[SerializationDiscountDetail] sdd join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID join [dbo].[Discount] d on sd.discountID = d.discountID  where d.startDate = ?   --and d.endingDate  = ? and d.countryID = 2 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNu |
|  | SELECT u.emailAddress, u.subscriberkey, u.firstName,u.lastName,u.address,u.address2,u.city, u.state,u.zipCode,u.carrierRoute from [CRM_bday_CA_month_stage] u  left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode where n.attributeCode is null order by u.subscriberKey asc |
|  | with assignedGift as ( select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName ,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode from [dbo].[CRM_bday_CA_code_export] c join [dbo].[CRM_bday_CA_guest_export] g on c.tmpId = g.tmpId )  select * from assignedGift |
|  | update [dbo].[SerializationDiscountDetail]  set customerNumber = ?, firstName = ?, lastName = ?, address = ?, address2 = ?, city = ?, state = ?, zipCode = ?, email = ?, isPoolAvailable = 0 where serializationDiscountDetailID = ? |
|  | select sdd.serializationDiscountDetailID, sdd.serializedNum   from [dbo].[SerializationDiscountDetail] sdd join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID join [dbo].[Discount] d on sd.discountID = d.discountID  where d.startDate = ?   --and d.endingDate  = ? and d.countryID = 2 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNu |
|  | SELECT u.emailAddress, u.subscriberkey,u.dayOfMonthAdded, u.firstName,u.lastName,u.address,u.address2,u.city, u.state,u.zipCode,u.carrierRoute from [CRM_bday_CA_month_stage] u  left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode where n.attributeCode is null and u.dayOfMonthAdded = ? and u.giftSent is null order by u.subscriberKey asc |
|  | with assignedGift as ( select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName ,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode from [dbo].[CRM_bday_CA_code_export] c join [dbo].[CRM_bday_CA_guest_export] g on c.tmpId = g.tmpId )  select * from assignedGift |
|  | update [dbo].[SerializationDiscountDetail]  set customerNumber = ?, firstName = ?, lastName = ?, address = ?, address2 = ?, city = ?, state = ?, zipCode = ?, email = ?, isPoolAvailable = 0 where serializationDiscountDetailID = ? |
|  | select  	distinct 	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value,   c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route from customer c 	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89) 	join customer_attribute c |
|  | select  	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value from customer c 	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89) 	join customer_attribute ca with (nolock) on cd.customer_id=ca.customer_id and ca.attribute_grouping_code  ='BDAY' 	join customer_attribute ca |
|  | select  	distinct 	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value,   c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route from customer c 	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89) 	join customer_attribute c |
|  | select  	distinct 	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value,                    c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route from customer c 	join customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89) 	join cus |
|  | select  	distinct 	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value, c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route from [stl-crmdb-p-01].crm.dbo.customer c 	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.d |
|  | select  	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value from [stl-crmdb-p-01].crm.dbo.customer c 	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.division_id in (86,89) 	join [stl-crmdb-p-01].crm.dbo.customer_attribute ca with (nolock) on cd.customer_id=ca.cust |
|  | select  	distinct 	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value, c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route from [stl-crmdb-p-01].crm.dbo.customer c 	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.customer_id and cd.d |
|  | select  	distinct 	cast(c.customer_no as varchar) as subscriberkey, 	e.email_address, 	ca.attribute_code, 	ca.attribute_comment, 	ca.attribute_value,                    c.first_name, c.last_name, a.address_1,a.address_2,a.address_3,a.address_4,a.post_code,a.carrier_route from [stl-crmdb-p-01].crm.dbo.customer c 	join [stl-crmdb-p-01].crm.dbo.customer_division cd with (nolock) on c.customer_id=cd.c |
|  | select sdd.serializationDiscountDetailID, sdd.serializedNum   from [dbo].[SerializationDiscountDetail] sdd join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID join [dbo].[Discount] d on sd.discountID = d.discountID  where d.startDate = ?   --and d.endingDate  = ? and d.countryID = 3 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNu |
|  | SELECT u.emailAddress, u.subscriberkey, u.firstName,u.lastName,u.address,u.address2,u.city, u.state,u.zipCode,u.carrierRoute from [CRM_bday_UK_month_stage] u  left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode where n.attributeCode is null order by u.subscriberKey asc |
|  | with assignedGift as ( select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName ,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode from [dbo].[CRM_bday_UK_code_export] c join [dbo].[CRM_bday_UK_guest_export] g on c.tmpId = g.tmpId )  select * from assignedGift |
|  | update [dbo].[SerializationDiscountDetail]  set customerNumber = ?, firstName = ?, lastName = ?, address = ?, address2 = ?, city = ?, state = ?, zipCode = ?, email = ?, isPoolAvailable = 0 where serializationDiscountDetailID = ? |
|  | select sdd.serializationDiscountDetailID, sdd.serializedNum   from [dbo].[SerializationDiscountDetail] sdd join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID join [dbo].[Discount] d on sd.discountID = d.discountID  where d.startDate = ?   --and d.endingDate  = ? and d.countryID = 3 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNu |
|  | SELECT u.emailAddress, u.subscriberkey,u.dayOfMonthAdded, u.firstName,u.lastName,u.address,u.address2,u.city, u.state,u.zipCode,u.carrierRoute from [CRM_bday_UK_month_stage] u  left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode where n.attributeCode is null and u.dayOfMonthAdded = ? and u.giftSent is null order by u.subscriberKey asc |
|  | with assignedGift as ( select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName ,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode from [dbo].[CRM_bday_UK_code_export] c join [dbo].[CRM_bday_UK_guest_export] g on c.tmpId = g.tmpId )  select * from assignedGift |
|  | update [dbo].[SerializationDiscountDetail]  set customerNumber = ?, firstName = ?, lastName = ?, address = ?, address2 = ?, city = ?, state = ?, zipCode = ?, email = ?, isPoolAvailable = 0 where serializationDiscountDetailID = ? |
|  | select sdd.serializationDiscountDetailID, sdd.serializedNum   from [dbo].[SerializationDiscountDetail] sdd join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID join [dbo].[Discount] d on sd.discountID = d.discountID  where d.startDate = ?   --and d.endingDate  = ? and d.countryID = 1 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNu |
|  | SELECT u.emailAddress, u.subscriberkey, u.firstName,u.lastName,u.address,u.address2,u.city, u.state,u.zipCode,u.carrierRoute from [CRM_bday_US_month_stage] u  left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode where n.attributeCode is null order by u.subscriberKey asc |
|  | with assignedGift as ( select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName ,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode from [dbo].[CRM_bday_US_code_export] c join [dbo].[CRM_bday_US_guest_export] g on c.tmpId = g.tmpId --where g.tmpID in (5490,1234,4277,2589,6251,12310,73616,49164,45389,5094) )  select * from assignedGift |
|  | update [dbo].[SerializationDiscountDetail]  set customerNumber = ?, firstName = ?, lastName = ?, address = ?, address2 = ?, city = ?, state = ?, zipCode = ?, email = ?, isPoolAvailable = 0 where serializationDiscountDetailID = ? |
|  | select sdd.serializationDiscountDetailID, sdd.serializedNum   from [dbo].[SerializationDiscountDetail] sdd join  [dbo].[SerializationDiscount] sd on sdd.serializationID = sd.serializationID join [dbo].[Discount] d on sd.discountID = d.discountID  where d.startDate = ?   --and d.endingDate  = ? and d.countryID = 1 and sd.serializationFileTypeID = 2 and sdd.isPoolAvailable = 1 and len(sdd.customerNu |
|  | SELECT u.emailAddress, u.subscriberkey,u.dayOfMonthAdded, u.firstName,u.lastName,u.address,u.address2,u.city, u.state,u.zipCode,u.carrierRoute from [CRM_bday_US_month_stage] u  left join [CRM_bday_dup_stage] n on u.subscriberkey=n.subscriberkey and u.attributeCode=n.attributeCode where n.attributeCode is null and u.dayOfMonthAdded = ? and u.giftSent is null order by u.subscriberKey asc |
|  | with assignedGift as ( select c.giftCodeID, c.giftCode,g.emailAddress ,g.subscriberKey ,g.firstName ,g.lastName,g.[address],g.address2,g.city,g.[state], g.zipcode from [dbo].[CRM_bday_US_code_export] c join [dbo].[CRM_bday_US_guest_export] g on c.tmpId = g.tmpId )  select * from assignedGift |
|  | update [dbo].[SerializationDiscountDetail]  set customerNumber = ?, firstName = ?, lastName = ?, address = ?, address2 = ?, city = ?, state = ?, zipCode = ?, email = ?, isPoolAvailable = 0 where serializationDiscountDetailID = ? |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[CRM_bday_CA_month_stage] |
|  | [dbo].[CRM_bday_CA_month_stage] |
|  | [dbo].[CRM_bday_UK_month_stage] |
|  | [dbo].[CRM_bday_UK_month_stage] |
|  | [dbo].[CRM_bday_US_month_stage] |
|  | [dbo].[CRM_bday_US_month_stage] |
|  | [dbo].[CRM_bday_CA_month_stage] |
|  | [dbo].[CRM_bday_CA_month_stage] |
|  | [dbo].[CRM_bday_UK_month_stage] |
|  | [dbo].[CRM_bday_UK_month_stage] |
|  | [dbo].[CRM_bday_US_month_stage] |
|  | [dbo].[CRM_bday_US_month_stage] |
|  | [dbo].[CRM_bday_CA_code_export] |
|  | [dbo].[CRM_bday_CA_guest_export] |
|  | [dbo].[CRM_bday_CA_code_export] |
|  | [dbo].[CRM_bday_CA_guest_export] |
|  | [dbo].[CRM_bday_CA_daily_stage] |
|  | [dbo].[CRM_bday_dup_stage] |
|  | [dbo].[CRM_bday_UK_daily_stage] |
|  | [dbo].[CRM_bday_US_daily_stage] |
|  | [dbo].[CRM_bday_CA_month_stage] |
|  | [dbo].[CRM_bday_dup_stage] |
|  | [dbo].[CRM_bday_UK_month_stage] |
|  | [dbo].[CRM_bday_US_month_stage] |
|  | [dbo].[CRM_bday_UK_code_export] |
|  | [dbo].[CRM_bday_UK_guest_export] |
|  | [dbo].[CRM_bday_UK_code_export] |
|  | [dbo].[CRM_bday_UK_guest_export] |
|  | [dbo].[CRM_bday_US_code_export] |
|  | [dbo].[CRM_bday_US_guest_export] |
|  | [dbo].[CRM_bday_US_code_export] |
|  | [dbo].[CRM_bday_US_guest_export] |

