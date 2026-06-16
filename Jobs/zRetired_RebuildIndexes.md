# Job: zRetired_RebuildIndexes_

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_RebuildIndexes_"]
    JOB --> RebuildIndexes_1["Step 1: RebuildIndexes [TSQL]"]`n```

## Steps

### Step 1: RebuildIndexes
**Subsystem:** TSQL  

```sql
exec spIndexRebuildReorganize
```


