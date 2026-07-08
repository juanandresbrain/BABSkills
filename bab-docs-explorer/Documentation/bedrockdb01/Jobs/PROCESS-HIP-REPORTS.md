# Job: PROCESS-HIP-REPORTS

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Captures sales data for electronic sounds, sends email to HIP Digital.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PROCESS-HIP-REPORTS"]
    JOB --> S1["Step 1: uno [TSQL]"]
```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec spAuditworksEmailHIP
```

