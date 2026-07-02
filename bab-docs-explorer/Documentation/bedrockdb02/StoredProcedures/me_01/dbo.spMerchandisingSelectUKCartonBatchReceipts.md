# dbo.spMerchandisingSelectUKCartonBatchReceipts

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingSelectUKCartonBatchReceipts"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingSelectUKCartonBatchReceipts]
as


-- =====================================================================================================
-- Name: spMerchandisingSelectUKCartonBatchReceipts
--
-- Description:	Looks for CBR Files Retrieved from UK Webstore SFTP Server, renames and copies for Pipeline to process into Merch
--
-- Input: NA
--
-- Output: Resultset formatted to meet Epicor requirements for Carton Batch Reciept Receipt Import.
--
-- Revision History
--		Name:			Date:			Comments:
--		Tim Callahan	09/06/2017		Created proc.	
-- =====================================================================================================

--check the directory to see if there are CBR files ready to import
-------------do a DIR command and store the results in a temp table

IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\WebCBR\*.txt /B'
delete from #DIR where output is null or output = 'File Not Found'


-- select * from #DIR


------------query temp table to see if there are CBR .txt files
if (select count(*) from #DIR) > 0


Begin 

			
		declare @files int,
				@filename varchar(100),
				@filepath varchar(100),
				@del varchar(100),
				@move varchar(1000),
				@copy varchar(1000),
				@query varchar(1000),
				@file_name varchar(100),
				@file_location varchar(100),
				@server varchar(20),
				@database varchar(20),
				@bcp varchar(1000),
				@timestamp varchar(52),
				@rename varchar(1000),
				@nameage varchar(104),
				@documentNumber varchar(9)

		select @filepath = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\WebCBR\'
		select @files = count(*) from #dir
		
		
---------Bulk Insert Loop
		while @files > 0
			begin
			    select @timestamp = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(hh, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar) + cast(datepart(ss, getdate()) as varchar)
				select @filename = max(output) from #dir
				
				select @rename = 'ren ' + @filepath + @filename + ' ' + @filename + '.' + @timestamp + '.GO' -- Change to .GO when happy 
				exec master..xp_cmdshell @rename

				select @copy = 'copy ' + @filepath + @filename + '.' + @timestamp + '.GO' + ' "\\pipeapp01\Company01\Text File to IM Import Tables  - Batch Carton\"'
		        exec master..xp_cmdshell @copy
				
				select @move = 'move ' + @filepath + @filename + '.' + @timestamp + '.GO' + ' \\kermode\FileRepository\MERCHANDISING\UK_Distro\WebCBR\Done\'
		        exec master..xp_cmdshell @move
				
				delete from #dir where output = @filename
				select @files = count(*) from #dir
								
				if @files < 1
					break
				else
					continue
					
			End

End
```

