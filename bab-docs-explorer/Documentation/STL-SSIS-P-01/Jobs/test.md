# Job: test

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["test"]
    JOB --> test_1["Step 1: test [CmdExec]"]`n```

## Steps

### Step 1: test
**Subsystem:** CmdExec  

```sql
powershell.exe -noninteractive -nologo -file "\\sharebear1\groups\Accounting\Daily Sales Worksheets\Automation\Execute-AutomatedSalesReports.ps1"
```


