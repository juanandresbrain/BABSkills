# Job: MERCHANDISING - Process - Merch to UK Item Master

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Exports item master data to UK warehouse

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to UK Item Master"]
    JOB --> 1___Export_File_1["Step 1: 1 - Export File [TSQL]"]`n    JOB --> 2___Upload_File_2["Step 2: 2 - Upload File [TSQL]"]`n```

## Steps

### Step 1: 1 - Export File
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputItemMasterXML_UK
```

### Step 2: 2 - Upload File
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFtpUKSKU -- Replaced on 2/2/2017

exec me_01.dbo.spMerchandisingFtpUKItemMaster_WinSCP
```


