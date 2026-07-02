# Job: Poll - Reload Job Status Data

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Poll - Reload Job Status Data"]
    JOB --> Reload_Job_Status_1["Step 1: Reload Job Status [SSIS]"]`n```

## Steps

### Step 1: Reload Job Status
**Subsystem:** SSIS  

```sql
/FILE "\"\\kermode\filerepository\Poll\Reload Job Status Data.dtsx\"" /CHECKPOINTING OFF /REPORTING E
```


