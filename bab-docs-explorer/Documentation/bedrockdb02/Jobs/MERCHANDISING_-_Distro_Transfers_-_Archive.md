# Job: MERCHANDISING - Distro Transfers - Archive

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Distro Transfers - Archive"]
    JOB --> step1_1["Step 1: step1 [TSQL]"]`n```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spDistroTransfers_Archive
```


