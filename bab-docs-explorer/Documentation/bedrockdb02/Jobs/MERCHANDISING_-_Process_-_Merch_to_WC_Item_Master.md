# Job: MERCHANDISING - Process - Merch to WC Item Master

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** uploads item master file to west coast warehouse - Dsabled on 10/11/2016 as DDC Advised they do not use the file

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to WC Item Master"]
    JOB --> 1___Export_File_1["Step 1: 1 - Export File [TSQL]"]`n```

## Steps

### Step 1: 1 - Export File
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputItemMasterWC
```


