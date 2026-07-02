# Job: GiftCard Process Hourly_Recurring

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["GiftCard Process Hourly_Recurring"]
    JOB --> step_1_1["Step 1: step 1 [SSIS]"]`n    JOB --> verify___process_2["Step 2: verify & process [SSIS]"]`n    JOB --> Write_STS_Files__Epicor__3["Step 3: Write STS Files (Epicor) [TSQL]"]`n```

## Steps

### Step 1: step 1
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\GiftCard_firstData_download\Package.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: verify & process
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\GiftCard_Process\GiftCard_Process.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"GC_archive\"";"\"\\stl-sql-p-04\d$\BABWSCORE01_D\GCArchive\\"" /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Write STS Files (Epicor)
**Subsystem:** TSQL  

```sql
EXEC PAPAMART.dw.dbo.spGiftCard_GenerateSalesAuditFiles
```


