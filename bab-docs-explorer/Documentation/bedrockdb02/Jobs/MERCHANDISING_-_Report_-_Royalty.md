# Job: MERCHANDISING - Report - Royalty

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Royalty Report for Physical Inventory - consolidates a series of Smartlook reports into a single query

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Royalty"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingRoyaltyReports
```


