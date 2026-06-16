# Job: WMS_Report - PartnerOperatedStore_2079

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - PartnerOperatedStore_2079"]
    JOB --> daily_1["Step 1: daily [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** TSQL  

```sql
exec [WMS].[spEmailUKpartnerOperatedTransferOrder] '2079'
```


