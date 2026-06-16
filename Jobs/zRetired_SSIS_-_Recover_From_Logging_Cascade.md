# Job: zRetired_SSIS - Recover From Logging Cascade

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_SSIS - Recover From Logging Cascade"]
    JOB --> Execute_delete_top_10_1["Step 1: Execute delete top 10 [TSQL]"]`n```

## Steps

### Step 1: Execute delete top 10
**Subsystem:** TSQL  

```sql
BEGIN TRANSACTION       -- Delete some small number of rows at a time       DELETE TOP (10)  internal.operations        WHERE operation_id IN (SELECT operation_id FROM internal.operations WITH (NOLOCK) WHERE start_time < GETDATE())         COMMIT TRANSACTION     CHECKPOINT -- for simple recovery model
```


