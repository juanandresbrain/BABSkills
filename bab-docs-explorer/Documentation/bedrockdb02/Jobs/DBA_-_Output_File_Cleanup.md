# Job: DBA - Output File Cleanup

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - Output File Cleanup"]
    JOB --> New_DBA___Output_File_Cleanup_1["Step 1: New DBA - Output File Cleanup [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - Output File Cleanup
**Subsystem:** CMDEXEC  

```sql
cmd /q /c "For /F "tokens=1 delims=" %v In ('ForFiles /P "D:\MSSQL11.MSSQLSERVER\MSSQL\LOG" /m *_*_*_*.txt /d -30 2^>^&1') do if EXIST "D:\MSSQL11.MSSQLSERVER\MSSQL\LOG"\%v echo del "D:\MSSQL11.MSSQLSERVER\MSSQL\LOG"\%v& del "D:\MSSQL11.MSSQLSERVER\MSSQL\LOG"\%v"
DBA - Repository Transfers	Yes	Job to transfer all DBAUtility log tables to Central Repository tables
SET @Revision = '06/28/2012'
	1	spDBA_Transfer_DDLChangesRepository	TSQL	EXEC dbo.spDBA_Transfer_DDLChangesRepository
DBA - Repository Transfers	Yes	Job to transfer all DBAUtility log tables to Central Repository tables
SET @Revision = '06/28/2012'
	2	spDBA_Transfer_ObjectVersionRepository	TSQL	EXEC dbo.spDBA_ObjectVersionLog 
EXEC dbo.spDBA_Transfer_ObjectVersionRepository
```


