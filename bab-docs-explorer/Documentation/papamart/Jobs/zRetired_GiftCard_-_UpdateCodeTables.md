# Job: zRetired_GiftCard - UpdateCodeTables

**Enabled:** No  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_GiftCard - UpdateCodeTables"]
    JOB --> S1["Step 1: step1 [TSQL]"]
```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
exec spGiftCard_UpdateCodeTables
```

