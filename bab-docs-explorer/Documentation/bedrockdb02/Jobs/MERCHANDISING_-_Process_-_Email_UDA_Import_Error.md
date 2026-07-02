# Job: MERCHANDISING - Process - Email UDA Import Error

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures Pipeline error log for UDA imports, sends email

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Email UDA Import Error"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailImportUDAerrors
```


