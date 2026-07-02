# Job: ZRetired_MERCHANDISING - Process - PMSOrderNumberExportFile

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ZRetired_MERCHANDISING - Process - PMSOrderNumberExportFile"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingProcessPMSOrderNumberExportFile
```


