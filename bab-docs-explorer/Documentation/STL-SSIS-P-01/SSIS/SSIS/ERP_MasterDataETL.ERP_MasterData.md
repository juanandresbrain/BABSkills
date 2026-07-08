# SSIS Package: ERP_MasterData

**Project:** ERP_MasterDataETL  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP_EMAIL | SMTP |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| ERP_MasterData | Package |
| Data Load Sequence | SEQUENCE |
| Foreach Loop - Item Master - Products XML | FOREACHLOOP |
| Archive File | FileSystemTask |
| Data Flow - ItemMasterProducts XML | Pipeline |
| Delete Old Files | ExecuteSQLTask |
| Error File | FileSystemTask |
| Merge ItemMasterProducts | ExecuteSQLTask |
| Products - Log Start | ExecuteSQLTask |
| Stage File | FileSystemTask |
| Truncate Stage | ExecuteSQLTask |
| Update Log - Archive File | ExecuteSQLTask |
| Update Log - Error File | ExecuteSQLTask |
| Update Log - Merge Error | ExecuteSQLTask |
| Update Log - Success | ExecuteSQLTask |
| Foreach Loop - Item Master UOM XML | FOREACHLOOP |
| Archive File | FileSystemTask |
| Data Flow - Items UOM XML | Pipeline |
| Delete Old Files | ExecuteSQLTask |
| Error File | FileSystemTask |
| Merge Items UOM | ExecuteSQLTask |
| Stage File | FileSystemTask |
| Truncate Stage | ExecuteSQLTask |
| UOM - Log Start | ExecuteSQLTask |
| Update Log - Archive File | ExecuteSQLTask |
| Update Log - Error File | ExecuteSQLTask |
| Update Log - Merge Error | ExecuteSQLTask |
| Update Log - Success | ExecuteSQLTask |
| Foreach Loop - Item Master XML | FOREACHLOOP |
| Archive File | FileSystemTask |
| Data Flow - Item Master XML | Pipeline |
| Delete Old Files | ExecuteSQLTask |
| Error File | FileSystemTask |
| ItemMaster - Log Start | ExecuteSQLTask |
| Merge ItemMaster | ExecuteSQLTask |
| Stage File | FileSystemTask |
| Truncate Stage | ExecuteSQLTask |
| Update Log - Archive File | ExecuteSQLTask |
| Update Log - Error File | ExecuteSQLTask |
| Update Log - Merge Error | ExecuteSQLTask |
| Update Log - Success | ExecuteSQLTask |
| Foreach Loop - Vendors | FOREACHLOOP |
| Archive File | FileSystemTask |
| Data Flow - Vendor XML | Pipeline |
| Delete Old Files | ExecuteSQLTask |
| Error File | FileSystemTask |
| Merge VendorMaster | ExecuteSQLTask |
| Stage File | FileSystemTask |
| Truncate Stage | ExecuteSQLTask |
| Update Log - Archive File | ExecuteSQLTask |
| Update Log - Error File | ExecuteSQLTask |
| Update Log - Merge Error | ExecuteSQLTask |
| Update Log - Success | ExecuteSQLTask |
| Vendors - Log Start | ExecuteSQLTask |
| Foreach Loop - Warehouse | FOREACHLOOP |
| Archive File | FileSystemTask |
| Data Flow - Warehouse XML | Pipeline |
| Delete Old Files | ExecuteSQLTask |
| Error File | FileSystemTask |
| Merge WarehouseMaster | ExecuteSQLTask |
| Stage File | FileSystemTask |
| Truncate Stage | ExecuteSQLTask |
| Update Log - Archive File | ExecuteSQLTask |
| Update Log - Error File | ExecuteSQLTask |
| Update Log - Merge Error | ExecuteSQLTask |
| Update Log - Success | ExecuteSQLTask |
| Warehouse - Log Start | ExecuteSQLTask |
| Missing Data Check Email | SEQUENCE |
| spEmailItemsMissingDimensionData | ExecuteSQLTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- Data Load Sequence [SEQUENCE]
  - Foreach Loop - Item Master - Products XML [FOREACHLOOP]
    - Archive File [FileSystemTask]
    - Data Flow - ItemMasterProducts XML [Pipeline]
    - Delete Old Files [ExecuteSQLTask]
    - Error File [FileSystemTask]
    - Merge ItemMasterProducts [ExecuteSQLTask]
    - Products - Log Start [ExecuteSQLTask]
    - Stage File [FileSystemTask]
    - Truncate Stage [ExecuteSQLTask]
    - Update Log - Archive File [ExecuteSQLTask]
    - Update Log - Error File [ExecuteSQLTask]
    - Update Log - Merge Error [ExecuteSQLTask]
    - Update Log - Success [ExecuteSQLTask]
  - Foreach Loop - Item Master UOM XML [FOREACHLOOP]
    - Archive File [FileSystemTask]
    - Data Flow - Items UOM XML [Pipeline]
    - Delete Old Files [ExecuteSQLTask]
    - Error File [FileSystemTask]
    - Merge Items UOM [ExecuteSQLTask]
    - Stage File [FileSystemTask]
    - Truncate Stage [ExecuteSQLTask]
    - UOM - Log Start [ExecuteSQLTask]
    - Update Log - Archive File [ExecuteSQLTask]
    - Update Log - Error File [ExecuteSQLTask]
    - Update Log - Merge Error [ExecuteSQLTask]
    - Update Log - Success [ExecuteSQLTask]
  - Foreach Loop - Item Master XML [FOREACHLOOP]
    - Archive File [FileSystemTask]
    - Data Flow - Item Master XML [Pipeline]
    - Delete Old Files [ExecuteSQLTask]
    - Error File [FileSystemTask]
    - ItemMaster - Log Start [ExecuteSQLTask]
    - Merge ItemMaster [ExecuteSQLTask]
    - Stage File [FileSystemTask]
    - Truncate Stage [ExecuteSQLTask]
    - Update Log - Archive File [ExecuteSQLTask]
    - Update Log - Error File [ExecuteSQLTask]
    - Update Log - Merge Error [ExecuteSQLTask]
    - Update Log - Success [ExecuteSQLTask]
  - Foreach Loop - Vendors [FOREACHLOOP]
    - Archive File [FileSystemTask]
    - Data Flow - Vendor XML [Pipeline]
    - Delete Old Files [ExecuteSQLTask]
    - Error File [FileSystemTask]
    - Merge VendorMaster [ExecuteSQLTask]
    - Stage File [FileSystemTask]
    - Truncate Stage [ExecuteSQLTask]
    - Update Log - Archive File [ExecuteSQLTask]
    - Update Log - Error File [ExecuteSQLTask]
    - Update Log - Merge Error [ExecuteSQLTask]
    - Update Log - Success [ExecuteSQLTask]
    - Vendors - Log Start [ExecuteSQLTask]
  - Foreach Loop - Warehouse [FOREACHLOOP]
    - Archive File [FileSystemTask]
    - Data Flow - Warehouse XML [Pipeline]
    - Delete Old Files [ExecuteSQLTask]
    - Error File [FileSystemTask]
    - Merge WarehouseMaster [ExecuteSQLTask]
    - Stage File [FileSystemTask]
    - Truncate Stage [ExecuteSQLTask]
    - Update Log - Archive File [ExecuteSQLTask]
    - Update Log - Error File [ExecuteSQLTask]
    - Update Log - Merge Error [ExecuteSQLTask]
    - Update Log - Success [ExecuteSQLTask]
    - Warehouse - Log Start [ExecuteSQLTask]
