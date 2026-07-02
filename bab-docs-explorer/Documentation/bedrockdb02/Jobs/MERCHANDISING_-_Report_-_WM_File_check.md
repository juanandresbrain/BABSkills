# Job: MERCHANDISING - Report - WM File check

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Sends email if WM / TPM xml files are stuck in error directories

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - WM File check"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailWMTPMDirectoryErrors
```


