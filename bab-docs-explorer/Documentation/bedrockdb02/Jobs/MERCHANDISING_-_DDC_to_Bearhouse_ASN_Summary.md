# Job: MERCHANDISING - DDC to Bearhouse ASN Summary

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures Shipment data for shipments shipped from DDC to Bearhouse 'yesterday'

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - DDC to Bearhouse ASN Summary"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectDDCASNSummary
MERCHANDISING - DISTRO IMPORT | EXPORT | SPLIT	Yes	Imports Distros into Merch & Validate
Exports Distros from Merch
Runs Split Tool. 
Final Destination is me_01..Distribution_Data_After_Split. 

Starts SSIS SQL Agent Job on STL-SSIS-P-01 WMS_TransferOrderCreateFromAptos, which will push Distros to Dynamics.

This is SQL agent job step one of three for the new distro export process as of 8/1/2022 which includes integration of 3PW to Dyanamics.	1	Import Distros	TSQL	exec me_01.dbo.spMerchandisingImportDistributions
MERCHANDISING - DISTRO IMPORT | EXPORT | SPLIT	Yes	Imports Distros into Merch & Validate
Exports Distros from Merch
Runs Split Tool. 
Final Destination is me_01..Distribution_Data_After_Split. 

Starts SSIS SQL Agent Job on STL-SSIS-P-01 WMS_TransferOrderCreateFromAptos, which will push Distros to Dynamics.

This is SQL agent job step one of three for the new distro export process as of 8/1/2022 which includes integration of 3PW to Dyanamics.	2	Validate Distro CSV Import	TSQL	exec me_01.dbo.spMerchandisingDistroImportValidation	
MERCHANDISING - DISTRO IMPORT | EXPORT | SPLIT	Yes	Imports Distros into Merch & Validate
Exports Distros from Merch
Runs Split Tool. 
Final Destination is me_01..Distribution_Data_After_Split. 

Starts SSIS SQL Agent Job on STL-SSIS-P-01 WMS_TransferOrderCreateFromAptos, which will push Distros to Dynamics.

This is SQL agent job step one of three for the new distro export process as of 8/1/2022 which includes integration of 3PW to Dyanamics.	3	Validate Distro NON CSV Import	TSQL	exec me_01.dbo.spMerchandisingDistroTransfersValidation
MERCHANDISING - DISTRO IMPORT | EXPORT | SPLIT	Yes	Imports Distros into Merch & Validate
Exports Distros from Merch
Runs Split Tool. 
Final Destination is me_01..Distribution_Data_After_Split. 

Starts SSIS SQL Agent Job on STL-SSIS-P-01 WMS_TransferOrderCreateFromAptos, which will push Distros to Dynamics.

This is SQL agent job step one of three for the new distro export process as of 8/1/2022 which includes integration of 3PW to Dyanamics.	4	DistroExport and Split	TSQL	exec me_01.dbo.spMerchandisingStageDistroSplit
MERCHANDISING - DISTRO IMPORT | EXPORT | SPLIT	Yes	Imports Distros into Merch & Validate
Exports Distros from Merch
Runs Split Tool. 
Final Destination is me_01..Distribution_Data_After_Split. 

Starts SSIS SQL Agent Job on STL-SSIS-P-01 WMS_TransferOrderCreateFromAptos, which will push Distros to Dynamics.

This is SQL agent job step one of three for the new distro export process as of 8/1/2022 which includes integration of 3PW to Dyanamics.	5	Execute SQL Agent WMS_TransferOrderCreateFromAptos	TSQL	EXEC [STL-SSIS-P-01].msdb.dbo.sp_start_job @job_name='WMS_TransferOrderCreateFromAptos'
```


