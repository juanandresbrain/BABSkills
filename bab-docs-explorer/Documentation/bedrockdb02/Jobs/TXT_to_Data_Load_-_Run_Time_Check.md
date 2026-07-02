# Job: TXT to Data Load - Run Time Check

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** This job was created to monitor if the TXT to Data Load job is running past a specified time.  If it runs past the specified time, the TXT Admin will be alerted via email.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["TXT to Data Load - Run Time Check"]
    JOB --> spTXTDataLoad_RunTimeCheck_1["Step 1: spTXTDataLoad_RunTimeCheck [TSQL]"]`n```

## Steps

### Step 1: spTXTDataLoad_RunTimeCheck
**Subsystem:** TSQL  

```sql
EXEC [MerchandisingPlanning].[spTXTDataLoad_RunTimeCheck]
```


