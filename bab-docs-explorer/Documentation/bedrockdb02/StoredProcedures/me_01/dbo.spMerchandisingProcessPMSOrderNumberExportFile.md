# dbo.spMerchandisingProcessPMSOrderNumberExportFile

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingProcessPMSOrderNumberExportFile"]
    dbo_PMSOrderNumberExport(["dbo.PMSOrderNumberExport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PMSOrderNumberExport |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingProcessPMSOrderNumberExportFile]

as 
-- =====================================================================================================
-- Name: spMerchandisingProcessPMSOrderNumberExportFile
--
-- Description:	Imports PMSOrderNumberExport.csv files on \\bearservice01\ESEsport folder records and saves them into a table on me_01.
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Lee		09/19/2016		created proc
-- =====================================================================================================

set nocount on

----PART ONE - IMPORT SHIPMENT FILES

IF (Object_ID('tempdb..#files') IS NOT NULL) DROP TABLE #files
create table #files (output varchar(1000))
insert #files exec master..xp_cmdshell 'dir \\bearservice01\ESExport\*.csv /B'
delete from #files where output is null or output = 'File Not Found'

if (select count(*) from #files) > 0

BEGIN
		IF (Object_ID('tempdb..#file_input') IS NOT NULL) DROP TABLE #file_input
			create table #file_input
			(pms_no varchar(7),
			 es_no varchar(20))
		
		declare @files int,
				@filename varchar(52),
				@filepath varchar(100),
				@bulkinsert varchar(4000),
				@del varchar(1000),
				@move varchar(1000),
				@query varchar(1000),
				@file_name varchar(100),
				@file_location varchar(1000),
				@server varchar(20),
				@database varchar(20),
				@bcp varchar(1000),
				@date varchar(200)


		set @date = convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())) + convert(varchar, datepart(ss, getdate()))
		select @filepath = '\\bearservice01\ESExport\'
		select @files = count(*) from #files

		while @files > 0
			begin

				select @filename = max(output) from #files
				select @bulkinsert = 'bulk insert #file_input from ''' + @filepath + @filename + ''' with (FIELDTERMINATOR = '','', ROWTERMINATOR = ''\n'')'
				exec (@bulkinsert)
				
				select @move = 'copy ' + @filepath + @filename + ' \\kermode\FileRepository\MERCHANDISING\ESExport\Done\' + 'PMSOrderNumberExport' + '_' + @date + '.csv'

				exec master..xp_cmdshell @move
								
				delete from #files where output = @filename
				select @files = count(*) from #files
								
				if @files < 1
					break
				else
					continue
			end

insert into	PMSOrderNumberExport
select	pms_no, 
		es_no, 
		getdate() as entry_date
from #file_input


end
```

