# Job: zRetired_05_BigWebCartReport_Email

**Enabled:** No  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_05_BigWebCartReport_Email"]
    JOB --> S1["Step 1: BIGWebCartReports_Email [TSQL]"]
```

## Steps

### Step 1: BIGWebCartReports_Email
**Subsystem:** TSQL  

```sql
exec spWebCartReports_Email
```

