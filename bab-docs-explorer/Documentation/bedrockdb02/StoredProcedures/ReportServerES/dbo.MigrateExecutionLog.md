# dbo.MigrateExecutionLog

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.MigrateExecutionLog"]
    dbo_ExecutionLog_Old(["dbo.ExecutionLog_Old"]) --> SP
    dbo_ExecutionLogStorage(["dbo.ExecutionLogStorage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ExecutionLog_Old |
| dbo.ExecutionLogStorage |

## Stored Procedure Code

```sql

```

