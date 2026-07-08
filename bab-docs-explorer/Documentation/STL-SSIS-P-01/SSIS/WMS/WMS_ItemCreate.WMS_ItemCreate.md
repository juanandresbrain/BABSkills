# SSIS Package: WMS_ItemCreate

**Project:** WMS_ItemCreate  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| ArchiveFolder | FILE |  |  |  |
| Flat File Connection Manager | FLATFILE |  |  |  |
| GetBlobUrl | HTTP (KingswaySoft) |  |  |  |
| GetStatus | HTTP (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| ItemCreateXML | FLATFILE |  |  |  |
| ItemUpcXML | FLATFILE |  |  |  |
| ME_01 | OLEDB | bedrockdb02 | me_01 | Data Source=bedrockdb02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| PostTriggerImport | HTTP (KingswaySoft) |  |  |  |
| SMTP_EMAIL | SMTP |  |  |  |
| XML FILES | FILE |  |  |  |
| silverdeltalake | OLEDB | azsynapsewkstt3osb-ondemand.sql.azuresynapse.net | silverdeltalake | Data Source=azsynapsewkstt3osb-ondemand.sql.azuresynapse.net; Initial Catalog=silverdeltalake; Provider=SQLNCLI11.1; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| WMS_ItemCreate | Package |
| File Generation and Move | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| Item Sequence | SEQUENCE |
| Foreach Item Create | FOREACHLOOP |
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
| Foreach Loop - Cleanup Folder Before Staging New Files | FOREACHLOOP |
| Archive Files | FileSystemTask |
| Get RowCount | ExecuteSQLTask |
| Item XML File | ExecuteSQLTask |
| Sequence Container | SEQUENCE |
| Foreach Loop - Copy Manifest and Header File - serv | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Foreach Loop - Copy Manifest and Header Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Merch vs Serv | ExecuteSQLTask |
| XML Files | SEQUENCE |
| EcoResProductCategoryAssignment | ExecuteSQLTask |
| EcoResProductSpecificUOMConversion | ExecuteSQLTask |
| EcoResProductV2 | ExecuteSQLTask |
| EcoResReleasedProductV2 | ExecuteSQLTask |
| Item XML File | ExecuteSQLTask |
| Prestage | ExecuteSQLTask |
| PurchProductApprovedVendor | ExecuteSQLTask |
| PurchVendorProductDescription | ExecuteSQLTask |
| Zip File | ExecuteProcess |
| UPC Sequence | SEQUENCE |
| Foreach Item UPC | FOREACHLOOP |
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
| Foreach Loop - Cleanup Folder Before Staging New Files | FOREACHLOOP |
| Archive Files | FileSystemTask |
| Foreach Loop - Copy Manifest and Header Files 1 | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Get RowCount | ExecuteSQLTask |
| UPC XML File | ExecuteSQLTask |
| Zip File 1 | ExecuteProcess |
| Stage Company Entities | ExecuteSQLTask |
| Pick a Path | ExecuteSQLTask |
| Stage Data | SEQUENCE |
| Merge Item Data | ExecuteSQLTask |
| Merge Item Vendor Data | ExecuteSQLTask |
| Stage dynamics_EcoResProduct | Pipeline |
| Stage Dynamics_ProductOUM | Pipeline |
| Stage Item Data | Pipeline |
| Stage Item Vendor Data | Pipeline |
| Stage ItemUOM | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| Update Send Data for Items Not Found | ExecuteSQLTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- File Generation and Move [SEQUENCE]
  - Foreach Loop - Per Entity [FOREACHLOOP]
    - Item Sequence [SEQUENCE]
      - Foreach Item Create [FOREACHLOOP]
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
      - Foreach Loop - Cleanup Folder Before Staging New Files [FOREACHLOOP]
        - Archive Files [FileSystemTask]
      - Get RowCount [ExecuteSQLTask]
      - Item XML File [ExecuteSQLTask]
      - Sequence Container [SEQUENCE]
        - Foreach Loop - Copy Manifest and Header File - serv [FOREACHLOOP]
          - Copy Manifest & Header [FileSystemTask]
        - Foreach Loop - Copy Manifest and Header Files [FOREACHLOOP]
          - Copy Manifest & Header [FileSystemTask]
        - Merch vs Serv [ExecuteSQLTask]
      - XML Files [SEQUENCE]
        - EcoResProductCategoryAssignment [ExecuteSQLTask]
        - EcoResProductSpecificUOMConversion [ExecuteSQLTask]
        - EcoResProductV2 [ExecuteSQLTask]
        - EcoResReleasedProductV2 [ExecuteSQLTask]
        - Item XML File [ExecuteSQLTask]
        - Prestage [ExecuteSQLTask]
        - PurchProductApprovedVendor [ExecuteSQLTask]
        - PurchVendorProductDescription [ExecuteSQLTask]
      - Zip File [ExecuteProcess]
    - UPC Sequence [SEQUENCE]
      - Foreach Item UPC [FOREACHLOOP]
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
      - Foreach Loop - Cleanup Folder Before Staging New Files [FOREACHLOOP]
        - Archive Files [FileSystemTask]
      - Foreach Loop - Copy Manifest and Header Files 1 [FOREACHLOOP]
        - Copy Manifest & Header [FileSystemTask]
      - Get RowCount [ExecuteSQLTask]
      - UPC XML File [ExecuteSQLTask]
      - Zip File 1 [ExecuteProcess]
  - Stage Company Entities [ExecuteSQLTask]
- Pick a Path [ExecuteSQLTask]
- Stage Data [SEQUENCE]
  - Merge Item Data [ExecuteSQLTask]
  - Merge Item Vendor Data [ExecuteSQLTask]
  - Stage Dynamics_ProductOUM [Pipeline]
  - Stage Item Data [Pipeline]
  - Stage Item Vendor Data [Pipeline]
  - Stage ItemUOM [Pipeline]
  - Stage dynamics_EcoResProduct [Pipeline]
  - Truncate Stage [ExecuteSQLTask]
  - Update Send Data for Items Not Found [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_File_Generation_and_Move["File Generation and Move"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence["Item Sequence"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create["Foreach Item Create"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop_Wait["Wait"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Set_RowsCount["Set RowsCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Stage_Blob_URL["Stage Blob URL"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Trigger_Import["Trigger Import"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Loop___Cleanup_Folder_Before_Staging_New_Files["Foreach Loop - Cleanup Folder Before Staging New Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Loop___Cleanup_Folder_Before_Staging_New_Files_Archive_Files["Archive Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Get_RowCount["Get RowCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Item_XML_File["Item XML File"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container["Sequence Container"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Foreach_Loop___Copy_Manifest_and_Header_File___serv["Foreach Loop - Copy Manifest and Header File - serv"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Foreach_Loop___Copy_Manifest_and_Header_File___serv_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Foreach_Loop___Copy_Manifest_and_Header_Files["Foreach Loop - Copy Manifest and Header Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Foreach_Loop___Copy_Manifest_and_Header_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Merch_vs_Serv["Merch vs Serv"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files["XML Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductCategoryAssignment["EcoResProductCategoryAssignment"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductSpecificUOMConversion["EcoResProductSpecificUOMConversion"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductV2["EcoResProductV2"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResReleasedProductV2["EcoResReleasedProductV2"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_Item_XML_File["Item XML File"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_Prestage["Prestage"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_PurchProductApprovedVendor["PurchProductApprovedVendor"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_PurchVendorProductDescription["PurchVendorProductDescription"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Zip_File["Zip File"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence["UPC Sequence"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC["Foreach Item UPC"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop_Wait["Wait"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Set_RowsCount["Set RowsCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Stage_Blob_URL["Stage Blob URL"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Trigger_Import["Trigger Import"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Loop___Cleanup_Folder_Before_Staging_New_Files["Foreach Loop - Cleanup Folder Before Staging New Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Loop___Cleanup_Folder_Before_Staging_New_Files_Archive_Files["Archive Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Loop___Copy_Manifest_and_Header_Files_1["Foreach Loop - Copy Manifest and Header Files 1"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Loop___Copy_Manifest_and_Header_Files_1_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Get_RowCount["Get RowCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_UPC_XML_File["UPC XML File"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Zip_File_1["Zip File 1"]
    n_Package_File_Generation_and_Move_Stage_Company_Entities["Stage Company Entities"]
    n_Package_Pick_a_Path["Pick a Path"]
    n_Package_Stage_Data["Stage Data"]
    n_Package_Stage_Data_Merge_Item_Data["Merge Item Data"]
    n_Package_Stage_Data_Merge_Item_Vendor_Data["Merge Item Vendor Data"]
    n_Package_Stage_Data_Stage_dynamics_EcoResProduct["Stage dynamics_EcoResProduct"]
    n_Package_Stage_Data_Stage_Dynamics_ProductOUM["Stage Dynamics_ProductOUM"]
    n_Package_Stage_Data_Stage_Item_Data["Stage Item Data"]
    n_Package_Stage_Data_Stage_Item_Vendor_Data["Stage Item Vendor Data"]
    n_Package_Stage_Data_Stage_ItemUOM["Stage ItemUOM"]
    n_Package_Stage_Data_Truncate_Stage["Truncate Stage"]
    n_Package_Stage_Data_Update_Send_Data_for_Items_Not_Found["Update Send Data for Items Not Found"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Foreach_Loop_Container_Archive_Files
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop_Wait --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Stage_Blob_URL --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Set_RowsCount
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Trigger_Import --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_ProcessStatus_For_Loop
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Foreach_Loop_Container --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Trigger_Import
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Set_BatchID___LoopCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Stage_Blob_URL
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Set_RowsCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create_Foreach_Loop_Container
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Merch_vs_Serv --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Foreach_Loop___Copy_Manifest_and_Header_Files
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Merch_vs_Serv --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container_Foreach_Loop___Copy_Manifest_and_Header_File___serv
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_Prestage --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_PurchProductApprovedVendor
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_PurchProductApprovedVendor --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_PurchVendorProductDescription
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_PurchVendorProductDescription --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductCategoryAssignment
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductCategoryAssignment --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductSpecificUOMConversion
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductSpecificUOMConversion --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductV2
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResProductV2 --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files_EcoResReleasedProductV2
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Item_XML_File --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Zip_File
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Zip_File --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Item_Create
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Foreach_Loop___Cleanup_Folder_Before_Staging_New_Files --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Get_RowCount
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Get_RowCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Item_XML_File
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Get_RowCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_XML_Files --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence_Sequence_Container
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Foreach_Loop_Container_Archive_Files
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop_Wait --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Stage_Blob_URL --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Set_RowsCount
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Trigger_Import --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_ProcessStatus_For_Loop
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Foreach_Loop_Container --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Trigger_Import
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Set_BatchID___LoopCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Stage_Blob_URL
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Set_RowsCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC_Foreach_Loop_Container
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Loop___Cleanup_Folder_Before_Staging_New_Files --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Get_RowCount
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_UPC_XML_File --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Loop___Copy_Manifest_and_Header_Files_1
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Loop___Copy_Manifest_and_Header_Files_1 --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Zip_File_1
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Get_RowCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_UPC_XML_File
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Zip_File_1 --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence_Foreach_Item_UPC
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Item_Sequence --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_UPC_Sequence
    n_Package_File_Generation_and_Move_Stage_Company_Entities --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity
    n_Package_Stage_Data_Stage_Item_Data --> n_Package_Stage_Data_Stage_Item_Vendor_Data
    n_Package_Stage_Data_Truncate_Stage --> n_Package_Stage_Data_Stage_Item_Data
    n_Package_Stage_Data_Merge_Item_Data --> n_Package_Stage_Data_Merge_Item_Vendor_Data
    n_Package_Stage_Data_Stage_Item_Vendor_Data --> n_Package_Stage_Data_Merge_Item_Data
    n_Package_Stage_Data_Merge_Item_Vendor_Data --> n_Package_Stage_Data_Stage_ItemUOM
    n_Package_Stage_Data_Stage_ItemUOM --> n_Package_Stage_Data_Stage_Dynamics_ProductOUM
    n_Package_Stage_Data_Merge_Item_Data --> n_Package_Stage_Data_Stage_dynamics_EcoResProduct
    n_Package_Stage_Data_Stage_dynamics_EcoResProduct --> n_Package_Stage_Data_Update_Send_Data_for_Items_Not_Found
    n_Package_Pick_a_Path --> n_Package_File_Generation_and_Move
    n_Package_Pick_a_Path --> n_Package_Stage_Data
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | ArchiveFolder | Yes |
| User | AzCopytoBlobCommand | Yes |
| User | AzCopytoBlobCommand2 | Yes |
| User | BatchID | No |
| User | BlobURL | No |
| User | BlobURLRecordSet | No |
| User | CompanyEntities | No |
| User | DataEntityName | No |
| User | DateTimeStamp | Yes |
| User | DefinitionGroupID | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | Entity | No |
| User | FileName | No |
| User | FileNameForCleanUpLoop | No |
| User | FileToDeleteUPC | No |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | HeaderAndManifestForLoop | No |
| User | JSON_GetBlobURL | Yes |
| User | JSON_GetSummaryStatus | Yes |
| User | LoopCount | No |
| User | PackageAPIHeaderAndManifestPath | Yes |
| User | ProcessStatus | No |
| User | RowCountUPC | No |
| User | RowsCount | No |
| User | RowsCountItem | No |
| User | RunControlFlag | No |
| User | SQLItemLoadViewByEntity | Yes |
| User | SQL_GetBlobURLCommand | Yes |
| User | SQL_GetSummaryStatus | Yes |
| User | SQL_TriggerImport | Yes |
| User | SQL_TriggerImportUPC | Yes |
| User | SQL_VendorDataFlow | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | ZipCommand | Yes |
| User | ZipCommand2 | Yes |
| User | ZipDest | Yes |
| User | ZipDest2 | Yes |
| User | ZipSource | Yes |
| User | isServItem | No |

### Expression-bound variable values

#### User::ArchiveFolder

**Expression:**

```sql
@[$Package::WMS_ItemCreateFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-P-01\IntegrationStaging\ERP\Items\Archive\
```

#### User::AzCopytoBlobCommand

**Expression:**

```sql
"cp \"" +  @[User::ZipDest] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-P-01\IntegrationStaging\ERP\Items\Serv1100.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
```

#### User::AzCopytoBlobCommand2

**Expression:**

```sql
"cp \"" +  @[User::ZipDest2] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-P-01\IntegrationStaging\ERP\Items\ItemUPC1100.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
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
2024320155140500
```

#### User::DefinitionGroupID

**Expression:**

```sql
@[$Package::WMS_ItemCreateMerchVsServ] == "Serv" ?  @[$Package::WMS_ItemCreateSERVDefinitionGroupID] :  @[$Package::WMS_ItemCreateBlobDefinitionGroupID]
```

**Evaluated value:**

```sql
ServiceItemCreateUpdate
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
3/20/2024
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
2024-03-20
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
3/20/2024
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
2024-03-20
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
@[$Package::WMS_PackageAPI_StaticPackageFilesPath] + "ItemCreate"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\ItemCreate
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
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[DefinitionGroupID] + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as executionId, 'ServiceItemCreateUpdate1100' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1100' as legalEntityId
```

#### User::SQL_TriggerImportUPC

**Expression:**

```sql
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[$Package::WMS_ItemCreateUPCDefinitionGroupID] + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as executionId, 'ItemUPCCreate1100' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1100' as legalEntityId
```

#### User::SQL_VendorDataFlow

**Expression:**

```sql
"
select
	s.style_code as ITEMNUMBER,
	v.Entity AS DataAreaId,
	att.attribute_set_code as FactoryCode,
	v.VendorAccountNumber,
	sv.Vendor_Style as VendorProductNumber,
	v.InsertDate as EFFECTIVEDATE
from attribute a with (nolock)
join entity_attribute_set eas with (nolock) on a.attribute_id=eas.attribute_id
join attribute_set att with (nolock) on eas.attribute_set_id = att.attribute_set_id
join parent_type pt with (nolock) on eas.parent_type=pt.parent_type_code
join style s with (nolock) on eas.parent_id=s.style_id
join style_vendor sv with (nolock) on s.style_id = sv.style_id --and sv.primary_vendor_flag = 1
join vendor mv with (nolock) on sv.vendor_id=mv.vendor_id 
join ["+ @[$Package::IntegrationStaging_ServerName]  +"].IntegrationStaging.ERP.VendorMaster v 
	on att.attribute_set_code=v.BABFactoryCode
	and mv.Vendor_Code=v.BABVendorCode
where 1=1
	and a.attribute_label='FACTORY'
	and a.active_flag=1
	and pt.parent_type_descr='Style'
	and s.active_flag=1
	and att.active_flag=1
"
```

**Evaluated value:**

```sql

select
	s.style_code as ITEMNUMBER,
	v.Entity AS DataAreaId,
	att.attribute_set_code as FactoryCode,
	v.VendorAccountNumber,
	sv.Vendor_Style as VendorProductNumber,
	v.InsertDate as EFFECTIVEDATE
from attribute a with (nolock)
join entity_attribute_set eas with (nolock) on a.attribute_id=eas.attribute_id
join attribute_set att with (nolock) on eas.attribute_set_id = att.attribute_set_id
join parent_type pt with (nolock) on eas.parent_type=pt.parent_type_code
join style s with (nolock) on eas.parent_id=s.style_id
join style_vendor sv with (nolock) on s.style_id = sv.style_id --and sv.primary_vendor_flag = 1
join vendor mv with (nolock) on sv.vendor_id=mv.vendor_id 
join [STL-SSIS-P-01].IntegrationStaging.ERP.VendorMaster v 
	on att.attribute_set_code=v.BABFactoryCode
	and mv.Vendor_Code=v.BABVendorCode
where 1=1
	and a.attribute_label='FACTORY'
	and a.active_flag=1
	and pt.parent_type_descr='Style'
	and s.active_flag=1
	and att.active_flag=1

```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
3/19/2024
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
2024-03-19
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-P-01\IntegrationStaging\ERP\Items\Serv1100.zip"  "*.xml" -sdel
```

#### User::ZipCommand2

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest2]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-P-01\IntegrationStaging\ERP\Items\ItemUPC1100.zip"  "*.xml" -sdel
```

#### User::ZipDest

**Expression:**

```sql
@[$Package::WMS_ItemCreateFileStageLocation]  + @[$Package::WMS_ItemCreateMerchVsServ]  +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-P-01\IntegrationStaging\ERP\Items\Serv1100.zip
```

#### User::ZipDest2

**Expression:**

```sql
@[$Package::WMS_ItemCreateFileStageLocation]  + "ItemUPC" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-P-01\IntegrationStaging\ERP\Items\ItemUPC1100.zip
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

### Set ProcessStatus

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\Foreach Item Create\ProcessStatus For Loop\Set ProcessStatus`  
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
		when ? < 1 --- designed to let the loop escape if still not finihed after 52 loops
			then count(*)
		else 1
	end as ProcessStatus
from ProcStatus
where ProcessStatus = 1
```

### Wait

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\Foreach Item Create\ProcessStatus For Loop\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:01:59'
```

### Set BatchID - LoopCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\Foreach Item Create\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\Foreach Item Create\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### Get RowCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\Get RowCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select count(*) as RowsCount
from erp.ItemLoadtoD365
where 1=1
and SendData=1
and entity=?

```

### Item XML File

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\Item XML File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
declare 
	@sql varchar(100),
	@file varchar(100),
	@Entity varchar(100),
	@Location varchar(1000),
	@ItemType varchar(100)

select
	@Entity=?,
	@Location=?,
	@ItemType=?,
	@sql = 'exec IntegrationStaging.WMS.spQueryItemCreateXML @entity=''' + @Entity + ''', @ItemType=''' + @ItemType +'''',
	@file = 'ItemCreateUpdate.xml'

	exec WEB.spOutputXMLFile 
	@Query = @sql, 
	@FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
	@FileName = @file

```

### Merch vs Serv

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\Sequence Container\Merch vs Serv`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
--
```

### EcoResProductCategoryAssignment

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\EcoResProductCategoryAssignment`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
  declare 
 @sql varchar(1000),
 @file varchar(100),
 @Entity varchar(100),
 @Location varchar(1000),
 @ItemType varchar(100)

select
 @Entity=?,
 @Location=?,
 @ItemType=?,
 @sql = 'exec IntegrationStaging.WMS.spQueryItemCreateEcoResProductCategoryAssignmentXML @entity=''' + @Entity + ''', @ItemType=''' + @ItemType +'''',
 @file = 'Product category assignments.xml'

 exec WEB.spOutputXMLFile 
 @Query = @sql, 
 @FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
 @FileName = @file
```

### EcoResProductSpecificUOMConversion

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\EcoResProductSpecificUOMConversion`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
  declare 
 @sql varchar(1000),
 @file varchar(100),
 @Entity varchar(100),
 @Location varchar(1000),
 @ItemType varchar(100)

select
 @Entity=?,
 @Location=?,
 @ItemType=?,
 @sql = 'exec IntegrationStaging.WMS.spQueryItemCreateEcoResProductSpecificUOMXML @entity=''' + @Entity + ''', @ItemType=''' + @ItemType +'''',
 @file = 'Product specific unit conversions.xml'

IF(select 
	COUNT(*) AS [Count]
  from WMS.ItemUOMStageForDynamics uom with (nolock)
  where uom.style_code in (
		select e.ItemNumber
		from ERP.ItemLoadtoD365 e
		where 1=1
		and e.SendData = 1 --this is only set on insert or update
		and e.UpdateDate is null --this is only set on update, means this is the first time item is flowing
		and e.entity=1100
		group by e.ItemNumber
	) ) > =1
  BEGIN
	exec WEB.spOutputXMLFile 
		@Query = @sql, 
		@FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
		@FileName = @file
  END
```

### EcoResProductV2

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\EcoResProductV2`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
 declare 
 @sql varchar(1000),
 @file varchar(100),
 @Entity varchar(100),
 @Location varchar(1000),
 @ItemType varchar(100)

select
 @Entity=?,
 @Location=?,
 @ItemType=?,
 @sql = 'exec IntegrationStaging.WMS.spQueryItemCreateEcoResProductV2XML @entity=''' + @Entity + ''', @ItemType=''' + @ItemType +'''',
 @file = 'Products V2.xml'

 exec WEB.spOutputXMLFile 
 @Query = @sql, 
 @FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
 @FileName = @file
```

### EcoResReleasedProductV2

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\EcoResReleasedProductV2`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
  declare 
 @sql varchar(1000),
 @file varchar(100),
 @Entity varchar(100),
 @Location varchar(1000),
 @ItemType varchar(100)

select
 @Entity=?,
 @Location=?,
 @ItemType=?,
 @sql = 'exec IntegrationStaging.WMS.spQueryItemCreateEcoResReleasedProductV2XML @entity=''' + @Entity + ''', @ItemType=''' + @ItemType +'''',
 @file = 'Released products V2.xml'

 exec WEB.spOutputXMLFile 
 @Query = @sql, 
 @FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
 @FileName = @file
```

### Item XML File

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\Item XML File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
declare 
 @sql varchar(100),
 @file varchar(100),
 @Entity varchar(100),
 @Location varchar(1000),
 @ItemType varchar(100)

select
 @Entity=?,
 @Location=?,
 @ItemType=?,
 @sql = 'exec IntegrationStaging.WMS.spQueryItemCreateXML @entity=''' + @Entity + ''', @ItemType=''' + @ItemType +'''',
 @file = 'ItemCreateUpdate.xml'

 exec WEB.spOutputXMLFile 
 @Query = @sql, 
 @FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
 @FileName = @file

```

### Prestage

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\Prestage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec WMS.spQueryItemCreatePreStage @entity=?, @ItemType=?
```

### PurchProductApprovedVendor

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\PurchProductApprovedVendor`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
declare 
 @sql varchar(1000),
 @file varchar(100),
 @Entity varchar(100),
 @Location varchar(1000),
 @ItemType varchar(100)

select
 @Entity=?,
 @Location=?,
 @ItemType=?,
 @sql = 'exec IntegrationStaging.WMS.spQueryItemCreateVendorXML @entity=''' + @Entity + '''',
 @file = 'Approved vendor list by products.xml'

 IF((
	SELECT COUNT(*) [Count]
	FROM ERP.ItemLoadtoD365	i
		JOIN ERP.ItemVendorLoadtoD365 v ON i.ITEMNUMBER = v.ITEMNUMBER AND i.Entity = v.DataAreaID
	where 1=1
	and i.SendData = 1
	and i.Entity = @Entity 
	and v.deletedFromSource IS NULL --LT
  ) >= 1 AND @ItemType = 'MERCH') 
  BEGIN
	 exec WEB.spOutputXMLFile 
	 @Query = @sql, 
	 @FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
	 @FileName = @file
  END
```

### PurchVendorProductDescription

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Item Sequence\XML Files\PurchVendorProductDescription`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
declare 
 @sql varchar(1000),
 @file varchar(100),
 @Entity varchar(100),
 @Location varchar(1000),
 @ItemType varchar(100)

select
 @Entity=?,
 @Location=?,
 @ItemType=?,
 @sql = 'exec IntegrationStaging.WMS.spQueryItemCreateVendorProdDescXML @entity=''' + @Entity + '''',
 @file = 'External item descriptions for vendors V2.xml'

 IF((
	SELECT COUNT(*) [Count]
	FROM ERP.ItemLoadtoD365	i
		JOIN ERP.ItemVendorLoadtoD365 v ON i.ITEMNUMBER = v.ITEMNUMBER AND i.Entity = v.DataAreaID
	where 1=1
	and i.SendData = 1
	and i.Entity = @Entity 
	and v.deletedFromSource IS NULL --LT
  ) >= 1 AND @ItemType = 'MERCH') 

  BEGIN
	exec WEB.spOutputXMLFile 
		@Query = @sql, 
		@FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
		@FileName = @file
  END
```

### Set ProcessStatus

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\UPC Sequence\Foreach Item UPC\ProcessStatus For Loop\Set ProcessStatus`  
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

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\UPC Sequence\Foreach Item UPC\ProcessStatus For Loop\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:59'
```

### Set BatchID - LoopCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\UPC Sequence\Foreach Item UPC\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\UPC Sequence\Foreach Item UPC\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### Get RowCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\UPC Sequence\Get RowCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select count(*) as RowsCount
from erp.ItemLoadtoD365
where 1=1
and SendData=1
and entity=?
and UpdateDate is null
```

### UPC XML File

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\UPC Sequence\UPC XML File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
declare 
	@sql varchar(100),
	@file varchar(100),
	@Entity varchar(100),
	@Location varchar(1000)

select
	@Entity=?,
	@Location=?,
	@sql = 'exec IntegrationStaging.WMS.spQueryItemUPCXML @entity=''' + @Entity + '''',
	@file = 'Item - barcodes V3.xml'

	exec WEB.spOutputXMLFile 
	@Query = @sql, 
	@FileLocation = @Location, --'\\stl-ssis-T-01\IntegrationStaging\ERP\Items\', 
	@FileName = @file
```

### Stage Company Entities

**Path:** `Package\File Generation and Move\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
select Entity
from erp.ItemLoadtoD365
where SendData = 1
and case when ServiceItem = '1' then 'Serv' else 'Merch' end = 'Serv' group by Entity
```

**Property expression (runtime override):**

```sql
"select Entity
from erp.ItemLoadtoD365
where SendData = 1
and case when ServiceItem = '1' then 'Serv' else 'Merch' end = '" + @[$Package::WMS_ItemCreateMerchVsServ] + "' group by Entity"
```

### Pick a Path

**Path:** `Package\Pick a Path`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
--
```

### Merge Item Data

**Path:** `Package\Stage Data\Merge Item Data`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec ERP.spMergeItemLoadtoD365 'DELTA'
```

**Property expression (runtime override):**

```sql
"exec ERP.spMergeItemLoadtoD365 " +  "'" + @[$Package::WMS_ItemCreateLoadType] + "'"
```

### Merge Item Vendor Data

**Path:** `Package\Stage Data\Merge Item Vendor Data`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeItemVendorLoadtoD365
```

### Truncate Stage

**Path:** `Package\Stage Data\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.ItemLoadtoD365Stage
TRUNCATE TABLE WMS.ItemUOMStageForDynamics
TRUNCATE TABLE ERP.ItemVendorLoadtoD365Stage
TRUNCATE TABLE dynamics_productuom
TRUNCATE TABLE dynamics_EcoResProduct
```

### Update Send Data for Items Not Found

**Path:** `Package\Stage Data\Update Send Data for Items Not Found`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
UPDATE ERP.ItemLoadtoD365
SET SendData=1
WHERE 1=1
	AND DATEDIFF(hh, ISNULL(updateDate, InsertDate), getdate()) >=3 
	AND ItemNumber not in (SELECT DisplayProductNumber FROM dbo.dynamics_EcoResProduct)
	AND SendData=0
	AND ISNUMERIC(ItemNumber) = 1
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |
| silverdatalake_dynamics_EcoResProduct |  | OLEDBSource | Stage dynamics_EcoResProduct | silverdeltalake | SqlCommand |
| silverdeltalake_dynamics_productuom |  | OLEDBSource | Stage Dynamics_ProductOUM | silverdeltalake | SqlCommand |
| vwERPItemLoadtoD365 |  | OLEDBSource | Stage Item Data | ME_01 | SqlCommand |
| Vendor |  | OLEDBSource | Stage Item Vendor Data | ME_01 | SqlCommand |
| vwWMSItemUOMs |  | OLEDBSource | Stage ItemUOM | ME_01 | SqlCommand |

#### Trigger Columns — SqlCommand

```sql
select 'do nothing' as DoNothing
```

#### silverdatalake_dynamics_EcoResProduct — SqlCommand

```sql
SELECT DISTINCT 
     CAST(DisplayProductNumber AS nvarchar(25)) as 'DisplayProductNumber'
  FROM silverdeltalake.dbo.dynamics_EcoResProduct
  WHERE 1=1
     AND ISNUMERIC(DisplayProductNumber) = 1
```

#### silverdeltalake_dynamics_productuom — SqlCommand

```sql
SELECT CAST([displayProductNumber] AS nvarchar(25)) [displayProductNumber]
      ,[Denominator]
      ,CAST([Factor] AS int) [Factor]
      ,CAST([fromSymbol] AS nvarchar(10)) [fromSymbol]
      ,CAST([InnerOffset] AS int) [InnerOffset]
      ,CAST([toSymbol] AS nvarchar(10)) [toSymbol]
      ,[Numerator]
      ,CAST([OuterOffset] AS int) [OuterOffset]
  FROM [dbo].[dynamics_productuom]
```

#### vwERPItemLoadtoD365 — SqlCommand

```sql
SELECT *   FROM [me_01].[dbo].[vwERPItemLoadtoD365] 
  wHERE itemnumber = '021709'
```

#### Vendor — SqlCommand

```sql
select
	s.style_code as ITEMNUMBER,
	v.Entity AS DataAreaId,
	att.attribute_set_code as FactoryCode,
	v.VendorAccountNumber,
	sv.Vendor_Style as VendorProductNumber,
	v.InsertDate as EFFECTIVEDATE
from attribute a with (nolock)
join entity_attribute_set eas with (nolock) on a.attribute_id=eas.attribute_id
join attribute_set att with (nolock) on eas.attribute_set_id = att.attribute_set_id
join parent_type pt with (nolock) on eas.parent_type=pt.parent_type_code
join style s with (nolock) on eas.parent_id=s.style_id
join style_vendor sv with (nolock) on s.style_id = sv.style_id --and sv.primary_vendor_flag = 1
join vendor mv with (nolock) on sv.vendor_id=mv.vendor_id 
join [stl-ssis-t-01].IntegrationStaging.ERP.VendorMaster v 
	on att.attribute_set_code=v.BABFactoryCode
	and mv.Vendor_Code=v.BABVendorCode
where 1=1
	and a.attribute_label='FACTORY'
	and a.active_flag=1
	and pt.parent_type_descr='Style'
	and s.active_flag=1
	and att.active_flag=1
```

#### vwWMSItemUOMs — SqlCommand

```sql
select 
			style_code,
			order_multiple,
			distribution_multiple,
			'CS' as FromUnitSymbol,
			'EA' as ToUnitSymbol,
			1 as Denominator,
			order_multiple as Factor
		from style
		--where style_code = '029351'
		UNION
		select 
			style_code,
			order_multiple,
			distribution_multiple,
			'CS' as FromUnitSymbol,
			'IP' as ToUnitSymbol,
			1 as Denominator,
			order_multiple / distribution_multiple as Factor
		from style
		--where style_code = '029351'
		UNION
		select 
			style_code,
			order_multiple,
			distribution_multiple,
			'IP' as FromUnitSymbol,
			'EA' as ToUnitSymbol,
			1 as Denominator,
			distribution_multiple as Factor
		from style
		--where style_code = '029351'
		UNION
		select 
			style_code,
			order_multiple,
			distribution_multiple,
			'EA' as FromUnitSymbol,
			'WMEA' as ToUnitSymbol,
			1 as Denominator,
			1 as Factor
		from style
		--where style_code = '029351'
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| dynamics_EcoResProduct |  | OLEDBDestination | Stage dynamics_EcoResProduct | IntegrationStaging |  |
| dynamics_productuom |  | OLEDBDestination | Stage Dynamics_ProductOUM | IntegrationStaging |  |
| ItemLoadtoD365Stage |  | OLEDBDestination | Stage Item Data | IntegrationStaging |  |
| ItemVendorLoadtoD365Stage |  | OLEDBDestination | Stage Item Vendor Data | IntegrationStaging |  |
| ItemUOMStageForDynamics |  | OLEDBDestination | Stage ItemUOM | IntegrationStaging |  |
