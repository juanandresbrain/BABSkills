# dbo.spDecryptFiles

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDecryptFiles"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
------------------------------------------------------------------------------------------------
CREATE proc [dbo].[spDecryptFiles] 

as

set nocount on

EXEC master..xp_CMDShell '"D:\IntegrationStaging\concur\decrypt.bat"'
```

