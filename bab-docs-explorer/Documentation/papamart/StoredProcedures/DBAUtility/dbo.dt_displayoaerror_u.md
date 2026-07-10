# dbo.dt_displayoaerror_u

**Database:** DBAUtility  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dt_displayoaerror_u"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.dt_displayoaerror_u
    @iObject int,
    @iresult int
as

set nocount on

declare @vchOutput      nvarchar(255)
declare @hr             int
declare @vchSource      nvarchar(255)
declare @vchDescription nvarchar(255)

    exec @hr = sp_OAGetErrorInfo @iObject, @vchSource OUT, @vchDescription OUT

    select @vchOutput = @vchSource + ': ' + @vchDescription
    raiserror (@vchOutput,16,-1)

    return
```

