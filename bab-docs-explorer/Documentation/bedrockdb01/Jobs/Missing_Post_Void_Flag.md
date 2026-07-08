# Job: Missing_Post_Void_Flag

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Reports Post Voiding transactions that the coorisponding Voided transaction is not flagged in SA as a Post-Voided transaction  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Missing_Post_Void_Flag"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spMissingPostVoidFlag
```

