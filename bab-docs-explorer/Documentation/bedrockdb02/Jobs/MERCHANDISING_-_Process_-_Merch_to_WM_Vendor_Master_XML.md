# Job: MERCHANDISING - Process - Merch to WM Vendor Master XML

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** exports vendor master xml to WM

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to WM Vendor Master XML"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputVendorMasterXML
MERCHANDISING - Process - MinMaxProfileArchive	Yes	Captures current date and all data from min_max_profile table. 
This data is normally overwritten every Sunday and there is no other archive of this data, yet we need to report against it.
Process also archives configuration data.	1	one	TSQL	exec me_01.dbo.spMerchandisingInsertMinMaxProfileArchive
```


