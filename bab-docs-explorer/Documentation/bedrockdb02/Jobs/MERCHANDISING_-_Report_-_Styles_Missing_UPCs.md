# Job: MERCHANDISING - Report - Styles Missing UPCs

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** sends email for styles which don't have a upc

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Styles Missing UPCs"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailMissingUPCs
MERCHANDISING - Report - Styles With Multiple Colors	Yes	Sends summary email to notify us of styles with multiple colors flagged as reorderable.
This can cause duplicates when exporting distros.	1	uno	TSQL	exec me_01.dbo.spMerchandisingSelectStylesWithMultipleColors
```


