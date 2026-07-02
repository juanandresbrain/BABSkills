# Job: New_Store_Setup_Check

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Performs some checks on store setup and reports to the business user responsible for said setup

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New_Store_Setup_Check"]
    JOB --> Merch_1["Step 1: Merch [TSQL]"]`n```

## Steps

### Step 1: Merch
**Subsystem:** TSQL  

```sql
exec spNewStoreSetupCheckMerch
```