- Missing Data Check Email [SEQUENCE]
  - spEmailItemsMissingDimensionData [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Data_Load_Sequence["Data Load Sequence"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML["Foreach Loop - Item Master - Products XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Archive_File["Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Data_Flow___ItemMasterProducts_XML["Data Flow - ItemMasterProducts XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Delete_Old_Files["Delete Old Files"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Error_File["Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Merge_ItemMasterProducts["Merge ItemMasterProducts"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Products___Log_Start["Products - Log Start"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Stage_File["Stage File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Truncate_Stage["Truncate Stage"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Archive_File["Update Log - Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Error_File["Update Log - Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Merge_Error["Update Log - Merge Error"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Success["Update Log - Success"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML["Foreach Loop - Item Master UOM XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Archive_File["Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Data_Flow___Items_UOM_XML["Data Flow - Items UOM XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Delete_Old_Files["Delete Old Files"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Error_File["Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Merge_Items_UOM["Merge Items UOM"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Stage_File["Stage File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Truncate_Stage["Truncate Stage"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_UOM___Log_Start["UOM - Log Start"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Archive_File["Update Log - Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Error_File["Update Log - Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Merge_Error["Update Log - Merge Error"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Success["Update Log - Success"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML["Foreach Loop - Item Master XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Archive_File["Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Data_Flow___Item_Master_XML["Data Flow - Item Master XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Delete_Old_Files["Delete Old Files"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Error_File["Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_ItemMaster___Log_Start["ItemMaster - Log Start"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Merge_ItemMaster["Merge ItemMaster"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Stage_File["Stage File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Truncate_Stage["Truncate Stage"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Archive_File["Update Log - Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Error_File["Update Log - Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Merge_Error["Update Log - Merge Error"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Success["Update Log - Success"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors["Foreach Loop - Vendors"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Archive_File["Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Data_Flow___Vendor_XML["Data Flow - Vendor XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Delete_Old_Files["Delete Old Files"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Error_File["Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Merge_VendorMaster["Merge VendorMaster"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Stage_File["Stage File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Truncate_Stage["Truncate Stage"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Archive_File["Update Log - Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Error_File["Update Log - Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Merge_Error["Update Log - Merge Error"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Success["Update Log - Success"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Vendors___Log_Start["Vendors - Log Start"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse["Foreach Loop - Warehouse"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Archive_File["Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Data_Flow___Warehouse_XML["Data Flow - Warehouse XML"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Delete_Old_Files["Delete Old Files"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Error_File["Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Merge_WarehouseMaster["Merge WarehouseMaster"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Stage_File["Stage File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Truncate_Stage["Truncate Stage"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Archive_File["Update Log - Archive File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Error_File["Update Log - Error File"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Merge_Error["Update Log - Merge Error"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Success["Update Log - Success"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Warehouse___Log_Start["Warehouse - Log Start"]
    n_Package_Missing_Data_Check_Email["Missing Data Check Email"]
    n_Package_Missing_Data_Check_Email_spEmailItemsMissingDimensionData["spEmailItemsMissingDimensionData"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Stage_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Data_Flow___ItemMasterProducts_XML
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Data_Flow___ItemMasterProducts_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Merge_ItemMasterProducts --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Merge_Error
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Truncate_Stage --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Stage_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Products___Log_Start --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Truncate_Stage
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Merge_ItemMasterProducts
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Data_Flow___ItemMasterProducts_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Error_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Delete_Old_Files --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Products___Log_Start
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Merge_ItemMasterProducts --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master___Products_XML_Update_Log___Success
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Data_Flow___Items_UOM_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Stage_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Data_Flow___Items_UOM_XML
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Delete_Old_Files --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_UOM___Log_Start
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Truncate_Stage --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Stage_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_UOM___Log_Start --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Truncate_Stage
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Data_Flow___Items_UOM_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Error_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Merge_Items_UOM
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Merge_Items_UOM --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Success
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Merge_Items_UOM --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_UOM_XML_Update_Log___Merge_Error
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Data_Flow___Item_Master_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Stage_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Data_Flow___Item_Master_XML
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Delete_Old_Files --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_ItemMaster___Log_Start
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Truncate_Stage --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Stage_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Data_Flow___Item_Master_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Error_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_ItemMaster___Log_Start --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Truncate_Stage
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Merge_ItemMaster
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Merge_ItemMaster --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Merge_Error
    n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Merge_ItemMaster --> n_Package_Data_Load_Sequence_Foreach_Loop___Item_Master_XML_Update_Log___Success
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Stage_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Data_Flow___Vendor_XML
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Data_Flow___Vendor_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Delete_Old_Files --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Vendors___Log_Start
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Data_Flow___Vendor_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Truncate_Stage --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Stage_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Vendors___Log_Start --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Truncate_Stage
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Error_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Merge_VendorMaster
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Merge_VendorMaster --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Success
    n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Merge_VendorMaster --> n_Package_Data_Load_Sequence_Foreach_Loop___Vendors_Update_Log___Merge_Error
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Stage_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Data_Flow___Warehouse_XML
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Data_Flow___Warehouse_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Delete_Old_Files --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Warehouse___Log_Start
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Data_Flow___Warehouse_XML --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Truncate_Stage --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Stage_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Warehouse___Log_Start --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Truncate_Stage
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Archive_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Archive_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Merge_WarehouseMaster
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Merge_WarehouseMaster --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Success
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Error_File --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Error_File
    n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Merge_WarehouseMaster --> n_Package_Data_Load_Sequence_Foreach_Loop___Warehouse_Update_Log___Merge_Error
    n_Package_Data_Load_Sequence --> n_Package_Missing_Data_Check_Email
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | Entity | No |
| User | ItemMasterArchiveFileName | Yes |
| User | ItemMasterDropFolder | Yes |
| User | ItemMasterErrorFileName | Yes |
| User | ItemMasterOriginalFileName | No |
| User | ItemMasterProductsArchiveFileName | Yes |
| User | ItemMasterProductsErrorFileName | Yes |
| User | ItemMasterProductsOriginalFileName | No |
| User | ItemMasterProductsXMLFileName | Yes |
| User | ItemMasterXMLFileName | Yes |
| User | ItemUOMDropFolder | Yes |
| User | ItemUOMXMLFileName | Yes |
| User | ItemsUOMArchiveFileName | Yes |
| User | ItemsUOMErrorFileName | Yes |
| User | ItemsUOMOriginalFileName | No |
| User | ProductsDropFolder | Yes |
| User | VendorDropFolder | Yes |
| User | VendorMasterArchiveFileName | Yes |
| User | VendorMasterErrorFileName | Yes |
| User | VendorMasterOriginalFileName | No |
| User | VendorMasterXMLFileName | Yes |
| User | WarehouseDropFolder | Yes |
| User | WarehouseMasterArchiveFileName | Yes |
| User | WarehouseMasterErrorFileName | Yes |
| User | WarehouseMasterOriginalFileName | No |
| User | WarehouseMasterXMLFileName | Yes |

### Expression-bound variable values

#### User::ItemMasterArchiveFileName

**Expression:**

```sql
@[User::ItemMasterDropFolder] + "Archive\\ItemMaster." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ItemMaster.2020312124940950.xml
```

#### User::ItemMasterDropFolder

**Expression:**

```sql
@[$Package::ERP_ItemMasterDropFolder] + @[User::Entity] + "\\Outbound\\"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\
```

#### User::ItemMasterErrorFileName

**Expression:**

```sql
@[User::ItemMasterDropFolder] + "Archive\\ErrorFiles\\ItemMaster.Error." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ErrorFiles\ItemMaster.Error.2020312124940950.xml
```

#### User::ItemMasterProductsArchiveFileName

**Expression:**

```sql
@[User::ProductsDropFolder] + "Archive\\ItemMasterProducts." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ItemMasterProducts.2020312124940950.xml
```

#### User::ItemMasterProductsErrorFileName

**Expression:**

```sql
@[User::ProductsDropFolder] + "Archive\\ErrorFiles\\ItemMasterProducts.Error." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ErrorFiles\ItemMasterProducts.Error.2020312124940950.xml
```

#### User::ItemMasterProductsXMLFileName

**Expression:**

```sql
@[User::ProductsDropFolder] + "ETLStage\\ItemMasterProducts.xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\ETLStage\ItemMasterProducts.xml
```

#### User::ItemMasterXMLFileName

**Expression:**

```sql
@[User::ItemMasterDropFolder] + "ETLStage\\ItemMaster.xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\ETLStage\ItemMaster.xml
```

#### User::ItemUOMDropFolder

**Expression:**

```sql
@[$Package::ERP_ItemUOMDropFolder] +  @[User::Entity] + "\\Outbound\\"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\
```

#### User::ItemUOMXMLFileName

**Expression:**

```sql
@[User::ItemUOMDropFolder] + "ETLStage\\ItemsUOM.xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\ETLStage\ItemsUOM.xml
```

#### User::ItemsUOMArchiveFileName

**Expression:**

```sql
@[User::ItemUOMDropFolder] + "Archive\\ItemsUOM." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ItemsUOM.2020312124940950.xml
```

#### User::ItemsUOMErrorFileName

**Expression:**

```sql
@[User::ItemUOMDropFolder] + "Archive\\ErrorFiles\\ItemsUOM.Error." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ErrorFiles\ItemsUOM.Error.2020312124940950.xml
```

#### User::ProductsDropFolder

**Expression:**

```sql
@[$Package::ERP_ProductFileDropFolder] +  @[User::Entity] + "\\Outbound\\"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\
```

#### User::VendorDropFolder

**Expression:**

```sql
@[$Package::ERP_VendorFileDropFolder] +  @[User::Entity] + "\\"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Vendors\prod\1200\
```

#### User::VendorMasterArchiveFileName

**Expression:**

```sql
@[User::VendorDropFolder] + "Archive\\VendorMaster." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Vendors\prod\1200\Archive\VendorMaster.2020312124940953.xml
```

#### User::VendorMasterErrorFileName

**Expression:**

```sql
@[User::VendorDropFolder] + "Archive\\ErrorFiles\\VendorMaster.Error." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Vendors\prod\1200\Archive\ErrorFiles\VendorMaster.Error.2020312124940953.xml
```

#### User::VendorMasterXMLFileName

**Expression:**

```sql
@[User::VendorDropFolder] + "ETLStage\\VendorMaster.xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Vendors\prod\1200\ETLStage\VendorMaster.xml
```

#### User::WarehouseDropFolder

**Expression:**

```sql
@[$Package::ERP_WarehouseFileDropFolder] +  @[User::Entity] + "\\"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Warehouse\prod\1200\
```

#### User::WarehouseMasterArchiveFileName

**Expression:**

```sql
@[User::WarehouseDropFolder] + "Archive\\WarehouseMaster." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Warehouse\prod\1200\Archive\WarehouseMaster.2020312124940953.xml
```

#### User::WarehouseMasterErrorFileName

**Expression:**

```sql
@[User::WarehouseDropFolder] + "Archive\\ErrorFiles\\WarehouseMaster.Error." + 
(DT_WSTR, 4) YEAR( getdate()  ) +  (DT_WSTR, 2) MONTH( getdate()  ) + (DT_WSTR, 2) DAY( getdate()  ) +  (DT_WSTR, 2) DATEPART("Hh", getdate() ) + (DT_WSTR, 2) DATEPART("mi", getdate() )+ (DT_WSTR, 2) DATEPART("ss", getdate() ) + (DT_WSTR, 3) DATEPART("ms", getdate() )+ ".xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Warehouse\prod\1200\Archive\ErrorFiles\WarehouseMaster.Error.2020312124940953.xml
```

#### User::WarehouseMasterXMLFileName

**Expression:**

```sql
@[User::WarehouseDropFolder] + "ETLStage\\WarehouseMaster.xml"
```

**Evaluated value:**

```sql
\\stl-dynsnc-P-01\BABWIntegrations\Warehouse\prod\1200\ETLStage\WarehouseMaster.xml
```

## Execute SQL Tasks

### Delete Old Files

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Delete Old Files`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec spDeleteOldFiles @path = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\', @filemask = '*.xml', @retention = 7
```

**Property expression (runtime override):**

```sql
"exec spDeleteOldFiles @path = '" + @[User::ProductsDropFolder] + "Archive\\', @filemask = '*.xml', @retention = 7"
```

### Merge ItemMasterProducts

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Merge ItemMasterProducts`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeItemMasterProducts
```

### Products - Log Start

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Products - Log Start`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
insert ERP.IntegrationLog (ProcessName, ProcessDateTime, TaskName, Entity, ImportFilename) 
values (?,?,?,?,?)
```

### Truncate Stage

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.ItemMasterProductsStage


```

### Update Log - Archive File

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Update Log - Archive File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ArchiveFileName = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ItemMasterProducts.2020312124940940.xml', DataStaged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ArchiveFileName = '" + @[User::ItemMasterProductsArchiveFileName]  + "', DataStaged = 1 where ImportFileName = '" + @[User::ItemMasterProductsOriginalFileName]  + "'"
```

### Update Log - Error File

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Update Log - Error File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ErrorFileName = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ErrorFiles\ItemMasterProducts.Error.2020312124940940.xml' where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ErrorFileName = '" + @[User::ItemMasterProductsErrorFileName]  + "' where ImportFileName = '" + @[User::ItemMasterProductsOriginalFileName]  + "'"
```

### Update Log - Merge Error

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Update Log - Merge Error`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = '" + @[User::ItemMasterProductsOriginalFileName]  + "'"
```

### Update Log - Success

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master - Products XML\Update Log - Success`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = '" + @[User::ItemMasterProductsOriginalFileName]  + "'"
```

### Delete Old Files

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\Delete Old Files`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec spDeleteOldFiles @path = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\', @filemask = '*.xml', @retention = 7
```

**Property expression (runtime override):**

```sql
"exec spDeleteOldFiles @path = '" + @[User::ItemUOMDropFolder] + "Archive\\', @filemask = '*.xml', @retention = 7"
```

### Merge Items UOM

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\Merge Items UOM`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeItemsUOM
```

### Truncate Stage

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.ItemsUOMStage

```

### UOM - Log Start

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\UOM - Log Start`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
insert ERP.IntegrationLog (ProcessName, ProcessDateTime, TaskName, Entity, ImportFilename) 
values (?,?,?,?,?)
```

### Update Log - Archive File

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\Update Log - Archive File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ArchiveFileName = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ItemsUOM.2020312124940943.xml', DataStaged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ArchiveFileName = '" + @[User::ItemsUOMArchiveFileName]  + "', DataStaged = 1 where ImportFileName = '" + @[User::ItemsUOMOriginalFileName]  + "'"
```

### Update Log - Error File

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\Update Log - Error File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ErrorFileName = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ErrorFiles\ItemsUOM.Error.2020312124940943.xml' where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ErrorFileName = '" + @[User::ItemsUOMErrorFileName]  + "' where ImportFileName = '" + @[User::ItemsUOMOriginalFileName]  + "'"
```

### Update Log - Merge Error

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\Update Log - Merge Error`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = '" + @[User::ItemsUOMOriginalFileName]  + "'"
```

### Update Log - Success

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master UOM XML\Update Log - Success`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = '" + @[User::ItemsUOMOriginalFileName]  + "'"
```

### Delete Old Files

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\Delete Old Files`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec spDeleteOldFiles @path = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\', @filemask = '*.xml', @retention = 1
```

**Property expression (runtime override):**

```sql
"exec spDeleteOldFiles @path = '" + @[User::ItemMasterDropFolder] + "Archive\\', @filemask = '*.xml', @retention = 1"
```

### ItemMaster - Log Start

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\ItemMaster - Log Start`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
insert ERP.IntegrationLog (ProcessName, ProcessDateTime, TaskName, Entity, ImportFilename) 
values (?,?,?,?,?)
```

### Merge ItemMaster

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\Merge ItemMaster`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeItemMaster
```

### Truncate Stage

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.ItemMasterStage


```

### Update Log - Archive File

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\Update Log - Archive File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ArchiveFileName = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ItemMaster.2020312124940943.xml', DataStaged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ArchiveFileName = '" + @[User::ItemMasterArchiveFileName]  + "', DataStaged = 1 where ImportFileName = '" + @[User::ItemMasterOriginalFileName]  + "'"
```

### Update Log - Error File

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\Update Log - Error File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ErrorFileName = '\\stl-dynsnc-P-01\BABWIntegrations\WMS_Items\prod\1200\Outbound\Archive\ErrorFiles\ItemMaster.Error.2020312124940943.xml' where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ErrorFileName = '" + @[User::ItemMasterErrorFileName]  + "' where ImportFileName = '" + @[User::ItemMasterOriginalFileName]  + "'"
```

### Update Log - Merge Error

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\Update Log - Merge Error`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = '" + @[User::ItemMasterOriginalFileName]  + "'"
```

### Update Log - Success

**Path:** `Package\Data Load Sequence\Foreach Loop - Item Master XML\Update Log - Success`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = '" + @[User::ItemMasterOriginalFileName]  + "'"
```

### Delete Old Files

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Delete Old Files`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec spDeleteOldFiles @path = '\\stl-dynsnc-P-01\BABWIntegrations\Vendors\prod\1200\Archive\', @filemask = '*.xml', @retention = 7
```

**Property expression (runtime override):**

```sql
"exec spDeleteOldFiles @path = '" + @[User::VendorDropFolder] + "Archive\\', @filemask = '*.xml', @retention = 7"
```

### Merge VendorMaster

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Merge VendorMaster`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeVendorMaster
```

### Truncate Stage

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.VendorMasterStage


```

### Update Log - Archive File

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Update Log - Archive File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ArchiveFileName = '\\stl-dynsnc-P-01\BABWIntegrations\Vendors\prod\1200\Archive\VendorMaster.2020312124940947.xml', DataStaged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ArchiveFileName = '" + @[User::VendorMasterArchiveFileName]  + "', DataStaged = 1 where ImportFileName = '" + @[User::VendorMasterOriginalFileName]  + "'"
```

### Update Log - Error File

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Update Log - Error File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ErrorFileName = '\\stl-dynsnc-P-01\BABWIntegrations\Vendors\prod\1200\Archive\ErrorFiles\VendorMaster.Error.2020312124940947.xml' where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ErrorFileName = '" + @[User::VendorMasterErrorFileName]  + "' where ImportFileName = '" + @[User::VendorMasterOriginalFileName]  + "'"
```

### Update Log - Merge Error

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Update Log - Merge Error`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = '" + @[User::VendorMasterOriginalFileName]  + "'"
```

### Update Log - Success

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Update Log - Success`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = '" + @[User::VendorMasterOriginalFileName]  + "'"
```

### Vendors - Log Start

**Path:** `Package\Data Load Sequence\Foreach Loop - Vendors\Vendors - Log Start`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
insert ERP.IntegrationLog (ProcessName, ProcessDateTime, TaskName, Entity, ImportFilename) 
values (?,?,?,?,?)
```

### Delete Old Files

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Delete Old Files`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec spDeleteOldFiles @path = '\\stl-dynsnc-P-01\BABWIntegrations\Warehouse\prod\1200\Archive\', @filemask = '*.xml', @retention = 7
```

**Property expression (runtime override):**

```sql
"exec spDeleteOldFiles @path = '" + @[User::WarehouseDropFolder] + "Archive\\', @filemask = '*.xml', @retention = 7"
```

### Merge WarehouseMaster

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Merge WarehouseMaster`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeWarehouseMaster 
```

### Truncate Stage

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.WarehouseMasterStage

```

### Update Log - Archive File

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Update Log - Archive File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ArchiveFileName = '\\stl-dynsnc-P-01\BABWIntegrations\Warehouse\prod\1200\Archive\WarehouseMaster.2020312124940947.xml', DataStaged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ArchiveFileName = '" + @[User::WarehouseMasterArchiveFileName]  + "', DataStaged = 1 where ImportFileName = '" + @[User::WarehouseMasterOriginalFileName]  + "'"
```

### Update Log - Error File

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Update Log - Error File`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set ErrorFileName = '\\stl-dynsnc-P-01\BABWIntegrations\Warehouse\prod\1200\Archive\ErrorFiles\WarehouseMaster.Error.2020312124940947.xml' where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set ErrorFileName = '" + @[User::WarehouseMasterErrorFileName]  + "' where ImportFileName = '" + @[User::WarehouseMasterOriginalFileName]  + "'"
```

### Update Log - Merge Error

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Update Log - Merge Error`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 0 where ImportFileName = '" + @[User::WarehouseMasterOriginalFileName]  + "'"
```

### Update Log - Success

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Update Log - Success`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = 'o.xml'
```

**Property expression (runtime override):**

```sql
"update ERP.IntegrationLog set DataMerged = 1 where ImportFileName = '" + @[User::WarehouseMasterOriginalFileName]  + "'"
```

### Warehouse - Log Start

**Path:** `Package\Data Load Sequence\Foreach Loop - Warehouse\Warehouse - Log Start`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
insert ERP.IntegrationLog (ProcessName, ProcessDateTime, TaskName, Entity, ImportFilename) 
values (?,?,?,?,?)
```

### spEmailItemsMissingDimensionData

**Path:** `Package\Missing Data Check Email\spEmailItemsMissingDimensionData`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spEmailItemsMissingDimensionData
```

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| ItemMasterProductsStage |  | OLEDBDestination | Data Flow - ItemMasterProducts XML | IntegrationStaging |  |
| ItemsUOMStage |  | OLEDBDestination | Data Flow - Items UOM XML | IntegrationStaging |  |
| ItemMasterStage |  | OLEDBDestination | Data Flow - Item Master XML | IntegrationStaging |  |
| VendorMasterStage |  | OLEDBDestination | Data Flow - Vendor XML | IntegrationStaging |  |
| WarehouseMasterStage |  | OLEDBDestination | Data Flow - Warehouse XML | IntegrationStaging |  |
