# Job: WEB - FTP UK Upload

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - FTP UK Upload"]
    JOB --> FTP_1["Step 1: FTP [TSQL]"]`n```

## Steps

### Step 1: FTP
**Subsystem:** TSQL  

```sql
exec web.spFTPukORDERS
```


