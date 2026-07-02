# dbo.spDBA_RebuildIndexes_TableList_2000

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_RebuildIndexes_TableList_2000"]
    dbo_INDEX_MAINT_HIST(["dbo.INDEX_MAINT_HIST"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.INDEX_MAINT_HIST |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDBA_RebuildIndexes_TableList_2000] 
@TableListCommaDelimited VARCHAR(2000), 
	@MaxLogicalfrag DECIMAL = 15.0,  @MaxScanDensity DECIMAL = 90.0
	, @DatabaseName varchar(150), @RunMinutes SMALLINT = 120
	, @Schema varchar(25) = 'dbo'
	, @Action varchar(25) = 'Rebuild'
	, @Logging varchar(3) = 'No'
AS
-- =============================================================================================================
-- Name: spDBA_RebuildIndexes_2000
--
-- Description:	Performs maintenance on indexes depending on parameters passed in.
--	Use this procedure with SQL Server 2000 databases and SQL Server 2005 databasess that are compatibility 80.
--	The Rebuild option does the best job of maintaining indexes but causes blocking and can fill the log.
--	The Reorg option is not as good as rebuild, but is an online operation.
--	Use the reorg option when other database activities prevent using the rebuild option.
--	
--	@MaxLogicalfrag			-- Maximum fragmentation after which indexes will be rebuilt.
--	@MaxScanDensity			-- Minimum average page fullness before the index must be rebuilt.
--  @DatabaseName			-- Name of the db
--	@RunMinutes				-- Number of minutes after which another rebuild will not start
--  @Schema					-- Table schema name
--  @Action					-- Choose between doing a rebuild or defrag.  Base decision on maintenance window and testing.
--  @Logging				-- Yes or no.  If yes then latest statements logged to DBAUtility..INDEX_MAINT_HIST
--  
-- Output: returns error messages
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	12/31/2008		Created based on article http://blogs.digineer.com/blogs/larar/archive/2006/08/16/smart-index-defrag-reindex-for-a-consolidated-sql-server-2005-environment.aspx
--										Added logic to not start another rebuild if past a specified number of minutes. 	
--		Gary Derikito	6/1/2009		Correct case to allow for case sensitive dbs.	
--		Gary Derikito	7/31/2009		Add filter on tables with x* and tmp* prefix and optional filter on schema.
--		Gary Derikito	8/3/2009		Add filter on tables with %.% because the period caused issues with 3 part naming.
--		Gary Derikito	8/9/2009		Add reorg section inspired by http://www.mssqltips.com/tip.asp?tip=1165.  Reorg is online while rebuild is offline.
--		Gary Derikito	8/10/2009		Add #IndexProperty process because property function has to be run in local database.
--		Gary Derikito	8/11/2009		Add optional logging of latest statements
--		Mike Pelikan	2/21/2012		Added comma delimited 

/*
exec spDBA_RebuildIndexes_2000 1,  90, 'dw', 10, 'dbo'
exec spDBA_RebuildIndexes_2000 1,  90, 'dw', 10, 'pm_repo'
exec spDBA_RebuildIndexes_2000 1,  90, 'dw', 10
exec spDBA_RebuildIndexes_2000 1,  90, 'dw', 10, 'cube'

spDBA_RebuildIndexes_2000 @MaxLogicalfrag = 0.0, @MaxScanDensity = 90.0, @DatabaseName = 'dw_test', @RunMinutes = 120, @Schema = 'dbo', @Action = 'Defrag', @Logging = 'Yes'
spDBA_RebuildIndexes_2000 @MaxLogicalfrag = 3.0, @MaxScanDensity = 90.0, @DatabaseName = 'dw_test', @RunMinutes = 120, @Schema = 'dbo', @Action = 'Defrag', @Logging = 'Yes'
spDBA_RebuildIndexes_2000 @MaxLogicalfrag = 3.0, @MaxScanDensity = 80.0, @DatabaseName = 'dw_test', @RunMinutes = 120, @Schema = 'dbo', @Action = 'Rebuild', @Logging = 'Yes'
spDBA_RebuildIndexes_2000 @MaxLogicalfrag = 70.0, @MaxScanDensity = 30.0, @DatabaseName = 'dw_test', @RunMinutes = 120, @Schema = 'dbo', @Action = 'Rebuild', @Logging = 'Yes'

spDBA_RebuildIndexes_2000 @MaxLogicalfrag = 15.0, @MaxScanDensity = 80.0, @DatabaseName = 'dw_test', @RunMinutes = 120, @Schema = 'dbo', @Action = 'Defrag', @Logging = 'Yes'

*/
-- =============================================================================================================

-- Declare variables
SET NOCOUNT ON
DECLARE @TableName VARCHAR (128)
DECLARE @TableSchema varchar(128)
DECLARE @execstr   VARCHAR (255)
DECLARE @ObjectId  INT
DECLARE @IndexId   INT
DECLARE @IndexName   VARCHAR (255)
DECLARE @LogicalFrag    DECIMAL
DECLARE @ScanDensity    DECIMAL
DECLARE @StartTime	DATETIME
DECLARE @FinishLine DATETIME
DECLARE @SQL NVARCHAR (1000)


--capture when the run is started
SET @StartTime = getdate()

SELECT @FinishLine = DATEADD(mi, @RunMinutes, @StartTime) 

-- Create the temp tables
CREATE TABLE #tables(
	TableName varchar(255)
	,TableSchema varchar(255)
	,UpdateStats TINYINT
)

