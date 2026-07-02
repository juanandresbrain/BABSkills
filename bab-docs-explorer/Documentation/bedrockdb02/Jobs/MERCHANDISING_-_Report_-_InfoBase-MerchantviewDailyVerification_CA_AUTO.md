# Job: MERCHANDISING - Report - InfoBase-MerchantviewDailyVerification_CA_AUTO

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Kicks off IB to MA validations

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - InfoBase-MerchantviewDailyVerification_CA_AUTO"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
Exec [me_01].[dbo].[spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2]
```


