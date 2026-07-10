# dbo.fn_removecharacters

**Database:** DBAUtility  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(200)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_removecharacters"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @word | varchar | 200 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fn_removecharacters 
	(@word varchar(200))
RETURNS varchar(200)
AS
BEGIN
DECLARE @word_out varchar(200)
Declare @counter smallint
Declare @len smallint
Declare @char char(1)

Set @len=len(ltrim(rtrim(@word)))
Set @counter=1
Set @word=upper(ltrim(rtrim(@word)))

While @counter<=@len and @len>0
BEGIN
     Set @char=substring(@word,@counter,1)
     IF ASCII(@char) between 65 and 90
     BEGIN
          IF @word_out is null
               SET @word_out=@char
          ELSE
               SET @word_out=@word_out+@char
     END
     SET @counter=@counter+1
END
RETURN @word_out

END
```

