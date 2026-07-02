# Job: zRetire - MERCHANDISING - Process - Merch to CN - Vendor Master Upload

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetire - MERCHANDISING - Process - Merch to CN - Vendor Master Upload"]
    JOB --> Generate_Vendor_Master_File_1["Step 1: Generate Vendor Master File [TSQL]"]`n    JOB --> SFTP_2["Step 2: SFTP [TSQL]"]`n```

## Steps

### Step 1: Generate Vendor Master File
**Subsystem:** TSQL  

```sql
exec spMerchandisingOutputVendorMasterCN
```

### Step 2: SFTP
**Subsystem:** TSQL  

```sql
exec spMerchandisingFtpCNVendorMaster
```


