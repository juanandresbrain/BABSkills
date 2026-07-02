# Job: MERCHANDISING - Report - Pool Point Transfer Receipts

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures transfer receipts of condos or bales from pool points to stores, sends email to distro team

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Pool Point Transfer Receipts"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectPoolPointTransferReceipts
```


