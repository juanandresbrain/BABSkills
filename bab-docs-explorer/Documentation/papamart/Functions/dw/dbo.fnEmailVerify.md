# dbo.fnEmailVerify

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(500)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnEmailVerify"]
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
CREATE FUNCTION fnEmailVerify 
	(@email varchar(100))
RETURNS varchar(500)
AS
BEGIN
DECLARE @tempemail nvarchar(50)
DECLARE @atcounter as tinyint
DECLARE @atfinder as tinyint
DECLARE @ValidateEmail as varchar(500)
SET @ValidateEmail = 'TRUE' --Assume true on init 
IF LEN(RTRIM(LTRIM(@email)))<= 6 
BEGIN 
   SET @ValidateEmail='You did not enter an email address!'
END
ELSE IF PATINDEX ( '%@%' , @email )=0
BEGIN 
   SET @ValidateEmail='Your email address does not contain an @ sign.'
END
ELSE IF PATINDEX ( '% %' , RTRIM(LTRIM(@email)) )>0
BEGIN 
   SET @ValidateEmail='Your email address contains a space.'
END
ELSE IF Left(@email,1)='@'
BEGIN 
  SET @ValidateEmail='Your @ sign can not be the first character in your email address!'
END
ELSE IF Right(@email,1)= '@'
BEGIN 
   SET @ValidateEmail='Your @sign can not be the last character in your email address!'
END
ELSE IF right(@email,1) NOT LIKE '[a-z]' and right(@email,1) NOT LIKE '[0-9]'
BEGIN
	SET @ValidateEmail='The last character in your email address must be alpha or numeric!'
END
ELSE IF Len(@email) < 6 
BEGIN
   SET @ValidateEmail = 'Your email address is shorter than 6 characters which is impossible.'
End 
ELSE IF PATINDEX('%.%',@email)=0
BEGIN
	SET @ValidateEmail = 'Your email address must contain a period.'
END
ELSE IF PATINDEX('%.%',reverse(@email))> PATINDEX('%@%',reverse(@email))
BEGIN 
 SET @ValidateEmail = 'Your email address must contain a @ and then a period.'
END
ELSE IF left(@email,4)='www.'
BEGIN 
   SET @ValidateEmail='Email address begins with www.'
END
SET @tempemail = @email 
SET @atcounter=0
SET @atfinder=PATINDEX ( '%@%' , @tempemail )
While  @atfinder <> 0
BEGIN 
   SET  @atcounter = @atcounter+1 
   SET @tempemail = substring(@tempemail,@atfinder+1,len(@tempemail)) 
   SET @atfinder=PATINDEX ( '%@%' , @tempemail )
CONTINUE
END
IF @atcounter > 1 
BEGIN
   SET @ValidateEmail = 'You have more than 1 @ sign in your email address'
End  
RETURN @ValidateEmail	
END
```

