# Job: MERCHANDISING - Email New Country

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Looks for new country records which exist in country table but not in keith_country table, sends email.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Email New Country"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailNewCountry
```


