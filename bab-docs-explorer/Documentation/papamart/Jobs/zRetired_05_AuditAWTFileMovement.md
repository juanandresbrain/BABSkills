# Job: zRetired_05_AuditAWTFileMovement

**Enabled:** No  
**Server:** papamart  
**Description:** exec [spAuditAWTFileMovement]  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_05_AuditAWTFileMovement"]
    JOB --> S1["Step 1: [spAuditAWTFileMovement] [TSQL]"]
```

## Steps

### Step 1: [spAuditAWTFileMovement]
**Subsystem:** TSQL  

```sql
exec spAuditAWTFileMovement
```

