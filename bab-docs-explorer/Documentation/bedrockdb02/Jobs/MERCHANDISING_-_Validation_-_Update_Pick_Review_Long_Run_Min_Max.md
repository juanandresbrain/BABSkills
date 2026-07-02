# Job: MERCHANDISING - Validation - Update Pick Review/Long Run Min Max

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** If Min Max Job Runs Long and Does not complete by 11:59 am on Sunday Night, This will Update Pick Review Job to Run the next day Once Min Max Completes and will Trigger Pick review job to run.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Validation - Update Pick Review/Long Run Min Max"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[spMerchandisingUpdatePickReviewParameters]
```


