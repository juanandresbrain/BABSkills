# Job: Vouchers with Negative Balance

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Emails notification if vouchers are found with a negative balance  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Vouchers with Negative Balance"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spVouchers_with_Negative_Balance
```

