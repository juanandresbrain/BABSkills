# Job: Replication agents checkup

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Detects replication agents that are not logging history actively.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Replication agents checkup"]
    JOB --> S1["Step 1: Run agent. [TSQL]"]
```

## Steps

### Step 1: Run agent.
**Subsystem:** TSQL  

```sql
sys.sp_replication_agent_checkup @heartbeat_interval = 10
```

