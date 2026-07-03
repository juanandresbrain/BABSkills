# internal.get_principal_id_by_sid

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  
**Function Type:** Scalar Function  
**Returns:** int(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["internal.get_principal_id_by_sid"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @sid | adt_sid | 85 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql

CREATE FUNCTION [internal].[get_principal_id_by_sid]
(
        @sid        [internal].[adt_sid] 
)
RETURNS INT
AS
BEGIN
	DECLARE @Result INT
	select @Result = [principal_id] from [sys].[database_principals] where [sid]=@sid;
	RETURN @Result
END
```
