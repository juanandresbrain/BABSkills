# SSIS Package: SalesAuditToDynamicsPackageAPI_Parallel

**Project:** SalesAuditToDynamicsPackageAPI_Parallel  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| ArchiveFolder | FILE |  |  |  |
| FileDiscounts | FLATFILE |  |  |  |
| FileHeaders | FLATFILE |  |  |  |
| FileLines | FLATFILE |  |  |  |
| FilePayments | FLATFILE |  |  |  |
| FileTaxes | FLATFILE |  |  |  |
| GetBlobUrl | HTTP (KingswaySoft) |  |  |  |
| GetStatus | HTTP (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| PostTriggerImport | HTTP (KingswaySoft) |  |  |  |
| SMTP_EMAIL | SMTP |  |  |  |
| SQL_LOG | OLEDB | stl-ssis-p-01 | msdb | Data Source=stl-ssis-p-01; Initial Catalog=msdb; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| XML FILES | FILE |  |  |  |
| dw | OLEDB | papamart | dw | Data Source=papamart; Initial Catalog=dw; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| SalesAuditToDynamicsPackageAPI_Parallel | Package |
| SeqCont - File Generation | SEQUENCE |
| FEL - File Generation | FOREACHLOOP |
| Checks for Continue | ExecuteSQLTask |
| Foreach Loop - Copy Manifest and Header Files | FOREACHLOOP |
| Copy Manifest & Header | FileSystemTask |
| Foreach Loop Container | FOREACHLOOP |
| Move Zip to Company Folder | FileSystemTask |
| SeqCont - Generate CSV Files | SEQUENCE |
| DFT - Discount File | Pipeline |
| DFT - Header File | Pipeline |
| DFT - Payment File | Pipeline |
| DFT - Sales Detail File | Pipeline |
| DFT - Tax File | Pipeline |
| Zip File | ExecuteProcess |
| SeqCont - Load Target Trans To Ref Table | SEQUENCE |
| Data Flow Task - Load Target Trans | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| Stage Company Entities - Files | ExecuteSQLTask |
| SeqCont - Package API Transmission | SEQUENCE |
| FEL - API Transmission by Entity | FOREACHLOOP |
| Execute SQL Task - Check Trigger Response | ExecuteSQLTask |
| Execute SQL Task - Update Records as Exported | ExecuteSQLTask |
| Foreach Sales Files Upload | FOREACHLOOP |
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
| Send Mail Task - Trigger Import Failed | SendMailTask |
| Set Variable -  RowsCountAPI | ExecuteSQLTask |
| Stage Company Entities | ExecuteSQLTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- SeqCont - File Generation [SEQUENCE]
  - FEL - File Generation [FOREACHLOOP]
    - Checks for Continue [ExecuteSQLTask]
    - Foreach Loop - Copy Manifest and Header Files [FOREACHLOOP]
      - Copy Manifest & Header [FileSystemTask]
    - Foreach Loop Container [FOREACHLOOP]
      - Move Zip to Company Folder [FileSystemTask]
    - SeqCont - Generate CSV Files [SEQUENCE]
      - DFT - Discount File [Pipeline]
      - DFT - Header File [Pipeline]
      - DFT - Payment File [Pipeline]
      - DFT - Sales Detail File [Pipeline]
      - DFT - Tax File [Pipeline]
    - Zip File [ExecuteProcess]
  - SeqCont - Load Target Trans To Ref Table [SEQUENCE]
    - Data Flow Task - Load Target Trans [Pipeline]
    - Execute SQL Task [ExecuteSQLTask]
    - Stage Company Entities - Files [ExecuteSQLTask]
- SeqCont - Package API Transmission [SEQUENCE]
  - FEL - API Transmission by Entity [FOREACHLOOP]
    - Execute SQL Task - Check Trigger Response [ExecuteSQLTask]
    - Execute SQL Task - Update Records as Exported [ExecuteSQLTask]
    - Foreach Sales Files Upload [FOREACHLOOP]
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
    - Send Mail Task - Trigger Import Failed [SendMailTask]
    - Set Variable -  RowsCountAPI [ExecuteSQLTask]
  - Stage Company Entities [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_SeqCont___File_Generation["SeqCont - File Generation"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation["FEL - File Generation"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Checks_for_Continue["Checks for Continue"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Foreach_Loop___Copy_Manifest_and_Header_Files["Foreach Loop - Copy Manifest and Header Files"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Foreach_Loop___Copy_Manifest_and_Header_Files_Copy_Manifest___Header["Copy Manifest & Header"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Foreach_Loop_Container_Move_Zip_to_Company_Folder["Move Zip to Company Folder"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files["SeqCont - Generate CSV Files"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files_DFT___Discount_File["DFT - Discount File"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files_DFT___Header_File["DFT - Header File"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files_DFT___Payment_File["DFT - Payment File"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files_DFT___Sales_Detail_File["DFT - Sales Detail File"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files_DFT___Tax_File["DFT - Tax File"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Zip_File["Zip File"]
    n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table["SeqCont - Load Target Trans To Ref Table"]
    n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table_Data_Flow_Task___Load_Target_Trans["Data Flow Task - Load Target Trans"]
    n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table_Execute_SQL_Task["Execute SQL Task"]
    n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table_Stage_Company_Entities___Files["Stage Company Entities - Files"]
    n_Package_SeqCont___Package_API_Transmission["SeqCont - Package API Transmission"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity["FEL - API Transmission by Entity"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Execute_SQL_Task___Check_Trigger_Response["Execute SQL Task - Check Trigger Response"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Execute_SQL_Task___Update_Records_as_Exported["Execute SQL Task - Update Records as Exported"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload["Foreach Sales Files Upload"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Foreach_Loop_Container_Archive_Files["Archive Files"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Foreach_Loop_Container_azCopy_to_Blob["azCopy to Blob"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop["ProcessStatus For Loop"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop_Get_Summary_Status["Get Summary Status"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop_Set_ProcessStatus["Set ProcessStatus"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop_Wait["Wait"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Set_BatchID___LoopCount["Set BatchID - LoopCount"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Set_RowsCount["Set RowsCount"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Stage_Blob_URL["Stage Blob URL"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Trigger_Import["Trigger Import"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Send_Mail_Task___Trigger_Import_Failed["Send Mail Task - Trigger Import Failed"]
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Set_Variable____RowsCountAPI["Set Variable -  RowsCountAPI"]
    n_Package_SeqCont___Package_API_Transmission_Stage_Company_Entities["Stage Company Entities"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files --> n_Package_SeqCont___File_Generation_FEL___File_Generation_Foreach_Loop___Copy_Manifest_and_Header_Files
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Foreach_Loop___Copy_Manifest_and_Header_Files --> n_Package_SeqCont___File_Generation_FEL___File_Generation_Zip_File
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Zip_File --> n_Package_SeqCont___File_Generation_FEL___File_Generation_Foreach_Loop_Container
    n_Package_SeqCont___File_Generation_FEL___File_Generation_Checks_for_Continue --> n_Package_SeqCont___File_Generation_FEL___File_Generation_SeqCont___Generate_CSV_Files
    n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table_Execute_SQL_Task --> n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table_Data_Flow_Task___Load_Target_Trans
    n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table_Data_Flow_Task___Load_Target_Trans --> n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table_Stage_Company_Entities___Files
    n_Package_SeqCont___File_Generation_SeqCont___Load_Target_Trans_To_Ref_Table --> n_Package_SeqCont___File_Generation_FEL___File_Generation
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Foreach_Loop_Container_azCopy_to_Blob --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Foreach_Loop_Container_Archive_Files
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop_Get_Summary_Status --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop_Set_ProcessStatus
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop_Wait --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop_Get_Summary_Status
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Stage_Blob_URL --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Set_RowsCount
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Trigger_Import --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_ProcessStatus_For_Loop
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Foreach_Loop_Container --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Trigger_Import
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Set_BatchID___LoopCount --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Stage_Blob_URL
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Set_RowsCount --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload_Foreach_Loop_Container
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Set_Variable____RowsCountAPI --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Foreach_Sales_Files_Upload --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Execute_SQL_Task___Check_Trigger_Response
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Execute_SQL_Task___Check_Trigger_Response --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Execute_SQL_Task___Update_Records_as_Exported
    n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Execute_SQL_Task___Check_Trigger_Response --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity_Send_Mail_Task___Trigger_Import_Failed
    n_Package_SeqCont___Package_API_Transmission_Stage_Company_Entities --> n_Package_SeqCont___Package_API_Transmission_FEL___API_Transmission_by_Entity
    n_Package_SeqCont___File_Generation --> n_Package_SeqCont___Package_API_Transmission
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
| User | CompanyEntitiesFileGen | No |
| User | CompanyFolder | Yes |
| User | DataEntityName | No |
| User | DateTimeStamp | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | Entity | No |
| User | EntityFileGen | No |
| User | FileName | No |
| User | FileNameFileGen | No |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | HeaderAndManifestForLoop | No |
| User | JSON_GetBlobURL | Yes |
| User | JSON_GetSummaryStatus | Yes |
| User | LoopCount | No |
| User | PackageAPIHeaderAndManifestPath | Yes |
| User | ProcessStatus | No |
| User | RowsCount | No |
| User | RowsCountApi | No |
| User | RowsCountForFileGenContinue | No |
| User | RowsCountForPackageContinue | No |
| User | RunControlFlag | No |
| User | SQLItemLoadViewByEntity | Yes |
| User | SQL_GetBlobURLCommand | Yes |
| User | SQL_GetSummaryStatus | Yes |
| User | SQL_TriggerImport | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | TriggerResponseResult | No |
| User | ZipCommand | Yes |
| User | ZipDest | Yes |
| User | ZipSource | Yes |
| User | ZipSourceApiLoop | Yes |

### Expression-bound variable values

#### User::ArchiveFolder

**Expression:**

```sql
@[$Package::SalesAuditTransactionsFileStageLocation]+ @[User::Entity] +"\\"+ "Archive\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesAuditTransactions\1100\Archive\
```

#### User::AzCopytoBlobCommand

**Expression:**

```sql
"cp \"" +  @[User::ZipSourceApiLoop] + "\" \"" +  @[User::BlobURL] + "\""
```

**Evaluated value:**

```sql
cp "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesAuditTransactions\1100\SalesAuditTransactions1100.zip" "xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw"
```

#### User::CompanyFolder

**Expression:**

```sql
@[$Package::SalesAuditTransactionsFileStageLocation]+ @[User::EntityFileGen]+"\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesAuditTransactions\1100\
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
202351985254903
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
5/19/2023
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
2023-05-19
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
5/19/2023
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
2023-05-19
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
@[$Package::WMS_PackageAPI_StaticPackageFilesPath] + "SalesAuditTransactions"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\PackageAPI\SalesAuditTransactions
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
"select cast('" +  @[User::BlobURL] + "' as nvarchar(4000)) as packageUrl, cast('" +  @[User::BatchID] + "' as varchar(50)) as executionId, '" +  @[$Package::SalesAuditTransactionsBlobDefinitionGroupID]  + @[User::Entity] + "' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '" +  @[User::Entity] + "' as legalEntityId"
```

**Evaluated value:**

```sql
select cast('xxxhttps://buildabeartest1f07fd6bdd.blob.core.windows.net/dmf/%7BD2926CE8-9FC9-4B7B-86FA-FEEF91855A32%7D?sv=2014-02-14&sr=b&sig=7yBv4KhQnhXaeiY6MUoX5likoaAyY7FjjFf%2Bpuhr4DY%3D&st=2020-07-27T19%3A54%3A03Z&se=2020-07-27T20%3A29%3A03Z&sp=rw' as nvarchar(4000)) as packageUrl, cast('5ECF043F-9E41-46F7-9FE9-0634BCE2C644' as varchar(50)) as executionId, 'SalesAuditTransactions1100' as definitionGroupId, 'true' as [execute], 'true' as overwrite, '1100' as legalEntityId
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
5/18/2023
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
2023-05-18
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesAuditTransactions\SalesAuditTransactions1100.zip"  "*.*" -sdel
```

#### User::ZipDest

**Expression:**

```sql
@[$Package::SalesAuditTransactionsFileStageLocation] + "SalesAuditTransactions" +  @[User::EntityFileGen] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesAuditTransactions\SalesAuditTransactions1100.zip
```

#### User::ZipSource

**Expression:**

```sql
"*.*"
```

**Evaluated value:**

```sql
*.*
```

#### User::ZipSourceApiLoop

**Expression:**

```sql
@[$Package::SalesAuditTransactionsFileStageLocation] + @[User::Entity] +"\\"+ "SalesAuditTransactions" +  @[User::Entity] + ".zip"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\Dynamics\WarehouseInterfaces\SalesAuditTransactions\1100\SalesAuditTransactions1100.zip
```

## Execute SQL Tasks

### Checks for Continue

**Path:** `Package\SeqCont - File Generation\FEL - File Generation\Checks for Continue`  
**Connection:** dw (papamart/dw)  

```sql

select count (*) as RowsCountForFileGenContinue
from tmpDynamicsRetailTransactionIdExport
Where Entity = ?
```

### Execute SQL Task

**Path:** `Package\SeqCont - File Generation\SeqCont - Load Target Trans To Ref Table\Execute SQL Task`  
**Connection:** dw (papamart/dw)  

```sql
Truncate Table tmpDynamicsRetailTransactionIdExport
```

### Stage Company Entities - Files

**Path:** `Package\SeqCont - File Generation\SeqCont - Load Target Trans To Ref Table\Stage Company Entities - Files`  
**Connection:** dw (papamart/dw)  

```sql
-- old 
/*
select Entity
from DynamicsTransactionHeaderFacts
where
(
	(
		IsCurrent = 1
		and CurrentSentDate is null 
		and BatchID is null
	) -- 
or 
	(
		IsNegatedCurrent =1 
		and NegativeSentDate is null 
		and BatchID is null
	) -- These Represent Negate Transactions 
)
--and RetailReceiptId in ('466760805','466722451')
group by entity 
order by 1
*/


select Entity
from tmpDynamicsRetailTransactionIdExport
group by entity 
order by 1



```

### Execute SQL Task - Check Trigger Response

**Path:** `Package\SeqCont - Package API Transmission\FEL - API Transmission by Entity\Execute SQL Task - Check Trigger Response`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
declare 	@batchID nvarchar (100), 
	@Entity varchar (4)
--set @batchID = '{604952AB-2881-4A2C-BCB4-61D45A7801AB}' -- Testing Purposes
--set @Entity = '1100'
set @batchID = ? 
set @Entity = ?


select case when left(a.TriggerResponse, 15) 
	like '%error%'
	then 'Fail'
		else 'Pass'
	end 
as TriggerResponseResult
from wms.DynamicsPackageAPILog a
where 1=1
and a.IntegrationName = 'SalesAuditToDynamicsPackageAPI_Parallel'
and a.BatchID = @batchID
and a.Entity = @Entity



```

### Execute SQL Task - Update Records as Exported

**Path:** `Package\SeqCont - Package API Transmission\FEL - API Transmission by Entity\Execute SQL Task - Update Records as Exported`  
**Connection:** dw (papamart/dw)  

```sql
declare 	@batchID nvarchar (100), 
	@Entity varchar (4)
set @batchID = ? 
set @Entity = ?
	

		


update [dbo].[DynamicsTransactionHeaderFacts]
	set CurrentSentDate = getdate (), BatchID = @batchID
	Where Entity = @Entity
	and CurrentSentDate is null 
	and BatchID is null 
	and RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport) -- Added 1/20/2023



update [dbo].[DynamicsSalesDetailFacts]
	set CurrentSentDate = getdate (), BatchID = @batchID
	Where Entity = @Entity
	and CurrentSentDate is null 
	and BatchID is null 
	and RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport) -- Added 1/20/2023


update [dbo].[DynamicsDiscountFacts]
	set CurrentSentDate = getdate (), BatchID = @batchID
	Where Entity = @Entity
	and CurrentSentDate is null 
	and BatchID is null 
	and RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport) -- Added 1/20/2023

update [dbo].[DynamicsTaxFacts] 
	set CurrentSentDate = getdate (), BatchID = @batchID
	Where Entity = @Entity
	and CurrentSentDate is null 
	and BatchID is null 
	and RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport) -- Added 1/20/2023
	   
update [dbo].[DynamicsPaymentFacts]
	set CurrentSentDate = getdate (), BatchID = @batchID
	Where Entity = @Entity
	and CurrentSentDate is null 
	and BatchID is null 
	and RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport) -- Added 1/20/2023

update [dbo].[DynamicsTransactionUpdateLog] 
	set BatchID = @batchID, UpdateProcessed = getdate() 
	Where BatchID is null 
	and RetailReceiptId in (select distinct RetailReceiptId from tmpDynamicsRetailTransactionIdExport) -- Added 1/31/2023

update dbo.[DynamicsTransactionNegateOnlyLog]
	set BatchID = @batchID, UpdateProcessed = getdate() 
	Where BatchID is null 
	and RetailReceiptId in (select distinct RetailReceiptId from tmpDynamicsRetailTransactionIdExport) -- Added 4/17/2023


	
```

### Set ProcessStatus

**Path:** `Package\SeqCont - Package API Transmission\FEL - API Transmission by Entity\Foreach Sales Files Upload\ProcessStatus For Loop\Set ProcessStatus`  
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

**Path:** `Package\SeqCont - Package API Transmission\FEL - API Transmission by Entity\Foreach Sales Files Upload\ProcessStatus For Loop\Wait`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
waitfor delay '00:00:59'
```

### Set BatchID - LoopCount

**Path:** `Package\SeqCont - Package API Transmission\FEL - API Transmission by Entity\Foreach Sales Files Upload\Set BatchID - LoopCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select 
newid() as BatchID, 
0 as LoopCount

```

### Set RowsCount

**Path:** `Package\SeqCont - Package API Transmission\FEL - API Transmission by Entity\Foreach Sales Files Upload\Set RowsCount`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
update wms.DynamicsPackageAPILog
set RowsCount=?
where BatchID=?
```

### Set Variable -  RowsCountAPI

**Path:** `Package\SeqCont - Package API Transmission\FEL - API Transmission by Entity\Set Variable -  RowsCountAPI`  
**Connection:** dw (papamart/dw)  

```sql
select count (*) RowsCountApi
from tmpDynamicsRetailTransactionIdExport
where Entity = ?
```

### Stage Company Entities

**Path:** `Package\SeqCont - Package API Transmission\Stage Company Entities`  
**Connection:** dw (papamart/dw)  

```sql
select Entity
from tmpDynamicsRetailTransactionIdExport
group by entity 
order by 1

```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Source - DW - DynamicsDiscountFacts |  | OLEDBSource | DFT - Discount File | dw | SqlCommand |
| OLE DB Source - DW - DynamicsTransactionHeaderFacts |  | OLEDBSource | DFT - Header File | dw | SqlCommand |
| OLE DB Source -DW - DynamicsPaymentFacts |  | OLEDBSource | DFT - Payment File | dw | SqlCommand |
| OLE DB Source - DW - DynamicsSalesDetailFacts |  | OLEDBSource | DFT - Sales Detail File | dw | SqlCommand |
| OLE DB Source - DW - DynamicsTaxFacts |  | OLEDBSource | DFT - Tax File | dw | SqlCommand |
| OLE DB Source - DW - DynamicsTransactionHeaderFacts |  | OLEDBSource | Data Flow Task - Load Target Trans | dw | SqlCommand |
| Start |  | OLEDBSource | Get Summary Status | IntegrationStaging |  |
| Get BLOB Command |  | OLEDBSource | Stage Blob URL | IntegrationStaging |  |
| Trigger Columns |  | OLEDBSource | Trigger Import | IntegrationStaging | SqlCommand |

#### OLE DB Source - DW - DynamicsDiscountFacts — SqlCommand

```sql
-- Old Method Used CTE to Specify Target Transactions
-- Now Building a Reference Table within the FEL 
--with Transactions as (
--select distinct RetailTransactionId
--from [dbo].[DynamicsTransactionHeaderFacts] (nolock) 
--where IsCurrent = 1
--and CurrentSentDate is null 
--and BatchID is null -- Unsure about this condition 
--and Entity = ?
----and TransDate = '5-1-2022' -- Testing Purposes Only 
----and InventLocationId = '1001' -- Testing Purposes Only 
----and RetailTransactionId in ('1239-1239Int-20230117-466450659_1','1175-1175Int-20230117-466457881_1','1404-1404Int-20230117-466455909_1','1404-1404Int-20230118-466488161_1','2063-2063Int-20230117-466432196_1','2063-2063Int-20230119-466519702_1') -- Testing Purposes Only 
--)


select * 
from [dbo].[DynamicsDiscountFacts]
--where RetailTransactionId in (select distinct RetailTransactionId from Transactions)
where RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport)
and Entity = ?
order by RetailTransactionId
```

#### OLE DB Source - DW - DynamicsTransactionHeaderFacts — SqlCommand

```sql
-- Old Method Used CTE to Specify Target Transactions
-- Now Building a Reference Table within the FEL 
--with Transactions as (
--select distinct RetailTransactionId
--from [dbo].[DynamicsTransactionHeaderFacts] (nolock) 
--where IsCurrent = 1
--and CurrentSentDate is null 
--and BatchID is null -- Unsure about this condition 
--and Entity = ?
----and TransDate = '5-1-2022' -- Testing Purposes Only 
----and InventLocationId = '1001' -- Testing Purposes Only 
----and RetailTransactionId in ('1239-1239Int-20230117-466450659_1','1175-1175Int-20230117-466457881_1','1404-1404Int-20230117-466455909_1','1404-1404Int-20230118-466488161_1','2063-2063Int-20230117-466432196_1','2063-2063Int-20230119-466519702_1') -- Testing Purposes Only 
--)

select * 
from [dbo].[DynamicsTransactionHeaderFacts]
where RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport)
and Entity = ? -- This Isn't really necessary
order by RetailTransactionId
```

#### OLE DB Source -DW - DynamicsPaymentFacts — SqlCommand

```sql
-- Old Method Used CTE to Specify Target Transactions
-- Now Building a Reference Table within the FEL 
--with Transactions as (
--select distinct RetailTransactionId
--from [dbo].[DynamicsTransactionHeaderFacts] (nolock) 
--where IsCurrent = 1
--and CurrentSentDate is null 
--and BatchID is null -- Unsure about this condition 
--and Entity = ?
----and TransDate = '5-1-2022' -- Testing Purposes Only 
----and InventLocationId = '1001' -- Testing Purposes Only 
----and RetailTransactionId in ('1239-1239Int-20230117-466450659_1','1175-1175Int-20230117-466457881_1','1404-1404Int-20230117-466455909_1','1404-1404Int-20230118-466488161_1','2063-2063Int-20230117-466432196_1','2063-2063Int-20230119-466519702_1') -- Testing Purposes Only 
--)


select * 
from  [DynamicsPaymentFacts]
--where RetailTransactionId in (select distinct RetailTransactionId from Transactions)
where RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport)
and Entity = ?
order by RetailTransactionId
```

#### OLE DB Source - DW - DynamicsSalesDetailFacts — SqlCommand

```sql
-- Old Method Used CTE to Specify Target Transactions
-- Now Building a Reference Table within the FEL 
--with Transactions as (
--select distinct RetailTransactionId
--from [dbo].[DynamicsTransactionHeaderFacts] (nolock) 
--where IsCurrent = 1
--and CurrentSentDate is null 
--and BatchID is null -- Unsure about this condition 
--and Entity = ?
----and TransDate = '5-1-2022' -- Testing Purposes Only 
----and InventLocationId = '1001' -- Testing Purposes Only 
--and RetailTransactionId in ('1239-1239Int-20230117-466450659_1','1175-1175Int-20230117-466457881_1','1404-1404Int-20230117-466455909_1','1404-1404Int-20230118-466488161_1','2063-2063Int-20230117-466432196_1','2063-2063Int-20230119-466519702_1') -- Testing Purposes Only 
--)


select * 
from [dbo].[DynamicsSalesDetailFacts]
--where RetailTransactionId in (select distinct RetailTransactionId from Transactions)
where RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport)
and Entity = ?
order by RetailTransactionId
```

#### OLE DB Source - DW - DynamicsTaxFacts — SqlCommand

```sql
-- Old Method Used CTE to Specify Target Transactions
-- Now Building a Reference Table within the FEL 
--with Transactions as (
--select distinct RetailTransactionId
--from [dbo].[DynamicsTransactionHeaderFacts] (nolock) 
--where IsCurrent = 1
--and CurrentSentDate is null 
--and BatchID is null -- Unsure about this condition 
--and Entity = ?
----and TransDate = '5-1-2022' -- Testing Purposes Only 
----and InventLocationId = '1001' -- Testing Purposes Only 
----and RetailTransactionId in ('1239-1239Int-20230117-466450659_1','1175-1175Int-20230117-466457881_1','1404-1404Int-20230117-466455909_1','1404-1404Int-20230118-466488161_1','2063-2063Int-20230117-466432196_1','2063-2063Int-20230119-466519702_1') -- Testing Purposes Only 
--)

select * 
from  [DynamicsTaxFacts]
--where RetailTransactionId in (select distinct RetailTransactionId from Transactions)
where RetailTransactionId in (select distinct RetailTransactionId from tmpDynamicsRetailTransactionIdExport)
and Entity = ?
order by RetailTransactionId
```

#### OLE DB Source - DW - DynamicsTransactionHeaderFacts — SqlCommand

```sql
--select top 3600 RetailTransactionId, RetailReceiptId, Entity, TransDate -- We used for loadtesting purposes
select RetailTransactionId, RetailReceiptId, Entity, TransDate
from DynamicsTransactionHeaderFacts
where
(
	(
		IsCurrent = 1
		and CurrentSentDate is null 
		and BatchID is null
	) -- 
or 
	(
		IsNegatedCurrent =1 
		and NegativeSentDate is null 
		and BatchID is null
	) -- These Represent Negate Transactions 
)
--and TransDate between '01-29-2023' and '02-25-2023' -- Was used for load testing purposes 
--and InventLocationId = '1016'
--and RetailTransactionId in ('1016-1016Int-20230204-467484542_2') -- Used For Pushing Target Transactions
--and TransDate >= '02/26/2023'
--and RetailReceiptId in ('468706731') -- Testing Specific Transactions

group by RetailTransactionId, RetailReceiptId, Entity, TransDate
order by Entity, TransDate, RetailTransactionId
```

#### Trigger Columns — SqlCommand

```sql
select 'do nothing' as DoNothing
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| Flat File Destination - FileDiscounts |  | FlatFileDestination | DFT - Discount File | FileDiscounts |  |
| Flat File Destination - FileHeaders |  | FlatFileDestination | DFT - Header File | FileHeaders |  |
| Flat File Destination - FilePayments |  | FlatFileDestination | DFT - Payment File | FilePayments |  |
| Flat File Destination - FileLines |  | FlatFileDestination | DFT - Sales Detail File | FileLines |  |
| Flat File Destination - FileTaxes |  | FlatFileDestination | DFT - Tax File | FileTaxes |  |
| OLE DB Destination - DW - tmpDynamicsRetailTransactionIdExport |  | OLEDBDestination | Data Flow Task - Load Target Trans | dw |  |
| DynamicsPackageAPILog |  | OLEDBDestination | Stage Blob URL | IntegrationStaging |  |
| Recordset Destination |  | RecordsetDestination | Stage Blob URL |  |  |
