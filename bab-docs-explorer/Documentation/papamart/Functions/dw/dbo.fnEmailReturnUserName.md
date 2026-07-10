# dbo.fnEmailReturnUserName

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(100)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnEmailReturnUserName"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @email | varchar | 100 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fnEmailReturnUserName 
	(@email varchar(100) )
RETURNS varchar(100)
AS
BEGIN
IF PATINDEX('%@%',@email)= 0 RETURN NULL
RETURN substring(@email,1, PATINDEX('%@%',@email)-1)
END
```

