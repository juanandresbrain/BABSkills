# Job: MERCHANDISING - Process - WC Stock Adjustments

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Process inventory adjustment files from west coast dc, posts shrink adjustment file to Merch system

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - WC Stock Adjustments"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingProcessWcStockAdj

```


