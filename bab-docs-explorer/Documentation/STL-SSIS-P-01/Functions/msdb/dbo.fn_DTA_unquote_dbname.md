# dbo.fn_DTA_unquote_dbname

**Database:** msdb  
**Server:** STL-SSIS-P-01  
**Function Type:** Scalar Function  
**Returns:** sysname(256)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_DTA_unquote_dbname"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @dbname | nvarchar | 516 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
create function fn_DTA_unquote_dbname(@dbname nvarchar(258) )
returns sysname
as
begin
	declare @unquote nvarchar(258) 
	set @unquote = @dbname
	if(patindex(N'[[]%',@unquote) > 0)
		  select @unquote = right(@unquote, LEN(@unquote)-1)
	if(patindex(N'%]',@unquote)  > 0)
		  select @unquote = left(@unquote, LEN(@unquote)-1)
	select @unquote =REPLACE (@unquote,N']]',N']')
	return @unquote
end
```
