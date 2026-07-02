# Job: MERCHANDISING - Report - WM FedEx Tracking

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Sends email to Distro team with FedEx tracking information

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - WM FedEx Tracking"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spWMEmailFedExTracking
```


