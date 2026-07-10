# dbo.fnEmailCleanDomain

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(100)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnEmailCleanDomain"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @username | varchar | 100 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fnEmailCleanDomain
 	(@username varchar(100))
 RETURNS varchar(100)
AS
BEGIN
DECLARE @charcounter as smallint
DECLARE @charend as smallint
--Source: http://www.remote.org/jochen/mail/info/chars.html for valid characters in email
--Range 1 characters 0-47
SET @charcounter=0
SET @charend=47
WHILE @charcounter<= @charend
BEGIN
	IF PATINDEX('%'+char(@charcounter)+'%',@username)>0 and  @charcounter<>46
	BEGIN
		SET @username=replace(@username,char(@charcounter),'')
	END
	SET @charcounter=@charcounter+1
END
--Range 2 58 - 64
SET @charcounter=58
SET @charend=64
WHILE @charcounter<= @charend
BEGIN
	IF PATINDEX('%'+char(@charcounter)+'%',@username)>0 
	BEGIN
		SET @username=replace(@username,char(@charcounter),'')
	END
	SET @charcounter=@charcounter+1
END
--Range 4 91 - 97 
SET @charcounter=91
SET @charend=96
WHILE @charcounter<= @charend
BEGIN
	IF @charcounter<>95 and PATINDEX('%'+char(@charcounter)+'%',@username)>0 
	BEGIN
		SET @username=replace(@username,char(@charcounter),'')
	END
	SET @charcounter=@charcounter+1
END
--Range 5 123-255
SET @charcounter=123
SET @charend=255
WHILE @charcounter<= @charend
BEGIN
	IF PATINDEX('%'+char(@charcounter)+'%',@username)>0 
	BEGIN
		SET @username=replace(@username,char(@charcounter),'')
	END
	SET @charcounter=@charcounter+1
END
RETURN @username
END
```

