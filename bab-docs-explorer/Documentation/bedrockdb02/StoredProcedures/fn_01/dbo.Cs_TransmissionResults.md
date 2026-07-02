# dbo.Cs_TransmissionResults

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Cs_TransmissionResults"]
    dbo_Cs_ExportReg(["dbo.Cs_ExportReg"]) --> SP
    dbo_Cs_FileStat(["dbo.Cs_FileStat"]) --> SP
    dbo_Cs_Service(["dbo.Cs_Service"]) --> SP
    dbo_Sr_Parameter(["dbo.Sr_Parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Cs_ExportReg |
| dbo.Cs_FileStat |
| dbo.Cs_Service |
| dbo.Sr_Parameter |

## Stored Procedure Code

```sql

```

