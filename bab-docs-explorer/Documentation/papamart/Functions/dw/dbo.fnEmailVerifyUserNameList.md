# dbo.fnEmailVerifyUserNameList

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(2000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnEmailVerifyUserNameList"]
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
CREATE FUNCTION fnEmailVerifyUserNameList
 	(@username varchar(100))
 RETURNS varchar(2000)
AS
 BEGIN
DECLARE @charcounter as smallint
DECLARE @charend as smallint
DECLARE @ValidateEmail as varchar(5)
DECLARE @charlist varchar(2000) 
--Source: http://www.remote.org/jochen/mail/info/chars.html for valid characters in email
SET @ValidateEmail='TRUE'
SET @charlist='' 
--Range 1 characters 0-37
SET @charcounter=0
SET @charend=37
WHILE @charcounter<= @charend
BEGIN
	IF PATINDEX('%'+char(@charcounter)+'%',@username)>0 
	BEGIN
		SET @charlist=@charlist+convert(varchar(3),@charcounter)+'|'
	END
	SET @charcounter=@charcounter+1
END
--Range 2 characters 
SET @charcounter=40
SET @charend=44
WHILE @charcounter<= @charend
BEGIN
	IF PATINDEX('%'+char(@charcounter)+'%',@username)>0 and  
        @charcounter not in (42,43)
	BEGIN
		SET @charlist=@charlist+convert(varchar(3),@charcounter)+'|'
	END
	SET @charcounter=@charcounter+1
END
--Range 3 58 - 64
SET @charcounter=58
SET @charend=64
WHILE @charcounter<= @charend
BEGIN
	IF PATINDEX('%'+char(@charcounter)+'%',@username)>0 
	BEGIN
		SET @charlist=@charlist+convert(varchar(3),@charcounter)+'|'
	END
	SET @charcounter=@charcounter+1
END
--Range 4 91 - 93 
SET @charcounter=91
SET @charend=96
WHILE @charcounter<= @charend
BEGIN
	IF @charcounter<>95 and PATINDEX('%'+char(@charcounter)+'%',@username)>0 
	BEGIN
		SET @charlist=@charlist+convert(varchar(3),@charcounter)+'|'
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
		SET @charlist=@charlist+convert(varchar(3),@charcounter)+'|'
	END
	SET @charcounter=@charcounter+1
END
If @charlist='' 
RETURN @ValidateEmail
ELSE
RETURN @charlist
RETURN @ValidateEmail
END
```

