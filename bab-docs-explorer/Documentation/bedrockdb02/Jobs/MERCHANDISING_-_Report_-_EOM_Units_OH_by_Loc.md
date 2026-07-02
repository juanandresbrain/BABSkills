# Job: MERCHANDISING - Report - EOM Units OH by Loc

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - EOM Units OH by Loc"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportEOMUnitsOHbyLoc
MERCHANDISING - Report - ERD Summaries	No	Sends email summary of information that has been reported to the stores and BL's over the past 7 days for store shipments not received within 2 or 3 days past ERD			1	uno	TSQL	exec me_01.dbo.spMerchandisingEmailERDSummaries
```


