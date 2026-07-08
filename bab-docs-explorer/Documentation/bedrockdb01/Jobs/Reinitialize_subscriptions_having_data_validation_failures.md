# Job: Reinitialize subscriptions having data validation failures

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Reinitializes all subscriptions that have data validation failures.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Reinitialize subscriptions having data validation failures"]
    JOB --> S1["Step 1: Run agent. [TSQL]"]
```

## Steps

### Step 1: Run agent.
**Subsystem:** TSQL  

```sql
exec sys.sp_MSreinit_failed_subscriptions @failure_level = 1
```

