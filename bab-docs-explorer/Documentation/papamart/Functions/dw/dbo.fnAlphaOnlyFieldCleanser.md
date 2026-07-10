# dbo.fnAlphaOnlyFieldCleanser

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(8000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnAlphaOnlyFieldCleanser"]
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
CREATE FUNCTION dbo.fnAlphaOnlyFieldCleanser (@Field varchar(8000))
RETURNS varchar(8000)

/*
--****************************************************************************************************************
Function Name:	dbo.fnAlphaOnlyFieldCleanser

Author:			Funmi Agbebi

Date Created:	4/18/2008

Purpose:		Function to clean up fields that should hold letters of the alphabets only e.g. Name fields.

Description:	Strips input parameter of all but upper and lower case letter of the alphabet.  
				Also removes leading and trailing spaces, replaces null values with zero-length character string 

--****************************************************************************************************************
*/

BEGIN
     DECLARE @CleansedField varchar(8000)
     SET @CleansedField= 

      CASE 
        WHEN @Field is NULL THEN ''
		ELSE ltrim(rtrim(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace
			(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace
            (replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace
            (replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(@Field,
            '(',''),')',''),'*',''),'"',''),'!',''),'@',''),'#',''),'$',''),'%',''),'^',''),'&',''),
            '(',''),')',''),'_',''),'+',''),'=',''),'[',''),']',''),'\',''),'|',''),'{',''),'}',''),
            '0',''),'1',''),'2',''),'3',''),'4',''),'5',''),'6',''),'7',''),'8',''),'9',''),';',''),
            ':',''),'<',''),'>',''),',',''),'?',''),'/',''),'`',''),'~',''),'''',''),'.',' '),'-',' ')))
     END  

   RETURN(@CleansedField)
END
```

