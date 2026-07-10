# dbo.fnStringCount

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** tinyint(1)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnStringCount"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @string | varchar | 100 | NO |
| @searchstring | varchar | 100 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fnStringCount 
	(@string varchar(100), 
	 @searchstring varchar(100))
RETURNS tinyint
AS
BEGIN

DECLARE @atcounter tinyint
DECLARE @atfinder tinyint

SET @atcounter=0
SET @atfinder=PATINDEX ( '%'+ @searchstring+'%' , @string )
While  @atfinder <> 0
BEGIN 
   SET  @atcounter = @atcounter+1 
   SET @string = substring(@string,@atfinder+1,len(@string)) 
   SET @atfinder=PATINDEX ( '%'+ @searchstring+'%' , @string )
CONTINUE
END
RETURN @atcounter	

END


dbo,fnCRM_build_address_match_key,SQL_SCALAR_FUNCTION,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [fnCRM_build_address_match_key]
(
	-- Add the parameters for the function here
 @address_1 varchar(40) = NULL
,@address_2 varchar(40) = NULL
,@address_3 varchar(40) = NULL
,@address_4 varchar(40) = NULL
,@address_5 varchar(40) = NULL
,@address_6 varchar(40) = NULL
,@post_code varchar(20) = NULL
,@address_key_format varchar(25) = NULL
)
RETURNS varchar(28)
AS
BEGIN
	-- Declare the return variable here
	DECLARE 
	 @next_format_char char(1)
	,@pos int
	,@wk_address_match_key varchar(28)
	,@counter tinyint
	,@counter2 tinyint
	,@current_char char(1)
	,@previous_char char(1)
	,@length tinyint
	,@found bit
	,@wk_addr_1 varchar(40)
	,@wk_addr_2 varchar(40)
	,@wk_addr_3 varchar(40)
	,@wk_addr_4 varchar(40)
	,@wk_addr_5 varchar(40)
	,@wk_addr_6 varchar(40)
	,@wk_post_code varchar(20)
	,@address_match_key varchar(28) 

	-- Add the T-SQL statements to compute the return value here
SELECT	@address_1 = upper(ltrim(rtrim(@address_1))),
	@address_2 = upper(ltrim(rtrim(@address_2))),
	@address_3 = upper(ltrim(rtrim(@address_3))),
	@address_4 = upper(ltrim(rtrim(@address_4))),
	@address_5 = upper(ltrim(rtrim(@address_5))),
	@address_6 = upper(ltrim(rtrim(@address_6))),
	@post_code = upper(ltrim(rtrim(@post_code))),
	@address_key_format = upper(ltrim(rtrim(@address_key_format))),
	@wk_address_match_key = '',
	@previous_char=''

select @counter = 1

IF 	(@address_1 IS NOT NULL AND @address_1 <> '') OR 
	(@address_2 IS NOT NULL AND @address_2 <> '') OR 
	(@address_3 IS NOT NULL AND @address_3 <> '') OR 
   	(@address_4 IS NOT NULL AND @address_4 <> '') OR 
   	(@address_5 IS NOT NULL AND @address_5 <> '') OR 
   	(@address_6 IS NOT NULL AND @address_6 <> '') OR
   	(@post_code IS NOT NULL AND @post_code <> '')
