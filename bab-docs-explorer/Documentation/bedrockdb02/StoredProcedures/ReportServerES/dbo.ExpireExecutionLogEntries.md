# dbo.ExpireExecutionLogEntries

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ExpireExecutionLogEntries"]
    dbo_ConfigurationInfo(["dbo.ConfigurationInfo"]) --> SP
    dbo_ExecutionLogStorage(["dbo.ExecutionLogStorage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ConfigurationInfo |
| dbo.ExecutionLogStorage |

## Stored Procedure Code

```sql

```

