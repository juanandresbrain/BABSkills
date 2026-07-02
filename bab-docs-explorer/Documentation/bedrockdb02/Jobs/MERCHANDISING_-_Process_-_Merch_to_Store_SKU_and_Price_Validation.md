# Job: MERCHANDISING - Process - Merch to Store SKU and Price Validation

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Purpose is to notify IT of SKUs that are active at a store, but inactive in Merchandising. Captures data from every store, compares to Merchandising, sends email summary.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to Store SKU and Price Validation"]
    JOB --> uno_1["Step 1: uno [SSIS]"]`n```

## Steps

### Step 1: uno
**Subsystem:** SSIS  

```sql
/FILE "\"\\kermode\d$\SSIS Packages\InactiveSkuValidation\InactiveSkuValidation_.dtsx\"" /CHECKPOINTING OFF /REPORTING E
```


