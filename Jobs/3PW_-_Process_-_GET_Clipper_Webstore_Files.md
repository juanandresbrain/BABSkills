# Job: 3PW - Process - GET Clipper Webstore Files

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["3PW - Process - GET Clipper Webstore Files"]
    JOB --> spMerchandisingFTPgetUKfiles_Web_WinSCP_1["Step 1: spMerchandisingFTPgetUKfiles_Web_WinSCP [TSQL]"]`n```

## Steps

### Step 1: spMerchandisingFTPgetUKfiles_Web_WinSCP
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFTPgetUKfiles_Web_WinSCP]    
```


