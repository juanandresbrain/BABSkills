# dbo.fnTimeOnly

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** datetime(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnTimeOnly"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @DATE | datetime | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[fnTimeOnly] (@DATE datetime)
RETURNS datetime
AS
Begin
DECLARE @TimeOnly datetime
     SET @TimeOnly = CONVERT(VARCHAR(8),@Date,108) -- Returns Hours, Minutes, Seconds
Return @TimeOnly
End
```

