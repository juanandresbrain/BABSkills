# Job: WEB-PartyBookingDailySummary

**Enabled:** No  
**Server:** bearcluster01  
**Description:** runs daily party summary US only for Heather.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-PartyBookingDailySummary"]
    JOB --> step1_1["Step 1: step1 [TSQL]"]`n```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
exec [spRPT_PartyBookingSummaryDailyUS] 'cherylmc@buildabear.com;annies@buildabear.com;michaelg@buildabear.com;brandis@buildabear.com;aimeez@buildabear.com;elizabethb@buildabear.com;RozJ@buildabear.com;'
```