CREATE TABLE #fraglist (
   OwnerName varchar(128),
   ObjectName CHAR (255),
   ObjectId INT,
   IndexName CHAR (255),
   IndexId INT,
   Lvl INT,
   CountPages INT,
   CountRows INT,
   MinRecSize INT,
   MaxRecSize INT,
   AvgRecSize INT,
   ForRecCount INT,
   Extents INT,
   ExtentSwitches INT,
   AvgFreeBytes INT,
   AvgPageDensity INT,
   ScanDensity DECIMAL,
   BestCount INT,
   ActualCount INT,
   LogicalFrag DECIMAL,
   ExtentFrag DECIMAL)

INSERT INTO #tables(TableName, TableSchema)
EXEC('SELECT TABLE_NAME, TABLE_SCHEMA
   FROM ' + @DatabaseName + '.INFORMATION_SCHEMA.TABLES T
   INNER JOIN (SELECT txt_value FROM DBAUtility.dbo.fnDBA_ParseDelimitedVarchar('''+@TableListCommaDelimited+''',''' + ',' + ''')) tmpT ON T.TABLE_NAME = tmpT.txt_value
   WHERE TABLE_TYPE = ''BASE TABLE''' + ' AND TABLE_NAME NOT LIKE ''x%''' + ' AND TABLE_NAME NOT LIKE ''%.%''' + ' AND TABLE_NAME NOT LIKE ''tmp%'''
	+ ' AND TABLE_SCHEMA = ''' + @Schema + ''''
	+ ' ORDER BY TABLE_NAME')

--select * from #tables return
--store index property data in a temp table because the function needs to run in the local database
CREATE TABLE #IndexProperty (
	ObjectId	INT
	,IndexId	INT
	,IndexName	VARCHAR(255)
	,IndexDepth	INT)


-- Declare cursor
DECLARE tables CURSOR FOR
   SELECT TableName, TableSchema
   FROM #tables

-- Open the cursor
OPEN tables

-- Loop through all the tables in the database
FETCH NEXT
   FROM tables
   INTO @TableName, @TableSchema

WHILE @@FETCH_STATUS = 0
BEGIN

-- Do the showcontig of all indexes of the table
   INSERT INTO #fraglist (
	ObjectName, ObjectId, IndexName, IndexId, Lvl, CountPages, CountRows, MinRecSize, MaxRecSize, AvgRecSize, ForRecCount, Extents, ExtentSwitches, AvgFreeBytes, AvgPageDensity, ScanDensity, BestCount, ActualCount, LogicalFrag, ExtentFrag
	)
   EXEC ('USE ' + @DatabaseName + ' DBCC SHOWCONTIG (''' + @TableSchema + '.' + @TableName + ''') 
      WITH FAST, TABLERESULTS, ALL_INDEXES, NO_INFOMSGS')

   UPDATE #fraglist
   SET OwnerName = @TableSchema
   WHERE OwnerName IS NULL

   FETCH NEXT
      FROM tables
      INTO @TableName, @TableSchema

END

-- Close and deallocate the cursor
CLOSE tables
DEALLOCATE tables

--select * from #fraglist return

/********************************/
---Update fraglist with INDEXPROPERTY value

DECLARE IndexProp CURSOR FOR
   SELECT ObjectId, IndexId, IndexName
   FROM #fraglist

OPEN IndexProp

FETCH NEXT FROM IndexProp INTO @ObjectId,  @IndexId, @IndexName

WHILE @@FETCH_STATUS = 0
BEGIN


	SET @SQL = 'USE ' + @DatabaseName + '; SELECT ' + CAST(@ObjectId AS VARCHAR(50)) + ', ' + CAST(@IndexId AS VARCHAR(50)) + ', ' + '''' + @IndexName + '''' + ',
	INDEXPROPERTY (' + CAST(@ObjectId AS VARCHAR(50)) + ', ' + '''' + @IndexName + '''' + ', ' + '''IndexDepth''' + ') IndexDepth'

	INSERT INTO #IndexProperty(
		ObjectId
		,INDEXID
		,IndexName
		,IndexDepth)
	
	EXEC sp_executesql @SQL

FETCH NEXT FROM IndexProp INTO @ObjectId,  @IndexId, @IndexName
END

CLOSE IndexProp
DEALLOCATE IndexProp

SET @ObjectId = NULL
SET @IndexId = NULL
SET @IndexName = NULL  

--select * from #fraglist
--select * from #IndexProperty
--return
/********************************/

---optional log the latest statements

IF @Logging = 'Yes'
BEGIN
	--check for the local logging table
    IF EXISTS ( SELECT  *
                FROM    dbo.sysobjects
                WHERE   id = OBJECT_ID(N'[DBAUtility].[dbo].[INDEX_MAINT_HIST]') ) 
		BEGIN
			DELETE [DBAUtility].[dbo].[INDEX_MAINT_HIST]
		END
	ELSE
		BEGIN

			CREATE TABLE [DBAUtility].[dbo].[INDEX_MAINT_HIST](
				[RUN_DT] [smalldatetime] NULL,
				[SQL_TXT] [varchar](1000) NULL
			)

		END
END

----------------------------------
IF @Action = 'Rebuild'
BEGIN -- start of rebuild section

-- Declare cursor for list of indexes to be defragged
-- If clustered index meets the criteria, just reindex the entire table
-- If clustered index does not require a reindex, only return the non-clustered
-- which meet the criteria.
DECLARE indexes CURSOR FOR
        SELECT f.ObjectName, f.OwnerName, f.ObjectId, f.IndexId, f.IndexName, f.LogicalFrag, f.ScanDensity
        FROM #fraglist f JOIN #IndexProperty p ON (f.ObjectId = p.ObjectId AND f.IndexId = p.IndexId)    
        WHERE (f.LogicalFrag >= @MaxLogicalfrag
                OR f.ScanDensity < @MaxScanDensity)
--                AND INDEXPROPERTY (ObjectId, IndexName, 'IndexDepth') > 0
				AND p.IndexDepth > 0 --indexproperty function has to be run in local database
                AND NOT EXISTS(SELECT ObjectId 
                                FROM #fraglist i1 
                                WHERE IndexId = 1 
                                AND (LogicalFrag >= @MaxLogicalfrag
                                OR ScanDensity < @MaxScanDensity)
				AND i1.ObjectId = f.ObjectId)
        UNION 
        SELECT f.ObjectName, f.OwnerName, f.ObjectId, f.IndexId, f.IndexName, f.LogicalFrag, f.ScanDensity
        FROM #fraglist f JOIN #IndexProperty p ON (f.ObjectId = p.ObjectId AND f.IndexId = p.IndexId)
        WHERE (f.LogicalFrag >= @MaxLogicalfrag
                OR f.ScanDensity < @MaxScanDensity)
--                AND INDEXPROPERTY (ObjectId, IndexName, 'IndexDepth') > 0
				AND p.IndexDepth > 0 --indexproperty function has to be run in local database
                AND f.IndexId = 1 
                AND (f.LogicalFrag >= @MaxLogicalfrag
                OR f.ScanDensity < @MaxScanDensity)
        ORDER BY f.ObjectName, f.IndexId


--        SELECT ObjectName, OwnerName, ObjectId, IndexId, IndexName, LogicalFrag, ScanDensity
--        FROM #fraglist f    
--        WHERE (LogicalFrag >= @MaxLogicalfrag
--                OR ScanDensity < @MaxScanDensity)
----                AND INDEXPROPERTY (ObjectId, IndexName, 'IndexDepth') > 0
--                AND NOT EXISTS(SELECT ObjectId 
--                                FROM #fraglist i1 
--                                WHERE IndexId = 1 
--                                AND (LogicalFrag >= @MaxLogicalfrag
--                                OR ScanDensity < @MaxScanDensity)
--				AND i1.ObjectId = f.ObjectId)
--        UNION 
--        SELECT ObjectName, OwnerName, ObjectId, IndexId, IndexName, LogicalFrag, ScanDensity
--        FROM #fraglist f    
--        WHERE (LogicalFrag >= @MaxLogicalfrag
--                OR ScanDensity < @MaxScanDensity)
----                AND INDEXPROPERTY (ObjectId, IndexName, 'IndexDepth') > 0
--                AND IndexId = 1 
--                AND (LogicalFrag >= @MaxLogicalfrag
--                OR ScanDensity < @MaxScanDensity)
--        ORDER BY ObjectName, IndexId

-- Open the cursor
OPEN indexes

-- loop through the indexes
FETCH NEXT
   FROM indexes
   INTO @TableName, @TableSchema, @ObjectId, @IndexId, @IndexName, @LogicalFrag, @ScanDensity

--select @TableName, @TableSchema, @ObjectId, @IndexId, @IndexName, @LogicalFrag, @ScanDensity
--return


WHILE @@FETCH_STATUS = 0
BEGIN

        IF @IndexId = 1
        BEGIN

--           PRINT 'Executing DBCC DBREINDEX ('+ RTRIM(@TableSchema) + '.' + RTRIM(@TableName) + ') - fragmentation currently '
--                + RTRIM(CONVERT(varchar(15),@LogicalFrag)) + '% and Scan Density currently '
--                + RTRIM(CONVERT(VARCHAR(15), @ScanDensity))

          SELECT @execstr = 'USE ' + @DatabaseName + ' DBCC DBREINDEX (['+ RTRIM(@TableSchema) + '.' + RTRIM(@TableName) + '])'
--  		SELECT @execstr
			IF @Logging = 'Yes'
			BEGIN
				INSERT INTO [DBAUtility].[dbo].[INDEX_MAINT_HIST] (RUN_DT, SQL_TXT)
				SELECT GETDATE(), @execstr
			END 

          EXEC (@execstr)

        END

        IF @IndexId > 1

        BEGIN
--           PRINT 'Executing DBCC DBREINDEX ('+ RTRIM(@TableSchema) + '.' + RTRIM(@TableName) + ',' 
--                + RTRIM(@indexid) + ') - fragmentation currently '
--                + RTRIM(CONVERT(VARCHAR(15),@LogicalFrag)) + '% and Scan Density currently '
--                + RTRIM(CONVERT(VARCHAR(15), @ScanDensity))

          SELECT @execstr = 'USE ' + @DatabaseName + ' DBCC DBREINDEX (['+ RTRIM(@TableSchema) + '.'  + RTRIM(@TableName) + '],' + RTRIM(@IndexName) + ')'
--  		SELECT @execstr

			IF @Logging = 'Yes'
			BEGIN
				INSERT INTO [DBAUtility].[dbo].[INDEX_MAINT_HIST] (RUN_DT, SQL_TXT)
				SELECT GETDATE(), @execstr
			END 

          EXEC (@execstr)

        END

		--check how long the job has been running.  Do not run anymore if finishline crossed.
		IF GETDATE() > @FinishLine
		GOTO Crash

   FETCH NEXT
      FROM indexes
      INTO @TableName, @TableSchema, @ObjectId, @IndexId, @IndexName, @LogicalFrag, @ScanDensity

END

-- Close and deallocate the cursor

CLOSE indexes
DEALLOCATE indexes
END -- end of rebuild section



IF @Action = 'Defrag'
BEGIN -- start of Defrag section

-- Declare cursor for list of indexes to be defragged 
DECLARE indexes CURSOR FOR 
   SELECT f.ObjectName, f.ObjectId, f.IndexId, f.LogicalFrag 
   FROM #fraglist f JOIN #IndexProperty p ON (f.ObjectId = p.ObjectId AND f.IndexId = p.IndexId)
   WHERE f.LogicalFrag >= @MaxLogicalfrag
      --AND INDEXPROPERTY (ObjectId, IndexName, 'IndexDepth') > 0 
		AND p.IndexDepth > 0

-- Open the cursor 
OPEN indexes 

-- loop through the indexes 
FETCH NEXT FROM indexes INTO @TableName, @ObjectId, @IndexId, @LogicalFrag 

--select @tablename, @objectid, @indexid, @LogicalFrag 

WHILE @@FETCH_STATUS = 0 
BEGIN 

--   PRINT 'Executing DBCC INDEXDEFRAG (0, ' + RTRIM(@TableName) + ', 
--      ' + RTRIM(@IndexId) + ') - fragmentation currently ' 
--       + RTRIM(CONVERT(VARCHAR(15),@LogicalFrag)) + '%' 
   SELECT @execstr = 'USE ' + @DatabaseName + ' DBCC INDEXDEFRAG (0, ' + RTRIM(@ObjectId) + ', 
       ' + RTRIM(@IndexId) + ')' 
--	select    @execstr

		IF @Logging = 'Yes'
		BEGIN
			INSERT INTO [DBAUtility].[dbo].[INDEX_MAINT_HIST] (RUN_DT, SQL_TXT)
			SELECT GETDATE(), @execstr
		END 


	EXEC (@execstr) 

	--Track which tables to update statistics
	--Run update stats once per table
	UPDATE #tables SET UpdateStats = 1 WHERE TableName = @TableName

	--check how long the job has been running.  Do not run anymore if finishline crossed.
   IF GETDATE() > @FinishLine
   GOTO Crash

FETCH NEXT FROM indexes INTO @TableName, @ObjectId, @IndexId, @LogicalFrag 
END 

-- Close and deallocate the cursor 
CLOSE indexes 
DEALLOCATE indexes 

SET @TableName = NULL
SET @TableSchema = NULL
SET @execstr = NULL

--select * from #tables
---update statistics

DECLARE NewStats CURSOR FOR
   SELECT TableName, TableSchema
   FROM #tables
	WHERE UpdateStats = 1

-- Open the cursor
OPEN NewStats

-- Loop through all the tables in the database
FETCH NEXT FROM NewStats INTO @TableName, @TableSchema

WHILE @@FETCH_STATUS = 0
BEGIN --begin update stats loop

--   PRINT 'Executing UPDATE STATISTICS ON ' + RTRIM(@TableName) 
   SELECT @execstr = 'USE ' + @DatabaseName + ' UPDATE STATISTICS ' + @TableName
--	select    @execstr

		IF @Logging = 'Yes'
		BEGIN
			INSERT INTO [DBAUtility].[dbo].[INDEX_MAINT_HIST] (RUN_DT, SQL_TXT)
			SELECT GETDATE(), @execstr
		END 

	EXEC (@execstr) 

FETCH NEXT FROM NewStats INTO @TableName, @TableSchema
END --end update stats loop

CLOSE NewStats
DEALLOCATE NewStats

END -- end of Defrag section


-- Delete the temporary table 
DROP TABLE #fraglist 
DROP TABLE #IndexProperty
DROP TABLE #tables

RETURN 0

Crash:
	BEGIN	
		CLOSE indexes
		DEALLOCATE indexes
		RAISERROR('Rebuild index has taken longer than limit of run minutes: %d', 1, 2, @RunMinutes )  WITH LOG
		RETURN 99
	END
```

