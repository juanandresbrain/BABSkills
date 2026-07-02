# Job: USICOAL_Trans_Count_Check

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Checks transaction counts for current day and emails if count is below 100

## Architecture Diagram

```mermaid
flowchart LR
    JOB["USICOAL_Trans_Count_Check"]
    JOB --> Step_1_1["Step 1: Step 1 [TSQL]"]`n```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spUSICOALTransCountCheck
```


