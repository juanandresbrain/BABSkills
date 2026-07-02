# Job: MERCHANDISING - Process - Transfer Import Validation

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends summary email to Distro team to report on Transfers imported into Merch, sends txt alert if transfers aren't in Merch

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Transfer Import Validation"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingTransferImportValidation
```


