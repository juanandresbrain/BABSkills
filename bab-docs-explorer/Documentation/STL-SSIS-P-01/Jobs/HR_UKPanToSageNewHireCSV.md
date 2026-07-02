# Job: HR_UKPanToSageNewHireCSV

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_UKPanToSageNewHireCSV"]
    JOB --> nightly_run_1["Step 1: nightly run [SSIS]"]`n```

## Steps

### Step 1: nightly run
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UKPanToSageNewHireCSV\HR_UKPanToSageNewHireCSV.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par FtpServerExePath;"\"C$\Program Files (x86)\WinSCP\WinSCP.exe\"" /Par FtpServerName;"\"stl-ssis-t-01\"" /Par FtpWinScpLog;"\"/log=\"\"\\stl-ssis-P-01\C$\Program Files (x86)\WinSCP\Logs\HR_UKPanToSageNewHireLoadFile.log.txt\"\"\"" /Par FtpWinScpScript;"\"/script=\"\"\\stl-ssis-p-01\IntegrationStaging\HR\UKPanToSage\WinSCP\winscp_script.txt\"\"\"" /Par "\"IntegrationStaging_ServerName\"";"\"stl-ssis-p-01\"" /Par "\"PersonnelActionNotification_ServerName\"";kodiak /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"dw_ServerName\"";papamart /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


