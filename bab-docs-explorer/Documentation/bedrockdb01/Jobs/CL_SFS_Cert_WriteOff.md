# Job: CL_SFS_Cert_WriteOff

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Creates SFS certificate write-off file and moves files for processing 1/18/2018 - [Paul B] - Disabled job due to no more SFS Certificates available for write-off since 9/15/2017. This is due to the change from SFS Certs to Serialized Coupons for Bonus Club members which started in early 2017  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CL_SFS_Cert_WriteOff"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spCL_WriteOffSFScerts
```

