# Job: Replication monitoring refresher for CRDM_Distributor.

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Replication monitoring refresher for CRDM_Distributor.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Replication monitoring refresher for CRDM_Distributor."]
    JOB --> S1["Step 1: Run agent. [TSQL]"]
```

## Steps

### Step 1: Run agent.
**Subsystem:** TSQL  

```sql
exec dbo.sp_replmonitorrefreshjob
```

