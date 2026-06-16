# Job: ES Sku Merge

**Enabled:** Yes  
**Description:** Merge BEDROCKDB02 ES Sku data for JumpMind Endless Aisle

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ES Sku Merge"]
    JOB --> EXEC_ES_spES_Sku_Merge_1["Step 1: EXEC ES.spES_Sku_Merge [TSQL]"]`n```

## Steps

### Step 1: EXEC ES.spES_Sku_Merge
**Subsystem:** TSQL  

```sql
EXEC IntegrationStaging.ES.spES_Sku_Merge
```


