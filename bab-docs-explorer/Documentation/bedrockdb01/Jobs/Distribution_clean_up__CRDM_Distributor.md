# Job: Distribution clean up: CRDM_Distributor

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Removes replicated transactions from the distribution database.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Distribution clean up: CRDM_Distributor"]
    JOB --> S1["Step 1: Run agent. [TSQL]"]
```

## Steps

### Step 1: Run agent.
**Subsystem:** TSQL  

```sql
EXEC dbo.sp_MSdistribution_cleanup @min_distretention = 0, @max_distretention = 72
```

