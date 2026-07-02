# Job: MERCHANDISING - Report - Royalty Attributes

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends emails with styles with updates made to royalty attribute

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Royalty Attributes"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportRoyaltyUpdates
```


