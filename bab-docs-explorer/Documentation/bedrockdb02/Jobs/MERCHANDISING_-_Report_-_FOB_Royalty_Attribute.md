# Job: MERCHANDISING - Report - FOB Royalty Attribute

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Executes stored procedure to provide all instances where a style added the attribute_set "FOB" to the attribute "LICEN'.  Output is sent in an attachment to selected recipients and MerchAdmin.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - FOB Royalty Attribute"]
    JOB --> Execute_Stored_Procedure_1["Step 1: Execute Stored Procedure [TSQL]"]`n```

## Steps

### Step 1: Execute Stored Procedure
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputFOBRoyalty
```


