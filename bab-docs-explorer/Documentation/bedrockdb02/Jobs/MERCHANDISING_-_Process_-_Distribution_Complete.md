# Job: MERCHANDISING - Process - Distribution Complete

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Creates a 'distribution complete' document for the Pipeline to close distros that are 21 days or older (28 days for franchisees) or with 0 allocated qty. Replaces original process on WMETL01 SQL Agent: WAREHOUSES_HOST_Distribution_Complete_V2

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Distribution Complete"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectDistroComplete
```


