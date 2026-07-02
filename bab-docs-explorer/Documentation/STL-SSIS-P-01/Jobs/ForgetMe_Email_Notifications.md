# Job: ForgetMe Email Notifications

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ForgetMe Email Notifications"]
    JOB --> New_ForgetMe_Requests_1["Step 1: New ForgetMe Requests [TSQL]"]`n    JOB --> ForgetMe_Requests_Approaching_Deadline_2["Step 2: ForgetMe Requests Approaching Deadline [TSQL]"]`n```

## Steps

### Step 1: New ForgetMe Requests
**Subsystem:** TSQL  

```sql
EXEC [bearcluster01.sql.buildabear.com].[BABWForgetMe].[dbo].[spForgetMeNewRequestEmail] 
```

### Step 2: ForgetMe Requests Approaching Deadline
**Subsystem:** TSQL  

```sql
EXEC [bearcluster01.sql.buildabear.com].[BABWForgetMe].[dbo].[spForgetMeRequestEmail] 
```


