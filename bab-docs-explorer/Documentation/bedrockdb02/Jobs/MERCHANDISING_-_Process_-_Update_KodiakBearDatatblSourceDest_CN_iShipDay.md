# Job: MERCHANDISING - Process - Update KodiakBearDatatblSourceDest_CN iShipDay

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Update KodiakBearDatatblSourceDest_CN iShipDay"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec spMerchandisingUpdateKodiakBearDatatblSourceDest_CN 
```


