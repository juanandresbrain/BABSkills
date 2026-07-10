# Job: zRetired_05_FindMismatchedAmountForPartyDeposit

**Enabled:** No  
**Server:** papamart  
**Description:** 05_FindMismatchedAmountForPartyDeposit  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_05_FindMismatchedAmountForPartyDeposit"]
    JOB --> S1["Step 1: step 1 [TSQL]"]
```

## Steps

### Step 1: step 1
**Subsystem:** TSQL  

```sql
exec spFindMismatchedAmountForPartyDeposit 0
```

