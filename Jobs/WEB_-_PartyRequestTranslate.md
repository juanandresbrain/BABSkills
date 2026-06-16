# Job: WEB - PartyRequestTranslate

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - PartyRequestTranslate"]
    JOB --> Execute_1["Step 1: Execute [CmdExec]"]`n    JOB --> EXEC__BEARCLUSTER01_SQL_BUILDABEAR_COM__BABWPartyPlanner_dbo_spLoadOrderIdForPartyESOrder_2["Step 2: EXEC [BEARCLUSTER01.SQL.BUILDABEAR.COM].BABWPartyPlanner.dbo.spLoadOrderIdForPartyESOrder [TSQL]"]`n```

## Steps

### Step 1: Execute
**Subsystem:** CmdExec  

```sql
\\stl-ssis-p-01\ETL Executables\PartyRequestTranslate\PartyRequestTranslate.exe "\\kermode/FileRepository/PartyRequestWebShip/"
```

### Step 2: EXEC [BEARCLUSTER01.SQL.BUILDABEAR.COM].BABWPartyPlanner.dbo.spLoadOrderIdForPartyESOrder
**Subsystem:** TSQL  

```sql
EXEC [BEARCLUSTER01.SQL.BUILDABEAR.COM].BABWPartyPlanner.dbo.spLoadOrderIdForPartyESOrder
```


