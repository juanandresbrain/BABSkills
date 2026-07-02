# Job: MERCHANDISING - Process - Add MSOUND Attribute

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Identifies styles which should have MSOUND attribute, generates file for Pipeline to add the attribute.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Add MSOUND Attribute"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputMsoundAttribute
```


