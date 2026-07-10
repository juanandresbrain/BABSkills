# Job: zRetired_Distro - Mismatched StdPackQty With 980

**Enabled:** No  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_Distro - Mismatched StdPackQty With 980"]
    JOB --> S1["Step 1: step1 [TSQL]"]
```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
exec spDistro_MismatchedStdPackQtyWith980
```

