# Job: SFS Cert Balance Report

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Send SFS voucher balance info to Jack M at period end 01/17/2018 - [Paul B] - Job disabled per the request of Jeff Kimsey  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SFS Cert Balance Report"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spSFSvoucherBalanceReport
```

