# Job: POS_JumpMindEndlessAisleOrdersNotInEntSelling

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["POS_JumpMindEndlessAisleOrdersNotInEntSelling"]
    JOB --> spEmailEndlessAisleOrdersNotInEsell_1["Step 1: spEmailEndlessAisleOrdersNotInEsell [TSQL]"]`n```

## Steps

### Step 1: spEmailEndlessAisleOrdersNotInEsell
**Subsystem:** TSQL  

```sql
EXEC [IntegrationStaging].[ES].[spEmailEndlessAisleOrdersNotInEsell]
```


