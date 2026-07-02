# dbo.Cs_TransmissionStart

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Cs_TransmissionStart"]
    dbo_Cs_ExportReg(["dbo.Cs_ExportReg"]) --> SP
    dbo_Cs_FileStat(["dbo.Cs_FileStat"]) --> SP
    dbo_Ex_OutputStat(["dbo.Ex_OutputStat"]) --> SP
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Cs_ExportReg |
| dbo.Cs_FileStat |
| dbo.Ex_OutputStat |
| dbo.Sr_History |
| dbo.Sv_GetNextID |

## Stored Procedure Code

```sql

```

