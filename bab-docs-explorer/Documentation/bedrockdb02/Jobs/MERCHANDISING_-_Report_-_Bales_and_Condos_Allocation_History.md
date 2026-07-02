# Job: MERCHANDISING - Report - Bales and Condos Allocation History

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Executes stored procedure to provide historical (daily) allocations of stuffing bales and condos for both NA & EU. Output is emailed to MerchAdmin and Chad Vitale.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Bales and Condos Allocation History"]
    JOB --> Execute_Stored_Procedure_1["Step 1: Execute Stored Procedure [TSQL]"]`n```

## Steps

### Step 1: Execute Stored Procedure
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputBaleCondo
```


