# Job: VAT Missing on UK Trans

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Sends email alert in the event this process finds UK sale transacation(s) with Merchandise item(s) sold and no VAT received line in the transaction.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["VAT Missing on UK Trans"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spVAT_Missing_UK_Trans
```

