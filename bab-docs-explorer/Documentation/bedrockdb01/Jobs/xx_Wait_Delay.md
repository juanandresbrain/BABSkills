# Job: xx Wait Delay

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["xx Wait Delay"]
    JOB --> S1["Step 1: UNO [TSQL]"]
```

## Steps

### Step 1: UNO
**Subsystem:** TSQL  

```sql
WAITFOR DELAY '00:01:00'; -- Wait for 1 min
```

