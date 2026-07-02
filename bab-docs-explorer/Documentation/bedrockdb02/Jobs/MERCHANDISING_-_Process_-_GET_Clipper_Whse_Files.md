# Job: MERCHANDISING - Process - GET Clipper Whse Files

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Retrieves whse files from UK Clipper SFTP server, placess them into the correct interface directories on Kermode\UK Distro

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - GET Clipper Whse Files"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
-- exec me_01.dbo.spMerchandisingFTPgetUKfiles -- Replaced on 2/9/2017, new proc leverages SFTP
exec me_01.dbo.spMerchandisingFTPgetUKfiles_WinSCP
```


