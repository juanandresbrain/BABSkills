# Job: New DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES"]
    JOB --> New_DBA___DatabaseIntegrityCheck___SYSTEM_DATABASES_1["Step 1: New DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES [TSQL]"]`n```

## Steps

### Step 1: New DBA - DatabaseIntegrityCheck - SYSTEM_DATABASES
**Subsystem:** TSQL  

```sql
IF sys.fn_hadr_backup_is_preferred_replica('DBAUtility') = 1
BEGIN
     EXECUTE [dbo].[DatabaseIntegrityCheck] @Databases = 'SYSTEM_DATABASES', @LogToTable = 'Y'
END
```


