# Job: Annual Update Alert

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Run stored procedure to check if the following Sunday is the beigining of the fourth fiscal quarter.  If so, send an email to ES Support as a reminder of the annual tasks that need to be performed.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Annual Update Alert"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
EXEC me_01.dbo.spAnnualReminder_FiscalQuarterCheck
```


