# Job: POS_MergeZebraLabelPricing

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["POS_MergeZebraLabelPricing"]
    JOB --> Merge_Data_1["Step 1: Merge Data [TSQL]"]`n```

## Steps

### Step 1: Merge Data
**Subsystem:** TSQL  

```sql
USE [IntegrationStaging]  GO    DECLARE @RC int  EXECUTE @RC = [POS].[spMergeZebraLabelPricing]   GO  
```


