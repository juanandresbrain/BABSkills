# SSIS Package: ExportWebCouponsPackage

**Project:** WebCoupons  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| Coupons.zip | FILE |  |  |  |
| Kodiak.DiscountMstrData | OLEDB | Kodiak | DiscountMstrData | Data Source=Kodiak; Initial Catalog=DiscountMstrData; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP_EMAIL | SMTP |  |  |  |
| SQL_LOG | OLEDB | stl-ssis-p-01 | msdb | Data Source=stl-ssis-p-01; Initial Catalog=msdb; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| STL-SSIS-P-01 | SMOServer |  |  |  |
| STL-SSIS-P-01.IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| ExportWebCouponsPackage | Package |
| File Generation and Move | SEQUENCE |
| Archive ZIP File | FileSystemTask |
| Copy File to FTP Stage | FileSystemTask |
| Delete Old Files | ExecuteSQLTask |
| SendEmail | ExecuteSQLTask |
| Zip Files | ExecuteProcess |
| Foreach New Discount Coupon | FOREACHLOOP |
| Export Coupons XML File | ExecuteSQLTask |
| Set discountID as Exported | ExecuteSQLTask |
| Stage Discount Coupon Data | SEQUENCE |
| Copy Coupon Data to Staging | Pipeline |
| Get DiscountCoupons List | ExecuteSQLTask |
| Get TotalNewItems Count | ExecuteSQLTask |
| Truncate Staging | ExecuteSQLTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- File Generation and Move [SEQUENCE]
  - Archive ZIP File [FileSystemTask]
  - Copy File to FTP Stage [FileSystemTask]
  - Delete Old Files [ExecuteSQLTask]
  - SendEmail [ExecuteSQLTask]
  - Zip Files [ExecuteProcess]
- Foreach New Discount Coupon [FOREACHLOOP]
  - Export Coupons XML File [ExecuteSQLTask]
  - Set discountID as Exported [ExecuteSQLTask]
