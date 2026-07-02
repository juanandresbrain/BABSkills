# Job: New DBA - Output File Cleanup

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Source: https://ola.hallengren.com

## Architecture Diagram

```mermaid
flowchart LR
    JOB["New DBA - Output File Cleanup"]
    JOB --> New_DBA___Output_File_Cleanup_1["Step 1: New DBA - Output File Cleanup [CMDEXEC]"]`n```

## Steps

### Step 1: New DBA - Output File Cleanup
**Subsystem:** CMDEXEC  

```sql
cmd /q /c "For /F "tokens=1 delims=" %v In ('ForFiles /P "$(ESCAPE_SQUOTE(SQLLOGDIR))" /m *_*_*_*.txt /d -30 2^>^&1') do if EXIST "$(ESCAPE_SQUOTE(SQLLOGDIR))"\%v echo del "$(ESCAPE_SQUOTE(SQLLOGDIR))"\%v& del "$(ESCAPE_SQUOTE(SQLLOGDIR))"\%v"
```


