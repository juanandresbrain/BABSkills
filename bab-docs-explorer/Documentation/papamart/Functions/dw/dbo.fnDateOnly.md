# dbo.fnDateOnly

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** datetime(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDateOnly"]
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
CREATE FUNCTION dbo.fnDateOnly (@DATE datetime)
RETURNS datetime
AS
Begin
DECLARE @DateOnly datetime
     SET @DateOnly = DATEADD(day,DATEDIFF(day,0,@Date),0)
Return @DateOnly
End
```

