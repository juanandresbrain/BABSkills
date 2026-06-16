# Job: zRetired_WEB - Custom Export Import Debug

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - Custom Export Import Debug"]
    JOB --> Run_Package_1["Step 1: Run Package [TSQL]"]`n```

## Steps

### Step 1: Run Package
**Subsystem:** TSQL  

```sql
DECLARE @execution_id AS BIGINT    SELECT  TOP 1 @execution_id =  [execution_id]  FROM [SSISDB].[internal].[execution_parameter_values]  WHERE parAmeter_name = 'LOGGING_LEVEL'  ORDER BY 1 DESC    EXEC ssisdb.catalog.start_execution @execution_id  
```


