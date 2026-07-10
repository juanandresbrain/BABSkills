# dbo.fnAddressFieldCleanser

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(8000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnAddressFieldCleanser"]
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
CREATE FUNCTION dbo.fnAddressFieldCleanser (@Field varchar(8000))
RETURNS varchar(8000)

/*
--****************************************************************************************************************
Function Name:	dbo.fnAddressFieldCleanser

Author:			Funmi Agbebi

Date Created:	4/18/2008

Purpose:		Function to clean up address fields

Description:	Strips input parameter of all but upper and lower case letter of the alphabet and numbers 0-9.  
				Also removes leading and trailing spaces, replaces null values with zero-length character string 

--****************************************************************************************************************
*/

BEGIN
     DECLARE @CleansedField varchar(8000)
     SET @CleansedField= 

      CASE 
        WHEN @Field is NULL THEN ''
		ELSE ltrim(rtrim(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace
            (replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace
            (replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(@Field,
            '(',''),')',''),'*',''),'"',''),'!',''),'@',''),'#',''),'$',''),'%',''),'^',''),'&',''),
            '(',''),')',''),'_',''),'+',''),'=',''),'[',''),']',''),'\',''),'|',''),'{',''),'}',''),
            ';',''),':',''),'<',''),'>',''),',',''),'?',''),'/',''),'`',''),'~',''),'''',''),'--','')))
       END  

   RETURN(@CleansedField)
END
```

