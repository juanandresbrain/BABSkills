# SSIS Package: WMS_TransferOrderCreateFromAptos

**Project:** WMS_TransferOrderCreateFromAptos  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| Flat File Connection Manager | FLATFILE |  |  |  |
| GetBlobUrl | HTTP (KingswaySoft) |  |  |  |
| GetStatus | HTTP (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| ME_01 | OLEDB | bedrockdb02 | me_01 | Data Source=bedrockdb02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| MerchProd | OLEDB | bedrockdb02 | me_01 | Data Source=bedrockdb02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| POtoSOCreateAPI | HTTP (KingswaySoft) |  |  |  |
| PostTriggerImport | HTTP (KingswaySoft) |  |  |  |
| SMTP | SMTP |  |  |  |
| SalesOrderCreateXML | FLATFILE |  |  |  |
| TOCreateAPI | HTTP (KingswaySoft) |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| WMS_TransferOrderCreateFromAptos | Package |
| File Generation and Move | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| DataFlow XML File | Pipeline |
| DataFlow XML File OLD | Pipeline |
| Foreach Loop - Copy Manifest and Header Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Foreach SalesOrder Create | FOREACHLOOP |
| Foreach Loop Container | FOREACHLOOP |
| Archive Files | FileSystemTask |
| azCopy to Blob | ExecuteProcess |
| ProcessStatus For Loop | FORLOOP |
| Get Summary Status | Pipeline |
| Set ProcessStatus | ExecuteSQLTask |
| Wait 30 Seconds | ExecuteSQLTask |
| Set BatchID - LoopCount | ExecuteSQLTask |
| Set BAtchID and ExportFlag SO | ExecuteSQLTask |
| Set RowsCount | ExecuteSQLTask |
| Stage Blob URL | Pipeline |
| Trigger Import | Pipeline |
| Zip File | ExecuteProcess |
| Stage Company Entities | ExecuteSQLTask |
| ON DEMAND | SEQUENCE |
| AptosShipmentNumber Stage | ExecuteSQLTask |
| Foreach Loop - SalesOders API | FOREACHLOOP |
| DataFlow - POtoSOCreate API | Pipeline |
| SEQ - Export Distros From Merch to Store Shipments | SEQUENCE |
| PreStage Store Shipments from Merch | ExecuteSQLTask |
| SEQ - Stage StoreShipments to IntegrationStaging | SEQUENCE |
| Data Flow StoreShipmentExportStage | Pipeline |
| Merge StoreShipmentExport | ExecuteSQLTask |
| Set Exported Flag | ExecuteSQLTask |
| Truncate Stage | ExecuteSQLTask |
| SEQ - TOCreate and POtoSOCreate | SEQUENCE |
| Sales Order Sequence | SEQUENCE |
| AptosShipmentNumber Stage | ExecuteSQLTask |
| Foreach Loop - SalesOders API | FOREACHLOOP |
| DataFlow - POtoSOCreate API | Pipeline |
| Set BAtchID and ExportFlag SO | ExecuteSQLTask |
| Transfer Order Sequence | SEQUENCE |
| AptosShipmentNumber Stage | ExecuteSQLTask |
| Foreach Loop - TransferOrder API | FOREACHLOOP |
| DataFlow - TOCreate API | Pipeline |
| Set BAtchID and ExportFlag TO | ExecuteSQLTask |
| SEQ Validation | SEQUENCE |
| Distro Export Validation Stage | Pipeline |
| Email Summary | ExecuteSQLTask |
| Email Validation | ExecuteSQLTask |
| Store Shipment Export Stage | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- File Generation and Move [SEQUENCE]
  - Foreach Loop - Per Entity [FOREACHLOOP]
    - DataFlow XML File [Pipeline]
    - DataFlow XML File OLD [Pipeline]
    - Foreach Loop - Copy Manifest and Header Files [FOREACHLOOP]
      - Copy Manifest & Header [FileSystemTask]
    - Foreach SalesOrder Create [FOREACHLOOP]
      - Foreach Loop Container [FOREACHLOOP]
        - Archive Files [FileSystemTask]
        - azCopy to Blob [ExecuteProcess]
      - ProcessStatus For Loop [FORLOOP]
        - Get Summary Status [Pipeline]
        - Set ProcessStatus [ExecuteSQLTask]
        - Wait 30 Seconds [ExecuteSQLTask]
      - Set BAtchID and ExportFlag SO [ExecuteSQLTask]
      - Set BatchID - LoopCount [ExecuteSQLTask]
      - Set RowsCount [ExecuteSQLTask]
      - Stage Blob URL [Pipeline]
      - Trigger Import [Pipeline]
    - Zip File [ExecuteProcess]
  - Stage Company Entities [ExecuteSQLTask]
- ON DEMAND [SEQUENCE]
  - AptosShipmentNumber Stage [ExecuteSQLTask]
  - Foreach Loop - SalesOders API [FOREACHLOOP]
    - DataFlow - POtoSOCreate API [Pipeline]
- SEQ - Export Distros From Merch to Store Shipments [SEQUENCE]
  - PreStage Store Shipments from Merch [ExecuteSQLTask]
- SEQ - Stage StoreShipments to IntegrationStaging [SEQUENCE]
  - Data Flow StoreShipmentExportStage [Pipeline]
  - Merge StoreShipmentExport [ExecuteSQLTask]
  - Set Exported Flag [ExecuteSQLTask]
  - Truncate Stage [ExecuteSQLTask]
- SEQ - TOCreate and POtoSOCreate [SEQUENCE]
  - Sales Order Sequence [SEQUENCE]
    - AptosShipmentNumber Stage [ExecuteSQLTask]
    - Foreach Loop - SalesOders API [FOREACHLOOP]
      - DataFlow - POtoSOCreate API [Pipeline]
      - Set BAtchID and ExportFlag SO [ExecuteSQLTask]
  - Transfer Order Sequence [SEQUENCE]
    - AptosShipmentNumber Stage [ExecuteSQLTask]
    - Foreach Loop - TransferOrder API [FOREACHLOOP]
      - DataFlow - TOCreate API [Pipeline]
      - Set BAtchID and ExportFlag TO [ExecuteSQLTask]
- SEQ Validation [SEQUENCE]
  - Distro Export Validation Stage [Pipeline]
  - Email Summary [ExecuteSQLTask]
  - Email Validation [ExecuteSQLTask]
  - Store Shipment Export Stage [Pipeline]
  - Truncate Stage [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_File_Generation_and_Move["File Generation and Move"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_XML_File["DataFlow XML File"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_XML_File_OLD["DataFlow XML File OLD"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files["Foreach Loop - Copy Manifest and Header Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create["Foreach SalesOrder Create"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop_Wait_30_Seconds["Wait 30 Seconds"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_BAtchID_and_ExportFlag_SO["Set BAtchID and ExportFlag SO"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_RowsCount["Set RowsCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Stage_Blob_URL["Stage Blob URL"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Trigger_Import["Trigger Import"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File["Zip File"]
    n_Package_File_Generation_and_Move_Stage_Company_Entities["Stage Company Entities"]
    n_Package_ON_DEMAND["ON DEMAND"]
    n_Package_ON_DEMAND_AptosShipmentNumber_Stage["AptosShipmentNumber Stage"]
    n_Package_ON_DEMAND_Foreach_Loop___SalesOders_API["Foreach Loop - SalesOders API"]
    n_Package_ON_DEMAND_Foreach_Loop___SalesOders_API_DataFlow___POtoSOCreate_API["DataFlow - POtoSOCreate API"]
    n_Package_SEQ___Export_Distros_From_Merch_to_Store_Shipments["SEQ - Export Distros From Merch to Store Shipments"]
    n_Package_SEQ___Export_Distros_From_Merch_to_Store_Shipments_PreStage_Store_Shipments_from_Merch["PreStage Store Shipments from Merch"]
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging["SEQ - Stage StoreShipments to IntegrationStaging"]
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Data_Flow_StoreShipmentExportStage["Data Flow StoreShipmentExportStage"]
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Merge_StoreShipmentExport["Merge StoreShipmentExport"]
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Set_Exported_Flag["Set Exported Flag"]
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Truncate_Stage["Truncate Stage"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate["SEQ - TOCreate and POtoSOCreate"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence["Sales Order Sequence"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_AptosShipmentNumber_Stage["AptosShipmentNumber Stage"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_Foreach_Loop___SalesOders_API["Foreach Loop - SalesOders API"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_Foreach_Loop___SalesOders_API_DataFlow___POtoSOCreate_API["DataFlow - POtoSOCreate API"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_Foreach_Loop___SalesOders_API_Set_BAtchID_and_ExportFlag_SO["Set BAtchID and ExportFlag SO"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence["Transfer Order Sequence"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_AptosShipmentNumber_Stage["AptosShipmentNumber Stage"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_Foreach_Loop___TransferOrder_API["Foreach Loop - TransferOrder API"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_Foreach_Loop___TransferOrder_API_DataFlow___TOCreate_API["DataFlow - TOCreate API"]
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_Foreach_Loop___TransferOrder_API_Set_BAtchID_and_ExportFlag_TO["Set BAtchID and ExportFlag TO"]
    n_Package_SEQ_Validation["SEQ Validation"]
    n_Package_SEQ_Validation_Distro_Export_Validation_Stage["Distro Export Validation Stage"]
    n_Package_SEQ_Validation_Email_Summary["Email Summary"]
    n_Package_SEQ_Validation_Email_Validation["Email Validation"]
    n_Package_SEQ_Validation_Store_Shipment_Export_Stage["Store Shipment Export Stage"]
    n_Package_SEQ_Validation_Truncate_Stage["Truncate Stage"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Foreach_Loop_Container_Archive_Files
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop_Wait_30_Seconds --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Stage_Blob_URL --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_RowsCount
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Trigger_Import --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_ProcessStatus_For_Loop
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Foreach_Loop_Container --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Trigger_Import
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_BatchID___LoopCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Stage_Blob_URL
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_RowsCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Foreach_Loop_Container
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_BatchID___LoopCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create_Set_BAtchID_and_ExportFlag_SO
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_XML_File --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_SalesOrder_Create
    n_Package_File_Generation_and_Move_Stage_Company_Entities --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity
    n_Package_ON_DEMAND_AptosShipmentNumber_Stage --> n_Package_ON_DEMAND_Foreach_Loop___SalesOders_API
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Truncate_Stage --> n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Data_Flow_StoreShipmentExportStage
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Data_Flow_StoreShipmentExportStage --> n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Set_Exported_Flag
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Set_Exported_Flag --> n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging_Merge_StoreShipmentExport
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_Foreach_Loop___SalesOders_API_DataFlow___POtoSOCreate_API --> n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_Foreach_Loop___SalesOders_API_Set_BAtchID_and_ExportFlag_SO
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_AptosShipmentNumber_Stage --> n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence_Foreach_Loop___SalesOders_API
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_Foreach_Loop___TransferOrder_API_DataFlow___TOCreate_API --> n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_Foreach_Loop___TransferOrder_API_Set_BAtchID_and_ExportFlag_TO
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_AptosShipmentNumber_Stage --> n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence_Foreach_Loop___TransferOrder_API
    n_Package_SEQ___TOCreate_and_POtoSOCreate_Transfer_Order_Sequence --> n_Package_SEQ___TOCreate_and_POtoSOCreate_Sales_Order_Sequence
    n_Package_SEQ_Validation_Truncate_Stage --> n_Package_SEQ_Validation_Distro_Export_Validation_Stage
    n_Package_SEQ_Validation_Distro_Export_Validation_Stage --> n_Package_SEQ_Validation_Store_Shipment_Export_Stage
    n_Package_SEQ_Validation_Store_Shipment_Export_Stage --> n_Package_SEQ_Validation_Email_Validation
    n_Package_SEQ_Validation_Email_Summary --> n_Package_SEQ_Validation_Truncate_Stage
    n_Package_SEQ___Export_Distros_From_Merch_to_Store_Shipments --> n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging
    n_Package_SEQ___Stage_StoreShipments_to_IntegrationStaging --> n_Package_SEQ___TOCreate_and_POtoSOCreate
    n_Package_File_Generation_and_Move --> n_Package_SEQ_Validation
    n_Package_SEQ___TOCreate_and_POtoSOCreate --> n_Package_File_Generation_and_Move
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | AptosShipmentNumberInLoop | No |
| User | AptosShipmentNumberStage | No |
| User | ArchiveFolder | Yes |
| User | AzCopytoBlobCommand | Yes |
| User | BatchID | No |
| User | BlobURL | No |
| User | BlobURLRecordSet | No |
| User | CompanyEntities | No |
| User | DataEntityName | No |
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
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | ZipCommand | Yes |
| User | ZipDest | Yes |
| User | ZipSource | Yes |

### Expression-bound variable values

#### User::ArchiveFolder

**Expression:**

```sql
@[$Package::WMS_SalesOrderCreateFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesOrderCreate\Archive\
```

#### User::AzCopytoBlobCommand

**Expression:**

```sql
"cp \"" +  @[User::ZipDest] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesOrderCreate\SalesOrderCreate1700.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
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
202282144725860
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
8/2/2022
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
2022-8-2
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
8/2/2022
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
2022-8-2
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
@[$Package::WMS_PackageAPI_StaticPackageFilesPath] + "SalesOrderCreate"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\SalesOrderCreate
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
where Entity = '1700'
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
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[$Package::WMS_SalesOrderCreateBlobDefinitionGroupID] + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as executionId, 'InterCoCreate1700' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1700' as legalEntityId
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
8/1/2022
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
2022-8-1
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesOrderCreate\SalesOrderCreate1700.zip"  "*.xml" -sdel
```

#### User::ZipDest

**Expression:**

```sql
@[$Package::WMS_SalesOrderCreateFileStageLocation]  + "SalesOrderCreate" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesOrderCreate\SalesOrderCreate1700.zip
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

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach SalesOrder Create\ProcessStatus For Loop\Set ProcessStatus`  
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
  when ? < 200 --- designed to let the loop escape if still not finihed after 20 loops
   then count(*)
  else 1
 end as ProcessStatus
from ProcStatus
where ProcessStatus = 1
```

### Wait 30 Seconds

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach SalesOrder Create\ProcessStatus For Loop\Wait 30 Seconds`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:30'
```

### Set BAtchID and ExportFlag SO

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach SalesOrder Create\Set BAtchID and ExportFlag SO`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update sse
set 
	sse.ExportDate=getdate(),
	sse.BatchID = '5ECF043F-9E41-46F7-9FE9-0634BCE2C644' 
from WMS.StoreShipmentExport sse 
where 
	sse.ExportDate is NULL 
	and OrderType='SalesOrder' 
	and AptosShipmentNumber = ''
```

**Property expression (runtime override):**

```sql
"update sse
set 
	sse.ExportDate=getdate(),
	sse.BatchID = '" +  @[User::BatchID] + "' 
from WMS.StoreShipmentExport sse 
where 
	sse.ExportDate is NULL 
	and OrderType='SalesOrder' 
	and AptosShipmentNumber = '" +  @[User::AptosShipmentNumberInLoop] + "'"
```

### Set BatchID - LoopCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach SalesOrder Create\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach SalesOrder Create\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### Stage Company Entities

**Path:** `Package\File Generation and Move\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
WITH
ProdView as ---PRE-ECO PROD VIEW (THE UPDATED VIEW FOR TEST IS vwStoreShipmentsToDynamicsPOtoSO AND WILL BE USED WHEN WE HAVE ALL WHSES INTERFACING IN DYNAMICS)
 (
  select 
   Entity,
   BABAptosShipmentNumber as AptosShipmentNumber
  from wms.vwStoreShipmentsToDynamicsPOtoSO
 )
select 
  Entity,
 AptosShipmentNumber, 
count(*) as Rowz
from ProdView
group by Entity,AptosShipmentNumber 
```

### AptosShipmentNumber Stage

**Path:** `Package\ON DEMAND\AptosShipmentNumber Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select AptosShipmentNumber
from wms.SToreShipmentExport
where 1=1
--and ExportDate is NULL
and CountryCode <> 'US'
and AptosShipmentNumber='2900120341'
group by AptosShipmentNumber
```

### PreStage Store Shipments from Merch

**Path:** `Package\SEQ - Export Distros From Merch to Store Shipments\PreStage Store Shipments from Merch`  
**Connection:** ME_01 (bedrockdb02/me_01)  

```sql
exec spMerchandisingStageDistrosToStoreShipments
```

### Merge StoreShipmentExport

**Path:** `Package\SEQ - Stage StoreShipments to IntegrationStaging\Merge StoreShipmentExport`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec WMS.spMergeStoreShipmentExport
```

### Set Exported Flag

**Path:** `Package\SEQ - Stage StoreShipments to IntegrationStaging\Set Exported Flag`  
**Connection:** ME_01 (bedrockdb02/me_01)  

```sql
update store_shipment_export
set exported=1
where exported is NULL	
```

### Truncate Stage

**Path:** `Package\SEQ - Stage StoreShipments to IntegrationStaging\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE WMS.StoreShipmentExportStage
```

### AptosShipmentNumber Stage

**Path:** `Package\SEQ - TOCreate and POtoSOCreate\Sales Order Sequence\AptosShipmentNumber Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select AptosShipmentNumber
from wms.StoreShipmentExport
where ExportDate is NULL
and OrderType='SalesOrder'
group by AptosShipmentNumber

/*
select AptosShipmentNumber
from wms.SToreShipmentExport
where ExportDate is NULL
and CountryCode <> 'US'
group by AptosShipmentNumber
*/

```

### Set BAtchID and ExportFlag SO

**Path:** `Package\SEQ - TOCreate and POtoSOCreate\Sales Order Sequence\Foreach Loop - SalesOders API\Set BAtchID and ExportFlag SO`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update sse
set 
	sse.ExportDate=getdate(),
	sse.BatchID = '{E53D5B89-026D-4C24-BC23-D49BD931C6D9}' 
from WMS.StoreShipmentExport sse 
where 
	sse.ExportDate is NULL 
	and AptosShipmentNumber = ''
```

**Property expression (runtime override):**

```sql
"update sse
set 
	sse.ExportDate=getdate(),
	sse.BatchID = '" +  @[System::ExecutionInstanceGUID] + "' 
from WMS.StoreShipmentExport sse 
where 
	sse.ExportDate is NULL 
	and AptosShipmentNumber = '" +  @[User::AptosShipmentNumberInLoop] + "'"
```

### AptosShipmentNumber Stage

**Path:** `Package\SEQ - TOCreate and POtoSOCreate\Transfer Order Sequence\AptosShipmentNumber Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select AptosShipmentNumber
from wms.StoreShipmentExport
where ExportDate is NULL
and OrderType='TransferOrder'
group by AptosShipmentNumber

/*
select AptosShipmentNumber
from wms.SToreShipmentExport
where ExportDate is NULL
and CountryCode = 'US'
group by AptosShipmentNumber
*/
```

### Set BAtchID and ExportFlag TO

**Path:** `Package\SEQ - TOCreate and POtoSOCreate\Transfer Order Sequence\Foreach Loop - TransferOrder API\Set BAtchID and ExportFlag TO`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
update sse
set 
	sse.ExportDate=getdate(),
	sse.BatchID = '{E53D5B89-026D-4C24-BC23-D49BD931C6D9}' 
from WMS.StoreShipmentExport sse 
where 
	sse.ExportDate is NULL 
	and AptosShipmentNumber = ''
```

**Property expression (runtime override):**

```sql
"update sse
set 
	sse.ExportDate=getdate(),
	sse.BatchID = '" +  @[System::ExecutionInstanceGUID] + "' 
from WMS.StoreShipmentExport sse 
where 
	sse.ExportDate is NULL 
	and AptosShipmentNumber = '" +  @[User::AptosShipmentNumberInLoop] + "'"
```

### Email Summary

**Path:** `Package\SEQ Validation\Email Summary`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec WMS.spEmailTransferOrderSalesOrderExport '{E53D5B89-026D-4C24-BC23-D49BD931C6D9}'
```

**Property expression (runtime override):**

```sql
"exec WMS.spEmailTransferOrderSalesOrderExport '" +  @[System::ExecutionInstanceGUID] + "'"
```

### Email Validation

**Path:** `Package\SEQ Validation\Email Validation`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec WMS.spEmailAptosDistributionExportValidation
```

### Truncate Stage

**Path:** `Package\SEQ Validation\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
truncate table WMS.ValidationAptosDistroAfterSplit
truncate table WMS.ValidationAptosStoreShipmentExport
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| Sales Orders |  | OLEDBSource | DataFlow XML File | IntegrationStaging | SqlCommand |
| SalesOrders |  | OLEDBSource | DataFlow XML File OLD | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Import |  | OLEDBSource | Trigger Import | IntegrationStaging |  |
| OLE DB Source |  | OLEDBSource | DataFlow - POtoSOCreate API | IntegrationStaging | SqlCommand |
| Store_Shipment_Export |  | OLEDBSource | Data Flow StoreShipmentExportStage | ME_01 | SqlCommand |
| StoreShipmentExport |  | OLEDBSource | DataFlow - POtoSOCreate API | IntegrationStaging | SqlCommand |
| StoreShipmentExport |  | OLEDBSource | DataFlow - TOCreate API | IntegrationStaging | SqlCommand |
| me_01 - ddas - Distros from Past 7 Days |  | OLEDBSource | Distro Export Validation Stage | ME_01 | SqlCommand |
| me_01  - Store Shipment Export |  | OLEDBSource | Store Shipment Export Stage | ME_01 | SqlCommand |

#### Sales Orders — SqlCommand

```sql
WITH
ShipmentNumber as 
	(
		select BABAptosShipmentNumber 
		from wms.vwStoreShipmentsToDynamicsPOtoSO 
		where BABAptosShipmentNumber = ?
		group by BABAptosShipmentNumber
	),
X (xml) as
	(
			select 
					(
						select distinct 
							'' as [@PURCHASEORDERNUMBER],
							vw.BABAptosShipmentNumber as [@BABAPTOSPOSHIPMENTNUM],		
							vw.ToWarehouse as [@DEFAULTRECEIVINGSITEID],		
							vw.ToWarehouse as [@DEFAULTRECEIVINGWAREHOUSEID],	
							vw.ModeOfDelivery as [@DELIVERYMODEID],				
							'BestServe' as [@DELIVERYTERMSID],				
							vw.OrderVendorAccountNumber as [@ORDERVENDORACCOUNTNUMBER]
						for xml path('PurchPurchaseOrderHeaderV2Entity'), Type
					),
					(
						select
							'' as [@LINENUMBER],					
							vw.BABAptosDistroNumber as [@BABAPTOSPOLINEDISTRONUM],		
							vw.BABAptosDistroLineNumber as [@BABAPTOSPOLINEDISTROLINENUM],	
							vw.ItemNumber as [@ITEMNUMBER],					
							'AVAIL' as [@ORDEREDINVENTORYSTATUSID],	
							vw.quantity as [@ORDEREDPURCHASEQUANTITY],		
							vw.UOM as [@PURCHASEUNITSYMBOL],			
							vw.ShipDate as [@REQUESTEDSHIPPINGDATE],		
							vw.ReceiptDate as [@REQUESTEDDELIVERYDATE],
							vw.ToWarehouse as [@RECEIVINGSITEID],		
							vw.ToWarehouse as [@RECEIVINGWAREHOUSEID]
						from wms.vwStoreShipmentsToDynamicsPOtoSO vw
						join ShipmentNumber sn on vw.BABAptosShipmentNumber=sn.BABAptosShipmentNumber
						for xml path('PurchPurchaseOrderLineV2Entity'), Type
					)
			from wms.vwStoreShipmentsToDynamicsPOtoSO vw
			join ShipmentNumber sn on vw.BABAptosShipmentNumber=sn.BABAptosShipmentNumber
			group by 
				vw.BABAptosShipmentNumber,
				vw.ToWarehouse,
				vw.ModeOfDelivery,
				vw.OrderVendorAccountNumber
			for xml path('Document'), Type
	)
select cast(xml as nvarchar(max)) as x
from x
```

#### SalesOrders — SqlCommand

```sql
WITH
ProdView as ---PRE-ECO PROD VIEW (THE UPDATED VIEW FOR TEST IS vwStoreShipmentsToDynamicsPOtoSO AND WILL BE USED WHEN WE HAVE ALL WHSES INTERFACING IN DYNAMICS)
	(
		select 
			cast('1100' as varchar(4)) as Entity,
			--cast('CUST000058' as varchar(10)) as CustomerAccountNumber,
			cast(case 
					when wm.Entity = 1700 then 'CUST000058'
					when wm.Entity = 2110 then 'CUST000022'
					when wm.Entity = 3001 then 'CUST000059'
					else 'CUST000058'
				 end 
				as varchar(10)
				) as CustomerAccountNumber,
			ToWarehouse as StoreDepartment,
			--'None' as deliveryType,
			'Direct' as deliveryType,
			convert(varchar(10), ShipDate,101) as ShipDate,
			convert(varchar(10), ReceiptDate,101) as ReceiptDate,
			AptosShipmentNumber as BABAptosShipmentNumber,
			--AptosShipmentNumber + '00'	as BABAptosShipmentNumber,
			DeliveryTerms,
			--case when left(ModeOfDelivery, 5)='FEDEX' then 'INTLFX' else ModeOfDelivery end as ModeOfDelivery,
			isnull(ModeOfDelivery,1) ModeOfDelivery,
			ToWarehouse,
			FromWarehouse,
			ItemNumber,	
			AptosDistroNumber as BABAptosDistroNumber,
			AptosDistroLineNumber as BABAptosDistroLineNumber,
			quantity,	
			UnitOfMeasure as UOM,	
			InventoryStatus
		from WMS.StoreShipmentExport sse
		join erp.WarehouseMaster wm on sse.ToWarehouse=wm.WarehouseID
		where 1=1
		and ExportDate is null
		and AptosShipmentNumber = ?
	),
X (xml) as
	(
			select 
					(
						select distinct 
							'' as [@PURCHASEORDERNUMBER],
							BABAptosShipmentNumber as [@BABAPTOSPOSHIPMENTNUM],		
							ToWarehouse as [@DEFAULTRECEIVINGSITEID],		
							ToWarehouse as [@DEFAULTRECEIVINGWAREHOUSEID],	
							ModeOfDelivery as [@DELIVERYMODEID],				
							'BestServe' as [@DELIVERYTERMSID],				
							case --for now will always bee 1100/99001
								when Entity=1100 then 99001 -- Canada Stores
								when Entity = 2110 then 99004 -- Denmark Stores
							end as [@ORDERVENDORACCOUNTNUMBER]
						for xml path('PurchPurchaseOrderHeaderV2Entity'), Type
					),
					(
						select
							'' as [@LINENUMBER],					
							BABAptosDistroNumber as [@BABAPTOSPOLINEDISTRONUM],		
							BABAptosDistroLineNumber as [@BABAPTOSPOLINEDISTROLINENUM],	
							ItemNumber as [@ITEMNUMBER],					
							'AVAIL' as [@ORDEREDINVENTORYSTATUSID],	
							quantity as [@ORDEREDPURCHASEQUANTITY],		
							UOM as [@PURCHASEUNITSYMBOL],			
							ShipDate as [@REQUESTEDSHIPPINGDATE],		
							ReceiptDate as [@REQUESTEDDELIVERYDATE],
							ToWarehouse as [@RECEIVINGSITEID],		
							ToWarehouse as [@RECEIVINGWAREHOUSEID]
						from ProdView
						for xml path('PurchPurchaseOrderLineV2Entity'), Type
					)
			from ProdView
			group by 
				BABAptosShipmentNumber,
				ToWarehouse,
				ModeOfDelivery,
				case --for now will always bee 1100/99001
					when Entity=1100 then 99001 -- Canada Stores
					when Entity = 2110 then 99004 -- Denmark Stores
				end
			for xml path('Document'), Type
	)
select cast(xml as nvarchar(max)) as x
from x
```

#### OLE DB Source — SqlCommand

```sql
select * 
from WMS.vwStoreShipmentsToDynamicsPOtoSO_ONDEMAND
where BABAptosShipmentNumber = ?
```

#### Store_Shipment_Export — SqlCommand

```sql
with 
--CountryFlag as
--	(
--		select 	
--			l.location_code as LocationCode,
--			c.country_code as CountryCode
--		from location l with (nolock)
--		inner join address a  with (nolock) on l.location_id = a.parent_id
--			and l.location_status_id <> 5
--			and	a.parent_type = 2
--			and	address_type_id = 1
--		join keith_country c with (nolock) on a.country_id = c.country_id
--	),
PreStage as
	(
		select  
			ss.warehouse as FromWarehouse,
			ss.location_code as ToWarehouse,
			cast(ss.rec_type as int) as rec_type,
			'BestServe' as DeliveryTerms,
			ss.document_number as AptosShipmentNumber,
			ss.style_code as ItemNumber,
			ss.distribution_number as AptosDistroNumber,
			ss.distribution_line_number as AptosDistroLineNumber,
			cast(ss.release_date as date) as ShipDate,
			Null as ReceiptDate, --need to derive this based on rec type, similar to how we estimate ERD on store shipments from warehouses
			ss.quantity,
			'ea' as UnitOfMeasure,
			'AVAIL' as InventoryStatus,
			case 
				when ss.rec_type in ('1','6','8','9','56','61','1006') then isnull(we.truck_980,7)--truck
				when ss.rec_type in ('54','58','80','81','82','83','84','1004') then isnull(we.ground_980,7)--ground
				when ss.rec_type in ('51','52','73','85','86','1001','1002') then '1'--1 day
				when ss.rec_type in ('53','74','87','1003','57','1007','62') then '2'--2 day -- includes courier and intnl priority
				when ss.rec_type in ('60','88','1010') then '3'--3 day
				when ss.rec_type in ('55','89','1005') then datediff(dd, datepart(dw, ss.release_date),7) -- saturday
				when ss.rec_type in ('63') then isnull(we.intnl_econ_980,5)--Intl Economy -- santiago will provide list by store, what's not provided will be 5 days
				when ss.rec_type in ('64','65') then '30'--30
				when ss.rec_type = '3' then isnull(we.supplySecond_980,7)
				when ss.rec_type = '7' then isnull(we.supplyThird_980,7)
				else 7
			end as transit_days,
			sm.cntry as CountryCode
		from store_shipment_export ss with (nolock)
		left join whse_erd we (nolock) on ss.location_code = we.location_code
		join VW_WMStoreMaster sm on ss.location_code=sm.Store_nbr 
		where ss.warehouse = '0980'
		--and datediff(dd, ss.release_date, getdate()) = 0 

		and datediff(dd, release_date, getdate()) = 0
	and warehouse = '0980'
	and datepart(hh, release_date) > 10
	)
select 
	FromWarehouse,
	ToWarehouse,
	rec_type,
	DeliveryTerms,
	AptosShipmentNumber,
	AptosDistroNumber,
	AptosDistroLineNumber,
	ItemNumber,
	ShipDate,
	case 
		when (datepart(dw, ShipDate) = 2 and transit_days > 4)
					or (datepart(dw, ShipDate) = 3 and transit_days > 3)
					or (datepart(dw, ShipDate) = 4 and transit_days > 2)
					or (datepart(dw, ShipDate) = 5 and transit_days > 1)
					or (datepart(dw, ShipDate) = 6)
		then cast(dateadd(day, (transit_days + 2), ShipDate) as date)
		when transit_days is NULL then cast(dateadd(day, (7), ShipDate) as date)
		else cast(dateadd(day, (transit_days), ShipDate) as date)
	end as ReceiptDate,
	quantity,
	UnitOfMeasure,
	InventoryStatus,
	CountryCode
from PreStage ps
--join CountryFlag c on ps.FromWarehouse=c.LocationCode
```

#### StoreShipmentExport — SqlCommand

```sql
select * 
from WMS.vwStoreShipmentsToDynamicsPOtoSO
where BABAptosShipmentNumber = ?
```

#### StoreShipmentExport — SqlCommand

```sql
select 
	ShipDate,	
	ReceiptDate,
	BABAptosShipmentNumber,	
	DeliveryTerms,	
	ModeOfDelivery,	
	ToWarehouse,	
	FromWarehouse,	
	ItemNumber,	
	BABAptosDistroNumber,	
	BABAptosDistroLineNumber,	
	quantity,	
	UOM,	
	InventoryStatus,	
	Company
from wms.vwStoreShipmentsToDynamicsTO
where BABAptosShipmentNumber = ?
```

#### me_01 - ddas - Distros from Past 7 Days — SqlCommand

```sql
--DISTROS FROM PAST 7 DAYS
select 
	ddas.distribution_number,
	ddas.ref_field_1 as distribution_line_number,
	ddas.SourceID,
	ddas.DestID,
	ddas.style_code,	
	ddas.rec_type,
	ddas.release_date,
	sse.document_number as StoreShipmentNumber
from distribution_data_after_split ddas with (nolock)
left join store_shipment_export sse with (nolock) 
	on ddas.distribution_number=sse.distribution_number
	and ddas.SourceID=sse.warehouse
	and ddas.DestID=sse.location_code
	and ddas.style_code=sse.style_code
	and ddas.rec_type=sse.rec_type
where 1=1
--and ddas.SourceID='0980'
and ddas.SourceID in ('0980','0960','2970') -- Added additional Warehouses 8/2/2022
and datediff(dd, ddas.release_date, getdate()) <= 7
and isnumeric(ddas.distribution_number) = 1 --excludes dynamics TO / SO
```

#### me_01  - Store Shipment Export — SqlCommand

```sql
--STORE SHIPMENTS STAGED PAST 7 DA7S
select 
	distribution_number,
	distribution_line_number,
	warehouse,
	location_code,
	style_code,
	rec_type,
	release_date,
	document_number as StoreShipmentNumber
from store_shipment_export
where 1=1
--and warehouse='0980'
and warehouse in ('0980','0960','2970') -- Added additional Warehouses 8/2/2022
and datediff(dd, release_date, getdate()) <= 7
and distribution_number <> 'DynamicsTo3PLOrdrExp' -- This is a place holder record for store shipment document numbers
and quantity <> 0 -- Invalid Records with a export quantity of 0
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| SalesOrderCreateXML |  | FlatFileDestination | DataFlow XML File | SalesOrderCreateXML |  |
| SalesOrderCreateXML |  | FlatFileDestination | DataFlow XML File OLD | SalesOrderCreateXML |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| Flat File Destination |  | FlatFileDestination | DataFlow - POtoSOCreate API | Flat File Connection Manager |  |
| StoreShipmentExportStage |  | OLEDBDestination | Data Flow StoreShipmentExportStage | IntegrationStaging |  |
| DynamicsAPIErrorLog |  | OLEDBDestination | DataFlow - POtoSOCreate API | IntegrationStaging |  |
| DynamicsAPILog |  | OLEDBDestination | DataFlow - POtoSOCreate API | IntegrationStaging |  |
| DynamicsAPILog |  | OLEDBDestination | DataFlow - TOCreate API | IntegrationStaging |  |
| WMS Validation Table |  | OLEDBDestination | Distro Export Validation Stage | IntegrationStaging |  |
| WMS Validation Table |  | OLEDBDestination | Store Shipment Export Stage | IntegrationStaging |  |
