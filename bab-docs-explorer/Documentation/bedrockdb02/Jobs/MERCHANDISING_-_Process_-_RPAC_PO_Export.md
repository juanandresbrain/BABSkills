# Job: MERCHANDISING - Process - RPAC PO Export

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Exports PO data to RPAC for styles with PAWID attribute

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - RPAC PO Export"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectRpacPO
```


