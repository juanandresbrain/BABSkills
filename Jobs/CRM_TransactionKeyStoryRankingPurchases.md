# Job: CRM_TransactionKeyStoryRankingPurchases

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM_TransactionKeyStoryRankingPurchases"]
    JOB --> daily_1["Step 1: daily [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** TSQL  

```sql
exec [papamart].[dw].[dbo].[spCRMTransactionSequenceKeyStoryRankingPurchases]     
```


