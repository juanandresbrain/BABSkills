# Job: Daily Notification History Summary

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Daily Notification History Summary"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spDailyNotificationHistorySummary
```

