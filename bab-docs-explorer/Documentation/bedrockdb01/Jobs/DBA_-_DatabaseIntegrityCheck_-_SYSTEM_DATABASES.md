# Job: DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Source: https://ola.hallengren.com  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES"]
    JOB --> S1["Step 1: DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES [CMDEXEC]"]
```

## Steps

### Step 1: DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES
**Subsystem:** CMDEXEC  

```sql
sqlcmd -E -S $(ESCAPE_SQUOTE(SRVR)) -d master -Q "EXECUTE [dbo].[DatabaseIntegrityCheck] @Databases = 'SYSTEM_DATABASES', @LogToTable = 'Y'" -b
```

