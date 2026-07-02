# Job: MERCHANDISING - Process - WM to Merch Post Wave Alloc Adj

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Captures post wave allocation adjustment data from WM.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - WM to Merch Post Wave Alloc Adj"]
    JOB --> 1___Export_Post_Wave_Pipeline_File_1["Step 1: 1 - Export Post Wave Pipeline File [TSQL]"]`n```

## Steps

### Step 1: 1 - Export Post Wave Pipeline File
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectWMPostWaveAllocAdj

```


