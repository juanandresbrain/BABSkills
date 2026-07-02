# Job: Min/Max History

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Calls [dbo].[spMerchandisingMinMaxHistory] to track min/max duration and profile count history

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Min/Max History"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
EXEC [dbo].[spMerchandisingMinMaxHistory]
```


