# dbo.CommandExecute

**Database:** master  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CommandExecute"]
    dbo_CommandLog(["dbo.CommandLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CommandLog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CommandExecute]
```

