# Job: WEB - Load Package Style Parties From Web

**Enabled:** Yes  
**Description:** Loads Package Style Parties From Web in the PartyRequest on Kodiak

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - Load Package Style Parties From Web"]
    JOB --> EXEC_Kodiak_PartyRequest_dbo_spLoadPackageStylePartiesFromWeb_1["Step 1: EXEC Kodiak.PartyRequest.dbo.spLoadPackageStylePartiesFromWeb [TSQL]"]`n```

## Steps

### Step 1: EXEC Kodiak.PartyRequest.dbo.spLoadPackageStylePartiesFromWeb
**Subsystem:** TSQL  

```sql
EXEC Kodiak.PartyRequest.dbo.spLoadPackageStylePartiesFromWeb
```


