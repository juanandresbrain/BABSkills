# dbo.fnTrimAndReplaceNulls

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(8000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnTrimAndReplaceNulls"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Field | varchar | 8000 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION dbo.fnTrimAndReplaceNulls (@Field varchar(8000))
RETURNS varchar(8000)

/*
--****************************************************************************************************************
Function Name:	dbo.fnTrimAndReplaceNulls

Author:			Funmi Agbebi

Date Created:	4/18/2008

Purpose:		Function 

Description:	Removes leading and trailing spaces and replaces null values with zero-length character string 

--****************************************************************************************************************
*/

BEGIN
     DECLARE @CleansedField varchar(8000)
     SET @CleansedField = 

      CASE 
        WHEN @Field is NULL THEN ''
        ELSE ltrim(rtrim(@Field))
       END  

   RETURN(@CleansedField)
END
```

