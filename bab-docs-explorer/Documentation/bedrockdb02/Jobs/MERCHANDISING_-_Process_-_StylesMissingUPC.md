# Job: MERCHANDISING - Process - StylesMissingUPC

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Creates pipeline file for styles which do not have a UPC.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - StylesMissingUPC"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputStylesMissingUPC
```


