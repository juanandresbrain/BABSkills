# Job: DeleteOldFiles

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DeleteOldFiles"]
    JOB --> DeleteOldFilesHardCodedDirectories_1["Step 1: DeleteOldFilesHardCodedDirectories [TSQL]"]`n```

## Steps

### Step 1: DeleteOldFilesHardCodedDirectories
**Subsystem:** TSQL  

```sql
exec spDeleteOldFilesHardCodedDirectories
```


