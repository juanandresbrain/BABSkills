# Job: MERCHANDISING - Report - InfoBase-MerchantviewDailyVerification_CA

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - InfoBase-MerchantviewDailyVerification_CA"]
    JOB --> MerchandisingReportInfobaseVsMerchantViewDailyVerification_ORIGINAL_1["Step 1: MerchandisingReportInfobaseVsMerchantViewDailyVerification_ORIGINAL [TSQL]"]`n```

## Steps

### Step 1: MerchandisingReportInfobaseVsMerchantViewDailyVerification_ORIGINAL
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2]
```


