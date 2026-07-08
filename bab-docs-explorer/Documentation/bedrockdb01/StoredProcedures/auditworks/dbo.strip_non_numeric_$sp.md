# dbo.strip_non_numeric_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.strip_non_numeric_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
create proc dbo.strip_non_numeric_$sp 

     @string nvarchar(255),
    @stripped_string nvarchar(255) OUTPUT
AS
DECLARE @ascii_value 		smallint,
	@nchar_position 		tinyint,
        @nchar 			nvarchar(1),
	@errno 			int,
	@string_length		tinyint


/*
**  Name:	 strip_non_numeric_$sp
**  Description: To remove non-numeric characters from a string.  
**               Intended for phone# cleanup.
**               

HISTORY:
Date      Name       Def#   Description
Jan05,11  Paul     105313   Use unicode datatypes
Oct23,06  Maryam  DV-1345   Handle null concats.
Aug30,01  Vicci      8415   Author

*/


BEGIN
  SELECT @string_length = LEN(@string),
  	 @nchar_position = 1

  IF @string_length = 0 or @string_length is null
   RETURN
  
  WHILE @nchar_position <= @string_length
  BEGIN
      SELECT @nchar = SUBSTRING(@string, @nchar_position, 1)
      
      SELECT @ascii_value = ASCII(@nchar) 
       								
      IF @ascii_value >= 48 AND @ascii_value <= 57	 -- IF character is numeric ( 0 to 9 )
        SELECT @stripped_string = ISNULL(@stripped_string,'') + @nchar
      
      SELECT @nchar_position = @nchar_position + 1
  END  
END
RETURN
```

