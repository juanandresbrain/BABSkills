# WM.spOutputXMLFile

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spOutputXMLFile"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc [WM].[spOutputXMLFile]
	@Query varchar(1000),
    @FileLocation varchar(100),
	@FileName varchar(100)

as

-- =====================================================================================================
-- Name: WEB.spOutputXMLFile
--
-- Description:	Outputs XML file in UTF-8 format, accepts Query, FileLocation and FileName parameters
--		
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		05-15-2017		Created proc.	
-- =====================================================================================================

set nocount on


declare 
	@bcp varchar(1000)

set @bcp = 'bcp "' + @query + '" queryout "' + @FileLocation +'Stage\' +  @FileName + '"  -T -c -C65001' ----c -C65001 means to use UTF-8, otherwise -w means Unicode

exec master..xp_cmdshell @bcp 

set @bcp = 'Move ' +  @FileLocation +'Stage\' +  @FileName + ' ' +  @FileLocation +  @FileName  

exec master..xp_cmdshell @bcp






WM,spRestageUKFTP,create proc WM.spRestageUKFTP 

as

set nocount on

-----------------------------------------------------------------------------------------------------------------------------------------------------------
--Dan Tweedie -	2017-11-08	- Created proc to run on demand, will look for files for orders identified as not having been FTP'd to UK, restages for FTP
---------------------------------------------------------------------------------------------------------------------------------------------------------------


---copies logged uploaded uk files to a temp folder, from there they need to be copy/pasted to \\kermode\FileRepository\OMSOrders\BABW-UK\Temp, then the ftp upload script needs to run

IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\OMSOrders\BABW-UK\Success\LoggedFiles\*.xml /B'
delete from #DIR where output is null or output = 'File Not Found'
or output not in (select OrderFileName 
					from WM.UKFTPSuccessFolder 
					where OrderNumber in (select OrderNumber from wm.OrdersNotSentToUK)
				)


declare 
	@count int,
	@FileName varchar(500),
	@Copy varchar(1000)

select @count = count(*) from #DIR

while @count > 0

begin
	select @FileName = max(output) from #DIR
	
	delete from #DIR where output = @FileName
	
	select @Copy = 'copy \\kermode\FileRepository\OMSOrders\BABW-UK\Success\LoggedFiles\' + @FileName + ' \\kermode\FileRepository\OMSOrders\BABW-UK\Temp\'
	EXEC master..xp_cmdshell @Copy
	
	set @count = @count-1
	
	if @count = 0 
	break
		else
	continue
end
```

