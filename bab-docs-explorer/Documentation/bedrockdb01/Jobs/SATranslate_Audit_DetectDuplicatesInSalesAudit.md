# Job: SATranslate_Audit_DetectDuplicatesInSalesAudit

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SATranslate_Audit_DetectDuplicatesInSalesAudit"]
    JOB --> S1["Step 1: step 1 [TSQL]"]
```

## Steps

### Step 1: step 1
**Subsystem:** TSQL  

```sql
exec spSA_DetectAndAlertAWproblems 30
```

