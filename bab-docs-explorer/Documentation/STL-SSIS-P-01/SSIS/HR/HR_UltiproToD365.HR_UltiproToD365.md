# SSIS Package: HR_UltiproToD365

**Project:** HR_UltiproToD365  
**Folder:** HR  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| ArchiveFolder | FILE |  |  |  |
| GetBlobUrl | HTTP (KingswaySoft) |  |  |  |
| GetStatus | HTTP (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| IntegrationStaging 1 | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| ME_01 | OLEDB | bedrockdb02 | me_01 | Data Source=bedrockdb02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| MultipleLocationFile | FLATFILE |  |  |  |
| PostTriggerImport | HTTP (KingswaySoft) |  |  |  |
| SMTP_EMAIL | SMTP |  |  |  |
| SQL_LOG | OLEDB | stl-ssis-p-01 | msdb | Data Source=stl-ssis-p-01; Initial Catalog=msdb; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| UserCreateCSV | FLATFILE |  |  |  |
| UserDeactivateCSV | FLATFILE |  |  |  |
| UserWHSCreateCSV | FLATFILE |  |  |  |
| XML FILES | FILE |  |  |  |
| papamart.dw | OLEDB | papamart | dw | Data Source=papamart; Initial Catalog=dw; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| setWorkUserPassword | HTTP (KingswaySoft) |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| WMS_UserCreate | Package |
| password update seq | SEQUENCE |
| Foreach Loop Container 1 | FOREACHLOOP |
| prep 1 row | ExecuteSQLTask |
| Truncate Stage | ExecuteSQLTask |
| UserCreate File Generation and Move NEW JSON | SEQUENCE |
| password reset URL | Pipeline |
| Send Mail Task | SendMailTask |
| Wait | ExecuteSQLTask |
| Truncate Stage | ExecuteSQLTask |
| User Create Stage | SEQUENCE |
| Stage User Data | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| varPasswordObject | ExecuteSQLTask |
| process multiple locations | SEQUENCE |
| Foreach Loop Container | FOREACHLOOP |
| archive | FileSystemTask |
| Data Flow Task | Pipeline |
| delete | FileSystemTask |
| merge | ExecuteSQLTask |
| truncate | ExecuteSQLTask |
| user create seq | SEQUENCE |
| set exported flag | SEQUENCE |
| set isExported | ExecuteSQLTask |
| User Create Stage | SEQUENCE |
| Stage User Data | Pipeline |
| Stage User_WHse Data | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| User Deactivate Stage 1 1 | SEQUENCE |
| Stage User Data | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| UserCreate File Generation and Move | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| DataFlow CSV Files | Pipeline |
| Foreach BlobUploadLoop | FOREACHLOOP |
| datestamp archive | FileSystemTask |
| Foreach Loop Container | FOREACHLOOP |
| Archive Files | FileSystemTask |
| azCopy to Blob | ExecuteProcess |
| ProcessStatus For Loop | FORLOOP |
| Get Summary Status | Pipeline |
| Set ProcessStatus | ExecuteSQLTask |
| Wait | ExecuteSQLTask |
| Set BatchID - LoopCount | ExecuteSQLTask |
| Set RowsCount | ExecuteSQLTask |
| Stage Blob URL | Pipeline |
| Trigger Import | Pipeline |
| Foreach Loop - Copy Manifest and Header Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Zip File | ExecuteProcess |
| Stage Company Entities | ExecuteSQLTask |
| UserDeactivate File Generation and Move | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| DataFlow CSV File | Pipeline |
| Foreach BlobUploadLoop | FOREACHLOOP |
| datestamp archive | FileSystemTask |
| Foreach Loop Container | FOREACHLOOP |
| Archive Files | FileSystemTask |
| azCopy to Blob | ExecuteProcess |
| ProcessStatus For Loop | FORLOOP |
| Get Summary Status | Pipeline |
| Set ProcessStatus | ExecuteSQLTask |
| Wait | ExecuteSQLTask |
| Set BatchID - LoopCount | ExecuteSQLTask |
| Set RowsCount | ExecuteSQLTask |
| Stage Blob URL | Pipeline |
| Trigger Import | Pipeline |
| Foreach Loop - Copy Manifest and Header Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Zip File | ExecuteProcess |
| Stage Company Entities | ExecuteSQLTask |
| Wait | ExecuteSQLTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- Wait [ExecuteSQLTask]
- password update seq [SEQUENCE]
  - Foreach Loop Container 1 [FOREACHLOOP]
    - Truncate Stage [ExecuteSQLTask]
    - UserCreate File Generation and Move NEW JSON [SEQUENCE]
      - Send Mail Task [SendMailTask]
      - password reset URL [Pipeline]
    - Wait [ExecuteSQLTask]
    - prep 1 row [ExecuteSQLTask]
  - Truncate Stage [ExecuteSQLTask]
  - User Create Stage [SEQUENCE]
    - Stage User Data [Pipeline]
    - Truncate Stage [ExecuteSQLTask]
  - varPasswordObject [ExecuteSQLTask]
- process multiple locations [SEQUENCE]
  - Foreach Loop Container [FOREACHLOOP]
    - Data Flow Task [Pipeline]
    - archive [FileSystemTask]
    - delete [FileSystemTask]
    - merge [ExecuteSQLTask]
    - truncate [ExecuteSQLTask]
- user create seq [SEQUENCE]
  - User Create Stage [SEQUENCE]
    - Stage User Data [Pipeline]
    - Stage User_WHse Data [Pipeline]
    - Truncate Stage [ExecuteSQLTask]
  - User Deactivate Stage 1 1 [SEQUENCE]
    - Stage User Data [Pipeline]
    - Truncate Stage [ExecuteSQLTask]
  - UserCreate File Generation and Move [SEQUENCE]
    - Foreach Loop - Per Entity [FOREACHLOOP]
      - DataFlow CSV Files [Pipeline]
      - Foreach BlobUploadLoop [FOREACHLOOP]
        - Foreach Loop Container [FOREACHLOOP]
          - Archive Files [FileSystemTask]
          - azCopy to Blob [ExecuteProcess]
        - ProcessStatus For Loop [FORLOOP]
          - Get Summary Status [Pipeline]
          - Set ProcessStatus [ExecuteSQLTask]
          - Wait [ExecuteSQLTask]
        - Set BatchID - LoopCount [ExecuteSQLTask]
        - Set RowsCount [ExecuteSQLTask]
        - Stage Blob URL [Pipeline]
        - Trigger Import [Pipeline]
        - datestamp archive [FileSystemTask]
      - Foreach Loop - Copy Manifest and Header Files [FOREACHLOOP]
        - Copy Manifest & Header [FileSystemTask]
      - Zip File [ExecuteProcess]
    - Stage Company Entities [ExecuteSQLTask]
  - UserDeactivate File Generation and Move [SEQUENCE]
    - Foreach Loop - Per Entity [FOREACHLOOP]
      - DataFlow CSV File [Pipeline]
      - Foreach BlobUploadLoop [FOREACHLOOP]
        - Foreach Loop Container [FOREACHLOOP]
          - Archive Files [FileSystemTask]
          - azCopy to Blob [ExecuteProcess]
        - ProcessStatus For Loop [FORLOOP]
          - Get Summary Status [Pipeline]
          - Set ProcessStatus [ExecuteSQLTask]
          - Wait [ExecuteSQLTask]
        - Set BatchID - LoopCount [ExecuteSQLTask]
        - Set RowsCount [ExecuteSQLTask]
        - Stage Blob URL [Pipeline]
        - Trigger Import [Pipeline]
        - datestamp archive [FileSystemTask]
      - Foreach Loop - Copy Manifest and Header Files [FOREACHLOOP]
        - Copy Manifest & Header [FileSystemTask]
      - Zip File [ExecuteProcess]
    - Stage Company Entities [ExecuteSQLTask]
  - set exported flag [SEQUENCE]
    - set isExported [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_password_update_seq["password update seq"]
    n_Package_password_update_seq_Foreach_Loop_Container_1["Foreach Loop Container 1"]
    n_Package_password_update_seq_Foreach_Loop_Container_1_prep_1_row["prep 1 row"]
    n_Package_password_update_seq_Foreach_Loop_Container_1_Truncate_Stage["Truncate Stage"]
    n_Package_password_update_seq_Foreach_Loop_Container_1_UserCreate_File_Generation_and_Move_NEW_JSON["UserCreate File Generation and Move NEW JSON"]
    n_Package_password_update_seq_Foreach_Loop_Container_1_UserCreate_File_Generation_and_Move_NEW_JSON_password_reset_URL["password reset URL"]
    n_Package_password_update_seq_Foreach_Loop_Container_1_UserCreate_File_Generation_and_Move_NEW_JSON_Send_Mail_Task["Send Mail Task"]
    n_Package_password_update_seq_Foreach_Loop_Container_1_Wait["Wait"]
    n_Package_password_update_seq_Truncate_Stage["Truncate Stage"]
    n_Package_password_update_seq_User_Create_Stage["User Create Stage"]
    n_Package_password_update_seq_User_Create_Stage_Stage_User_Data["Stage User Data"]
    n_Package_password_update_seq_User_Create_Stage_Truncate_Stage["Truncate Stage"]
    n_Package_password_update_seq_varPasswordObject["varPasswordObject"]
    n_Package_process_multiple_locations["process multiple locations"]
    n_Package_process_multiple_locations_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_process_multiple_locations_Foreach_Loop_Container_archive["archive"]
    n_Package_process_multiple_locations_Foreach_Loop_Container_Data_Flow_Task["Data Flow Task"]
    n_Package_process_multiple_locations_Foreach_Loop_Container_delete["delete"]
    n_Package_process_multiple_locations_Foreach_Loop_Container_merge["merge"]
    n_Package_process_multiple_locations_Foreach_Loop_Container_truncate["truncate"]
    n_Package_user_create_seq["user create seq"]
    n_Package_user_create_seq_set_exported_flag["set exported flag"]
    n_Package_user_create_seq_set_exported_flag_set_isExported["set isExported"]
    n_Package_user_create_seq_User_Create_Stage["User Create Stage"]
    n_Package_user_create_seq_User_Create_Stage_Stage_User_Data["Stage User Data"]
    n_Package_user_create_seq_User_Create_Stage_Stage_User_WHse_Data["Stage User_WHse Data"]
    n_Package_user_create_seq_User_Create_Stage_Truncate_Stage["Truncate Stage"]
    n_Package_user_create_seq_User_Deactivate_Stage_1_1["User Deactivate Stage 1 1"]
    n_Package_user_create_seq_User_Deactivate_Stage_1_1_Stage_User_Data["Stage User Data"]
    n_Package_user_create_seq_User_Deactivate_Stage_1_1_Truncate_Stage["Truncate Stage"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move["UserCreate File Generation and Move"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_CSV_Files["DataFlow CSV Files"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop["Foreach BlobUploadLoop"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_datestamp_archive["datestamp archive"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Wait["Wait"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount["Set RowsCount"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL["Stage Blob URL"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import["Trigger Import"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files["Foreach Loop - Copy Manifest and Header Files"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File["Zip File"]
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Stage_Company_Entities["Stage Company Entities"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move["UserDeactivate File Generation and Move"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_CSV_File["DataFlow CSV File"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop["Foreach BlobUploadLoop"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_datestamp_archive["datestamp archive"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Wait["Wait"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount["Set RowsCount"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL["Stage Blob URL"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import["Trigger Import"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files["Foreach Loop - Copy Manifest and Header Files"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File["Zip File"]
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Stage_Company_Entities["Stage Company Entities"]
    n_Package_Wait["Wait"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_password_update_seq_Foreach_Loop_Container_1_UserCreate_File_Generation_and_Move_NEW_JSON_password_reset_URL --> n_Package_password_update_seq_Foreach_Loop_Container_1_UserCreate_File_Generation_and_Move_NEW_JSON_Send_Mail_Task
    n_Package_password_update_seq_Foreach_Loop_Container_1_UserCreate_File_Generation_and_Move_NEW_JSON --> n_Package_password_update_seq_Foreach_Loop_Container_1_Truncate_Stage
    n_Package_password_update_seq_Foreach_Loop_Container_1_Truncate_Stage --> n_Package_password_update_seq_Foreach_Loop_Container_1_Wait
    n_Package_password_update_seq_Foreach_Loop_Container_1_prep_1_row --> n_Package_password_update_seq_Foreach_Loop_Container_1_UserCreate_File_Generation_and_Move_NEW_JSON
    n_Package_password_update_seq_User_Create_Stage_Truncate_Stage --> n_Package_password_update_seq_User_Create_Stage_Stage_User_Data
    n_Package_password_update_seq_User_Create_Stage --> n_Package_password_update_seq_varPasswordObject
    n_Package_password_update_seq_varPasswordObject --> n_Package_password_update_seq_Truncate_Stage
    n_Package_password_update_seq_Truncate_Stage --> n_Package_password_update_seq_Foreach_Loop_Container_1
    n_Package_process_multiple_locations_Foreach_Loop_Container_truncate --> n_Package_process_multiple_locations_Foreach_Loop_Container_Data_Flow_Task
    n_Package_process_multiple_locations_Foreach_Loop_Container_Data_Flow_Task --> n_Package_process_multiple_locations_Foreach_Loop_Container_merge
    n_Package_process_multiple_locations_Foreach_Loop_Container_merge --> n_Package_process_multiple_locations_Foreach_Loop_Container_archive
    n_Package_process_multiple_locations_Foreach_Loop_Container_archive --> n_Package_process_multiple_locations_Foreach_Loop_Container_delete
    n_Package_user_create_seq_User_Create_Stage_Stage_User_Data --> n_Package_user_create_seq_User_Create_Stage_Stage_User_WHse_Data
    n_Package_user_create_seq_User_Create_Stage_Truncate_Stage --> n_Package_user_create_seq_User_Create_Stage_Stage_User_Data
    n_Package_user_create_seq_User_Deactivate_Stage_1_1_Truncate_Stage --> n_Package_user_create_seq_User_Deactivate_Stage_1_1_Stage_User_Data
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_Archive_Files
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Wait --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_BatchID___LoopCount --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_datestamp_archive
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_CSV_Files --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Stage_Company_Entities --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_Archive_Files
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Wait --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_BatchID___LoopCount --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_datestamp_archive
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_CSV_File --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop
    n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Stage_Company_Entities --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move_Foreach_Loop___Per_Entity
    n_Package_user_create_seq_User_Create_Stage --> n_Package_user_create_seq_UserCreate_File_Generation_and_Move
    n_Package_user_create_seq_UserCreate_File_Generation_and_Move --> n_Package_user_create_seq_set_exported_flag
    n_Package_user_create_seq_User_Deactivate_Stage_1_1 --> n_Package_user_create_seq_UserDeactivate_File_Generation_and_Move
    n_Package_user_create_seq_set_exported_flag --> n_Package_user_create_seq_User_Deactivate_Stage_1_1
    n_Package_user_create_seq --> n_Package_Wait
    n_Package_Wait --> n_Package_password_update_seq
    n_Package_process_multiple_locations --> n_Package_user_create_seq
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | ArchiveFile | Yes |
| User | ArchiveFile2 | Yes |
| User | ArchiveFileDateStamped | Yes |
| User | ArchiveFileDateStamped2 | Yes |
| User | ArchiveFolder | Yes |
| User | ArchiveFolder2 | Yes |
| User | AzCopytoBlobCommand | Yes |
| User | AzCopytoBlobCommand2 | Yes |
| User | BatchID | No |
| User | BlobURL | No |
| User | BlobURLRecordSet | No |
| User | CompanyEntities | No |
| User | DataEntityName | No |
| User | DataEntityName2 | No |
| User | DataEntityName3 | No |
| User | DateTimeStamp | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | Entity | No |
| User | FileName | No |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | HeaderAndManifestForLoop | No |
| User | JSON_GetBlobURL | Yes |
| User | JSON_GetSummaryStatus | Yes |
| User | LoopCount | No |
| User | PackageAPIHeaderAndManifestPath | Yes |
| User | PackageAPIHeaderAndManifestPath2 | Yes |
| User | PackageName | No |
| User | ProcessStatus | No |
| User | RowsCount | No |
| User | RowsCount2 | No |
| User | RowsCount3 | No |
| User | RunControlFlag | No |
| User | SQLItemLoadViewByEntity | Yes |
| User | SQL_GetBlobURLCommand | Yes |
| User | SQL_GetSummaryStatus | Yes |
| User | SQL_TriggerImport | Yes |
| User | SQL_TriggerImport2 | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | ZipCommand | Yes |
| User | ZipCommand2 | Yes |
| User | ZipDest | Yes |
| User | ZipDest2 | Yes |
| User | ZipSource | Yes |
| User | ZipSource2 | Yes |
| User | ZipSource3 | Yes |
| User | varCompany | No |
| User | varInsertSQL | Yes |
| User | varMultipleUserFileArchived | Yes |
| User | varPass | No |
| User | varPasswordObject | No |
| User | varTest | Yes |
| User | varUserID | No |
| User | varWorkerName | No |

### Expression-bound variable values

#### User::ArchiveFile

**Expression:**

```sql
@[User::ArchiveFolder] + "UserCreate" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserCreate\Archive\UserCreate1100.zip
```

#### User::ArchiveFile2

**Expression:**

```sql
@[User::ArchiveFolder2] + "UserDeactivate" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserDeactivate\Archive\UserDeactivate1100.zip
```

#### User::ArchiveFileDateStamped

**Expression:**

```sql
@[User::ArchiveFolder] + "UserCreate" +  @[User::Entity] + "_" +   @[User::DateTimeStamp] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserCreate\Archive\UserCreate1100_20257211485613.zip
```

#### User::ArchiveFileDateStamped2

**Expression:**

```sql
@[User::ArchiveFolder2] + "UserDeactivate" +  @[User::Entity] + "_" +   @[User::DateTimeStamp] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserDeactivate\Archive\UserDeactivate1100_20257211485613.zip
```

#### User::ArchiveFolder

**Expression:**

```sql
@[$Package::WMS_UserCreateFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserCreate\Archive\
```

#### User::ArchiveFolder2

**Expression:**

```sql
@[$Package::WMS_UserDeactivateFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserDeactivate\Archive\
```

#### User::AzCopytoBlobCommand

**Expression:**

```sql
"cp \"" +  @[User::ZipDest] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserCreate\UserCreate1100.zip" "xxxhttps://buildabear1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
```

#### User::AzCopytoBlobCommand2

**Expression:**

```sql
"cp \"" +  @[User::ZipDest2] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserDeactivate\UserDeactivate1100.zip" "xxxhttps://buildabear1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
```

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
20257211485613
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
7/21/2025
```

#### User::EndDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::EndDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::EndDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::EndDate]),2)
```

**Evaluated value:**

```sql
2025-07-21
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
7/21/2025
```

#### User::GetDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::GetDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::GetDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::GetDate]),2)
```

**Evaluated value:**

```sql
2025-07-21
```

#### User::JSON_GetBlobURL

**Expression:**

```sql
"
{
    \"uniqueFileName\":\"" + @[User::BatchID] + "\"
}
"
```

**Evaluated value:**

```sql

{
    "uniqueFileName":"0E7E4435-B76A-47BD-A840-D89D3CBE0424"
}

```

#### User::JSON_GetSummaryStatus

**Expression:**

```sql
"
{
    \"executionId\":\"" + @[User::BatchID] + "\"
}
"
```

**Evaluated value:**

```sql

{
    "executionId":"0E7E4435-B76A-47BD-A840-D89D3CBE0424"
}

```

#### User::PackageAPIHeaderAndManifestPath

**Expression:**

```sql
@[$Package::WMS_PackageAPI_StaticPackageFilesPath] + "UserCreate"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\UserCreate
```

#### User::PackageAPIHeaderAndManifestPath2

**Expression:**

```sql
@[$Package::WMS_PackageAPI_StaticPackageFilesPath] + "UserDeactivate"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\UserDeactivate
```

#### User::SQLItemLoadViewByEntity

**Expression:**

```sql
"select *
 from vwERPItemLoadtoD365
where Entity = '" + @[User::Entity]  + "'"
```

**Evaluated value:**

```sql
select *
 from vwERPItemLoadtoD365
where Entity = '1100'
```

#### User::SQL_GetBlobURLCommand

**Expression:**

```sql
"select cast('" +  @[User::JSON_GetBlobURL]  + "' as varchar(100)) as Command, cast('" + @[User::BatchID] + "' as varchar(50)) as BatchID, getdate() as InsertDate "
```

**Evaluated value:**

```sql
select cast('
{
    "uniqueFileName":"0E7E4435-B76A-47BD-A840-D89D3CBE0424"
}
' as varchar(100)) as Command, cast('0E7E4435-B76A-47BD-A840-D89D3CBE0424' as varchar(50)) as BatchID, getdate() as InsertDate 
```

#### User::SQL_GetSummaryStatus

**Expression:**

```sql
"select cast('" +  @[User::JSON_GetSummaryStatus]  + "' as varchar(100)) as Command, cast('" + @[User::BatchID] + "' as varchar(50)) as BatchID, getdate() as InsertDate "
```

**Evaluated value:**

```sql
select cast('
{
    "executionId":"0E7E4435-B76A-47BD-A840-D89D3CBE0424"
}
' as varchar(100)) as Command, cast('0E7E4435-B76A-47BD-A840-D89D3CBE0424' as varchar(50)) as BatchID, getdate() as InsertDate 
```

#### User::SQL_TriggerImport

**Expression:**

```sql
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[$Package::WMS_UserCreateBlobDefinitionGroupID] + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabear1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('0E7E4435-B76A-47BD-A840-D89D3CBE0424' as varchar(50)) as executionId, 'MobileDeviceUserCreateUpdate1100' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1100' as legalEntityId
```

#### User::SQL_TriggerImport2

**Expression:**

```sql
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[$Package::WMS_UserDeactivateBlobDefinitionGroupID] + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabear1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('0E7E4435-B76A-47BD-A840-D89D3CBE0424' as varchar(50)) as executionId, 'MobileDeviceUserDeactivate1100' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1100' as legalEntityId
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
7/20/2025
```

#### User::StartDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::StartDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::StartDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::StartDate]),2)
```

**Evaluated value:**

```sql
2025-07-20
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  + "\"  \"" +  @[User::ZipSource2]  + "\"  \"" +  @[User::ZipSource3]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserCreate\UserCreate1100.zip"  "*.xml"  "*.csv"  "-x!*.zip" -sdel
```

#### User::ZipCommand2

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest2]  + "\"  \"" +  @[User::ZipSource]  + "\"  \"" +  @[User::ZipSource2]  + "\"  \"" +  @[User::ZipSource3]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserDeactivate\UserDeactivate1100.zip"  "*.xml"  "*.csv"  "-x!*.zip" -sdel
```

#### User::ZipDest

**Expression:**

```sql
@[$Package::WMS_UserCreateFileStageLocation]  + "UserCreate" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserCreate\UserCreate1100.zip
```

#### User::ZipDest2

**Expression:**

```sql
@[$Package::WMS_UserDeactivateFileStageLocation]  + "UserDeactivate" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserDeactivate\UserDeactivate1100.zip
```

#### User::ZipSource

**Expression:**

```sql
"*.xml"
```

**Evaluated value:**

```sql
*.xml
```

#### User::ZipSource2

**Expression:**

```sql
"*.csv"
```

**Evaluated value:**

```sql
*.csv
```

#### User::ZipSource3

**Expression:**

```sql
"-x!*.zip"
```

**Evaluated value:**

```sql
-x!*.zip
```

#### User::varInsertSQL

**Expression:**

```sql
"INSERT INTO [ERP].[UserLoadtoD365pwReset] ([workerName],[userID],[userPassword],[Company])
SELECT '" + @[User::varWorkerName] + "' , '" + @[User::varUserID] + "', '" + @[User::varPass] + "', '" + @[User::varCompany] + "'"
```

**Evaluated value:**

```sql
INSERT INTO [ERP].[UserLoadtoD365pwReset] ([workerName],[userID],[userPassword],[Company])
SELECT '' , '', '', ''
```

#### User::varMultipleUserFileArchived

**Expression:**

```sql
@[$Package::WMS_MultipleLocationFileArchive]  + "StoreAssociateMultipleLocationInterface" + "_" +  (DT_WSTR, 4) year(getdate()) +  (DT_WSTR, 2) month(getdate()) +  (DT_WSTR, 2) day(getdate()) + RIGHT("0" + (DT_STR, 2, 1252)DATEPART("hh", GetDate()), 2) + RIGHT("0" + (DT_STR, 2, 1252)DATEPART("mi", GetDate()), 2) + RIGHT("0" + (DT_STR, 2, 1252)DATEPART("ss", GetDate()), 2) + ".csv"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\HR\UltiproMultipleLocations\archive\StoreAssociateMultipleLocationInterface_2025721140805.csv
```

#### User::varTest

**Expression:**

```sql
@[$Package::WMS_PackageAPI_StaticPackageFilesPath]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\
```

## Execute SQL Tasks

### Wait

**Path:** `Package\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:59'
```

### Truncate Stage

**Path:** `Package\password update seq\Foreach Loop Container 1\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [ERP].[UserLoadtoD365pwReset]

```

### Wait

**Path:** `Package\password update seq\Foreach Loop Container 1\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:4'
```

### prep 1 row

**Path:** `Package\password update seq\Foreach Loop Container 1\prep 1 row`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
INSERT INTO [ERP].[UserLoadtoD365pwReset] ([workerName],[userID],[userPassword],[Company])
SELECT '' , '', '', ''
```

**Property expression (runtime override):**

```sql
@[User::varInsertSQL]
```

### Truncate Stage

**Path:** `Package\password update seq\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [ERP].[UserLoadtoD365pwReset]

```

### Truncate Stage

**Path:** `Package\password update seq\User Create Stage\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [ERP].[UserLoadtoD365pwReset]

```

### varPasswordObject

**Path:** `Package\password update seq\varPasswordObject`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select workerName, userID, userPassword, Company from  [ERP].[UserLoadtoD365pwReset]
```

### merge

**Path:** `Package\process multiple locations\Foreach Loop Container\merge`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec [dbo].[spMergeUsersMultipleLocs] 
```

### truncate

**Path:** `Package\process multiple locations\Foreach Loop Container\truncate`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
truncate table [ERP].[UserLoadtoD365multipleLocationsStage]
```

### Truncate Stage

**Path:** `Package\user create seq\User Create Stage\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [ERP].[UserLoadtoD365]
TRUNCATE TABLE [ERP].[UserWHSELoadtoD365]
```

### Truncate Stage

**Path:** `Package\user create seq\User Deactivate Stage 1 1\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [ERP].[UserDeactivateD365]
```

### Set ProcessStatus

**Path:** `Package\user create seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\ProcessStatus For Loop\Set ProcessStatus`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
With 
ProcStatus as 
	(
		select 
			case 
				when StatusResponse in ('Succeeded','PartiallySucceeded', 'Failed')
					then 1
				else 0
			end as ProcessStatus
		from wms.DynamicsPackageAPILog
		where BatchID= ?
	)
select 
	case 
		when ? < 52 --- designed to let the loop escape if still not finihed after 52 loops
			then count(*)
		else 1
	end as ProcessStatus
from ProcStatus
where ProcessStatus = 1
```

### Wait

**Path:** `Package\user create seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\ProcessStatus For Loop\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:30'
```

### Set BatchID - LoopCount

**Path:** `Package\user create seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\user create seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### Stage Company Entities

**Path:** `Package\user create seq\UserCreate File Generation and Move\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select Entity
from [ERP].[UserLoadtoD365]
--where SendData = 1
--and Entity in (2110, 2300, 3001)
group by Entity

```

### Set ProcessStatus

**Path:** `Package\user create seq\UserDeactivate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\ProcessStatus For Loop\Set ProcessStatus`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
With 
ProcStatus as 
 (
  select 
   case 
    when StatusResponse in ('Succeeded','PartiallySucceeded', 'Failed')
     then 1
    else 0
   end as ProcessStatus
  from wms.DynamicsPackageAPILog
  where BatchID= ?
 )
select 
 case 
  when ? < 5 --- designed to let the loop escape if still not finihed after 52 loops
   then count(*)
  else 1
 end as ProcessStatus
from ProcStatus
where ProcessStatus = 1
```

### Wait

**Path:** `Package\user create seq\UserDeactivate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\ProcessStatus For Loop\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:59'
```

### Set BatchID - LoopCount

**Path:** `Package\user create seq\UserDeactivate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\user create seq\UserDeactivate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### Stage Company Entities

**Path:** `Package\user create seq\UserDeactivate File Generation and Move\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select Entity
from [ERP].[UserDeactivateD365]
--where SendData = 1
--and Entity in (2110, 2300, 3001)
group by Entity
```

### set isExported

**Path:** `Package\user create seq\set exported flag\set isExported`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update [ERP].[UserLoadtoD365multipleLocations] set isExported = 1 
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| get userID |  | OLEDBSource | password reset URL | IntegrationStaging | SqlCommand |
| OLE DB Source |  | OLEDBSource | Stage User Data | IntegrationStaging | SqlCommand |
| Flat File Source |  | FlatFileSource | Data Flow Task | MultipleLocationFile |  |
| OLE DB Source |  | OLEDBSource | Stage User Data | papamart.dw | SqlCommand |
| OLE DB Source |  | OLEDBSource | Stage User_WHse Data | papamart.dw | SqlCommand |
| OLE DB Source |  | OLEDBSource | Stage User Data | papamart.dw | SqlCommand |
| dynUserAssignWHSE |  | OLEDBSource | DataFlow CSV Files | IntegrationStaging | SqlCommand |
| dynUserCreate |  | OLEDBSource | DataFlow CSV Files | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |
| dynUserDeactivate |  | OLEDBSource | DataFlow CSV File | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |

#### get userID — SqlCommand

```sql
select workerName, userID, userPassword, Company from [ERP].[UserLoadtoD365pwReset]
```

#### OLE DB Source — SqlCommand

```sql
select distinct USERID as 'userID', 'Retail Stores' as 'workerName' , USERID as 'pass',ENTITY as 'Company' from [ERP].[UserLoadtoD365] where USERID not in (select distinct WAREHOUSEMOBILEDEVICEUSERID from  [ERP].[UserLoadtoD365multipleLocations])
```

#### OLE DB Source — SqlCommand

```sql
with
wmsEntity
as
(
select cast(OperationalSiteID as varchar) as OperationalSiteID, Entity from [stl-ssis-p-01].IntegrationStaging.ERP.WarehouseMaster 
where WarehouseID not like '%[^0-9]%' and WarehouseID not in ('8010','10') and WarehouseID not like '9%'
union 
select '1068A'  as OperationalSiteID, '1100' as Entity 
)
select distinct 
	d.EmployeeID as [USERID]					
	,0 as [ADJUSTMENTQUANTITYLIMIT]
    ,0 as [COUNTINGAPPROVALPERCENTAGELIMIT]
    ,0 as [COUNTINGAPPROVALQUANTITYLIMIT]
    ,0 as [COUNTINGAPPROVALVALUELIMIT]
	,'Retail Stores' as [DEFAULTMOBILEDEVICEMENUITEMNAME]    
	,e.EecLocation as [DEFAULTWAREHOUSEID]
	,'No' as [ISAUTOMATEDWAREHOUSEWORKUSER]
	,'No' as [ISCOUNTINGSUPERVISOR]
	,'No' as [ISINACTIVE]
	,'No' as [ISINVENTORYMOVEMENTWITHASSOCIATEDWORKALLOWED]
	,'No' as [ISMANUALITEMREALLOCATIONALLOWED]
	,'No' as [ISSALESORDEROVERPICKINGALLOWED]
	,'No' as [ISTRANSFERORDEROVERPICKINGALLOWED]
	,'No' as [ISWAREHOUSEPICKLOCATIONOVERRIDEALLOWED]
	,'No' as [ISWAREHOUSEPUTLOCATIONOVERRIDEALLOWED]
	,d.FirstName + ' ' +  d.LastName as [USERNAME]											
    ,'PSNNUM000003668' as [WAREHOUSEWORKERPERSONNELNUMBER]
    ,w.Entity as [ENTITY]												
from [coredb01].[AIMSConfig].[dbo].[DataLoaderStaging] d
join papamart.DW.dbo.UHCMemp e on d.EmployeeID = e.EepEEID
join wmsEntity w on e.EecLocation = w.OperationalSiteID
--where cast(d.UpdatedTimeStamp as date) >= cast(getdate()-1 as date)
where 1=1
--and isnumeric(e.EecLocation) = 1
--and datediff(dd, d.UpdatedTimeStamp, getdate()) <= 0
and datediff(hh, d.UpdatedTimeStamp, getdate()) <= 23
--AND (e.EecOrgLvl1Description = 'Store' and e.JbcJobCode not like '%BB%')
--and e.EecOrgLvl1Description = 'Store'
and e.EecEmplStatus <> 'Terminated'
and d.ProvisioningEvent in ('H','P','R','RN','C') 
AND d.Title in 
('Assistant Workshop Manager','Assistant Workshop Manager Temp',
'Assistant Workshop Mgr CN','Assistant Workshop Mgr US','Associate Workshop Mgr','Chief Workshop Manager','Chief Workshop Manager - Canada','Chief Workshop Manager - Canada',
'Chief Workshop Manager - USA','Chief Workshop Manager Temp','Chief Workshop Manager Temp- Canada','Dual Chief Workshop Manager - Canada','Dual Chief Workshop Manager - US',
'Dual Site Chief Workshop Manager','General Manager','General Workhsop Manager','General Workshop Manager','IrelandAssistant Workshop Manager20','IrelandAssistant Workshop Manager30',
'IrelandChief Workshop Manager35','IrelandChief Workshop Manager35','IrelandChief Workshop Manager4','IrelandChief Workshop Manager40','IrelandSales Lead Hourly12','IrelandSales Lead Hourly20','IrelandSales Lead Hourly4',
'Sales Lead','Sales Lead - Canada','Sales Lead - US','Sales Lead Hourly','Sales Lead Temp - Canada','Sales Lead Temp Role - US','Sales Lead(Annual Salary)','Sales Lead(Hourly)',
'UKAssistant Workshop Manager20','UKAssistant Workshop Manager25','UKAssistant Workshop Manager30','UKAssistant Workshop Manager35','UKAssistant Workshop Manager40','UKChief Workshop Manager35',
'UKChief Workshop Manager40','UKDual Site Chief Workshop Manager35','UKDual Site Chief Workshop Manager40','UKSales Lead Hourly12','UKSales Lead Hourly20','UKSales Lead Hourly4')


union


select --distinct 
	u.WAREHOUSEMOBILEDEVICEUSERID as [USERID]					
	,0 as [ADJUSTMENTQUANTITYLIMIT]
    ,0 as [COUNTINGAPPROVALPERCENTAGELIMIT]
    ,0 as [COUNTINGAPPROVALQUANTITYLIMIT]
    ,0 as [COUNTINGAPPROVALVALUELIMIT]
	,'Retail Stores' as [DEFAULTMOBILEDEVICEMENUITEMNAME]    
	,left(min(u.WAREHOUSEID),4) as [DEFAULTWAREHOUSEID]
	,'No' as [ISAUTOMATEDWAREHOUSEWORKUSER]
	,'No' as [ISCOUNTINGSUPERVISOR]
	,'No' as [ISINACTIVE]
	,'No' as [ISINVENTORYMOVEMENTWITHASSOCIATEDWORKALLOWED]
	,'No' as [ISMANUALITEMREALLOCATIONALLOWED]
	,'No' as [ISSALESORDEROVERPICKINGALLOWED]
	,'No' as [ISTRANSFERORDEROVERPICKINGALLOWED]
	,'No' as [ISWAREHOUSEPICKLOCATIONOVERRIDEALLOWED]
	,'No' as [ISWAREHOUSEPUTLOCATIONOVERRIDEALLOWED]
	,Cast(coalesce (nullif (e.eepNamePreferred, ''), e.EepNameFirst) as NVarChar)  + ' ' +  Cast(e.EepNameLast as Nvarchar) as [USERNAME]	
    ,'PSNNUM000003668' as [WAREHOUSEWORKERPERSONNELNUMBER]
	 ,u.ENTITY  as [ENTITY]		
from [stl-ssis-p-01].IntegrationStaging.[ERP].[UserLoadtoD365multipleLocations] u
join papamart.DW.dbo.UHCMemp e on u.WAREHOUSEMOBILEDEVICEUSERID  = e.EepEEID
join [stl-ssis-p-01].IntegrationStaging.ERP.WarehouseMaster wm on wm.WarehouseId = left(u.WAREHOUSEID,4)
where 1=1
and isnull(u.isDeactivated,0) = 0 and isnull(u.isExported, 0) = 0
and wm.AreAdvancedWarehouseManagementProcessesEnabled = 'Yes'
group by u.WAREHOUSEMOBILEDEVICEUSERID, e.eepNamePreferred, e.EepNameFirst, e.EepNameLast , u.ENTITY
```

#### OLE DB Source — SqlCommand

```sql
with
wmsEntity
as
(
select cast(OperationalSiteID as varchar) as OperationalSiteID, Entity from [stl-ssis-p-01].IntegrationStaging.ERP.WarehouseMaster 
where WarehouseID not like '%[^0-9]%' and WarehouseID not in ('8010','10') and WarehouseID not like '9%' 
union 
select '1068A'  as OperationalSiteID, '1100' as Entity
)
select distinct 
	d.EmployeeID as [WAREHOUSEMOBILEDEVICEUSERID]					
	,e.EecLocation as [WAREHOUSEID]
                  ,w.Entity as [ENTITY]						
from [coredb01].[AIMSConfig].[dbo].[DataLoaderStaging] d
join papamart.DW.dbo.UHCMemp e on d.EmployeeID = e.EepEEID
join wmsEntity w on e.EecLocation = w.OperationalSiteID
--where cast(d.UpdatedTimeStamp as date) >= cast(getdate()-1 as date)

where 1=1
--and isnumeric(e.EecLocation) = 1
--and datediff(dd, d.UpdatedTimeStamp, getdate()) = 0
and datediff(hh, d.UpdatedTimeStamp, getdate()) <= 23
--AND (e.EecOrgLvl1Description = 'Store' and e.JbcJobCode not like '%BB%')
--and e.EecOrgLvl1Description = 'Store'
and e.EecEmplStatus <> 'Terminated'
and d.ProvisioningEvent in ('H','P','R','RN','C') 
AND d.Title in 
('Assistant Workshop Manager','Assistant Workshop Manager Temp',
'Assistant Workshop Mgr CN','Assistant Workshop Mgr US','Associate Workshop Mgr','Chief Workshop Manager','Chief Workshop Manager - Canada','Chief Workshop Manager - Canada',
'Chief Workshop Manager - USA','Chief Workshop Manager Temp','Chief Workshop Manager Temp- Canada','Dual Chief Workshop Manager - Canada','Dual Chief Workshop Manager - US',
'Dual Site Chief Workshop Manager','General Manager','General Workhsop Manager','General Workshop Manager','IrelandAssistant Workshop Manager20','IrelandAssistant Workshop Manager30',
'IrelandChief Workshop Manager35','IrelandChief Workshop Manager35','IrelandChief Workshop Manager4','IrelandChief Workshop Manager40','IrelandSales Lead Hourly12','IrelandSales Lead Hourly20','IrelandSales Lead Hourly4',
'Sales Lead','Sales Lead - Canada','Sales Lead - US','Sales Lead Hourly','Sales Lead Temp - Canada','Sales Lead Temp Role - US','Sales Lead(Annual Salary)','Sales Lead(Hourly)',
'UKAssistant Workshop Manager20','UKAssistant Workshop Manager25','UKAssistant Workshop Manager30','UKAssistant Workshop Manager35','UKAssistant Workshop Manager40','UKChief Workshop Manager35',
'UKChief Workshop Manager40','UKDual Site Chief Workshop Manager35','UKDual Site Chief Workshop Manager40','UKSales Lead Hourly12','UKSales Lead Hourly20','UKSales Lead Hourly4')

union 



select distinct 
	u.WAREHOUSEMOBILEDEVICEUSERID as [USERID]					
	,left(u.WAREHOUSEID,4) as [DEFAULTWAREHOUSEID]
	 ,u.ENTITY  as [ENTITY]		
from [stl-ssis-p-01].IntegrationStaging.[ERP].[UserLoadtoD365multipleLocations] u
join [stl-ssis-p-01].IntegrationStaging.ERP.WarehouseMaster wm on wm.WarehouseId = left(u.WAREHOUSEID,4)
where 1=1
and isnull(u.isDeactivated,0) = 0 and isnull(u.isExported, 0) = 0
and wm.AreAdvancedWarehouseManagementProcessesEnabled = 'Yes'
```

#### OLE DB Source — SqlCommand

```sql
with
wmsEntity
as
(
select OperationalSiteID, Entity from [stl-ssis-p-01].IntegrationStaging.ERP.WarehouseMaster 
where WarehouseID not like '%[^0-9]%' and WarehouseID not in ('8010','10') and WarehouseID not like '9%' 
)
select distinct 
	d.EmployeeID as [USERID]	
                 ,'PSNNUM000003668' as [WAREHOUSEWORKERPERSONNELNUMBER]	
                 ,'Yes' as [ISINACTIVE]			
                 ,w.Entity as [ENTITY]												
from [coredb01].[AIMSConfig].[dbo].[DataLoaderStaging] d
join papamart.DW.dbo.UHCMemp e on d.EmployeeID = e.EepEEID
join wmsEntity w on e.EecLocation = w.OperationalSiteID
--where cast(d.UpdatedTimeStamp as date) >= cast(getdate()-1 as date)
where 1=1
and d.EmployeeID = '0028417'
and isnumeric(e.EecLocation) = 1
and datediff(dd, d.UpdatedTimeStamp, getdate()) = 0
and datediff(hh, d.UpdatedTimeStamp, getdate()) <= 3
--AND (e.EecOrgLvl1Description = 'Store' and e.JbcJobCode not like '%BB%')
--and e.EecOrgLvl1Description = 'Store'
and e.EecEmplStatus <> 'Terminated'
and 
(
(d.ProvisioningEvent in ('P','RN','C') and d.Title in ('Bear Builder CN','UKBear Builder4','IrelandBear Builder4','Bear Builder US','Bear Builder','Bearbuilder'))
or 
(d.ProvisioningEvent = 'T' and d.Title in ('UKChief Workshop Manager40','UKAssistant Workshop Manager25','Dual Site Chief Workshop Manager','Assistant Workshop Mgr CN',
'IrelandSales Lead Hourly4','IrelandChief Workshop Manager4''IrelandChief Workshop Manager40','Sales Lead(Annual Salary)','IrelandSales Lead Hourly20','Assistant Workshop Manager',
'UKChief Workshop Manager35','Sales Lead - Canada','IrelandSales Lead Hourly12','Sales Lead - US','UKSales Lead Hourly12','IrelandAssistant Workshop Mana','Sales Lead','UKSales Lead Hourly20',
'Sales Lead Temp Role - US','UKAssistant Workshop Manager30','Assistant Workshop Mgr US','Chief Workshop Manager','Sales Lead Hourly','Chief Workshop Manager - Canad','UKDual Site Chief Workshop Man',
'IrelandAssistant Workshop Manager30','Sales Lead(Hourly)','UKDual Site Chief Workshop Manager40','UKDual Site Chief Workshop Manager35','UKSales Lead Hourly4','UKAssistant Workshop Manager40',
'Chief Workshop Manager - USA','Chief Workshop Manager - Canada','UKAssistant Workshop Manager35','UKAssistant Workshop Manager20'))
)
union
select 'test' as [USERID],'PSNNUM000003668' as [WAREHOUSEWORKERPERSONNELNUMBER]	,'Yes' as [ISINACTIVE],'1100' as [ENTITY]
```

#### dynUserAssignWHSE — SqlCommand

```sql
SELECT [WAREHOUSEID]
      ,[WAREHOUSEMOBILEDEVICEUSERID]
  FROM [ERP].[UserWHSELoadtoD365]
WHERE [ENTITY] = ?
```

#### dynUserCreate — SqlCommand

```sql
SELECT [USERID]
      ,[ADJUSTMENTQUANTITYLIMIT]
      ,[COUNTINGAPPROVALPERCENTAGELIMIT]
      ,[COUNTINGAPPROVALQUANTITYLIMIT]
      ,[COUNTINGAPPROVALVALUELIMIT]
      ,[DEFAULTMOBILEDEVICEMENUITEMNAME]
      ,[DEFAULTWAREHOUSEID]
      ,[ISAUTOMATEDWAREHOUSEWORKUSER]
      ,[ISCOUNTINGSUPERVISOR]
      ,[ISINACTIVE]
      ,[ISINVENTORYMOVEMENTWITHASSOCIATEDWORKALLOWED]
      ,[ISMANUALITEMREALLOCATIONALLOWED]
      ,[ISSALESORDEROVERPICKINGALLOWED]
      ,[ISTRANSFERORDEROVERPICKINGALLOWED]
      ,[ISWAREHOUSEPICKLOCATIONOVERRIDEALLOWED]
      ,[ISWAREHOUSEPUTLOCATIONOVERRIDEALLOWED]
      ,[USERNAME]
      ,[WAREHOUSEWORKERPERSONNELNUMBER]
      ,[ENTITY]
  FROM [ERP].[UserLoadtoD365] 
WHERE [ENTITY] = ?
```

#### Trigger Columns — SqlCommand

```sql
select 'do nothing' as DoNothing
```

#### dynUserDeactivate — SqlCommand

```sql
SELECT [USERID]
      ,[WAREHOUSEWORKERPERSONNELNUMBER]
      ,[ISINACTIVE]
      ,[ENTITY]
  FROM [ERP].[UserDeactivateD365]
WHERE [ENTITY] = ?
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| DynamicsAPILog |  | OLEDBDestination | password reset URL | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Stage User Data | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Stage User Data | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Stage User_WHse Data | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Stage User Data | IntegrationStaging |  |
| Flat File Destination |  | FlatFileDestination | DataFlow CSV Files | UserCreateCSV |  |
| Flat File Destination 1 |  | FlatFileDestination | DataFlow CSV Files | UserWHSCreateCSV |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| Flat File Destination |  | FlatFileDestination | DataFlow CSV File | UserDeactivateCSV |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
