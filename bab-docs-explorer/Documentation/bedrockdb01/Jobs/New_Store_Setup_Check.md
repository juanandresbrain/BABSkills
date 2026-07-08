# Job: New_Store_Setup_Check

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Performs some checks on store setup and reports to the business user responsible for said setup  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New_Store_Setup_Check"]
    JOB --> S1["Step 1: SA check [TSQL]"]
    S1 --> S2["Step 2: Comm check [TSQL]"]
```

## Steps

### Step 1: SA check
**Subsystem:** TSQL  

```sql
exec spNewStoreSetupCheckSA
```

### Step 2: Comm check
**Subsystem:** TSQL  

```sql
exec spNewStoreSetupCheckDE
```

