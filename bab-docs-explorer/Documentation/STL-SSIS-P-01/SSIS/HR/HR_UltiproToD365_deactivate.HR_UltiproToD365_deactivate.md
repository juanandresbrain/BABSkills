# SSIS Package: HR_UltiproToD365_deactivate

**Project:** HR_UltiproToD365_deactivate  
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
| HR_UltiproToD365_deactivate | Package |
| user deactivate seq | SEQUENCE |
| User Deactivate Stage 1 1 | SEQUENCE |
| Stage User Data | Pipeline |
| Truncate Stage | ExecuteSQLTask |
| UserCreate File Generation and Move | SEQUENCE |
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
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- user deactivate seq [SEQUENCE]
  - User Deactivate Stage 1 1 [SEQUENCE]
    - Stage User Data [Pipeline]
    - Truncate Stage [ExecuteSQLTask]
  - UserCreate File Generation and Move [SEQUENCE]
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
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_user_deactivate_seq["user deactivate seq"]
    n_Package_user_deactivate_seq_User_Deactivate_Stage_1_1["User Deactivate Stage 1 1"]
    n_Package_user_deactivate_seq_User_Deactivate_Stage_1_1_Stage_User_Data["Stage User Data"]
    n_Package_user_deactivate_seq_User_Deactivate_Stage_1_1_Truncate_Stage["Truncate Stage"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move["UserCreate File Generation and Move"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity["Foreach Loop - Per Entity"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_CSV_File["DataFlow CSV File"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop["Foreach BlobUploadLoop"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_datestamp_archive["datestamp archive"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Wait["Wait"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount["Set RowsCount"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL["Stage Blob URL"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import["Trigger Import"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files["Foreach Loop - Copy Manifest and Header Files"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File["Zip File"]
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Stage_Company_Entities["Stage Company Entities"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_user_deactivate_seq_User_Deactivate_Stage_1_1_Truncate_Stage --> n_Package_user_deactivate_seq_User_Deactivate_Stage_1_1_Stage_User_Data
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container_Archive_Files
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Wait --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Trigger_Import
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_BatchID___LoopCount --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Stage_Blob_URL
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Set_RowsCount --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_Foreach_Loop_Container
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_ProcessStatus_For_Loop --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop_datestamp_archive
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_DataFlow_CSV_File --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_Loop___Copy_Manifest_and_Header_Files --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Zip_File --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity_Foreach_BlobUploadLoop
    n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Stage_Company_Entities --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move_Foreach_Loop___Per_Entity
    n_Package_user_deactivate_seq_User_Deactivate_Stage_1_1 --> n_Package_user_deactivate_seq_UserCreate_File_Generation_and_Move
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
Archive\UserCreate1100.zip
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
Archive\UserCreate1100_202383115100987.zip
```

#### User::ArchiveFileDateStamped2

**Expression:**

```sql
@[User::ArchiveFolder2] + "UserDeactivate" +  @[User::Entity] + "_" +   @[User::DateTimeStamp] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\UserDeactivate\Archive\UserDeactivate1100_202383115100987.zip
```

#### User::ArchiveFolder

**Expression:**

```sql
@[$Package::WMS_UserCreateFileStageLocation]  + "Archive\\"
```

**Evaluated value:**

```sql
Archive\
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
cp "UserCreate1100.zip" "xxxhttps://buildabear1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
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
202383115100987
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
8/31/2023
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
2023-08-31
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
8/31/2023
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
2023-08-31
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
select cast('xxxhttps://buildabear1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('0E7E4435-B76A-47BD-A840-D89D3CBE0424' as varchar(50)) as executionId, 'MobileDeviceUserDeactivate1100' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1100' as legalEntityId
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
8/30/2023
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
2023-08-30
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  + "\"  \"" +  @[User::ZipSource2]  + "\"  \"" +  @[User::ZipSource3]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "UserCreate1100.zip"  "*.xml"  "*.csv"  "-x!*.zip" -sdel
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
UserCreate1100.zip
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

### Truncate Stage

**Path:** `Package\user deactivate seq\User Deactivate Stage 1 1\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [ERP].[UserDeactivateD365]
```

### Set ProcessStatus

**Path:** `Package\user deactivate seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\ProcessStatus For Loop\Set ProcessStatus`  
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

**Path:** `Package\user deactivate seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\ProcessStatus For Loop\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:30'
```

### Set BatchID - LoopCount

**Path:** `Package\user deactivate seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\user deactivate seq\UserCreate File Generation and Move\Foreach Loop - Per Entity\Foreach BlobUploadLoop\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### Stage Company Entities

**Path:** `Package\user deactivate seq\UserCreate File Generation and Move\Stage Company Entities`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select Entity
from [ERP].[UserDeactivateD365]
--where SendData = 1
--and Entity in (2110, 2300, 3001)
group by Entity

```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Source |  | OLEDBSource | Stage User Data | papamart.dw | SqlCommand |
| dynUserDeactivate |  | OLEDBSource | DataFlow CSV File | IntegrationStaging | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |

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

#### dynUserDeactivate — SqlCommand

```sql
SELECT [USERID]
      ,[WAREHOUSEWORKERPERSONNELNUMBER]
      ,[ISINACTIVE]
      ,[ENTITY]
  FROM [ERP].[UserDeactivateD365]
WHERE [ENTITY] = ?
```

#### Trigger Columns — SqlCommand

```sql
select 'do nothing' as DoNothing
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Destination |  | OLEDBDestination | Stage User Data | IntegrationStaging |  |
| Flat File Destination |  | FlatFileDestination | DataFlow CSV File | UserDeactivateCSV |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
