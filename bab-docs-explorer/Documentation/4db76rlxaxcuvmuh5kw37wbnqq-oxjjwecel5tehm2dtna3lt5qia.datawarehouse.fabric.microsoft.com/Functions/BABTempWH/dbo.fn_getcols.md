# dbo.fn_getcols

**Database:** BABTempWH  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_getcols"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

_No parameters._

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fn_getcols()
RETURNS TABLE
AS 
RETURN 
select cast(COLUMN_NAME as varchar(100)) as COLUMN_NAME 
from INFORMATION_SCHEMA.COLUMNS
```

