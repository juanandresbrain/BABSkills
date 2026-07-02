# Job: MERCHANDISING - Process - Franchisee Transfer UDA and CBR

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Reports via CSV file of franchises transfers, creates CBR for the transfers, creates UDA for the transfers

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Franchisee Transfer UDA and CBR"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputFranchiseeUDA
```


