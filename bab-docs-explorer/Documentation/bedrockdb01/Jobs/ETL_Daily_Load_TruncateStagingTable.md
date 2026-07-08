# Job: ETL_Daily_Load_TruncateStagingTable

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Clear out the staging table for the daily load from auditworks to papamart.dw so that we know when the load fails. The problem is that we shell out from Informatica to run a stored proc to load up Ld_POS_Daily_Load. If an error occurs, it can not stop the ETL load from progressing. So, the only way we know we died is to clear out this table separately from the load and the checking after the load to see if we really loaded anything. This problem could be coming from a log backup that was running at the  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ETL_Daily_Load_TruncateStagingTable"]
    JOB --> S1["Step 1: step1 [TSQL]"]
```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
truncate table Ld_POS_Daily_Load
```

