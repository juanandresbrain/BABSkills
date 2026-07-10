# Job: AzureLoadFranchiseeTopStyles

**Enabled:** Yes  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["AzureLoadFranchiseeTopStyles"]
    JOB --> S1["Step 1: Run stored Proc [TSQL]"]
```

## Steps

### Step 1: Run stored Proc
**Subsystem:** TSQL  

```sql
Execute azure.spGetFranchiseeTopStylesandAvailability
```

