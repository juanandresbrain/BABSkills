# Job: WEB - Commhub Process new Deck Orders

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - Commhub Process new Deck Orders"]
    JOB --> EXEC_ProcessNewDeckWebOrders_1["Step 1: EXEC ProcessNewDeckWebOrders [SSIS]"]`n```

## Steps

### Step 1: EXEC ProcessNewDeckWebOrders
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ComHub\ProcessNewDeckWebOrders.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par WebOrderProcessingServer;"\"bearcluster01.sql.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


