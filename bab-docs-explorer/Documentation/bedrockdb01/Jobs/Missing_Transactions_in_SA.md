# Job: Missing_Transactions_in_SA

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Lists Missing Transactions in SA. These listed transactions need to be resubmitted at the store level  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Missing_Transactions_in_SA"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spMissingTransactionsInSA
```

