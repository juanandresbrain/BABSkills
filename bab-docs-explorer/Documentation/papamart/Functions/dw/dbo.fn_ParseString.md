# dbo.fn_ParseString

**Database:** dw  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_ParseString"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @ParseString | varchar | 8000 | NO |
| @Separator | varchar | 10 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE function [dbo].[fn_ParseString] (@ParseString varchar(8000), @Separator as varchar(10)) 
returns @tempTable table

	(ParsedItem 	varchar(100))
as 
begin
	declare @tempstring varchar(100)
	if substring(@ParseString, len(@ParseString), 1) != @Separator
		set @ParseString = @ParseString + @Separator
	
	while len(@ParseString) > 0
	begin
		set @tempstring = left(@ParseString, charindex(@Separator, @ParseString) - 1)
	
		insert into @tempTable values(@tempstring)
		set @ParseString = substring(@ParseString, charindex(@Separator, @ParseString, 1) + 1, len(@ParseString))
	
		if charindex(@Separator, @ParseString, 1) = 0 
			set @ParseString = ''
	end
return
end
```

