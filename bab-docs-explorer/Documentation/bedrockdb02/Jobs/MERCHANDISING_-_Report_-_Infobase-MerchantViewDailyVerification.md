# Job: MERCHANDISING - Report - Infobase-MerchantViewDailyVerification

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Daily polling validation, comparing various inventory states between ME and MA.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Infobase-MerchantViewDailyVerification"]
    JOB --> Infobase_MerchantView_Daily_Verification_Results_1["Step 1: Infobase-MerchantView Daily Verification Results [TSQL]"]`n```

## Steps

### Step 1: Infobase-MerchantView Daily Verification Results
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification

```


