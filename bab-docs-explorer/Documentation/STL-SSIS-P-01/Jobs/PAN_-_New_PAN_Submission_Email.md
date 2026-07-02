# Job: PAN - New PAN Submission Email

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PAN - New PAN Submission Email"]
    JOB --> Exec_spNewPANSubmissionEmail_1["Step 1: Exec spNewPANSubmissionEmail [TSQL]"]`n```

## Steps

### Step 1: Exec spNewPANSubmissionEmail
**Subsystem:** TSQL  

```sql
EXEC KODIAK.PersonnelActionNotification.dbo.spNewPANSubmissionEmail
```


