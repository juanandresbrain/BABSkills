# Job: WEB - Email SalesAudit Duplicate Transactions

**Enabled:** Yes  
**Description:** Executes [bearcluster01.sql.buildabear.com].[WebOrderProcessing].[dbo].[spGetDuplicateSATransactionsByDate]

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - Email SalesAudit Duplicate Transactions"]
    JOB --> Execute_spGetDuplicateSATransactionsByDate_1["Step 1: Execute spGetDuplicateSATransactionsByDate [TSQL]"]`n```

## Steps

### Step 1: Execute spGetDuplicateSATransactionsByDate
**Subsystem:** TSQL  

```sql
EXEC [bearcluster01.sql.buildabear.com].[WebOrderProcessing].[dbo].[spGetDuplicateSATransactionsByDate]
```


