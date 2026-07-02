# Job: MERCHANDISING - Process - Supplies Sold UDA

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Creates UDA for supplies sold

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Supplies Sold UDA"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputSuppliesUDA
```


