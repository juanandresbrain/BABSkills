# Job: WMS_UpdateOrderItemOverrideSounds

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_UpdateOrderItemOverrideSounds"]
    JOB --> EXEC_spUpdateOrderItemOverrideSounds_1["Step 1: EXEC spUpdateOrderItemOverrideSounds [TSQL]"]`n```

## Steps

### Step 1: EXEC spUpdateOrderItemOverrideSounds
**Subsystem:** TSQL  

```sql
EXEC [bearcluster01.sql.buildabear.com].[WebOrderProcessing].[WM].[spUpdateOrderItemOverrideSounds]
```


