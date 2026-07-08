# Job: MissingTransQtyAlert

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Sends email and text alert if too many store/register combination transactions are missing from SA. Also lists Missing Transactions in SA.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MissingTransQtyAlert"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spMissingTransQtyAlert
```

