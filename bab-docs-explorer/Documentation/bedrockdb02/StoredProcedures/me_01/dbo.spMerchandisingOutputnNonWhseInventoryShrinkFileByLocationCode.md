# dbo.spMerchandisingOutputnNonWhseInventoryShrinkFileByLocationCode

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputnNonWhseInventoryShrinkFileByLocationCode"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputnNonWhseInventoryShrinkFileByLocationCode]
@Locationcode varchar (4)
as


	declare @query varchar(1000),
			@date varchar(200),
			@file_name varchar(100),
			@file_location varchar(100),
			@server varchar(20),
			@username varchar(20),
			@password varchar(20),
			@database varchar(20),
			@sqlcmd varchar(1000),
			@query_text varchar(4000)

			-- When Testinb 
			--, 			@Locationcode varchar (4)
			--set @Locationcode = '0003'

	select @query_text = 'exec spMerchandisingOutputnNonWhseInventoryShrinkBatchedByLocationCode '+@LocationCode
	set @date = convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())) + convert(varchar, datepart(ss, getdate()))
	set @query = @query_text
	--set @file_location = '\\pipeapp01\Company01\Text File to IM Import Tables- Import Shrink Adj\'
	set @file_location = '\\pipeapp01\Company01\Text File to IM Import Tables- Import Shrink Adj\Staging\'
	set @file_name = 'STSIMSA.StoreSyncLocationCode'+@LocationCode+'.' + @date + '.GO'
	set @server = 'bedrockdb02'
	set @database = 'me_01'
	set @sqlcmd = 'sqlcmd -S' + @server + ' -d' + @database + ' -Q' + '"' + @query + '"' + ' -o' + '"' + @file_location + @file_name + '"' + ' -s"," -w100 -W'
	exec master..xp_cmdshell @sqlcmd
```

