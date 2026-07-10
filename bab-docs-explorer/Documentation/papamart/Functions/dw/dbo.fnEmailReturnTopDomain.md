# dbo.fnEmailReturnTopDomain

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(100)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnEmailReturnTopDomain"]
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
CREATE FUNCTION fnEmailReturnTopDomain 
	(@email varchar(100) )
RETURNS varchar(100)
AS
BEGIN
IF PATINDEX('%.%',@email)=0 RETURN NULL
RETURN reverse(substring(reverse(@email),1,PATINDEX('%.%',reverse(@email))-1))
END
```

