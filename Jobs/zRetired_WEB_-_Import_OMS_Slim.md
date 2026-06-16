# Job: zRetired_WEB - Import OMS Slim

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - Import OMS Slim"]
    JOB --> EXEC_WOP_exe_1["Step 1: EXEC WOP.exe [TSQL]"]`n```

## Steps

### Step 1: EXEC WOP.exe
**Subsystem:** TSQL  

```sql
DECLARE @cmd VARCHAR(255), @returnStatus BIT    SET @CMD = '"\\STL-SSIS-P-01\ETL Executables\WebOrderProcessing\WOP.exe" \\kermode\FileRepository\omsOrders\babw-us\ \\kermode\FileRepository\omsOrders\babw-us\Success'    EXEC @returnStatus = master.dbo.xp_cmdshell @CMD
```


