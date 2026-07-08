# SSIS Package: ERP_ShipmentInvoiceToD365

**Project:** ERP_ShipmentInvoiceToD365  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| GetBlobUrl | HTTP (KingswaySoft) |  |  |  |
| GetStatus | HTTP (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| PostTriggerImport | HTTP (KingswaySoft) |  |  |  |
| SMTP_EMAIL | SMTP |  |  |  |
| SOCreateXML | FLATFILE |  |  |  |
| SQL_LOG | OLEDB | stl-ssis-p-01 | msdb | Data Source=stl-ssis-p-01; Initial Catalog=msdb; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| TOCreateXML | FLATFILE |  |  |  |
| me_01 | OLEDB | bedrockdb02 | me_01 | Data Source=bedrockdb02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| ERP_ShipmentInvoiceToD365 | Package |
| Manual Testing Tools | SEQUENCE |
| Get Summary Status - MANUALLY BY BATCH ID | Pipeline |
| Temp for Testing - Import 3PL Files | ExecuteSQLTask |
| SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status | SEQUENCE |
| File Generation and Move - SO | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| DataFlow XML File | Pipeline |
| Foreach - Create Blob - Upload - Trigger - Get Status | FOREACHLOOP |
| Foreach Loop Container | FOREACHLOOP |
| Archive Files | FileSystemTask |
| azCopy to Blob | ExecuteProcess |
| ProcessStatus For Loop | FORLOOP |
| Get Summary Status | Pipeline |
| Set ProcessStatus | ExecuteSQLTask |
| Wait 30 Seconds | ExecuteSQLTask |
| Set BatchID - LoopCount | ExecuteSQLTask |
| Set RowsCount | ExecuteSQLTask |
| Stage Blob URL | Pipeline |
| Trigger Import | Pipeline |
| Foreach Loop - Copy PackageTemplate Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| SetTransmitted | ExecuteSQLTask |
| Zip File | ExecuteProcess |
| Sales Order UDA | ExecuteSQLTask |
| Stage Company Entities | ExecuteSQLTask |
| File Generation and Move - TO | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| DataFlow XML File | Pipeline |
| Foreach - Create Blob - Upload - Trigger - Get Status | FOREACHLOOP |
| Foreach Loop Container | FOREACHLOOP |
| Archive Files | FileSystemTask |
| azCopy to Blob | ExecuteProcess |
| ProcessStatus For Loop | FORLOOP |
| Get Summary Status | Pipeline |
| Set ProcessStatus | ExecuteSQLTask |
| Wait 30 Seconds | ExecuteSQLTask |
| Set BatchID - LoopCount | ExecuteSQLTask |
| Set RowsCount | ExecuteSQLTask |
| Stage Blob URL | Pipeline |
| Trigger Import | Pipeline |
| Foreach Loop - Copy PackageTemplate Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| SetTransmitted | ExecuteSQLTask |
| Zip File | ExecuteProcess |
| Stage Company Entities | ExecuteSQLTask |
| Stage Shipment Data | SEQUENCE |
| Merge Shipments | ExecuteSQLTask |
| PreStage Shipments | SEQUENCE |
| PreStage Shipments CN | Pipeline |
| Prestage Shipments UK | Pipeline |
| PreStage Shipments WC | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| Stage Shipments | Pipeline |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- Manual Testing Tools [SEQUENCE]
  - Get Summary Status - MANUALLY BY BATCH ID [Pipeline]
  - Temp for Testing - Import 3PL Files [ExecuteSQLTask]
- SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status [SEQUENCE]
  - File Generation and Move - SO [SEQUENCE]
    - Foreach Loop - Per Entity [FOREACHLOOP]
      - DataFlow XML File [Pipeline]
      - Foreach - Create Blob - Upload - Trigger - Get Status [FOREACHLOOP]
        - Foreach Loop Container [FOREACHLOOP]
          - Archive Files [FileSystemTask]
          - azCopy to Blob [ExecuteProcess]
        - ProcessStatus For Loop [FORLOOP]
          - Get Summary Status [Pipeline]
          - Set ProcessStatus [ExecuteSQLTask]
          - Wait 30 Seconds [ExecuteSQLTask]
        - Set BatchID - LoopCount [ExecuteSQLTask]
        - Set RowsCount [ExecuteSQLTask]
        - Stage Blob URL [Pipeline]
        - Trigger Import [Pipeline]
      - Foreach Loop - Copy PackageTemplate Files [FOREACHLOOP]
        - Copy Manifest & Header [FileSystemTask]
      - SetTransmitted [ExecuteSQLTask]
      - Zip File [ExecuteProcess]
    - Sales Order UDA [ExecuteSQLTask]
    - Stage Company Entities [ExecuteSQLTask]
  - File Generation and Move - TO [SEQUENCE]
    - Foreach Loop - Per Entity [FOREACHLOOP]
      - DataFlow XML File [Pipeline]
      - Foreach - Create Blob - Upload - Trigger - Get Status [FOREACHLOOP]
        - Foreach Loop Container [FOREACHLOOP]
          - Archive Files [FileSystemTask]
          - azCopy to Blob [ExecuteProcess]
        - ProcessStatus For Loop [FORLOOP]
          - Get Summary Status [Pipeline]
          - Set ProcessStatus [ExecuteSQLTask]
          - Wait 30 Seconds [ExecuteSQLTask]
        - Set BatchID - LoopCount [ExecuteSQLTask]
        - Set RowsCount [ExecuteSQLTask]
        - Stage Blob URL [Pipeline]
        - Trigger Import [Pipeline]
      - Foreach Loop - Copy PackageTemplate Files [FOREACHLOOP]
        - Copy Manifest & Header [FileSystemTask]
      - SetTransmitted [ExecuteSQLTask]
      - Zip File [ExecuteProcess]
    - Stage Company Entities [ExecuteSQLTask]
- Stage Shipment Data [SEQUENCE]
  - Merge Shipments [ExecuteSQLTask]
  - PreStage Shipments [SEQUENCE]
    - PreStage Shipments CN [Pipeline]
    - PreStage Shipments WC [Pipeline]
    - Prestage Shipments UK [Pipeline]
    - Truncate Stage [ExecuteSQLTask]
  - Stage Shipments [Pipeline]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Manual_Testing_Tools["Manual Testing Tools"]
    n_Package_Manual_Testing_Tools_Get_Summary_Status___MANUALLY_BY_BATCH_ID["Get Summary Status - MANUALLY BY BATCH ID"]
    n_Package_Manual_Testing_Tools_Temp_for_Testing___Import_3PL_Files["Temp for Testing - Import 3PL Files"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status["SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO["File Generation and Move - SO"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_DataFlow_XML_File["DataFlow XML File"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status["Foreach - Create Blob - Upload - Trigger - Get Status"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Wait_30_Seconds["Wait 30 Seconds"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_RowsCount["Set RowsCount"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Stage_Blob_URL["Stage Blob URL"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Trigger_Import["Trigger Import"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files["Foreach Loop - Copy PackageTemplate Files"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_SetTransmitted["SetTransmitted"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Zip_File["Zip File"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Sales_Order_UDA["Sales Order UDA"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Stage_Company_Entities["Stage Company Entities"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO["File Generation and Move - TO"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_DataFlow_XML_File["DataFlow XML File"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status["Foreach - Create Blob - Upload - Trigger - Get Status"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Wait_30_Seconds["Wait 30 Seconds"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_RowsCount["Set RowsCount"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Stage_Blob_URL["Stage Blob URL"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Trigger_Import["Trigger Import"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files["Foreach Loop - Copy PackageTemplate Files"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_SetTransmitted["SetTransmitted"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Zip_File["Zip File"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Stage_Company_Entities["Stage Company Entities"]
    n_Package_Stage_Shipment_Data["Stage Shipment Data"]
    n_Package_Stage_Shipment_Data_Merge_Shipments["Merge Shipments"]
    n_Package_Stage_Shipment_Data_PreStage_Shipments["PreStage Shipments"]
    n_Package_Stage_Shipment_Data_PreStage_Shipments_PreStage_Shipments_CN["PreStage Shipments CN"]
    n_Package_Stage_Shipment_Data_PreStage_Shipments_Prestage_Shipments_UK["Prestage Shipments UK"]
    n_Package_Stage_Shipment_Data_PreStage_Shipments_PreStage_Shipments_WC["PreStage Shipments WC"]
    n_Package_Stage_Shipment_Data_PreStage_Shipments_Truncate_Stage["Truncate Stage"]
    n_Package_Stage_Shipment_Data_Stage_Shipments["Stage Shipments"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_Archive_Files
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Wait_30_Seconds --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Stage_Blob_URL --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_RowsCount
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Trigger_Import --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Trigger_Import
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_BatchID___LoopCount --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Stage_Blob_URL
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_RowsCount --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_DataFlow_XML_File --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_SetTransmitted
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Zip_File
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Zip_File --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_SetTransmitted --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Sales_Order_UDA
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Stage_Company_Entities --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO_Foreach_Loop___Per_Entity
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container_Archive_Files
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Wait_30_Seconds --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Stage_Blob_URL --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_RowsCount
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Trigger_Import --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_ProcessStatus_For_Loop
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Trigger_Import
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_BatchID___LoopCount --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Stage_Blob_URL
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Set_RowsCount --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status_Foreach_Loop_Container
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_DataFlow_XML_File --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_SetTransmitted
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Zip_File
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Zip_File --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach___Create_Blob___Upload___Trigger___Get_Status
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_SetTransmitted --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_PackageTemplate_Files
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Stage_Company_Entities --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO_Foreach_Loop___Per_Entity
    n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___TO --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status_File_Generation_and_Move___SO
    n_Package_Stage_Shipment_Data_PreStage_Shipments_Truncate_Stage --> n_Package_Stage_Shipment_Data_PreStage_Shipments_PreStage_Shipments_WC
    n_Package_Stage_Shipment_Data_PreStage_Shipments_PreStage_Shipments_WC --> n_Package_Stage_Shipment_Data_PreStage_Shipments_Prestage_Shipments_UK
    n_Package_Stage_Shipment_Data_PreStage_Shipments_Prestage_Shipments_UK --> n_Package_Stage_Shipment_Data_PreStage_Shipments_PreStage_Shipments_CN
    n_Package_Stage_Shipment_Data_Stage_Shipments --> n_Package_Stage_Shipment_Data_Merge_Shipments
    n_Package_Stage_Shipment_Data_PreStage_Shipments --> n_Package_Stage_Shipment_Data_Stage_Shipments
    n_Package_Stage_Shipment_Data --> n_Package_SEQ___Create_Blob___Upload_to_Blob___Trigger_Import___Get_Status
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | ArchiveFolder | Yes |
| User | ArchiveFolder_SO | Yes |
| User | AzCopytoBlobCommand | Yes |
| User | AzCopytoBlobCommand_SO | Yes |
| User | BatchID | No |
| User | BlobURL | No |
| User | BlobURLRecordSet | No |
| User | CompanyEntities | No |
| User | DataEntityName_SO | No |
| User | DataEntityName_TO | No |
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
| User | ProcessStatus | No |
| User | RowsCount | No |
| User | RunControlFlag | No |
| User | SQLItemLoadViewByEntity | Yes |
| User | SQL_GetBlobURLCommand | Yes |
| User | SQL_GetSummaryStatus | Yes |
| User | SQL_TriggerImport | Yes |
| User | SalesOrderInvoiceArchiveFolder | Yes |
| User | SalesOrderInvoiceD365DropFolder | Yes |
| User | SalesOrderInvoiceFile | No |
| User | SalesOrderInvoiceStage | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | TransferInvoiceArchiveFolder | Yes |
| User | TransferInvoiceD365DropFolder | Yes |
| User | TransferInvoiceFile | No |
| User | TransferInvoiceStage | Yes |
| User | ZipCommand | Yes |
| User | ZipCommand_SO | Yes |
| User | ZipDest | Yes |
| User | ZipDest_SO | Yes |
| User | ZipSource | Yes |

### Expression-bound variable values

#### User::ArchiveFolder

**Expression:**

```sql
@[$Package::WMS_TOCreateFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\TransferOrder\Archive\
```

#### User::ArchiveFolder_SO

**Expression:**

```sql
@[$Package::WMS_SOCreateFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\SalesOrder\Archive\
```

#### User::AzCopytoBlobCommand

**Expression:**

```sql
"cp \"" +  @[User::ZipDest] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\TransferOrder\ShipmentCreate3PL3001.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
```

#### User::AzCopytoBlobCommand_SO

**Expression:**

```sql
"cp \"" +  @[User::ZipDest_SO] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\SalesOrder\ShipmentCreate3PL3001.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
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
20228185740657
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
8/1/2022
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
2022-08-01
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
8/1/2022
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
2022-08-01
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
    "uniqueFileName":"5ECF043F-9E41-46F7-9FE9-0634BCE2C644"
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
    "executionId":"5ECF043F-9E41-46F7-9FE9-0634BCE2C644"
}

```

#### User::PackageAPIHeaderAndManifestPath

**Expression:**

```sql
@[$Package::WMS_PackageAPI_StaticPackageFilesPath]
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\
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
where Entity = '3001'
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
    "uniqueFileName":"5ECF043F-9E41-46F7-9FE9-0634BCE2C644"
}
' as varchar(100)) as Command, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as BatchID, getdate() as InsertDate 
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
    "executionId":"5ECF043F-9E41-46F7-9FE9-0634BCE2C644"
}
' as varchar(100)) as Command, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as BatchID, getdate() as InsertDate 
```

#### User::SQL_TriggerImport

**Expression:**

```sql
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[$Package::WMS_TOCreateBlobDefinitionGroupID] + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as executionId, 'TOShipmentImport3001' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '3001' as legalEntityId
```

#### User::SalesOrderInvoiceArchiveFolder

**Expression:**

```sql
@[User::SalesOrderInvoiceStage] + "Archive"
```

**Evaluated value:**

```sql
\\STL-SSIS-P-01\IntegrationStaging\ERP\PROD\Outbound\D365\ShipmentInvoices\SalesOrderInvoice\3001\Archive
```

#### User::SalesOrderInvoiceD365DropFolder

**Expression:**

```sql
@[$Package::ERP_ShipmentInvoice_SalesOrder_DropFolder] +  @[User::Entity] + "\\Inbound\\"
```

**Evaluated value:**

```sql
\\stl-dynsnc-t-02\BABWIntegrations\WMS_SO\test3\2100\Inbound\
```

#### User::SalesOrderInvoiceStage

**Expression:**

```sql
"\\\\" +  @[$Package::IntegrationStaging_ServerName] + "\\IntegrationStaging\\ERP\\" +  @[$Package::ERP_ShipmentInvoicePackageEnvironment] + "\\Outbound\\D365\\ShipmentInvoices\\SalesOrderInvoice\\" +  @[User::Entity] + "\\"
```

**Evaluated value:**

```sql
\\STL-SSIS-P-01\IntegrationStaging\ERP\PROD\Outbound\D365\ShipmentInvoices\SalesOrderInvoice\3001\
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
7/31/2022
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
2022-07-31
```

#### User::TransferInvoiceArchiveFolder

**Expression:**

```sql
@[User::TransferInvoiceStage] + "Archive"
```

**Evaluated value:**

```sql
\\STL-SSIS-P-01\IntegrationStaging\ERP\PROD\Outbound\D365\ShipmentInvoices\TransferInvoice\3001\Archive
```

#### User::TransferInvoiceD365DropFolder

**Expression:**

```sql
@[$Package::ERP_ShipmentInvoice_Transfer_DropFolder] +  @[User::Entity]
```

**Evaluated value:**

```sql
\\stl-dynsnc-t-02\BABWIntegrations\WMSTransferOrders\Inbound\test3\2100
```

#### User::TransferInvoiceStage

**Expression:**

```sql
"\\\\" + @[$Package::IntegrationStaging_ServerName] + "\\IntegrationStaging\\ERP\\" +  @[$Package::ERP_ShipmentInvoicePackageEnvironment] + "\\Outbound\\D365\\ShipmentInvoices\\TransferInvoice\\"+  @[User::Entity] + "\\"
```

**Evaluated value:**

```sql
\\STL-SSIS-P-01\IntegrationStaging\ERP\PROD\Outbound\D365\ShipmentInvoices\TransferInvoice\3001\
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\TransferOrder\ShipmentCreate3PL3001.zip"  "*.xml" -sdel
```

#### User::ZipCommand_SO

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest_SO]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\SalesOrder\ShipmentCreate3PL3001.zip"  "*.xml" -sdel
```

#### User::ZipDest

**Expression:**

```sql
@[$Package::WMS_TOCreateFileStageLocation]  + "ShipmentCreate3PL" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\TransferOrder\ShipmentCreate3PL3001.zip
```

#### User::ZipDest_SO

**Expression:**

```sql
@[$Package::WMS_SOCreateFileStageLocation]  + "ShipmentCreate3PL" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\ShipmentInvoice\SalesOrder\ShipmentCreate3PL3001.zip
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

## Execute SQL Tasks

### Temp for Testing - Import 3PL Files

**Path:** `Package\Manual Testing Tools\Temp for Testing - Import 3PL Files`  
**Connection:** me_01 (bedrockdb02/me_01)  

```sql
exec spMerchandisingSelectUKStoreShipments
exec spMerchandisingProcessCNShipmentsAllocAdj
exec spMerchandisingProcessWCShipmentsAllocAdj
```

### Set ProcessStatus

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - SO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\ProcessStatus For Loop\Set ProcessStatus`  
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
  when ? < 20 --- designed to let the loop escape if still not finihed after 20 loops
   then count(*)
  else 1
 end as ProcessStatus
from ProcStatus
where ProcessStatus = 1
```

### Wait 30 Seconds

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - SO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\ProcessStatus For Loop\Wait 30 Seconds`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:30'
```

### Set BatchID - LoopCount

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - SO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - SO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### SetTransmitted

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - SO\Foreach Loop - Per Entity\SetTransmitted`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update ERP.ShipmentInvoice 
set Transmitted = 1
where 1=1
and (left(OrderRef,2) = 'SO' or Entity=1200)
and Transmitted = 0
and Entity=?
```

### Sales Order UDA

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - SO\Sales Order UDA`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec ERP.spOutputSalesOrderUDA @BatchID = '{7DF8CE47-C9DD-4AEE-AE09-A31CDD4A493F}', @FileLocation = '\\pipeapp01\Company01\Text File to IM Import Tables - Import UDAs\'
```

**Property expression (runtime override):**

```sql
"exec ERP.spOutputSalesOrderUDA @BatchID = '" +  @[System::ExecutionInstanceGUID] + "', @FileLocation = '" +  @[$Package::ERP_ShipmentInvoice_SalesOrderUDAPath] + "'"
```

### Stage Company Entities

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - SO\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select Entity
from ERP.ShipmentInvoice with (nolock)
where 1=1
and Transmitted = 0
and (left(OrderRef,2) = 'SO' or Entity=1200)
group by Entity


```

### Set ProcessStatus

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - TO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\ProcessStatus For Loop\Set ProcessStatus`  
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
  when ? < 20 --- designed to let the loop escape if still not finihed after 20 loops
   then count(*)
  else 1
 end as ProcessStatus
from ProcStatus
where ProcessStatus = 1
```

### Wait 30 Seconds

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - TO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\ProcessStatus For Loop\Wait 30 Seconds`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:30'
```

### Set BatchID - LoopCount

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - TO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - TO\Foreach Loop - Per Entity\Foreach - Create Blob - Upload - Trigger - Get Status\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### SetTransmitted

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - TO\Foreach Loop - Per Entity\SetTransmitted`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update ERP.ShipmentInvoice 
set Transmitted = 1
where 1=1
and left(OrderRef,2) = 'TO'
and Transmitted = 0
and Entity=?
```

### Stage Company Entities

**Path:** `Package\SEQ - Create Blob - Upload to Blob - Trigger Import - Get Status\File Generation and Move - TO\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select Entity
from ERP.ShipmentInvoice with (nolock)
where 1=1
and Transmitted = 0
and left(OrderRef,2) = 'TO'
group by Entity

```

### Merge Shipments

**Path:** `Package\Stage Shipment Data\Merge Shipments`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeShipmentInvoice
```

### Truncate Stage

**Path:** `Package\Stage Shipment Data\PreStage Shipments\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.ShipmentInvoicePreStage
TRUNCATE TABLE ERP.ShipmentInvoiceStage

```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| Start |  | OLEDBSource | Get Summary Status - MANUALLY BY BATCH ID | IntegrationStaging | SqlCommand |
| ShipmentInvoiceSO |  | OLEDBSource | DataFlow XML File | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |
| ShipmentInvoiceTO |  | OLEDBSource | DataFlow XML File | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |
| ERP_DynamicsShipmentStage_CN |  | OLEDBSource | PreStage Shipments CN | me_01 | SqlCommand |
| ERP_DynamicsShipmentStage_UK |  | OLEDBSource | Prestage Shipments UK | me_01 | SqlCommand |
| ERP_DynamicsShipmentStage_WC |  | OLEDBSource | PreStage Shipments WC | me_01 | SqlCommand |
| vwShipmentInvoiceStage |  | OLEDBSource | Stage Shipments | IntegrationStaging |  |

#### Start — SqlCommand

```sql
select cast('
{
    "executionId":"{0EB9EE54-8BA8-4ACE-AD81-89ED7BF71A82}"
}
' as varchar(100)) as Command, cast('{0EB9EE54-8BA8-4ACE-AD81-89ED7BF71A82}' as varchar(50)) as BatchID, getdate() as InsertDate
```

#### ShipmentInvoiceSO — SqlCommand

```sql
with 
ShippedOrders as
	(
		select 
			Entity,
			InventLocationID as FROMWAREHOUSE,
			OrderRef as SALESID,
			ShipDate as ORDERSHIPDATE
		from ERP.ShipmentInvoice with (nolock)
		where 1=1
		and Transmitted = 0
		and left(OrderRef,2) = 'SO'
		--and Entity<>1200 --previously had this commented out since 1200 was only for the 1100 po receipts to 1200 shipment... now we have 1200 receipts from china whse
		and Entity= ?
		group by 
			Entity,
			InventLocationID, 
			OrderRef,
			ShipDate
	),
ShippedData as
	(
		select 
			si.Entity,
			si.InventLocationID as FROMWAREHOUSE,
			si.ItemID as ITEMID,
			sum(cast(si.Qty as int)) as ShippedQty,
			si.OrderRef as SALESID
		from ERP.ShipmentInvoice si with (nolock)
		join ShippedOrders so 
			on si.Entity=so.Entity
			and si.InventLocationID=so.FROMWAREHOUSE
			and si.OrderRef=SALESID
			and cast(si.ShipDate as datetime)=so.ORDERSHIPDATE
		where 1=1
		and si.Transmitted = 0
		and left(si.OrderRef,2) = 'SO'
		group by 
			si.Entity,
			si.InventLocationID, 
			si.ItemID,
			si.OrderRef
	),
OrderData as
	(
		select 
			dh.Entity,
			dh.FROMWAREHOUSE,
			dd.ItemNumber as ITEM,
			sum(cast(dd.Quantity as int)) as SALESQTY,
			dd.OrderId as SALESID,
			dd.ORDERLINENUMBER as SALESORDERLINENUMBER,
			dh.CustAccount as CUSTOMERACCOUNT,
			dd.UOM as SALESUNIT
		from erp.DistributionHeader dh with (nolock)
		join erp.DistributionDetail dd with (nolock) 
			on dh.OrderID = dd.OrderID 
			and dh.PickListID = dd.PickListID 
			and dh.entity = dd.entity 
		where dh.OrderType='Sales'
		and dd.OrderLineNumber is not null --as of 2021/01/23
		and exists 
					(
						select sd.SALESID 
						from ShippedData sd 
						where sd.Entity=dh.Entity
						and sd.FromWarehouse=dh.FromWarehouse
						and sd.SALESID=dh.OrderID
						and sd.ItemID=dd.ItemNumber
					)	
		group by 
			dh.Entity,
			dh.FROMWAREHOUSE,
			dd.ItemNumber,
			dd.OrderID,
			dd.ORDERLINENUMBER,
			dh.CustAccount,
			dd.UOM
	)
select 
	o.CUSTOMERACCOUNT,
	convert(varchar, isnull(so.ORDERSHIPDATE, dateadd(dd, +7, getdate())),101) as DELIVERYDATE,
	o.FROMWAREHOUSE,	
	o.ITEM,	
	o.SALESID,	
	o.SALESORDERLINENUMBER,
	isnull(sd.ShippedQty,0) as SALESQTY,
	o.SALESUNIT
from OrderData o
join ShippedOrders so 
	on o.Entity=so.Entity
	and o.FROMWAREHOUSE=so.FROMWAREHOUSE
	and o.SALESID=so.SALESID
left join ShippedData sd 
	on o.Entity=sd.Entity
	and o.FROMWAREHOUSE=sd.FROMWAREHOUSE
	and o.SALESID=sd.SALESID
	and o.ITEM=sd.ITEMID
UNION
select 
	'CUST000026' as CUSTOMERACCOUNT,
	convert(varchar, isnull(ShipDate, dateadd(dd, +7, getdate())),101) as DELIVERYDATE,
	InventLocationId as FROMWAREHOUSE,	
	ItemID as ITEM,	
	concat('1100',OrderRef) as SALESID,	
	SalesOrderLineNumber as SALESORDERLINENUMBER,
	sum(qty) as SALESQTY,
	'EA' as SALESUNIT
from erp.ShipmentInvoice
where entity=?
and left(OrderRef,2)<>'SO' --these are the shipments for 1100 po receipts
and entity=1200 
and transmitted=0
group by 
	convert(varchar, isnull(ShipDate, dateadd(dd, +7, getdate())),101),
	InventLocationId,
	ItemID,
	concat('1100',OrderRef),
	SalesOrderLineNumber
```

#### Trigger Columns — SqlCommand

```sql
select 'do nothing' as DoNothing
```

#### ShipmentInvoiceTO — SqlCommand

```sql
with 
ShippedOrders as
	(
		select 
			Entity,
			InventLocationID as FROMWAREHOUSE,
			OrderRef as TRANSFERID,
			cast(ShipDate as datetime) as TRANSFERSHIPDATE
		from ERP.ShipmentInvoice with (nolock)
		where 1=1
		and Transmitted = 0
		and left(OrderRef,2) = 'TO'
		and Entity = ?
		group by 
			Entity,
			InventLocationID, 
			OrderRef,
			ShipDate
	),
ShippedData as
	(
		select 
			si.Entity,
			si.InventLocationID as FROMWAREHOUSE,
			si.ItemID as ITEMID,
			sum(cast(si.Qty as int)) as ShippedQty,
			si.OrderRef as TRANSFERID,
			cast(si.ShipDate as datetime) as TRANSFERSHIPDATE
		from ERP.ShipmentInvoice si with (nolock)
		join ShippedOrders so 
			on si.Entity=so.Entity
			and si.InventLocationID=so.FROMWAREHOUSE
			and si.OrderRef=TRANSFERID
			and cast(si.ShipDate as datetime)=so.TRANSFERSHIPDATE
		where 1=1
		and si.Transmitted = 0
		and left(si.OrderRef,2) = 'TO'
		group by 
			si.Entity,
			si.InventLocationID, 
			si.ItemID,
			si.OrderRef,
			si.ShipDate
	),
OrderData as
	(
		select 
			dh.Entity,
			dh.FROMWAREHOUSE,
			dd.ItemNumber as ITEMID,
			sum(cast(dd.Quantity as int)) as QTYTRANSFER,
			dd.OrderId as TRANSFERID,
			dd.ORDERLINENUMBER
		from erp.DistributionHeader dh with (nolock)
		join erp.DistributionDetail dd with (nolock) 
			on dh.OrderID = dd.OrderID 
			and dh.PickListID = dd.PickListID 
			and dh.entity = dd.entity 
		where 1=1
		and dh.OrderType='Transfer'
		and dd.OrderLineNumber is not null --as of 2021/01/23
		and exists 
					(
						select sd.TransferID 
						from ShippedData sd 
						where sd.Entity=dh.Entity
						and sd.FromWarehouse=dh.FromWarehouse
						and sd.TransferID=dh.OrderID
						and sd.ItemID=dd.ItemNumber
					)	
		group by 
			dh.Entity,
			dh.FROMWAREHOUSE,
			dd.ItemNumber,
			dd.OrderID,
			dd.ORDERLINENUMBER
	)
select 
	o.FROMWAREHOUSE,	
	o.ITEMID,	
	isnull(sd.ShippedQty,0) as QTYTRANSFER, ---Join to OrderData shows they shipped the TO, so any item not shipoped will be 0
	o.TRANSFERID,	
	o.ORDERLINENUMBER,
	so.TRANSFERSHIPDATE
from ShippedOrders so 
join OrderData o
	on o.Entity=so.Entity
	and o.FROMWAREHOUSE=so.FROMWAREHOUSE
	and o.TRANSFERID=so.TRANSFERID
left join ShippedData sd 
	on o.Entity=sd.Entity
	and o.FROMWAREHOUSE=sd.FROMWAREHOUSE
	and o.TRANSFERID=sd.TRANSFERID
	and o.ITEMID=sd.ITEMID
```

#### ERP_DynamicsShipmentStage_CN — SqlCommand

```sql
select 
	fromLocation,	
	document_no,	
	location_code,	
	date_shipped,	
	distribution_no,	
	distribution_line,	
	style_code,	
	ordered_qty,	
	shipped_qty,	
	variance_qty,	
	carton_no,	
	rec_type,	
	external_system_name,
	cast(case when fromLocation='3980' then '1200' else '3001' end as nvarchar(40)) as Entity
from ERP_DynamicsShipmentStage_CN 
--where left(distribution_no, 2) in ('TO', 'SO')  -- Remarked Out on 6/21/2022
where datediff(dd, date_shipped, getdate()) <=7
and shipped_qty <> 0
```

#### ERP_DynamicsShipmentStage_UK — SqlCommand

```sql
select 
shipment as document_no, 
location_code, 
rec_type, 
cast(ship_date as date) as ship_date, 
style_code, 
req_qty as ordered_qty, 
sent_qty as shipped_qty, 
carton_nbr as carton_no, 
distribution_number as distribution_no,
distribution_line
from ERP_DynamicsShipmentStage_UK 
--where left(distribution_number, 2) in ('TO', 'SO')  -- Remarked Out on 6/21/2022
where datediff(dd, ship_date, getdate()) <=10
and sent_qty <> 0
```

#### ERP_DynamicsShipmentStage_WC — SqlCommand

```sql
select 
	document_no, 
	BOL, 
	location_code, 
	rec_type,
	cast(ship_date as date) as ship_date, 
	style_code,
	ordered_qty,
	shipped_qty,
	carton_no,
	distribution_no,
	distribution_line 
from ERP_DynamicsShipmentStage_WC
--where left(distribution_no, 2) in ('TO', 'SO') -- Remarked Out on 6/21/2022
where datediff(dd, ship_date, getdate()) <= 7
and shipped_qty <> 0
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| SOCreateXML |  | FlatFileDestination | DataFlow XML File | SOCreateXML |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| TOCreateXML |  | FlatFileDestination | DataFlow XML File | TOCreateXML |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| ShipmentInvoicePreStage |  | OLEDBDestination | PreStage Shipments CN | IntegrationStaging |  |
| ShipmentInvoicePreStage |  | OLEDBDestination | Prestage Shipments UK | IntegrationStaging |  |
| ShipmentInvoicePreStage |  | OLEDBDestination | PreStage Shipments WC | IntegrationStaging |  |
| ShipmentInvoiceStage |  | OLEDBDestination | Stage Shipments | IntegrationStaging |  |
