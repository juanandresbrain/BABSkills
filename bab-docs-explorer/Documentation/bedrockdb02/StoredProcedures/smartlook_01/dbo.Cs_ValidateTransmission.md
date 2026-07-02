# dbo.Cs_ValidateTransmission

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Cs_ValidateTransmission"]
    dbo_Cs_FileStat(["dbo.Cs_FileStat"]) --> SP
    dbo_Cs_ReTransmission(["dbo.Cs_ReTransmission"]) --> SP
    dbo_Cs_ValidateTransmission(["dbo.Cs_ValidateTransmission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Cs_FileStat |
| dbo.Cs_ReTransmission |
| dbo.Cs_ValidateTransmission |

## Stored Procedure Code

```sql

```

