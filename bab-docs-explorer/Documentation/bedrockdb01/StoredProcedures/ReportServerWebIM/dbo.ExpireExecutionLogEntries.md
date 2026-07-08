# dbo.ExpireExecutionLogEntries

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ExpireExecutionLogEntries"]
    ConfigurationInfo(["ConfigurationInfo"]) --> SP
    ExecutionLogStorage(["ExecutionLogStorage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ConfigurationInfo |
| ExecutionLogStorage |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ExpireExecutionLogEntries]
AS
SET NOCOUNT OFF
-- -1 means no expiration
if exists (select * from ConfigurationInfo where [Name] = 'ExecutionLogDaysKept' and CAST(CAST(Value as nvarchar) as integer) = -1)
begin
return
end

delete from ExecutionLogStorage
where DateDiff(day, TimeStart, getdate()) >= (select CAST(CAST(Value as nvarchar) as integer) from ConfigurationInfo where [Name] = 'ExecutionLogDaysKept')
```

