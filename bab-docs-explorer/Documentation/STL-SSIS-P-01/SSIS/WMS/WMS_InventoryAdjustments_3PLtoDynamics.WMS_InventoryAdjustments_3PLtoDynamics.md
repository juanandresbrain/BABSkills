# SSIS Package: WMS_InventoryAdjustments_3PLtoDynamics

**Project:** WMS_InventoryAdjustments_3PLtoDynamics  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| ArchiveFolder | FILE |  |  |  |
| GetBlobUrl | HTTP (KingswaySoft) |  |  |  |
| GetStatus | HTTP (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| InventoryAdjustmentXML | FLATFILE |  |  |  |
| ME_01 | OLEDB | bedrockdb02 | me_01 | Data Source=bedrockdb02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| PostTriggerImport | HTTP (KingswaySoft) |  |  |  |
| SMTP_EMAIL | SMTP |  |  |  |
| SQL_LOG | OLEDB | stl-ssis-p-01 | msdb | Data Source=stl-ssis-p-01; Initial Catalog=msdb; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| XML FILES | FILE |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| WMS_InventoryAdjustments_3PLtoDynamics | Package |
| File Generation and Move | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| DataFlow XML File | Pipeline |
| DataFlow XML File withCosts | Pipeline |
| Foreach Loop - Copy Manifest and Header Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Foreach ReleasedProductCreation | FOREACHLOOP |
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
| SetExported | ExecuteSQLTask |
| Zip File | ExecuteProcess |
| Stage Company Entities | ExecuteSQLTask |
| Get Summary Status - MANUALLY BY BATCH ID | Pipeline |
| Stage Data | SEQUENCE |
| Merge WarehouseInventoryAdjustment | ExecuteSQLTask |
| Stage 3PL Adj | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- File Generation and Move [SEQUENCE]
  - Foreach Loop - Per Entity [FOREACHLOOP]
    - DataFlow XML File [Pipeline]
    - DataFlow XML File withCosts [Pipeline]
    - Foreach Loop - Copy Manifest and Header Files [FOREACHLOOP]
      - Copy Manifest & Header [FileSystemTask]
    - Foreach ReleasedProductCreation [FOREACHLOOP]
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
    - SetExported [ExecuteSQLTask]
    - Zip File [ExecuteProcess]
  - Stage Company Entities [ExecuteSQLTask]
- Get Summary Status - MANUALLY BY BATCH ID [Pipeline]
- Stage Data [SEQUENCE]
  - Merge WarehouseInventoryAdjustment [ExecuteSQLTask]
  - Stage 3PL Adj [Pipeline]
  - Truncate Stage [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_File_Generation_and_Move["File Generation and Move"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_XML_File["DataFlow XML File"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_XML_File_withCosts["DataFlow XML File withCosts"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files["Foreach Loop - Copy Manifest and Header Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation["Foreach ReleasedProductCreation"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop_Wait_30_Seconds["Wait 30 Seconds"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Set_RowsCount["Set RowsCount"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Stage_Blob_URL["Stage Blob URL"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Trigger_Import["Trigger Import"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_SetExported["SetExported"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File["Zip File"]
    n_Package_File_Generation_and_Move_Stage_Company_Entities["Stage Company Entities"]
    n_Package_Get_Summary_Status___MANUALLY_BY_BATCH_ID["Get Summary Status - MANUALLY BY BATCH ID"]
    n_Package_Stage_Data["Stage Data"]
    n_Package_Stage_Data_Merge_WarehouseInventoryAdjustment["Merge WarehouseInventoryAdjustment"]
    n_Package_Stage_Data_Stage_3PL_Adj["Stage 3PL Adj"]
    n_Package_Stage_Data_Truncate_Stage["Truncate Stage"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Foreach_Loop_Container_Archive_Files
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop_Wait_30_Seconds --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Stage_Blob_URL --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Set_RowsCount
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Trigger_Import --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_ProcessStatus_For_Loop
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Foreach_Loop_Container --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Trigger_Import
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Set_BatchID___LoopCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Stage_Blob_URL
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Set_RowsCount --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation_Foreach_Loop_Container
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_XML_File --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_SetExported
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_ReleasedProductCreation
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_SetExported --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files
    n_Package_File_Generation_and_Move_Stage_Company_Entities --> n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity
    n_Package_Stage_Data_Truncate_Stage --> n_Package_Stage_Data_Stage_3PL_Adj
    n_Package_Stage_Data_Stage_3PL_Adj --> n_Package_Stage_Data_Merge_WarehouseInventoryAdjustment
    n_Package_Stage_Data --> n_Package_File_Generation_and_Move
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | AdjDate | No |
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
@[$Package::WMS_3PLInventoryAdjustmentsFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-P-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\Archive\
```

#### User::AzCopytoBlobCommand

**Expression:**

```sql
"cp \"" +  @[User::ZipDest] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-P-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\3PLInventoryAdjustments1100.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
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
20251911371997
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
1/9/2025
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
2025-01-09
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
1/9/2025
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
2025-01-09
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
@[$Package::WMS_PackageAPI_StaticPackageFilesPath] + "3PLInventoryAdjustments"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\3PLInventoryAdjustments
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
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[$Package::WMS_3PLInventoryAdjustmentsBlobDefinitionGroupID] + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as executionId, 'InventoryAdjustmentExport1100' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1100' as legalEntityId
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
1/8/2025
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
2025-01-08
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-P-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\3PLInventoryAdjustments1100.zip"  "*.xml" -sdel
```

#### User::ZipDest

**Expression:**

```sql
@[$Package::WMS_3PLInventoryAdjustmentsFileStageLocation]  + "3PLInventoryAdjustments" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-P-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\3PLInventoryAdjustments1100.zip
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

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach ReleasedProductCreation\ProcessStatus For Loop\Set ProcessStatus`  
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

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach ReleasedProductCreation\ProcessStatus For Loop\Wait 30 Seconds`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:30'
```

### Set BatchID - LoopCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach ReleasedProductCreation\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\Foreach ReleasedProductCreation\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### SetExported

**Path:** `Package\File Generation and Move\Foreach Loop - Per Entity\SetExported`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update erp.WarehouseInventoryAdjustment
set Exported= 1, ExportDate=getdate()
where 1=1
and Entity=?
and cast(AdjustmentDate as date)= ?
and Exported = 0

```

### Stage Company Entities

**Path:** `Package\File Generation and Move\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
with 
InventoryMultiple as
	(
		select uom.ProductNumber, uom.InventoryMultiple, uom.entity 
		from ERP.vwItemMasterUOM uom 
		join WMS.ItemMaster im with (nolock) on uom.ProductNumber=im.ItemNumber and uom.Entity=im.Entity
		where im.NecessaryProductionWorkingTimeSchedulingPropertyId in ('Supplies','Merch')
	),
InvAdj as
	(
		select 
			concat(
				replace(a.AdjustmentDate, '-', ''),
				a.WarehouseID,
				rank() over(order by a.WarehouseID, a.AdjustmentDate) 
			  )
			as JournalNumber,
			a.AdjustmentDate,
			a.ItemID,
			a.WarehouseID,
			SUM(a.Qty / im.InventoryMultiple) Qty,
			a.entity
		from erp.WarehouseInventoryAdjustment a
		join InventoryMultiple im on a.ItemID = im.ProductNumber and a.Entity = im.Entity 
		where 1=1
		and a.WarehouseID<>'9980'
--		and a.Entity=1100
		and a.Exported<>1
		group by 
			a.entity,
			a.ItemID,
			a.WarehouseID,
			a.AdjustmentDate 
	)
select
	Entity, cast(cast(AdjustmentDate as date) as varchar(10)) as AdjDate
from InvAdj
where Qty <> 0 
group by 
	Entity,  cast(cast(AdjustmentDate as date) as varchar(10))
```

### Merge WarehouseInventoryAdjustment

**Path:** `Package\Stage Data\Merge WarehouseInventoryAdjustment`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec ERP.spMergeWarehouseInventoryAdjustment
```

### Truncate Stage

**Path:** `Package\Stage Data\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE ERP.WarehouseInventoryAdjustmentStage
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| InventoryAdjustments |  | OLEDBSource | DataFlow XML File | IntegrationStaging | SqlCommand |
| InventoryAdjustments |  | OLEDBSource | DataFlow XML File withCosts | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status - MANUALLY BY BATCH ID | IntegrationStaging | SqlCommand |
| ERP_InventoryAdjustmentLog |  | OLEDBSource | Stage 3PL Adj | ME_01 | SqlCommand |

#### InventoryAdjustments — SqlCommand

```sql
with 
InventoryMultiple as
	(
		select uom.ProductNumber, uom.InventoryMultiple, uom.entity 
		from ERP.vwItemMasterUOM uom 
		join WMS.ItemMaster im with (nolock) on uom.ProductNumber=im.ItemNumber and uom.Entity=im.Entity
		where im.NecessaryProductionWorkingTimeSchedulingPropertyId in ('Supplies','Merch')
	),
InvAdj as
	(
		select 
			concat(
				replace(a.AdjustmentDate, '-', ''),
				a.WarehouseID,
				rank() over(order by a.WarehouseID, a.AdjustmentDate) 
			  )
			as JournalNumber,
			a.AdjustmentDate,
			a.ItemID,
			a.WarehouseID,
			SUM(a.Qty / im.InventoryMultiple) Qty,
			case when a.Description is NULL then 'InventoryAdjust' else concat('InventoryAdjust-',a.Description) end as Description
		from erp.WarehouseInventoryAdjustment a
		join InventoryMultiple im on a.ItemID = im.ProductNumber and a.Entity = im.Entity 
		where 1=1
		and a.WarehouseID<>'9980'
		and a.Exported<>1
		and a.Entity = ?
		and cast(a.AdjustmentDate as date) = ?
		group by 
			a.ItemID,
			a.WarehouseID,
			a.AdjustmentDate,
			a.Description
	),
LineNumbers as
	(
		select 
			JournalNumber,
			AdjustmentDate,
			ItemID,
			WarehouseID,
			Qty,
			Description,
			rank() over(partition by JournalNumber order by AdjustmentDate, WarehouseID, ItemID, Description) as LineNumber
		from InvAdj
		where Qty <> 0 
	)
select 
	'MAIN' as WAREHOUSELOCATIONID,
	'' as UNITCOSTQUANTITY,
	'' as UNITCOST,
	cast(AdjustmentDate as datetime) as TRANSACTIONDATE,
	'' as PRODUCTSTYLEID,
	'' as PRODUCTSIZEID,
	'' as PRODUCTCONFIGURATIONID,
	'' as PRODUCTCOLORID,
	LineNumber as LINENUMBER,
	'' as LICENSEPLATENUMBER,
	'' as JOURNALNUMBER, --JournalNumber  as JOURNALNUMBER,
	'IADJ' as JOURNALNAMEID,
	'' as ITEMSERIALNUMBER,
	ItemID as ITEMNUMBER,
	'' as ITEMBATCHNUMBER,
	WarehouseID as INVENTORYWAREHOUSEID,
	'' as INVENTORYSTATUSID,
	WarehouseID as INVENTORYSITEID,
	Qty as INVENTORYQUANTITY,
	'' as FIXEDCOSTCHARGES,
	concat(WarehouseID, '-9999-19--') as DEFAULTLEDGERDIMENSIONDISPLAYVALUE,
	'' as COSTAMOUNT,
	Description as 'INVENTORYADJUST'
from LineNumbers
```

#### Trigger Columns — SqlCommand

```sql
select 'do nothing' as DoNothing
```

#### Start — SqlCommand

```sql
select cast('
{
    "executionId":"{98DA859E-D7C3-4C56-AD79-CC65972955E3}"
}
' as varchar(100)) as Command, cast('{98DA859E-D7C3-4C56-AD79-CC65972955E3}' as varchar(50)) as BatchID, getdate() as InsertDate
```

#### ERP_InventoryAdjustmentLog — SqlCommand

```sql
select
	cast(
			case 
				when LocationCode = '0960'
					then '1100'
				when LocationCode = '2970' 
					then '2110' 
				when LocationCode in ('3970','3980','9942','8502','8505')
					then '3001'
			end as nvarchar(4)
		) as Entity,
	LocationCode,
	Style, 
	style as ItemID, 
	sum(Qty) as Qty,
	Description,
	cast(InsertDate as Date) as AdjustmentDate
from ERP_InventoryAdjustmentLog with (nolock)
where LocationCode not in ('0980') 
and datediff(dd, InsertDate, getdate()) <= 90 
group by 
	LocationCode,
	Style,
	Description,
	cast(InsertDate as Date)
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| WMS_3PLInventoryAdjustmentsXML |  | FlatFileDestination | DataFlow XML File | InventoryAdjustmentXML |  |
| WMS_3PLInventoryAdjustmentsXML |  | FlatFileDestination | DataFlow XML File withCosts | InventoryAdjustmentXML |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| WarehouseInventoryAdjustmentStage |  | OLEDBDestination | Stage 3PL Adj | IntegrationStaging |  |
