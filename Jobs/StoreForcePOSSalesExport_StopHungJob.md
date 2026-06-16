# Job: StoreForcePOSSalesExport_StopHungJob

**Enabled:** Yes  
**Description:** Stops job if it is running too long, will run the job again with the StoreForcePOSSalesExtractRunType parameter set to MergeAndFileOnly, so it will at least send the data that was captured before hanging.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["StoreForcePOSSalesExport_StopHungJob"]
    JOB --> spSQLAGentStopLongRunningJob_1["Step 1: spSQLAGentStopLongRunningJob [TSQL]"]`n```

## Steps

### Step 1: spSQLAGentStopLongRunningJob
**Subsystem:** TSQL  

```sql
declare @run int  select @run = 60    exec spSQLAGentStopLongRunningJob   @Job= 'StoreForcePosSalesExport_Every30Minutes',   @Runtime = @run,   @Rec = 'dant@buildabear.com'
```


