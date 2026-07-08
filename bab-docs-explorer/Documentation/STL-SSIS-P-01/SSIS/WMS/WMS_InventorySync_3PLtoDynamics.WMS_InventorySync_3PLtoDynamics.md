# SSIS Package: WMS_InventorySync_3PLtoDynamics

**Project:** WMS_InventorySync_3PLtoDynamics  
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
| WMS_InventorySync_3PLtoDynamics | Package |
| File Generation and Move | SEQUENCE |
| Foreach Loop - Per Entity | FOREACHLOOP |
| DataFlow XML File | Pipeline |
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
| Inventory Compare | Pipeline |
| Load WarehouseInventoryAdjustmentStage | Pipeline |
| Merge InventorySync3PLArchive | ExecuteSQLTask |
| Merge WarehouseInventoryAdjustment | ExecuteSQLTask |
| Stage Dynamics vs Whse | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- File Generation and Move [SEQUENCE]
  - Foreach Loop - Per Entity [FOREACHLOOP]
    - DataFlow XML File [Pipeline]
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
  - Inventory Compare [Pipeline]
  - Load WarehouseInventoryAdjustmentStage [Pipeline]
  - Merge InventorySync3PLArchive [ExecuteSQLTask]
  - Merge WarehouseInventoryAdjustment [ExecuteSQLTask]
  - Stage Dynamics vs Whse [Pipeline]
  - Truncate Stage [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_File_Generation_and_Move["File Generation and Move"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_XML_File["DataFlow XML File"]
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
    n_Package_Stage_Data_Inventory_Compare["Inventory Compare"]
    n_Package_Stage_Data_Load_WarehouseInventoryAdjustmentStage["Load WarehouseInventoryAdjustmentStage"]
    n_Package_Stage_Data_Merge_InventorySync3PLArchive["Merge InventorySync3PLArchive"]
    n_Package_Stage_Data_Merge_WarehouseInventoryAdjustment["Merge WarehouseInventoryAdjustment"]
    n_Package_Stage_Data_Stage_Dynamics_vs_Whse["Stage Dynamics vs Whse"]
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
    n_Package_Stage_Data_Truncate_Stage --> n_Package_Stage_Data_Stage_Dynamics_vs_Whse
    n_Package_Stage_Data_Stage_Dynamics_vs_Whse --> n_Package_Stage_Data_Inventory_Compare
    n_Package_Stage_Data_Merge_InventorySync3PLArchive --> n_Package_Stage_Data_Load_WarehouseInventoryAdjustmentStage
    n_Package_Stage_Data_Load_WarehouseInventoryAdjustmentStage --> n_Package_Stage_Data_Merge_WarehouseInventoryAdjustment
    n_Package_Stage_Data_Inventory_Compare --> n_Package_Stage_Data_Merge_InventorySync3PLArchive
    n_Package_Stage_Data --> n_Package_File_Generation_and_Move
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
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
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\Archive\
```

#### User::AzCopytoBlobCommand

**Expression:**

```sql
"cp \"" +  @[User::ZipDest] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\3PLInventoryAdjustments1200.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
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
202519121347837
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
where Entity = '1200'
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
select cast('xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as executionId, 'InventoryAdjustmentExport1200' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1200' as legalEntityId
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
a -tzip "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\3PLInventoryAdjustments1200.zip"  "*.xml" -sdel
```

#### User::ZipDest

**Expression:**

```sql
@[$Package::WMS_3PLInventoryAdjustmentsFileStageLocation]  + "3PLInventoryAdjustments" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\3PLInventoryAdjustments\3PLInventoryAdjustments1200.zip
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
set Exported= 1
where 1=1
and Entity=?
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
		where im.NecessaryProductionWorkingTimeSchedulingPropertyId in ('Merch', 'Supplies')
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
		and a.Exported<>1
		group by 
			a.entity,
			a.ItemID,
			a.WarehouseID,
			a.AdjustmentDate 
	)
select
	Entity
from InvAdj
where Qty <> 0 
group by 
	Entity

```

### Merge InventorySync3PLArchive

**Path:** `Package\Stage Data\Merge InventorySync3PLArchive`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
if (
		select count(*) 
		from wms.InventorySync3PLArchive a
		join wms.InventorySync3PLArchiveStage s 
			on a.InventoryDate=s.InventoryDate
			and a.LocationCode=s.LocationCode
		join wms.InventorySync3PLSafetyNet sn 
			on a.InventoryDate=sn.InventoryDate
			and a.LocationCode=sn.LocationCode
	) > 0
delete a 
from wms.InventorySync3PLArchive a
join wms.InventorySync3PLArchiveStage s 
	on a.InventoryDate=s.InventoryDate
	and a.LocationCode=s.LocationCode
join wms.InventorySync3PLSafetyNet sn 
	on a.InventoryDate=sn.InventoryDate
	and a.LocationCode=sn.LocationCode

----
insert wms.InventorySync3PLArchive
select s.*
from wms.InventorySync3PLArchiveStage s 
join wms.InventorySync3PLSafetyNet sn 
	on s.InventoryDate=sn.InventoryDate
	and s.LocationCode=sn.LocationCode


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
TRUNCATE TABLE WMS.DynInvSyncWhseStage
TRUNCATE TABLE WMS.DynInvSyncDynStage
TRUNCATE TABLE WMS.InventorySync3PLArchiveStage
TRUNCATE TABLE WMS.InventorySync3PLSafetyNet
TRUNCATE TABLE ERP.WarehouseInventoryAdjustmentStage
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| InventoryAdjustments |  | OLEDBSource | DataFlow XML File | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status - MANUALLY BY BATCH ID | IntegrationStaging | SqlCommand |
| SQL Compare |  | OLEDBSource | Inventory Compare | IntegrationStaging | SqlCommand |
| InventorySync3PLArchive |  | OLEDBSource | Load WarehouseInventoryAdjustmentStage | IntegrationStaging | SqlCommand |
| 3PL Staged Inventory |  | OLEDBSource | Stage Dynamics vs Whse | ME_01 | SqlCommand |
| Dynamics Inventory |  | OLEDBSource | Stage Dynamics vs Whse | IntegrationStaging | SqlCommand |

#### InventoryAdjustments — SqlCommand

```sql
with 
InventoryMultiple as
	(
		select uom.ProductNumber, uom.InventoryMultiple, uom.entity 
		from ERP.vwItemMasterUOM uom 
		join WMS.ItemMaster im with (nolock) on uom.ProductNumber=im.ItemNumber and uom.Entity=im.Entity
		where im.NecessaryProductionWorkingTimeSchedulingPropertyId in ('Merch', 'Supplies')
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
			SUM(a.Qty / im.InventoryMultiple) Qty
		from erp.WarehouseInventoryAdjustment a
		join InventoryMultiple im on a.ItemID = im.ProductNumber and a.Entity = im.Entity 
		where 1=1
		and a.WarehouseID<>'9980'
		and a.Exported<>1
		and a.Entity = ?
		group by 
			a.ItemID,
			a.WarehouseID,
			a.AdjustmentDate 
	),
LineNumbers as
	(
		select 
			JournalNumber,
			AdjustmentDate,
			ItemID,
			WarehouseID,
			Qty,
			rank() over(partition by JournalNumber order by AdjustmentDate, WarehouseID, ItemID) as LineNumber
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
	WarehouseID as INVENTORYWAREHOUSEID, ---technically I could pull this out of the warehouse master 
	'' as INVENTORYSTATUSID,
	case when WarehouseID in ('8502','8505') then '9940' else WarehouseID end as INVENTORYSITEID,
	Qty as INVENTORYQUANTITY,
	'' as FIXEDCOSTCHARGES,
	concat(WarehouseID, '-9999-19--') as DEFAULTLEDGERDIMENSIONDISPLAYVALUE,
	'' as COSTAMOUNT,
	'nightly sync inv-adj' as REASONCODE
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

#### SQL Compare — SqlCommand

```sql
with 
Items as
	(
		select ItemNumber, Entity, LocationCode
		from WMS.DynInvSyncDynStage
		group by ItemNumber, Entity, LocationCode
		UNION
		select ItemNumber, Entity, LocationCode
		from WMS.DynInvSyncWhseStage
		group by ItemNumber, Entity, LocationCode
	)
select 
	i.Entity,
	i.LocationCode,
	i.ItemNumber,
	cast(case i.LocationCode 
		when '2970' then '9970'
		when '3970' then '9940'
		when '3980' then '9941'
		when '0960' then '9960'
		when '9942' then '9942'
	end as nvarchar(4)) as DynWhseID,
	isnull(d.DynQty,0) as DynQty,
	isnull(d.InventoryMultiple,	0) as InventoryMultiple,
	isnull(d.InventoryDate, cast(getdate() as date)) as InventoryDate, --reason= we process inventory files for previous day at 2am-ish...
	isnull(w.WhseQty,0) WhseQty,
	isnull(w.WhseQty,0)-isnull(d.DynQty,0) as VarianceQty
from Items i
left join WMS.DynInvSyncDynStage d 
	on i.entity=d.Entity
	and i.LocationCode=d.LocationCode
	and i.ItemNumber=d.ItemNumber
left join WMS.DynInvSyncWhseStage w 
	on i.Entity=w.Entity
	and i.LocationCode=w.LocationCode
	and i.ItemNumber=w.ItemNumber


/*
select 
	d.Entity,	
	d.DynWhseID,	
	d.LocationCode,	
	d.ItemNumber,	
	d.DynQty,		
	d.InventoryMultiple,	
	d.InventoryDate,
	isnull(w.WhseQty,0) WhseQty,
	isnull(w.WhseQty,0)-d.DynQty as VarianceQty
from WMS.DynInvSyncDynStage d
left join WMS.DynInvSyncWhseStage w 
	on d.Entity=w.Entity
	and d.LocationCode=w.LocationCode
	and d.ItemNumber=w.ItemNumber
*/
```

#### InventorySync3PLArchive — SqlCommand

```sql
select 
	a.LocationCode,
	cast(a.DynWhseID as varchar) as WarehouseID,
	a.ItemNumber as Style,
	a.ItemNumber as ItemID,
	a.VarianceQty as Qty,
	'nightly sync inv-adj' as [Description],
	a.InventoryDate as AdjustmentDate,
	a.Entity
from wms.InventorySync3PLArchive a
join wms.InventorySync3PLSafetyNet sn --make sure we don't post sync file if there was not a file processed, hence the safety net
	on a.InventoryDate=sn.InventoryDate
	and a.LocationCode=sn.LocationCode
where cast(a.InventoryDate as date)=cast(getdate() as date)
```

#### 3PL Staged Inventory — SqlCommand

```sql
select 
	cast(style_code as varchar(6)) as ItemNumber,
	sum(qty) as WhseQty,
	location_code as LocationCode,
	cast(load_date as date) as InventoryDate,
	cast(
		case 
			when location_code='2970' then 2110
			when location_code in ('3970','8502','8505') then 3001
			when location_code IN ('3980','9942') then 1200
			when location_code='0960' then 1100
		end as nvarchar(4)
		) as Entity

from NightlyWhseInventory 
where cast(load_date as date)=cast(getdate() as date)
and location_code in ('2970','3970','3980','0960','8505','8502','9942')
--and location_code='0960'
--and style_code='018957'
group by 
	cast(style_code as varchar(6)),
	location_code,
cast(load_date as date)
order by 
cast(
		case 
			when location_code='2970' then 2110
			when location_code in ('3970','8502','8505') then 3001
			when location_code IN ('3980','9942') then 1200
			when location_code='0960' then 1100
		end as nvarchar(4)
		),
	location_code, 
	style_code
```

#### Dynamics Inventory — SqlCommand

```sql
select     --should include all items in dynamics per entity (merch and supplies, so should be left join to 3PL)
	cast(woh.ItemNumber as varchar(6)) as ItemNumber,
		case when im.NecessaryProductionWorkingTimeSchedulingPropertyId='Supplies' 
			then (
					sum((isnull(woh.AvailableOnHandQuantity,0) - isnull(woh.OnOrderQuantity,0)))
					*
					uom.InventoryMultiple
				)
			else sum((isnull(woh.AvailableOnHandQuantity,0) - isnull(woh.OnOrderQuantity,0)))
		 end as DynQty,
		
	--sum((isnull(woh.AvailableOnHandQuantity,0) - isnull(woh.OnOrderQuantity,0))) as DynQty,
	uom.InventoryMultiple,
	woh.InventoryWarehouseID as DynWhseID,
	case woh.InventoryWarehouseID 
		when '9970' then '2970'
		when '9940' then '3970'
		when '9941' then '3980'
		when '9960' then '0960'
		else cast(InventoryWarehouseID as varchar)
	end as LocationCode,
	woh.DataAreaID as Entity,
	cast(getdate() as date) as InventoryDate
from erp.vwItemMasterUOM uom
join wms.ItemMaster im 
	on uom.ProductNumber=im.ItemNumber
	and uom.Entity=im.Entity
	and im.NecessaryProductionWorkingTimeSchedulingPropertyId in ('Supplies','Merch')
	and uom.entity in ('1100', '2110', '3001','1200')
left join WMS.WarehouseOnHand woh 
	on uom.Entity=woh.DataAreaID
	and uom.ProductNumber=woh.ItemNumber
where 1=1 
and woh.InventoryWarehouseID not in ('9980', '1013') 
and isnumeric(left(woh.ItemNumber,1)) = 1
and woh.InventoryWarehouseID in ('9970','9940','9941','9942','9960','8502','8505')
--and woh.InventoryWarehouseID='9960'
--and im.itemNumber='018957'
group by 
	cast(woh.ItemNumber as varchar(6)), 
	uom.InventoryMultiple,
	woh.InventoryWarehouseID,
	case woh.InventoryWarehouseID 
		when '9970' then '2970'
		when '9940' then '3970'
		when '9941' then '3980'
		when '9960' then '0960'
		else cast(InventoryWarehouseID as varchar)
	end,
	woh.DataAreaID,
	im.NecessaryProductionWorkingTimeSchedulingPropertyId
Order by woh.DataAreaID, woh.InventoryWarehouseID, cast(woh.ItemNumber as varchar(6))
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| WMS_3PLInventoryAdjustmentsXML |  | FlatFileDestination | DataFlow XML File | InventoryAdjustmentXML |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
| InventorySync3PLArchiveStage |  | OLEDBDestination | Inventory Compare | IntegrationStaging |  |
| WarehouseInventoryAdjustmentStage |  | OLEDBDestination | Load WarehouseInventoryAdjustmentStage | IntegrationStaging |  |
| DynInvSyncDynStage |  | OLEDBDestination | Stage Dynamics vs Whse | IntegrationStaging |  |
| DynInvSyncWhseStage |  | OLEDBDestination | Stage Dynamics vs Whse | IntegrationStaging |  |
| InventorySync3PLSafetyNet |  | OLEDBDestination | Stage Dynamics vs Whse | IntegrationStaging |  |
