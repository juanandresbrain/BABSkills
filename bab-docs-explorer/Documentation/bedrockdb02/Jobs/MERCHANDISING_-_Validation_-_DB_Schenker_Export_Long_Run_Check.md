# Job: MERCHANDISING - Validation - DB Schenker Export Long Run Check

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Checks if DB Schenker Export is taking longer than 10 hours and sends alert to EntSysSupport

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Validation - DB Schenker Export Long Run Check"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[DBSchenkerPOExportTimeCheck]
```


