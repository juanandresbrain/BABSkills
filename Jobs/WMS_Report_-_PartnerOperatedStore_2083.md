# Job: WMS_Report - PartnerOperatedStore_2083

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - PartnerOperatedStore_2083"]
    JOB --> daily_1["Step 1: daily [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** TSQL  

```sql
exec [WMS].[spEmailUKpartnerOperatedTransferOrder] '2083'
```


