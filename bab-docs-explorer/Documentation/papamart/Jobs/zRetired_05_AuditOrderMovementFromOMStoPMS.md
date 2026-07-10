# Job: zRetired_05_AuditOrderMovementFromOMStoPMS

**Enabled:** No  
**Server:** papamart  
**Description:** exec DW.dbo.spAuditOrderMovementFromOMStoPMS  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_05_AuditOrderMovementFromOMStoPMS"]
    JOB --> S1["Step 1: step 1 [TSQL]"]
```

## Steps

### Step 1: step 1
**Subsystem:** TSQL  

```sql
exec spAuditOrderMovementFromOMStoPMS
```

