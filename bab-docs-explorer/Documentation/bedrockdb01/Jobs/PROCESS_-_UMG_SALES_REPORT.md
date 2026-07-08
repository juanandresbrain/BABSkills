# Job: PROCESS - UMG SALES REPORT

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Captures UMG digital sales data, uploads to UMG group each month. --NO LONGER NEEDED, PER LISA WAGGONER - 1/13/2015  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PROCESS - UMG SALES REPORT"]
    JOB --> S1["Step 1: uno [TSQL]"]
```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec spAuditworksUMGSalesFile
```

