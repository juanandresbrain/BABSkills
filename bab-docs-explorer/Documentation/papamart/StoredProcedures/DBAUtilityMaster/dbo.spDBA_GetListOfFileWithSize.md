# dbo.spDBA_GetListOfFileWithSize

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_GetListOfFileWithSize"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE   [dbo].[spDBA_GetListOfFileWithSize]   
( 
    @Dir    VARCHAR(1000) 
) 
AS 

-- =============================================================================================================
-- Name: spDBA_DatabaseBackup
--
-- Description:	Gets List of Files with Sizes


-- Available actions:
--	
-- Dependencies: 
--
----------------------------------------------------------------------------------------------------
--// Original Source: http://stackoverflow.com/questions/7952406/get-each-file-size-inside-a-folder-using-sql                                                     //--
----------------------------------------------------------------------------------------------------
--
-- Revision History
--		Name:			Date:			Comments:
--		Mike Pelikan	02/10/2012		Created based on script from http://stackoverflow.com/questions/7952406/get-each-file-size-inside-a-folder-using-sql  
--		Mike Pelikan	04/09/2012		Updated version number to show correction using global temp table

--------------------------------------------------------------------------------------------- 
-- Variable decleration 
--------------------------------------------------------------------------------------------- 
    declare @curdir nvarchar(400) 
    declare @line varchar(400) 
    declare @command varchar(400) 
    declare @counter int 
 
    DECLARE @1MB    DECIMAL 
    SET     @1MB = 1024 * 1024 
 
    DECLARE @1KB    DECIMAL 
    SET     @1KB = 1024  
 
--------------------------------------------------------------------------------------------- 
-- Temp tables creation 
--------------------------------------------------------------------------------------------- 
CREATE TABLE #dirs (DIRID int identity(1,1), directory varchar(400)) 
--CREATE TABLE ##FileSize (line varchar(400)) 
--CREATE TABLE output (Directory varchar(400), FilePath VARCHAR(400), SizeInMB DECIMAL(13,2), SizeInKB DECIMAL(13,2)) 
IF object_id('tempdb..##FileSize','u')  IS NULL
BEGIN	
	CREATE TABLE ##FileSize (Directory varchar(400), FilePath VARCHAR(400), SizeInMB DECIMAL(13,2), SizeInKB DECIMAL(13,2)) 
END

CREATE TABLE #tempFilePaths (Files VARCHAR(500)) 
CREATE TABLE #tempFileInformation (FilePath VARCHAR(500), FileSize VARCHAR(100)) 
 
--------------------------------------------------------------------------------------------- 
-- Call xp_cmdshell 
---------------------------------------------------------------------------------------------     
 
     SET @command = 'dir "'+ @Dir +'" /S/O/B/A:D' 
     INSERT INTO #dirs exec xp_cmdshell @command 
     INSERT INTO #dirs SELECT @Dir 
     SET @counter = (select count(*) from #dirs) 
 
--------------------------------------------------------------------------------------------- 
-- Process the return data 
---------------------------------------------------------------------------------------------       
        WHILE @Counter <> 0 
          BEGIN 
            DECLARE @filesize INT 
            SET @curdir = (SELECT directory FROM #dirs WHERE DIRID = @counter) 
            SET @command = 'dir "' + @curdir +'"' 
            ------------------------------------------------------------------------------------------ 
                -- Clear the table 
                DELETE FROM #tempFilePaths 
 
 
                INSERT INTO #tempFilePaths 
                EXEC MASTER..XP_CMDSHELL @command  
 
                --delete all directories 
                DELETE #tempFilePaths WHERE Files LIKE '%<dir>%' 
				
				--delete File Not Found
				DELETE #tempFilePaths WHERE Files = 'File Not Found'
				
                --delete all informational messages 
                DELETE #tempFilePaths WHERE Files LIKE ' %' 
 
                --delete the null values 
                DELETE #tempFilePaths WHERE Files IS NULL 
 
                --get rid of dateinfo 
                UPDATE #tempFilePaths SET files =RIGHT(files,(LEN(files)-20)) 
 
                --get rid of leading spaces 
                UPDATE #tempFilePaths SET files =LTRIM(files) 
 
                --split data into size and filename 
                ---------------------------------------------------------- 
                -- Clear the table 
                DELETE FROM #tempFileInformation; 
 
                -- Store the FileName & Size 
                INSERT INTO #tempFileInformation 
                SELECT   
                        RIGHT(files,LEN(files) -PATINDEX('% %',files)) AS FilePath, 
                        LEFT(files,PATINDEX('% %',files)) AS FileSize 
                FROM    #tempFilePaths 
 
                -------------------------------- 
                --  Remove the commas 
                UPDATE  #tempFileInformation 
                SET     FileSize = REPLACE(FileSize, ',','') 
 
 
 
                -------------------------------------------------------------- 
                -- Store the results in the output table 
                -------------------------------------------------------------- 
 
                INSERT INTO ##FileSize--(FilePath, SizeInMB, SizeInKB) 
                SELECT   
                        @curdir, 
                        FilePath, 
                        CAST(CAST(FileSize AS DECIMAL(13,2))/ @1MB AS DECIMAL(13,2)), 
                        CAST(CAST(FileSize AS DECIMAL(13,2))/ @1KB AS DECIMAL(13,2)) 
                FROM    #tempFileInformation 
 
            -------------------------------------------------------------------------------------------- 
 
 
            Set @counter = @counter -1 
           END 
 
 
    DELETE FROM ##FileSize WHERE Directory is null        
---------------------------------------------- 
-- DROP temp tables 
----------------------------------------------            
--DROP TABLE ##FileSize   
DROP TABLE #dirs   
DROP TABLE #tempFilePaths   
DROP TABLE #tempFileInformation   
--DROP TABLE #tempfinal   
 
 
--SELECT  * FROM  ##FileSize 
--DROP TABLE ##FileSize
```

