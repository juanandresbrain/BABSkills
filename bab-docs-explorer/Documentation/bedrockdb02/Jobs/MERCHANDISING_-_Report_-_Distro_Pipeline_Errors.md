# Job: MERCHANDISING - Report - Distro Pipeline Errors

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures and emails details of records that failed to integrate from the distro_transfers table to the Merchandising system.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Distro Pipeline Errors"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectDistroPipelineErrors
```


