# Job: DBA - IndexOptimize - USER_DATABASES

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Source: https://ola.hallengren.com  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - IndexOptimize - USER_DATABASES"]
    JOB --> S1["Step 1: DBA - IndexOptimize - USER_DATABASES [CMDEXEC]"]
```

## Steps

### Step 1: DBA - IndexOptimize - USER_DATABASES
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [dbo].[IndexOptimize] @Databases = 'USER_DATABASES', @LogToTable = 'Y'" -b
```

