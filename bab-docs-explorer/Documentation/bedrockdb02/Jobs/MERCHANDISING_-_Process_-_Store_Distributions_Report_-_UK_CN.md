# Job: MERCHANDISING - Process - Store Distributions Report - UK_CN

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email to UK and CN stores with CSV attachment of store shipment export

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Store Distributions Report - UK_CN"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectStoreDistribution_UK_CN
```


