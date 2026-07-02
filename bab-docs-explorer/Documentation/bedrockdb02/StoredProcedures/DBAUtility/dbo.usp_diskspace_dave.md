# dbo.usp_diskspace_dave

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_diskspace_dave"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[usp_diskspace_dave] AS

--  
-- -- SET QUOTED_IDENTIFIER ON 
-- -- GO
-- -- SET ANSI_NULLS ON 
-- -- GO
--  

set nocount on

DECLARE @hr int
DECLARE @fso int
DECLARE @drive char(1)
DECLARE @odrive int
DECLARE @TotalSize varchar(20)
DECLARE @MB bigint 
SET @MB = 1048576
declare @PercentFree int
declare @FreeSpace int

declare @date varchar(40)
set @date = convert(varchar, getdate(), 109)

-- this table must exist locally or the remote query will fail
IF (Object_ID('tempdb..##drives') IS NOT NULL) DROP TABLE ##drives
CREATE TABLE ##drives (
	drive char(1) PRIMARY KEY,
	FreeSpace int NULL,
	TotalSize int NULL,
	PercentFree	int null,
	DateStamp	datetime)

--truncate table dbo.drives

INSERT into ##drives(drive,FreeSpace)
EXEC master.dbo.xp_fixeddrives

EXEC @hr=sp_OACreate 'Scripting.FileSystemObject',@fso OUT

IF @hr <> 0 EXEC sp_OAGetErrorInfo @fso
DECLARE dcur CURSOR LOCAL FAST_FORWARD
FOR SELECT drive, freespace from ##drives
ORDER by drive
OPEN dcur
FETCH NEXT FROM dcur INTO @drive, @freespace
WHILE @@FETCH_STATUS=0
BEGIN
	EXEC @hr = sp_OAMethod @fso,'GetDrive', @odrive OUT, @drive
	IF @hr <> 0 EXEC sp_OAGetErrorInfo @fso

	EXEC @hr = sp_OAGetProperty @odrive,'TotalSize', @TotalSize OUT
	IF @hr <> 0 EXEC sp_OAGetErrorInfo @odrive

	-- do the percentfree first!!
	set @PercentFree = @FreeSpace/(cast(@TotalSize as float)/@MB)* 100
	set @TotalSize = @TotalSize/@MB

 	IF (Object_ID('tempdb..##nada') IS NOT NULL) DROP TABLE ##nada
	declare @sql varchar(8000)
	set @sql = '
	SELECT a.*
	into ##nada
	FROM OPENROWSET(''SQLOLEDB'',''papamart'';''link_writer'';''l1nkw'',
	''set nocount on 
		insert into dw.dbo.drives (server, drive, freespace, totalsize, percentfree, datestamp) values( ''''' + @@servername + ''''',''''' + @drive + ''''',''''' + cast(@freespace as varchar) + ''''',''''' + @TotalSize + ''''',''''' + cast(@PercentFree as varchar) + ''''',''''' + @date + ''''') 
		commit tran 
		select 1 as ErrorCode'') AS a'
-- 	print @sql
 	exec (@sql)
		
	FETCH NEXT FROM dcur INTO @drive, @freespace
END
CLOSE dcur
DEALLOCATE dcur
```

