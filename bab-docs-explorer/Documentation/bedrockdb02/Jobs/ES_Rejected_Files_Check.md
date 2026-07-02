# Job: ES_Rejected_Files_Check

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ES_Rejected_Files_Check"]
    JOB --> RTG_Files_Check_1["Step 1: RTG Files Check [TSQL]"]`n```

## Steps

### Step 1: RTG Files Check
**Subsystem:** TSQL  

```sql
exec spES_Rejected_Files_Check
```


