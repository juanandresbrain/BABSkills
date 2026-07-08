# Job: PollFileMove

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Moves poll files from oursblanc to posappsa01  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PollFileMove"]
    JOB --> S1["Step 1: Uno [TSQL]"]
```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
exec spAuditworksCopyPollFiles
```