BEGIN
	WHILE @counter <= DATALENGTH(@address_key_format)
	BEGIN

		select @found = 0
		SELECT @next_format_char = substring(@address_key_format, @counter, 1)
		select @counter = @counter + 1
		select @current_char = NULL

		IF @next_format_char <> @previous_char
			select 	@wk_addr_1 = @address_1,
				@wk_addr_2 = @address_2,
				@wk_addr_3 = @address_3,
				@wk_addr_4 = @address_4,
				@wk_addr_5 = @address_5,
				@wk_addr_6 = @address_6,
				@wk_post_code = @post_code

		IF  @next_format_char = 'A' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_1)
			BEGIN
				select @current_char = substring(@wk_addr_1,@counter2,1)
				IF (ascii(@current_char) >= 65 AND ascii(@current_char) <= 90)
				BEGIN
					select @length = DATALENGTH(@wk_addr_1) - (DATALENGTH(substring(@wk_addr_1,1,@counter2)))
					select @wk_addr_1 = substring(@wk_addr_1,1,(@counter2 - 1)) + substring(@wk_addr_1,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = (@wk_address_match_key + ' ')
		END
		ELSE
		IF  @next_format_char = 'B' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_2)
			BEGIN
				select @current_char = substring(@wk_addr_2,@counter2,1)
				IF (ascii(@current_char) >= 65 AND ascii(@current_char) <= 90)
				BEGIN
					select @length = DATALENGTH(@wk_addr_2) - (DATALENGTH(substring(@wk_addr_2,1,@counter2)))
					select @wk_addr_2 = substring(@wk_addr_2,1,(@counter2 - 1)) + substring(@wk_addr_2,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = 'C' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_3)
			BEGIN
				select @current_char = substring(@wk_addr_3,@counter2,1)
				IF (ascii(@current_char) >= 65 AND ascii(@current_char) <= 90)
				BEGIN
					select @length = DATALENGTH(@wk_addr_3) - (DATALENGTH(substring(@wk_addr_3,1,@counter2)))
					select @wk_addr_3 = substring(@wk_addr_3,1,(@counter2 - 1)) + substring(@wk_addr_3,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = 'D' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_4)
			BEGIN
				select @current_char = substring(@wk_addr_4,@counter2,1)
				IF (ascii(@current_char) >= 65 AND ascii(@current_char) <= 90)
				BEGIN
					select @length = DATALENGTH(@wk_addr_4) - (DATALENGTH(substring(@wk_addr_4,1,@counter2)))
					select @wk_addr_4 = substring(@wk_addr_4,1,(@counter2 - 1)) + substring(@wk_addr_4,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = 'E' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_5)
			BEGIN
				select @current_char = substring(@wk_addr_5,@counter2,1)
				IF (ascii(@current_char) >= 65 AND ascii(@current_char) <= 90)
				BEGIN
					select @length = DATALENGTH(@wk_addr_5) - (DATALENGTH(substring(@wk_addr_5,1,@counter2)))
					select @wk_addr_5 = substring(@wk_addr_5,1,(@counter2 - 1)) + substring(@wk_addr_5,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = 'F' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_6)
			BEGIN
				select @current_char = substring(@wk_addr_6,@counter2,1)
				IF (ascii(@current_char) >= 65 AND ascii(@current_char) <= 90)
				BEGIN
					select @length = DATALENGTH(@wk_addr_6) - (DATALENGTH(substring(@wk_addr_6,1,@counter2)))
					select @wk_addr_6 = substring(@wk_addr_6,1,(@counter2 - 1)) + substring(@wk_addr_6,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = '1' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_1)
			BEGIN
				select @current_char = substring(@wk_addr_1,@counter2,1)
				IF (ascii(@current_char) >= 48 AND ascii(@current_char) <= 57)
				BEGIN
					select @length = DATALENGTH(@wk_addr_1) - (DATALENGTH(substring(@wk_addr_1,1,@counter2)))
					select @wk_addr_1 = substring(@wk_addr_1,1,(@counter2 - 1)) + substring(@wk_addr_1,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF @next_format_char = '2' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_2)
			BEGIN
				select @current_char = substring(@wk_addr_2,@counter2,1)
				IF (ascii(@current_char) >= 48 AND ascii(@current_char) <= 57)
				BEGIN
					select @length = DATALENGTH(@wk_addr_2) - (DATALENGTH(substring(@wk_addr_2,1,@counter2)))
					select @wk_addr_2 = substring(@wk_addr_2,1,(@counter2 - 1)) + substring(@wk_addr_2,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = '3' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_3)
			BEGIN
				select @current_char = substring(@wk_addr_3,@counter2,1)
				IF (ascii(@current_char) >= 48 AND ascii(@current_char) <= 57)
				BEGIN
					select @length = DATALENGTH(@wk_addr_3) - (DATALENGTH(substring(@wk_addr_3,1,@counter2)))
					select @wk_addr_3 = substring(@wk_addr_3,1,(@counter2 - 1)) + substring(@wk_addr_3,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = '4' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_4)
			BEGIN
				select @current_char = substring(@wk_addr_4,@counter2,1)
				IF (ascii(@current_char) >= 48 AND ascii(@current_char) <= 57)
				BEGIN
					select @length = DATALENGTH(@wk_addr_4) - (DATALENGTH(substring(@wk_addr_4,1,@counter2)))
					select @wk_addr_4 = substring(@wk_addr_4,1,(@counter2 - 1)) + substring(@wk_addr_4,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = '5' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_5)
			BEGIN
				select @current_char = substring(@wk_addr_5,@counter2,1)
				IF (ascii(@current_char) >= 48 AND ascii(@current_char) <= 57)
				BEGIN
					select @length = DATALENGTH(@wk_addr_5) - (DATALENGTH(substring(@wk_addr_5,1,@counter2)))
					select @wk_addr_5 = substring(@wk_addr_5,1,(@counter2 - 1)) + substring(@wk_addr_5,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = '6' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_addr_6)
			BEGIN
				select @current_char = substring(@wk_addr_6,@counter2,1)
				IF (ascii(@current_char) >= 48 AND ascii(@current_char) <= 57)
				BEGIN
					select @length = DATALENGTH(@wk_addr_6) - (DATALENGTH(substring(@wk_addr_6,1,@counter2)))
					select @wk_addr_6 = substring(@wk_addr_6,1,(@counter2 - 1)) + substring(@wk_addr_6,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		ELSE
		IF  @next_format_char = 'P' 
		BEGIN
			select @counter2 = 1
			WHILE @counter2 <= DATALENGTH(@wk_post_code)
			BEGIN
				select @current_char = substring(@wk_post_code,@counter2,1)
				IF (ascii(@current_char) >= 48 AND ascii(@current_char) <= 57) OR (ascii(@current_char) >= 65 AND ascii(@current_char) <= 90)
			BEGIN
					select @length = DATALENGTH(@wk_post_code) - (DATALENGTH(substring(@wk_post_code,1,@counter2)))
					select @wk_post_code = substring(@wk_post_code,1,(@counter2 - 1)) + substring(@wk_post_code,(@counter2 + 1),@length)
					select @wk_address_match_key = @wk_address_match_key + @current_char
					select @found = 1
					BREAK
				END
				select @counter2 = @counter2 + 1
			END
			IF @found = 0
				select @wk_address_match_key = @wk_address_match_key + ' '
		END
		select @previous_char = @next_format_char
	END
	/* End of while loop */
	SELECT @address_match_key = @wk_address_match_key
END

ELSE
BEGIN
	SELECT @address_match_key = NULL
END

	-- Return the result of the function
	RETURN @address_match_key


END
```

