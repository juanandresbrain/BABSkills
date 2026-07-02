# Job: Execute the Automated Sales Reports

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Step one will trigger the job to fail if the data is not ready, else will go to step 2  refresh the reports.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Execute the Automated Sales Reports"]
    JOB --> Execute_the_Pre_Flight_Check_1["Step 1: Execute the Pre-Flight Check [SSIS]"]`n    JOB --> Process_Start_Notification_2["Step 2: Process Start Notification [TSQL]"]`n    JOB --> Execute_the_powershell_script_3["Step 3: Execute the powershell script [CmdExec]"]`n    JOB --> Job_Completion_Notice_4["Step 4: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: Execute the Pre-Flight Check
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\FinanceReportsPreFlightCheck\FinanceReportsPreFlightCheck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Process Start Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobStart   @ProcessName = 'Automated Sales Reports - Finance',   @SQLAgent = 'Execute the Automated Sales Reports',  @Recipients = 'FinancialAnalyst@buildabear.com;biadmin@buildabear.com'
```

### Step 3: Execute the powershell script
**Subsystem:** CmdExec  

```sql
powershell.exe -noninteractive -nologo -file "\\sharebear1\groups\Accounting\Daily Sales Worksheets\Automation\Execute-AutomatedSalesReports.ps1"
```

### Step 4: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Automated Finance Reports',   @SQLAgent = 'Execute the Automated Sales Reports',  @Recipients = 'biadmin@buildabear.com;financialanalyst@buildabear.com'
```


