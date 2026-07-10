# Job: zRetired_LoadDateDim

**Enabled:** No  
**Server:** papamart  
**Description:** Load DW date_dim with new data based on Max date in bedrockdb02.me_01.dbo.calendar_date  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_LoadDateDim"]
    JOB --> S1["Step 1: LoadDateDim [TSQL]"]
```

## Steps

### Step 1: LoadDateDim
**Subsystem:** TSQL  

```sql
EXEC [spDW_LoadDateDim]
```

