# dbo.fnEmailCleanse

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(100)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnEmailCleanse"]
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
CREATE FUNCTION fnEmailCleanse 
	(@email varchar(100))
RETURNS varchar(100)
AS
BEGIN
-- do some cleanup
SET @email = replace(@email, ',', '')
SET @email = replace(@email, '''', '')
SET @email = replace(@email, ' ', '')
SET @email = replace(@email, '#error#', '')
SET @email = replace(@email, '#', '')
SET @email = replace(@email, '!', '')
SET @email = replace(@email, '/', '')
SET @email = replace(@email, '.com.', '.com')
SET @email = replace(@email, '.comm', '.com')
SET @email = replace(@email, '&', '')
RETURN @email
END
```

