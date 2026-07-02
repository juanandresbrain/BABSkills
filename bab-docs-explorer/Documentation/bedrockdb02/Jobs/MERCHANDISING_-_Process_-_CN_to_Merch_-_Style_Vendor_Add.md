# Job: MERCHANDISING - Process - CN to Merch - Style Vendor Add

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Creates .GO file to add style vendors for CN styles where needed via pipeline.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - CN to Merch - Style Vendor Add"]
    JOB --> Execute_Stored_Procedure_1["Step 1: Execute Stored Procedure [TSQL]"]`n```

## Steps

### Step 1: Execute Stored Procedure
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputCNStyleVendor
```


