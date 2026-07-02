# Job: zRetire - MERCHANDISING - Process - Merch to CN - Store Master Upload

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetire - MERCHANDISING - Process - Merch to CN - Store Master Upload"]
    JOB --> Generate_File_1["Step 1: Generate File [TSQL]"]`n    JOB --> SFTP_2["Step 2: SFTP [TSQL]"]`n```

## Steps

### Step 1: Generate File
**Subsystem:** TSQL  

```sql
exec spMerchandisingOutputStoreMasterCN
```

### Step 2: SFTP
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCNStoreMaster
```


