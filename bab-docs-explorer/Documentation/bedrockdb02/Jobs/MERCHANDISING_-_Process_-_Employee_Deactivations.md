# Job: MERCHANDISING - Process - Employee Deactivations

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** For stores that are closed, creates a pipeline file to deactivate the store's employee account.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Employee Deactivations"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmployeeDeactivateActivate
```


