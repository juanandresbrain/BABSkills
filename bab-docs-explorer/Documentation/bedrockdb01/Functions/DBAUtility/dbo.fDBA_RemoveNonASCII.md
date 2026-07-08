# dbo.fDBA_RemoveNonASCII

**Database:** DBAUtility  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** varchar(255)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fDBA_RemoveNonASCII"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @nstring | nvarchar | 510 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[fDBA_RemoveNonASCII] 
(
    @nstring nvarchar(255)
)
RETURNS varchar(255)
AS
--from http://www.sqlservercentral.com/Forums/Topic1001736-391-1.aspx#bm1015640
BEGIN

    DECLARE @Result varchar(255)
    SET @Result = ''

    DECLARE @nchar nvarchar(1)
    DECLARE @position int

    SET @position = 1
    WHILE @position <= LEN(@nstring)
    BEGIN
        SET @nchar = SUBSTRING(@nstring, @position, 1)
        --Unicode & ASCII are the same from 1 to 255.
        --Only Unicode goes beyond 255
        --0 to 31 are non-printable characters
        IF UNICODE(@nchar) between 32 and 127
            SET @Result = @Result + @nchar
        SET @position = @position + 1
    END

    RETURN @Result

END
```

