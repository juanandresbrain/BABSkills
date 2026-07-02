# Job: MERCHANDISING - Report - Upcoming Price Changes

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email about price changes

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Upcoming Price Changes"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportUpcomingPriceChanges
MERCHANDISING - Report - Webstore Inventory	No	Reports archived web inventory into CSV file for Accounting and Planning, sends email
Replaces DTS on wmetl01 called webstore_inventory_daily (Merch 4.1 LIVE)	1	one	TSQL	exec me_01.dbo.spMerchandisingReportWebstoreInventory
```


