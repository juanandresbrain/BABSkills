# Job: 3PW - Process - GET Clipper Whse Files

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["3PW - Process - GET Clipper Whse Files"]
    JOB --> spMerchandisingFTPgetUKfiles_WinSCP_1["Step 1: spMerchandisingFTPgetUKfiles_WinSCP [TSQL]"]`n```

## Steps

### Step 1: spMerchandisingFTPgetUKfiles_WinSCP
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingFTPgetUKfiles_WinSCP]    
```