- Stage Discount Coupon Data [SEQUENCE]
  - Copy Coupon Data to Staging [Pipeline]
  - Get DiscountCoupons List [ExecuteSQLTask]
  - Get TotalNewItems Count [ExecuteSQLTask]
  - Truncate Staging [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_File_Generation_and_Move["File Generation and Move"]
    n_Package_File_Generation_and_Move_Archive_ZIP_File["Archive ZIP File"]
    n_Package_File_Generation_and_Move_Copy_File_to_FTP_Stage["Copy File to FTP Stage"]
    n_Package_File_Generation_and_Move_Delete_Old_Files["Delete Old Files"]
    n_Package_File_Generation_and_Move_SendEmail["SendEmail"]
    n_Package_File_Generation_and_Move_Zip_Files["Zip Files"]
    n_Package_Foreach_New_Discount_Coupon["Foreach New Discount Coupon"]
    n_Package_Foreach_New_Discount_Coupon_Export_Coupons_XML_File["Export Coupons XML File"]
    n_Package_Foreach_New_Discount_Coupon_Set_discountID_as_Exported["Set discountID as Exported"]
    n_Package_Stage_Discount_Coupon_Data["Stage Discount Coupon Data"]
    n_Package_Stage_Discount_Coupon_Data_Copy_Coupon_Data_to_Staging["Copy Coupon Data to Staging"]
    n_Package_Stage_Discount_Coupon_Data_Get_DiscountCoupons_List["Get DiscountCoupons List"]
    n_Package_Stage_Discount_Coupon_Data_Get_TotalNewItems_Count["Get TotalNewItems Count"]
    n_Package_Stage_Discount_Coupon_Data_Truncate_Staging["Truncate Staging"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_File_Generation_and_Move_Delete_Old_Files --> n_Package_File_Generation_and_Move_SendEmail
    n_Package_File_Generation_and_Move_Copy_File_to_FTP_Stage --> n_Package_File_Generation_and_Move_Archive_ZIP_File
    n_Package_File_Generation_and_Move_Archive_ZIP_File --> n_Package_File_Generation_and_Move_Delete_Old_Files
    n_Package_File_Generation_and_Move_Zip_Files --> n_Package_File_Generation_and_Move_Copy_File_to_FTP_Stage
    n_Package_Foreach_New_Discount_Coupon_Export_Coupons_XML_File --> n_Package_Foreach_New_Discount_Coupon_Set_discountID_as_Exported
    n_Package_Stage_Discount_Coupon_Data_Truncate_Staging --> n_Package_Stage_Discount_Coupon_Data_Copy_Coupon_Data_to_Staging
    n_Package_Stage_Discount_Coupon_Data_Copy_Coupon_Data_to_Staging --> n_Package_Stage_Discount_Coupon_Data_Get_DiscountCoupons_List
    n_Package_Stage_Discount_Coupon_Data_Get_DiscountCoupons_List --> n_Package_Stage_Discount_Coupon_Data_Get_TotalNewItems_Count
    n_Package_Stage_Discount_Coupon_Data --> n_Package_Foreach_New_Discount_Coupon
    n_Package_Foreach_New_Discount_Coupon --> n_Package_File_Generation_and_Move
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | CouponsFileRename | Yes |
| User | Current_cntryAbbr | No |
| User | Current_discountAmount | No |
| User | Current_discountID | No |
| User | Current_endingDate | No |
| User | Current_group | No |
| User | DiscountCouponsList | No |
| User | FTPStageDirectory | No |
| User | FileCount | No |
| User | FilePath | No |
| User | ListOfXMLFiles | No |
| User | TotalNewItems | No |
| User | ZipCommand | Yes |
| User | ZipDest | No |
| User | ZipSource | No |

### Expression-bound variable values

#### User::CouponsFileRename

**Expression:**

```sql
"\\\\STL-SSIS-P-01\\IntegrationStaging\\WEB\\Outbound\\Coupons\\Archive\\" + "Coupons" + 
(DT_WSTR, 4) YEAR( @[System::ContainerStartTime]  ) +  (DT_WSTR, 2) MONTH( @[System::ContainerStartTime]  ) + (DT_WSTR, 2) DAY( @[System::ContainerStartTime]  ) +  (DT_WSTR, 2) DATEPART("Hh", @[System::ContainerStartTime] ) + (DT_WSTR, 2) DATEPART("mi", @[System::ContainerStartTime] ) + (DT_WSTR, 2) DATEPART("ss", @[System::ContainerStartTime] ) + (DT_WSTR, 2) DATEPART("Ms", @[System::ContainerStartTime] ) + ".zip"
```

**Evaluated value:**

```sql
\\STL-SSIS-P-01\IntegrationStaging\WEB\Outbound\Coupons\Archive\Coupons20171019936390.zip
```

#### User::ZipCommand

**Expression:**

```sql
"a -tzip \""+ @[User::ZipDest]  + "\"  \"" +  @[User::ZipSource]  +"\" -sdel"
```

**Evaluated value:**

```sql
a -tzip "\\STL-SSIS-P-01\IntegrationStaging\WEB\Outbound\Coupons\Coupons.zip"  "\\STL-SSIS-P-01\IntegrationStaging\WEB\Outbound\Coupons\*.xml" -sdel
```

## Execute SQL Tasks

### Delete Old Files

**Path:** `Package\File Generation and Move\Delete Old Files`  
**Connection:** STL-SSIS-P-01.IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec spDeleteOldFiles @path = '\\STL-SSIS-P-01\IntegrationStaging\WEB\Outbound\Coupons\Archive', @filemask = '*.zip', @retention = 14
```

### SendEmail

**Path:** `Package\File Generation and Move\SendEmail`  
**Connection:** STL-SSIS-P-01.IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
EXEC dbo.spConvertCouponStagingtoHTML
```

### Export Coupons XML File

**Path:** `Package\Foreach New Discount Coupon\Export Coupons XML File`  
**Connection:** Kodiak.DiscountMstrData (Kodiak/DiscountMstrData)  

```sql
EXEC [dbo].[spExportWebCouponFiles] @discountID = ?, @discountAmount = ?, @endingDate = ?, @cntryAbbr = ?
```

### Set discountID as Exported

**Path:** `Package\Foreach New Discount Coupon\Set discountID as Exported`  
**Connection:** Kodiak.DiscountMstrData (Kodiak/DiscountMstrData)  

```sql
UPDATE Discount
SET isExportedToWeb = 1
WHERE discountID = ?
```

### Get DiscountCoupons List

**Path:** `Package\Stage Discount Coupon Data\Get DiscountCoupons List`  
**Connection:** STL-SSIS-P-01.IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
select * from [WEB].[DiscountCouponExport]
```

### Get TotalNewItems Count

**Path:** `Package\Stage Discount Coupon Data\Get TotalNewItems Count`  
**Connection:** STL-SSIS-P-01.IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
SELECT COUNT(*) as Result FROM [WEB].[DiscountCouponExport]
```

### Truncate Staging

**Path:** `Package\Stage Discount Coupon Data\Truncate Staging`  
**Connection:** STL-SSIS-P-01.IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE [WEB].[DiscountCouponExport]
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| DiscountMstrData |  | OLEDBSource | Copy Coupon Data to Staging | Kodiak.DiscountMstrData | SqlCommand |

#### DiscountMstrData — SqlCommand

```sql
SELECT discountID,
              discountAmount,
              cntryAbbr,
              endingDate,
              totalCoupons,
              couponNumber
FROM [dbo].[vwCouponsExportToWeb]
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| CouponExport Staging |  | OLEDBDestination | Copy Coupon Data to Staging | STL-SSIS-P-01.IntegrationStaging |  |
