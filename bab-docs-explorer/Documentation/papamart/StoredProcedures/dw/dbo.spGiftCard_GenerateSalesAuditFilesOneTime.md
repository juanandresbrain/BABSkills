# dbo.spGiftCard_GenerateSalesAuditFilesOneTime

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGiftCard_GenerateSalesAuditFilesOneTime"]
    dbo_merchandise_detail(["dbo.merchandise_detail"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_STS_DocumentNumber(["dbo.STS_DocumentNumber"]) --> SP
    dbo_transaction_header(["dbo.transaction_header"]) --> SP
    dbo_xp_cmdshell(["dbo.xp_cmdshell"]) --> SP
    dbo_xp_create_subdir(["dbo.xp_create_subdir"]) --> SP
    dbo_xp_fileexist(["dbo.xp_fileexist"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.merchandise_detail |
| dbo.sp_send_dbmail |
| dbo.STS_DocumentNumber |
| dbo.transaction_header |
| dbo.xp_cmdshell |
| dbo.xp_create_subdir |
| dbo.xp_fileexist |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spGiftCard_GenerateSalesAuditFilesOneTime]
AS

SET NOCOUNT ON

-- ===================================================================================================================================
--      Ian Wallace		12/06/2021		Created this veriosn of the proc to run when we need to submit rows to SA for whatever reason
-- ===================================================================================================================================

DECLARE @Revision DATETIME
SET @Revision = '11/30/2014'
 	
-- =============================================================================================================


SET NOCOUNT ON
----------------------------------------------------------------------------------------------------
--// Variable Declaration	                                                                    //--
----------------------------------------------------------------------------------------------------

DECLARE @MaxLastDocumentNumber BIGINT, @CurrentDate DATETIME
DECLARE @sql varchar(8000), @strFileName VARCHAR(20), @wrkDirectory VARCHAR(50), 
@STSDirectory VARCHAR(500), @STSDirectoryPrefix CHAR(4), @IPSTSDirectorySuffix CHAR(3), @TRSTSDirectorySuffix CHAR(3),
@intCounter INT, @bitFolderExists BIT, @chkdirectory VARCHAR(2000)

DECLARE @isError BIT, @errText VARCHAR(1000)
DECLARE @recipients AS VARCHAR(200)

DECLARE @StartDate DateTime, @intStoreID INT, @itemNumber INT, @LineNum INT
DECLARE @prevStartDate DateTime, @previntStoreID INT 		

DECLARE @file_results TABLE (file_exists int, file_is_a_directory int, parent_directory_exists int )

DECLARE @GCWrk TABLE (period_start_date DATETIME, store_id INT, item_num INT, unitcnt INT, DocumentNumber INT, LineNum CHAR(3))
DECLARE @GCDocNumber TABLE (period_start_date DATETIME, store_id INT, DocumentNumber INT IDENTITY(1,1) )


SELECT @strFileName = 'XPOLLD00130001', 
--@STSDirectory = '\\saapp01\PollData\',
--@STSDirectory = '\\posappsa01\sybwork\POLLFILES_LIVE\', -- changed 20150717 - bedrock go live
@STSDirectory = '\\KERMODE\FileRepository\Poll\', 
--@STSDirectory = '\\posappsatest01\sybwork\POLLFILES_TEST\',
@STSDirectoryPrefix = 'AWL.', @IPSTSDirectorySuffix = '.IP', @TRSTSDirectorySuffix = '.TR',
@recipients = 'ianw@buildabear.com'

IF OBJECT_ID('tempdb..#UKFiles') IS NOT NULL DROP TABLE #UKFiles
IF OBJECT_ID('tempdb..#NAFiles') IS NOT NULL DROP TABLE #NAFiles

IF OBJECT_ID('tempdb..##GCWork') IS NOT NULL DROP TABLE ##GCWork
CREATE TABLE ##GCWork (col1 VARCHAR(1000),store_id INT, LineNum INT)

----------------------------------------------------------------------------------------------------
--// Insert the data into the working tables                                                    //--
----------------------------------------------------------------------------------------------------


INSERT INTO @GCWrk (period_start_date, store_id, item_num, unitcnt)

	--select entry_date_time as period_start_date, store_no as store_id, upc_no as item_num, cast(sum(units)*-1 as int) as unitcnt
	--from bedrockdb01.auditworks.dbo.transaction_header th with (nolock)
	--	join bedrockdb01.auditworks.dbo.merchandise_detail md with (nolock)
	--	on md.transaction_id = th.transaction_id
	--where transaction_series = 'G'
	--	and entry_date_time in ('2022-08-30 05:00:00.000') 
	--	and edit_timestamp <> 831121206263  -- for 8/30  currently 8500 rows
	--	--and upc_no = 26478 
	--	--and upc_no = 25414
	--	--and upc_no = 26457
	--	--and upc_no = 26472
	--	--and upc_no = 28153
	--	--and upc_no = 28159
	--	--and upc_no = 29911
	--	--and upc_no = 29913
	--	--and upc_no = 29915
	--	--and upc_no = 29917
	--	--and upc_no = 126478
	--	--and upc_no = 129917
	--	--and upc_no = 425414
	--	--and upc_no = 426457
	--	--and upc_no = 426478
	--	--and upc_no = 426479
	--	--and upc_no = 428153
	--	--and upc_no = 428159
	--	--and upc_no = 429913
	--	--and upc_no = 429915
	--	and upc_no = 429917
	--	group by entry_date_time, store_no, upc_no
	--	having cast(sum(units)*-1 as int) <> 0
	--	order by store_no, upc_no asc 


	--select entry_date_time as period_start_date, store_no as store_id, upc_no as item_num, cast(sum(units)*-1 as int) as unitcnt
	--from bedrockdb01.auditworks.dbo.transaction_header th with (nolock)
	--	join bedrockdb01.auditworks.dbo.merchandise_detail md with (nolock)
	--	on md.transaction_id = th.transaction_id
	--where transaction_series = 'G'
	--	and entry_date_time in ('2022-08-31 05:00:00.000') 
	--	and edit_timestamp <>  901062425787   -- for 8/31   currently 9791 rows 
	--	--and upc_no = 26478
	--	--and upc_no = 25414
	--	--and upc_no = 26457
	--	--and upc_no = 26472
	--	--and upc_no = 28153
	--	--and upc_no = 28159
	--	--and upc_no = 29911
	--	--and upc_no = 29913
	--	--and upc_no = 29915
	--	--and upc_no = 29917
	--	--and upc_no = 126478
	--	--and upc_no = 129917
	--	--and upc_no = 425414
	--	--and upc_no = 426457
	--	--and upc_no = 426478
	--	--and upc_no = 426479
	--	--and upc_no = 428153
	--	--and upc_no = 428159
	--	--and upc_no = 429913
	--	--and upc_no = 429915
	--	and upc_no = 429917
	--	group by entry_date_time, store_no, upc_no
	--	having cast(sum(units)*-1 as int) <> 0
	--	order by store_no, upc_no asc 


	select entry_date_time as period_start_date, store_no as store_id, upc_no as item_num, cast(sum(units)*-1 as int) as unitcnt
	from bedrockdb01.auditworks.dbo.transaction_header th with (nolock)
		join bedrockdb01.auditworks.dbo.merchandise_detail md with (nolock)
		on md.transaction_id = th.transaction_id
	where transaction_series = 'G'
	and entry_date_time in ('2022-09-01 05:00:00.000') 
		and edit_timestamp <> 902062501123   -- for 9/1   currently 874 rows 
		--and upc_no = 26478
		--and upc_no = 25414
		--and upc_no = 26457
		--and upc_no = 26472
		--and upc_no = 28153
		--and upc_no = 28159
		--and upc_no = 29911
		--and upc_no = 29913
		--and upc_no = 29915
		--and upc_no = 29917
		--and upc_no = 126478
		--and upc_no = 129917
		--and upc_no = 425414
		--and upc_no = 426457
		--and upc_no = 426478
		--and upc_no = 426479
		--and upc_no = 428153
		--and upc_no = 428159
		--and upc_no = 429913
		--and upc_no = 429915
		and upc_no = 429917
		group by entry_date_time, store_no, upc_no
		having cast(sum(units)*-1 as int) <> 0
		order by store_no, upc_no asc 

		



--/*******  DEBUG  *********/
--SELECT * FROM @GCWrk
--/*******  DEBUG  *********/
----------------------------------------------------------------------------------------------------
--// Get the STS Document Numbers			                                                    //--
----------------------------------------------------------------------------------------------------

INSERT INTO @GCDocNumber
SELECT DISTINCT period_start_date, store_id 
FROM @GCWrk
ORDER BY 1, 2
--/*******  DEBUG  *********/
--SELECT * FROM @GCDocNumber
--/*******  DEBUG  *********/

SELECT @CurrentDate = GETDATE()
SELECT @MaxLastDocumentNumber = MAX(LastDocumentNumber) FROM KODIAK.beardata.dbo.STS_DocumentNumber

INSERT INTO KODIAK.beardata.dbo.STS_DocumentNumber
SELECT DISTINCT DocumentNumber + @MaxLastDocumentNumber, @CurrentDate, 'ParseValueLink'  FROM @GCDocNumber
/*******  DEBUG  *********/
SELECT DISTINCT DocumentNumber + @MaxLastDocumentNumber, @CurrentDate, 'ParseValueLink'  FROM @GCDocNumber
/*******  DEBUG  *********/

UPDATE wrk
SET DocumentNumber = dn.DocumentNumber + @MaxLastDocumentNumber
FROM @GCWrk wrk
INNER JOIN @GCDocNumber dn ON wrk.period_start_date = dn.period_start_date AND wrk.store_id = dn.store_id

----------------------------------------------------------------------------------------------------
--// Update the detail line numbers		                                                    //--
----------------------------------------------------------------------------------------------------

DECLARE lineNumber_csr CURSOR FOR
	SELECT period_start_date, store_id, item_num
	FROM @GCWrk

OPEN lineNumber_csr   
FETCH NEXT FROM lineNumber_csr INTO @StartDate, @intStoreID, @itemNumber

WHILE @@FETCH_STATUS = 0   
BEGIN  
	IF ISNULL(@prevStartDate, '1/1/1900') <> @StartDate OR ISNULL(@previntStoreID, 0) <> @intStoreID
	BEGIN
		SET @LineNum = 100
	END
	ELSE
	BEGIN
		SET @LineNum = @LineNum + 1
	END
       
	UPDATE @GCWrk
	SET LineNum = CAST(@LineNum AS CHAR(3))
	WHERE period_start_date = @StartDate AND store_id = @intStoreID AND item_num = @itemNumber

	SELECT @prevStartDate = @StartDate, @previntStoreID = @intStoreID
	      
	FETCH NEXT FROM lineNumber_csr INTO @StartDate, @intStoreID, @itemNumber
END   

CLOSE lineNumber_csr   
DEALLOCATE lineNumber_csr

----------------------------------------------------------------------------------------------------
--// Generate the file						                                                    //--
----------------------------------------------------------------------------------------------------

WHILE (SELECT COUNT(*) FROM @GCWrk) > 0
BEGIN
	SELECT @StartDate = MIN(period_start_date) FROM @GCWrk

	TRUNCATE TABLE ##GCWork

	INSERT INTO ##GCWork
	SELECT  'H' + CHAR(9) + CAST(store_id AS VARCHAR(10)) + CHAR(9) + '2' + CHAR(9) + 
		CONVERT(VARCHAR(10), period_start_date, 101) + ' ' +  CONVERT(VARCHAR(10), period_start_date, 8) +
		CHAR(9) + 'G' + CHAR(9) + CAST(DocumentNumber AS VARCHAR(10)) + CHAR(9) + '0' + CHAR(9) + '1' + CHAR(9) + '0' + CHAR(9) + CHAR(9) +  
		CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + '1' + CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + CHAR(9) + '0' col1, store_id, 0 LineNum
	FROM @GCWrk 
	WHERE  period_start_date = @StartDate
	UNION
	SELECT   'L' + CHAR(9) + LineNum  + CHAR(9) + '405' + CHAR(9) + '1' + CHAR(9) + RIGHT(REPLICATE('0',12) + CAST(item_num AS VARCHAR(12)), 12) + 
		CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + '1' + CHAR(9) + '0' + CHAR(9) + '1' + CHAR(9) + '0' + CHAR(9) + '1' + CHAR(9) + '0' + CHAR(9) + 
		'0' + CHAR(9) + '0' + CHAR(9) + '0' col1, store_id, LineNum
	--INTO ##Tran
	FROM @GCWrk 
	WHERE  period_start_date = @StartDate
	UNION
	SELECT   'M' + CHAR(9) + LineNum  + CHAR(9) + '1' + CHAR(9) + '2' + CHAR(9) + RIGHT(REPLICATE('0',12) + CAST(item_num AS VARCHAR(12)), 12)  + 
		CHAR(9) + CAST(unitcnt AS varchar(5)) + CHAR(9) + '1' + CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + '0' +
		CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + '0' + CHAR(9) + RIGHT(REPLICATE('0',12) + CAST(item_num AS VARCHAR(12)), 12) + CHAR(9) + '0' col1, store_id, LineNum
	
	FROM @GCWrk 
	WHERE period_start_date = @StartDate
	ORDER BY  store_id, LineNum
	

	--/*******  DEBUG  *********/
--	SELECT col1 FROM ##GCWork
--/*******  DEBUG  *********/

	----------------------------------------------------------------------------------------------------
	--// Validation					                                                    //--
	----------------------------------------------------------------------------------------------------
	SELECT @isError = 0, @errText = ''
	--if any nulls
	IF (SELECT COUNT(*) FROM ##GCWork WHERE col1 IS NULL) > 0 
	BEGIN
		SELECT @isError = 1, @errText = @errText + 'There are nulls in the Giftcard Transaction file. ' + CHAR(13)
	END
	--if there aren't matching L to M line counts
	IF (SELECT COUNT(*) FROM ##GCWork WHERE col1 LIKE 'L%') <> (SELECT COUNT(*) FROM ##GCWork WHERE col1 LIKE 'M%')
	BEGIN
		SELECT @isError = 1, @errText = @errText + 'The number of L lines do not match the number of M lines. ' + CHAR(13)
	END
	--Count of Gift cards for the day do not match.
	IF (SELECT SUM(unitcnt) FROM @GCWrk WHERE  period_start_date = @StartDate ) <> 
		(SELECT SUM(CAST(SUBSTRING(col1,24,CHARINDEX(CHAR(9) , col1, 25)-24) AS INT))FROM ##GCWork WHERE col1 LIKE 'M%' and col1 not like '%*%'	)
	BEGIN
		SELECT @isError = 1, @errText = @errText + 'The count of gift cards do not match from the source to the file. ' +CHAR(13)
	END


	----------------------------------------------------------------------------------------------------
	--// Create the directory					                                                    //--
	----------------------------------------------------------------------------------------------------
	--check to see if directory exists
	SELECT @intCounter = 112, @bitFolderExists  = 1

	WHILE @bitFolderExists = 1
	BEGIN
		DELETE FROM @file_results
		
		SET @wrkDirectory = RIGHT('00' + CAST(MONTH(@StartDate) AS VARCHAR(2)), 2) + RIGHT('00' + CAST(DAY(@StartDate) AS VARCHAR(2)), 2) + RIGHT( '0000' + CAST (@intCounter AS VARCHAR(4)), 4)
		SET @chkdirectory = @STSDirectory + @STSDirectoryPrefix + @wrkDirectory + @TRSTSDirectorySuffix
		
		INSERT INTO @file_results (file_exists, file_is_a_directory, parent_directory_exists)
		EXEC master.dbo.xp_fileexist @chkdirectory
     
		SELECT @bitFolderExists = file_is_a_directory from @file_results
		IF @bitFolderExists = 1
		BEGIN
			SET @intCounter = @intCounter + 1
		END
		ELSE
		BEGIN
			DELETE FROM @file_results

			SET @wrkDirectory = RIGHT('00' + CAST(MONTH(@StartDate) AS VARCHAR(2)), 2) + RIGHT('00' + CAST(DAY(@StartDate) AS VARCHAR(2)), 2) + RIGHT( '0000' + CAST (@intCounter AS VARCHAR(4)), 4)
			SET @chkdirectory = @STSDirectory + @STSDirectoryPrefix + @wrkDirectory + @IPSTSDirectorySuffix
		
			INSERT INTO @file_results (file_exists, file_is_a_directory, parent_directory_exists)
			EXEC master.dbo.xp_fileexist @chkdirectory
     
			SELECT @bitFolderExists = file_is_a_directory from @file_results
		
			IF @bitFolderExists = 1
			BEGIN
				SET @intCounter = @intCounter + 1
			END
		END
	END
	
	EXECUTE master.dbo.xp_create_subdir @chkdirectory
        select  @chkdirectory
	SELECT @sql = 'bcp "SELECT col1 FROM ##GCWork " queryout ' + @chkdirectory + '\' + @strFileName + '.tmp' + ' -c -t, -T ' ---S WBNSCOREDEV01\SQL2008R2' ---S KODIAK' 
	EXEC master.dbo.xp_cmdshell @sql
PRINT @sql
	
	IF @isError = 1 
	BEGIN
		SELECT @sql = 'RENAME ' + @chkdirectory + '\' + @strFileName + '.tmp' + ' ' + @strFileName + '.err'
		EXEC master.dbo.xp_cmdshell @sql

		SET @sql = @chkdirectory + '\' + @strFileName + '.err' 
		exec msdb.dbo.sp_send_dbmail 
		@recipients = @recipients,
		@body= @errText, 
		@file_attachments = @sql
	END
	ELSE
	BEGIN
		SELECT @sql = 'RENAME ' + @chkdirectory + '\' + @strFileName + '.tmp' + ' ' + @strFileName 
		EXEC master.dbo.xp_cmdshell @sql
PRINT @sql


	END

	DELETE FROM @GCWrk WHERE  period_start_date = @StartDate
END
```

