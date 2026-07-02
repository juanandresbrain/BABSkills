# dbo.spPaymentech_CopyFiles_US

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spPaymentech_CopyFiles_US"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spPaymentech_CopyFiles_US] 
--WITH EXECUTE AS 'BAB\SQLSERVICES'
AS
-- =============================================================================================================
-- Name: spPaymentech_CopyFiles
--
-- Description:	

--
-- Input:		
--				
--
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		BradA							Created
--		GaryD			20090914		Update recipients
--		davidr			20100214		fixed file length issue where the date was missing
--		GaryD			20110414		Update recipients
--		Mike Pelikan	20140507		Changed file drop location and email to db mail.
--		Mike Pelikan	20141020		added WITH EXECUTE AS
--		Ian Wallace		20150130		redesigned for new Chesapeake version
--      Ian Wallace		20180214		redesigned to copy to D365 interface server
--exec [spPaymentech_CopyFiles]
-- =============================================================================================================


declare @sql varchar(8000)
declare @destdrive varchar(5)
declare @sourcedrive varchar(5)
declare @command varchar(300)

IF (Object_ID('tempdb..##paymentech_error') IS NOT NULL) DROP TABLE ##paymentech_error
create table ##paymentech_error (
	message	varchar(100)
)

set @destdrive = 'u:'
set @sourcedrive = 'v:'
set @sql = ''

truncate table ##paymentech_error

set @command = 'net use ' + @destdrive + ' /d'
insert into ##paymentech_error
exec master..xp_cmdshell @command

-- if the drive is not mounted then trying to delete it will spawn the following message, nothing to be concerned about
if (select count(*) from ##paymentech_error where message = 'The network connection could not be found.') >= 1
begin 
	truncate table ##paymentech_error
end

--set @command = 'net use ' + @destdrive + ' "\\stl-dynsnc-p-01\oData\paymentechD365"'
set @command = 'net use ' + @destdrive + ' "\\stl-ssis-p-01\IntegrationStaging\paymentech\paymentechD365"'
insert into ##paymentech_error
exec master..xp_cmdshell @command

-- if not successful, then send error
if ((select count(*) from ##paymentech_error where message like '%The command completed successfully%') = 0)
begin
	delete from ##paymentech_error where message is null

	exec msdb.dbo.sp_send_dbmail 
	@recipients = 'ianw@buildabear.com',
	@subject='Paymentech File Pull - Error', 
	@query_result_width = 250,
	@query= 'select * from ##paymentech_error'
end

set @sql = ''

truncate table ##paymentech_error

set @command = 'net use ' + @sourcedrive + ' /d'
insert into ##paymentech_error
exec master..xp_cmdshell @command

-- if the drive is not mounted then trying to delete it will spawn the following message, nothing to be concerned about
if (select count(*) from ##paymentech_error where message = 'The network connection could not be found.') >= 1
begin 
	truncate table ##paymentech_error
end

--set @command = 'net use ' + @sourcedrive + ' "\\babwenc01\d$\paymentech" cp5ftp /user:BABWENC01\cpSftp'
set @command = 'net use ' + @sourcedrive + ' "\\stl-ssis-p-01\IntegrationStaging\paymentech"'
insert into ##paymentech_error
exec master..xp_cmdshell @command

-- if not successful, then send error
if ((select count(*) from ##paymentech_error where message like '%The command completed successfully%') = 0)
begin
	delete from ##paymentech_error where message is null

	exec msdb.dbo.sp_send_dbmail
	@profile_name = 'admin', 
	@recipients = 'ianw@buildabear.com',
	@subject='Paymentech File Pull - Error', 
	@query_result_width = 250,
	@query= 'select * from ##paymentech_error'
end


IF (Object_ID('tempdb..#source') IS NOT NULL) DROP TABLE #source
create table #source (
	filename	varchar(100)
)

set @command = 'dir /b ' + @sourcedrive + '\*.dfr'
insert into #source
exec master..xp_cmdshell @command

delete from #source where filename is null

IF (Object_ID('tempdb..#source_yesterday') IS NOT NULL) DROP TABLE #source_yesterday
create table #source_yesterday (
	filename	varchar(100)
)

insert into #source_yesterday (filename)
select filename from #source
where cast(substring(filename, 12, 6) as datetime) = dateadd(dd, -1, cast(convert(varchar,getdate(), 101) as datetime)) and len(filename) > 22
and filename like '%0162056%'

--select * from #source
--select * from #source_yesterday
------------------------------------------------------------------

declare curFilenames cursor
for
	select s.filename from #source_yesterday s		
open curFilenames
declare @filename	varchar(100)
fetch next from curFilenames into @filename
while (@@fetch_STATUS <> -1)
begin
print @filename
	set @command = 'copy ' + @sourcedrive + '\' + @filename + ' ' + @destdrive + '\' + @filename
	exec master..xp_cmdshell @command
	fetch next from curFilenames into @filename
end
close curFilenames
deallocate curFilenames

set @command = 'net use ' + @destdrive + ' /d'
exec master..xp_cmdshell @command
set @command = 'net use ' + @sourcedrive + ' /d'
exec master..xp_cmdshell @command
```

