# Job: zRetired - MERCHANDISING - Process - Merch to Whse Distro Export BAK

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Exports Distros from Merchandising to All Warehouses; renamed with BAK by Lizzy T on 02/25/2020 to allow for new WMS upgraded job to run.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired - MERCHANDISING - Process - Merch to Whse Distro Export BAK"]
    JOB --> Import_Distros_1["Step 1: Import Distros [TSQL]"]`n    JOB --> Validate_Distro_CSV_Import_2["Step 2: Validate Distro CSV Import [TSQL]"]`n    JOB --> Validate_Distro_NON_CSV_Import_3["Step 3: Validate Distro NON CSV Import [TSQL]"]`n    JOB --> Stage_Distro_Split_4["Step 4: Stage Distro Split [TSQL]"]`n    JOB --> Export_to_WM_5["Step 5: Export to WM [TSQL]"]`n    JOB --> Export_WM_to_WEB_6["Step 6: Export WM to WEB [TSQL]"]`n    JOB --> Export_Summary___WM_7["Step 7: Export Summary - WM [TSQL]"]`n    JOB --> Export_to_WC_8["Step 8: Export to WC [TSQL]"]`n    JOB --> FTP_Upload_to_WC_9["Step 9: FTP Upload to WC [TSQL]"]`n    JOB --> Store_Shipment_Confirmation___WC_10["Step 10: Store Shipment Confirmation - WC [TSQL]"]`n    JOB --> Export_Summary___WC_11["Step 11: Export Summary - WC [TSQL]"]`n    JOB --> Export_to_UK_12["Step 12: Export to UK [TSQL]"]`n    JOB --> FTP_Upload_to_UK_13["Step 13: FTP Upload to UK [TSQL]"]`n    JOB --> Store_Shipment_Confirmation___UK_14["Step 14: Store Shipment Confirmation - UK [TSQL]"]`n    JOB --> Export_Summary___UK_15["Step 15: Export Summary - UK [TSQL]"]`n    JOB --> Costco_Distros_16["Step 16: Costco Distros [TSQL]"]`n    JOB --> Export_to_CN_17["Step 17: Export to CN [TSQL]"]`n    JOB --> FTP_Upload_to_CN_18["Step 18: FTP Upload to CN [TSQL]"]`n    JOB --> Store_Shipment_Confirmation___CN_19["Step 19: Store Shipment Confirmation - CN [TSQL]"]`n    JOB --> Export_Summary___CN_20["Step 20: Export Summary - CN [TSQL]"]`n```

## Steps

### Step 1: Import Distros
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingImportDistributions
```

### Step 2: Validate Distro CSV Import
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDistroImportValidation
```

### Step 3: Validate Distro NON CSV Import
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingDistroTransfersValidation
```

### Step 4: Stage Distro Split
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingStageDistroSplit
```

### Step 5: Export to WM
**Subsystem:** TSQL  

```sql
--exec me_01.dbo.spMerchandisingExportStoreDistributionsWM
```

### Step 6: Export WM to WEB
**Subsystem:** TSQL  

```sql
--exec me_01.dbo.spMerchandisingExportWebDistros
```

### Step 7: Export Summary - WM
**Subsystem:** TSQL  

```sql
--exec me_01.dbo.spMerchandisingToWmDistroExportNotification
```

### Step 8: Export to WC
**Subsystem:** TSQL  

```sql
IF DATEPART(HOUR, GETDATE()) >= '13'


Begin 

	exec me_01.dbo.spMerchandisingExportStoreDistributionsWC

End 

```

### Step 9: FTP Upload to WC
**Subsystem:** TSQL  

```sql
IF DATEPART(HOUR, GETDATE()) >= '13'


Begin 

	exec me_01.dbo.spMerchandisingFtpWCDistro

End 

```

### Step 10: Store Shipment Confirmation - WC
**Subsystem:** TSQL  

```sql
IF DATEPART(HOUR, GETDATE()) >= '13'

Begin 

	exec me_01.dbo.spMerchandisingReportStoreShipmentExportConfirmationWC

End 

```

### Step 11: Export Summary - WC
**Subsystem:** TSQL  

```sql
IF DATEPART(HOUR, GETDATE()) >= '13'

Begin 

	exec me_01.dbo.spMerchandisingToWCDistroExportNotification

End 

```

### Step 12: Export to UK
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingExportStoreDistributionsUK
```

### Step 13: FTP Upload to UK
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFtpUKDistro -- Replaced on 2/2/2017

exec me_01.dbo.spMerchandisingFTPUKDistro_WinSCP
```

### Step 14: Store Shipment Confirmation - UK
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportStoreShipmentExportConfirmationUK
```

### Step 15: Export Summary - UK
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingToUKDistroExportNotification
```

### Step 16: Costco Distros
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectCostcoDistributions
```

### Step 17: Export to CN
**Subsystem:** TSQL  

```sql
exec spMerchandisingExportStoreDistributionsCN
```

### Step 18: FTP Upload to CN
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCNDistro
```

### Step 19: Store Shipment Confirmation - CN
**Subsystem:** TSQL  

```sql
exec spMerchandisingReportStoreShipmentExportConfirmationCN
```

### Step 20: Export Summary - CN
**Subsystem:** TSQL  

```sql
--exec spMerchandisingToCNDistroExportNotification
-- Remarked out on 9/6/2018 isnt useful anyway
```


