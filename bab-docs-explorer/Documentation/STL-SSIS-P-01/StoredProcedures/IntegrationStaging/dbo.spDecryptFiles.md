# dbo.spDecryptFiles

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDecryptFiles"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
------------------------------------------------------------------------------------------------
CREATE proc [dbo].[spDecryptFiles] 

as

set nocount on

EXEC master..xp_CMDShell '"D:\IntegrationStaging\concur\decrypt.bat"'
```

