# Job: Voucher_WriteOff_Counts

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Voucher_WriteOff_Counts"]
    JOB --> S1["Step 1: Voucher WriteOff Counts [TSQL]"]
```

## Steps

### Step 1: Voucher WriteOff Counts
**Subsystem:** TSQL  

```sql
EXEC spVoucherWriteOffCounts
```

