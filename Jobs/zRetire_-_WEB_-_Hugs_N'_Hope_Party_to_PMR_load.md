# Job: zRetire - WEB - Hugs N' Hope Party to PMR load

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetire - WEB - Hugs N' Hope Party to PMR load"]
    JOB --> run_Kodiak_PartyRequest_dbo_spLoadHugsNHopeFromWeb_1["Step 1: run Kodiak.PartyRequest.dbo.spLoadHugsNHopeFromWeb [TSQL]"]`n```

## Steps

### Step 1: run Kodiak.PartyRequest.dbo.spLoadHugsNHopeFromWeb
**Subsystem:** TSQL  

```sql
EXEC Kodiak.PartyRequest.dbo.spLoadHugsNHopeFromWeb
```


