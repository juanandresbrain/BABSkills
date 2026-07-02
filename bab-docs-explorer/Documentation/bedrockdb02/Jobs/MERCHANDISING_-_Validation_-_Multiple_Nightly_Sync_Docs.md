# Job: MERCHANDISING - Validation - Multiple Nightly Sync Docs

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email and text message if multiple nightly sync documents have posted for a single location on the same day

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Validation - Multiple Nightly Sync Docs"]
    JOB --> spMerchandisingSelectMultipleShrinkDocs_1["Step 1: spMerchandisingSelectMultipleShrinkDocs [TSQL]"]`n```

## Steps

### Step 1: spMerchandisingSelectMultipleShrinkDocs
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectMultipleShrinkDocs
```


