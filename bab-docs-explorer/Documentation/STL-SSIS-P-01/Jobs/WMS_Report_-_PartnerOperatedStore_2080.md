# Job: WMS_Report - PartnerOperatedStore_2080

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - PartnerOperatedStore_2080"]
    JOB --> daily_1["Step 1: daily [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** TSQL  

```sql
exec [WMS].[spEmailUKpartnerOperatedTransferOrder] '2080'
```


