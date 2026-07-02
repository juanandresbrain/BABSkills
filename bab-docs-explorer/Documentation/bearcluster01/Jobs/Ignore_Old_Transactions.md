# Job: Ignore Old Transactions

**Enabled:** No  
**Server:** bearcluster01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Ignore Old Transactions"]
    JOB --> Ignore_Old_Transactions_1["Step 1: Ignore Old Transactions [TSQL]"]`n```

## Steps

### Step 1: Ignore Old Transactions
**Subsystem:** TSQL  

```sql
  UPDATE [ApplicationResources].[POS].[JumpMindAPI_Logging]
  SET processed = 1
  WHERE CAST(jsonDateTime AS DATE) <> '2024-09-24' AND processed = 0
```


