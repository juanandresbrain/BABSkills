# Job: zRetired_WMS_CostcoEmailTrackingUpdateGiftcardDB

**Enabled:** No  
**Description:** Sends email to Costco with tracking numbers, updates GiftCard database to set shipped status

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WMS_CostcoEmailTrackingUpdateGiftcardDB"]
    JOB --> EmailCostcoTrackingUpdateGiftcardDB_1["Step 1: EmailCostcoTrackingUpdateGiftcardDB [TSQL]"]`n```

## Steps

### Step 1: EmailCostcoTrackingUpdateGiftcardDB
**Subsystem:** TSQL  

```sql
exec wms.spEmailCostcoTrackingUpdateGiftcardDB
```


