# Job: zRetired_WEB - onDemandWebPriceBookExport

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - onDemandWebPriceBookExport"]
    JOB --> Execute_Stored_Proc_1["Step 1: Execute Stored Proc [TSQL]"]`n```

## Steps

### Step 1: Execute Stored Proc
**Subsystem:** TSQL  

```sql
DECLARE @execution_id AS BIGINT    SELECT  TOP 1 @execution_id =  [execution_id]  FROM [SSISDB].[internal].[execution_parameter_values]  WHERE parAmeter_name = 'PricebookRunDate'  ORDER BY 1 DESC    EXEC ssisdb.catalog.start_execution @execution_id  
```


