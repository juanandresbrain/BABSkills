# Job: HangingSQLConnectionCheck_MasterController

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Presently being called from Storeforce job ----    Specifically designed to try to connect to all stores, then figure out which stores are 'hanging' so we can not try to connect to those stores. Final list (maybe none, or one or a few) is on IntegrationStaging..HangingSQLConnectionCheck_StoresNotConnected     The best case run history would be to run Step 1 and 'fail' (it raises error if it doesn't need to kill the running job, either way will proceed to next step), then steps 2 and 3, then 'fail' step 4 (d

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HangingSQLConnectionCheck_MasterController"]
    JOB --> Kill_Job_if_Needed___0_1["Step 1: Kill Job if Needed - 0 [TSQL]"]`n    JOB --> Start_Job___HangingSQLConnectionCheck_PhaseOne___1_2["Step 2: Start Job - HangingSQLConnectionCheck_PhaseOne - 1 [TSQL]"]`n    JOB --> Wait___1_3["Step 3: Wait - 1 [TSQL]"]`n    JOB --> Kill_Job_if_Needed___1_4["Step 4: Kill Job if Needed - 1 [TSQL]"]`n    JOB --> Start_Job___HangingSQLConnectionCheck_PhaseTwo___2_5["Step 5: Start Job - HangingSQLConnectionCheck_PhaseTwo - 2 [TSQL]"]`n    JOB --> Wait___2_6["Step 6: Wait - 2 [TSQL]"]`n    JOB --> Kill_Job_if_Needed___2_7["Step 7: Kill Job if Needed - 2 [TSQL]"]`n    JOB --> Start_Job___HangingSQLConnectionCheck_PhaseTwo___3_8["Step 8: Start Job - HangingSQLConnectionCheck_PhaseTwo - 3 [TSQL]"]`n    JOB --> Wait___3_9["Step 9: Wait - 3 [TSQL]"]`n    JOB --> Kill_Job_if_Needed___3_10["Step 10: Kill Job if Needed - 3 [TSQL]"]`n    JOB --> Start_Job___HangingSQLConnectionCheck_PhaseTwo___4_11["Step 11: Start Job - HangingSQLConnectionCheck_PhaseTwo - 4 [TSQL]"]`n    JOB --> Wat___4_12["Step 12: Wat - 4 [TSQL]"]`n    JOB --> Kill_Job_If_Needed___4_13["Step 13: Kill Job If Needed - 4 [TSQL]"]`n    JOB --> Start_Job___HangingSQLConnectionCheck_PhaseTwo___5_14["Step 14: Start Job - HangingSQLConnectionCheck_PhaseTwo - 5 [TSQL]"]`n    JOB --> Wait___5_15["Step 15: Wait - 5 [TSQL]"]`n    JOB --> Kill_Job_If_Needed___5_16["Step 16: Kill Job If Needed - 5 [TSQL]"]`n    JOB --> End_Job_17["Step 17: End Job [TSQL]"]`n```

## Steps

### Step 1: Kill Job if Needed - 0
**Subsystem:** TSQL  

```sql
TRUNCATE TABLE HangingSQLConnectionCheck_StoresNotConnected  exec spHangingSQLConnectionCheck_KillJob 'HangingSQLConnectionCheck_PhaseOne'  --proc is designed to 'fail' if there is no need to end the job, so the step will then go to the last step  exec spHangingSQLConnectionCheck_KillJob 'HangingSQLConnectionCheck_PhaseTwo'   
```

### Step 2: Start Job - HangingSQLConnectionCheck_PhaseOne - 1
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='HangingSQLConnectionCheck_PhaseOne'
```

### Step 3: Wait - 1
**Subsystem:** TSQL  

```sql
waitfor delay '00:01:10'
```

### Step 4: Kill Job if Needed - 1
**Subsystem:** TSQL  

```sql
exec spHangingSQLConnectionCheck_KillJob 'HangingSQLConnectionCheck_PhaseOne'  --proc is designed to 'fail' if there is no need to end the job, so the step will then go to the last step
```

### Step 5: Start Job - HangingSQLConnectionCheck_PhaseTwo - 2
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='HangingSQLConnectionCheck_PhaseTwo'
```

### Step 6: Wait - 2
**Subsystem:** TSQL  

```sql
waitfor delay '00:01:10'
```

### Step 7: Kill Job if Needed - 2
**Subsystem:** TSQL  

```sql
exec spHangingSQLConnectionCheck_KillJob 'HangingSQLConnectionCheck_PhaseTwo'  --proc is designed to 'fail' if there is no need to end the job, so the step will then go to the last step
```

### Step 8: Start Job - HangingSQLConnectionCheck_PhaseTwo - 3
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='HangingSQLConnectionCheck_PhaseTwo'
```

### Step 9: Wait - 3
**Subsystem:** TSQL  

```sql
waitfor delay '00:01:10'
```

### Step 10: Kill Job if Needed - 3
**Subsystem:** TSQL  

```sql
exec spHangingSQLConnectionCheck_KillJob 'HangingSQLConnectionCheck_PhaseTwo'  --proc is designed to 'fail' if there is no need to end the job, so the step will then go to the last step
```

### Step 11: Start Job - HangingSQLConnectionCheck_PhaseTwo - 4
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='HangingSQLConnectionCheck_PhaseTwo'
```

### Step 12: Wat - 4
**Subsystem:** TSQL  

```sql
waitfor delay '00:01:10'
```

### Step 13: Kill Job If Needed - 4
**Subsystem:** TSQL  

```sql
exec spHangingSQLConnectionCheck_KillJob 'HangingSQLConnectionCheck_PhaseTwo'  --proc is designed to 'fail' if there is no need to end the job, so the step will then go to the last step
```

### Step 14: Start Job - HangingSQLConnectionCheck_PhaseTwo - 5
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='HangingSQLConnectionCheck_PhaseTwo'
```

### Step 15: Wait - 5
**Subsystem:** TSQL  

```sql
waitfor delay '00:01:10'
```

### Step 16: Kill Job If Needed - 5
**Subsystem:** TSQL  

```sql
exec spHangingSQLConnectionCheck_KillJob 'HangingSQLConnectionCheck_PhaseTwo'  --proc is designed to 'fail' if there is no need to end the job, so the step will then go to the last step
```

### Step 17: End Job
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'HangingSQLConnectionCheck_MasterController',   @SQLAgent = 'HangingSQLConnectionCheck_MasterController',  @Recipients = 'biadmin@buildabear.com'
```


