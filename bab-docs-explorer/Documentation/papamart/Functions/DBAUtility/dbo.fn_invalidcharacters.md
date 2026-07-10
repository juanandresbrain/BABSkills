# dbo.fn_invalidcharacters

**Database:** DBAUtility  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(10)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_invalidcharacters"]
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
CREATE FUNCTION fn_invalidcharacters
	(@word varchar(200))
RETURNS varchar(10)
AS
BEGIN
DECLARE @word_out varchar(200)
Declare @counter smallint
Declare @len smallint
Declare @char char(1)


Set @len=len(ltrim(rtrim(@word)))
Set @counter=1
Set @word=upper(ltrim(rtrim(@word)))
Set @char=substring(@word,@counter,1)

While @counter<=@len     
BEGIN
     IF (ASCII(@char) not between 65 and 90 and ASCII(@char) not in (45,32,39)) 
     RETURN 'TRUE'
     SET @counter=@counter+1
     Set @char=substring(@word,@counter,1)
Continue
END

Return 'FALSE'

END
```

