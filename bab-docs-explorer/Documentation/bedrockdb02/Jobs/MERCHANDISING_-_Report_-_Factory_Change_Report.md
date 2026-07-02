# Job: MERCHANDISING - Report - Factory Change Report

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Executes stored procedure to provide all instances where a style reported a factory change within the last week, providing that style had an existing factory code to begin with. Output is sent in an attachment to QC recipients and MerchAdmin.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Factory Change Report"]
    JOB --> Execute_Stored_Procedure_1["Step 1: Execute Stored Procedure [TSQL]"]`n```

## Steps

### Step 1: Execute Stored Procedure
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputFactoryChange
```


