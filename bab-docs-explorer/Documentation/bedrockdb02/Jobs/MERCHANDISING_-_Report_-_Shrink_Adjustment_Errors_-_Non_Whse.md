# Job: MERCHANDISING - Report - Shrink Adjustment Errors - Non Whse

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures and emails a summary of shrink adjustments errors logged from the pipeline for non warehouse shrink adjustments

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Shrink Adjustment Errors - Non Whse"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectShrinkErrors
```


