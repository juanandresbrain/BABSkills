# dbo.spMerchandisingImportCNCBROutput

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingImportCNCBROutput"]
    dbo_CNCBR(["dbo.CNCBR"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CNCBR |

## Stored Procedure Code

```sql
create proc spMerchandisingImportCNCBROutput

as 

-- =====================================================================================================
-- Name: spMerchandisingImportCNCBROutput
--
-- Description:	Bulk insert carton receipt file from CN warehouse, outputs file to pipeline
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/25/2016		Created proc.	
-- =====================================================================================================

set nocount on

IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFER_CBR\*.csv /B'
delete from #DIR where output is null or output = 'File Not Found'

------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0

		begin
					--import file into work table
					if (object_id('me_01..CNCBR') is not null) drop table CNCBR
					create table CNCBR
					(location_code varchar(4),
					carton_no varchar(20))

					bulk insert CNCBR
					from '\\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFER_CBR\TransferCBR.csv'
					with 
					(
					FIELDTERMINATOR = ',',
					ROWTERMINATOR = '\n'
					)
					--rename file with timestamp
					EXEC master..xp_cmdshell 'ren \\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFER_CBR\TransferCBR.csv TransferCBR.csv%date:~4,2%%date:~7,2%%date:~10%.dat'
					--move file to DONE folder
					EXEC master..xp_cmdshell 'move \\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFER_CBR\*.csv \\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFER_CBR\done'
					---generate carton batch receipt file for pipeline
							declare @query2 varchar(1000),
							@file_location2 varchar(100),
							@file_name2 varchar(100),
							@server2 varchar(52),
							@database2 varchar(52),
							@bcp varchar(1000)

					set @query2 = 'set nocount on select ''BC'', ''A'', carton_nbr, ''location_code'', ''099060199'' from CNCBR'
					set @file_location2 = '\\pipeapp01\Company01\Text File to IM Import Tables  - Batch Carton\'
					set @file_name2 = 'STSIMCTN.CN.' + convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + '.GO'
					set @server2 = 'bedrockdb02'
					set @database2 = 'me_01'
					set @bcp = 'bcp "' + @query2 + '" queryout "' + @file_location2 + @file_name2 + '" -T -c -Sbedrockdb02'

					exec master..xp_cmdshell @bcp
			end
```

