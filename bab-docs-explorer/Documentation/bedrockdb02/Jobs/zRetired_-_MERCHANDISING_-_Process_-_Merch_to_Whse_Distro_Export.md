# Job: zRetired - MERCHANDISING - Process - Merch to Whse Distro Export

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Exports Distros from Merchandising to All Warehouses; Pushed to production on 02/25/2020 by Lizzy T to acommodate changes due to the Dynamics WMS upgrade. Retired on 7/30/2022 as related to 3PW Integration into Dynamics

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired - MERCHANDISING - Process - Merch to Whse Distro Export"]
    JOB --> Import_Distros_1["Step 1: Import Distros [TSQL]"]`n    JOB --> Validate_Distro_CSV_Import_2["Step 2: Validate Distro CSV Import [TSQL]"]`n    JOB --> Validate_Distro_NON_CSV_Import_3["Step 3: Validate Distro NON CSV Import [TSQL]"]`n    JOB --> Stage_Distro_Split_4["Step 4: Stage Distro Split [TSQL]"]`n    JOB --> Export_to_WC_5["Step 5: Export to WC [TSQL]"]`n    JOB --> FTP_Upload_to_WC_6["Step 6: FTP Upload to WC [TSQL]"]`n    JOB --> Store_Shipment_Confirmation___WC_7["Step 7: Store Shipment Confirmation - WC [TSQL]"]`n    JOB --> Export_Summary___WC_8["Step 8: Export Summary - WC [TSQL]"]`n    JOB --> Export_to_UK_9["Step 9: Export to UK [TSQL]"]`n    JOB --> FTP_Upload_to_UK_10["Step 10: FTP Upload to UK [TSQL]"]`n    JOB --> Store_Shipment_Confirmation___UK_11["Step 11: Store Shipment Confirmation - UK [TSQL]"]`n    JOB --> Export_Summary___UK_12["Step 12: Export Summary - UK [TSQL]"]`n    JOB --> Export_to_CN_13["Step 13: Export to CN [TSQL]"]`n    JOB --> FTP_Upload_to_CN_14["Step 14: FTP Upload to CN [TSQL]"]`n    JOB --> Store_Shipment_Confirmation___CN_15["Step 15: Store Shipment Confirmation - CN [TSQL]"]`n    JOB --> Export_Summary___CN_16["Step 16: Export Summary - CN [TSQL]"]`n    JOB --> Execute_WMS_TransferOrderCreateFromAptos_17["Step 17: Execute WMS_TransferOrderCreateFromAptos [TSQL]"]`n```

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

### Step 5: Export to WC
**Subsystem:** TSQL  

```sql
--IF DATEPART(HOUR, GETDATE()) >= '13'
IF CONVERT(VARCHAR,GETDATE(), 108) >= '12:30:00' -- Updated to 12:30 per SR #28327, LT 09/16/20

Begin 

	exec me_01.dbo.spMerchandisingExportStoreDistributionsWC

End 

```

### Step 6: FTP Upload to WC
**Subsystem:** TSQL  

```sql
--IF DATEPART(HOUR, GETDATE()) >= '13'
IF CONVERT(VARCHAR,GETDATE(), 108) >= '12:30:00' -- Updated to 12:30 per SR #28327, LT 09/16/20

Begin 

	-- exec me_01.dbo.spMerchandisingFtpWCDistro-- Replaced with WinSCP script
	exec me_01.dbo.spMerchandisingFtpWCDistroWinSCP

End 

```

### Step 7: Store Shipment Confirmation - WC
**Subsystem:** TSQL  

```sql
--IF DATEPART(HOUR, GETDATE()) >= '13'
IF CONVERT(VARCHAR,GETDATE(), 108) >= '12:30:00' -- Updated to 12:30 per SR #28327, LT 09/16/20

Begin 

	exec me_01.dbo.spMerchandisingReportStoreShipmentExportConfirmationWC

End 

```

### Step 8: Export Summary - WC
**Subsystem:** TSQL  

```sql
--IF DATEPART(HOUR, GETDATE()) >= '13'
IF CONVERT(VARCHAR,GETDATE(), 108) >= '12:30:00' -- Updated to 12:30 per SR #28327, LT 09/16/20

Begin 

	exec me_01.dbo.spMerchandisingToWCDistroExportNotification

End 

```

### Step 9: Export to UK
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingExportStoreDistributionsUK
```

### Step 10: FTP Upload to UK
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFtpUKDistro -- Replaced on 2/2/2017

exec me_01.dbo.spMerchandisingFTPUKDistro_WinSCP
```

### Step 11: Store Shipment Confirmation - UK
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportStoreShipmentExportConfirmationUK
```

### Step 12: Export Summary - UK
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingToUKDistroExportNotification
```

### Step 13: Export to CN
**Subsystem:** TSQL  

```sql
exec spMerchandisingExportStoreDistributionsCN
```

### Step 14: FTP Upload to CN
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCNDistro
```

### Step 15: Store Shipment Confirmation - CN
**Subsystem:** TSQL  

```sql
exec spMerchandisingReportStoreShipmentExportConfirmationCN
```

### Step 16: Export Summary - CN
**Subsystem:** TSQL  

```sql
--exec spMerchandisingToCNDistroExportNotification
-- Remarked out on 9/6/2018 isnt useful anyway
```

### Step 17: Execute WMS_TransferOrderCreateFromAptos
**Subsystem:** TSQL  

```sql
EXEC [STL-SSIS-P-01].msdb.dbo.sp_start_job @job_name='WMS_TransferOrderCreateFromAptos'
```


