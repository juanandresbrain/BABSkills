# Job: DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES"]
    JOB --> New_DBA___DatabaseIntegrityCheck___SYSTEM_DATABASES_1["Step 1: New DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d DBAUtility -Q "EXECUTE [dbo].[DatabaseIntegrityCheck] @Databases = 'SYSTEM_DATABASES', @LogToTable = 'Y'" -b
```


