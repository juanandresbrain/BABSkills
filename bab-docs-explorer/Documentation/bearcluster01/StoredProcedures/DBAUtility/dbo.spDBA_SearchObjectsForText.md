# dbo.spDBA_SearchObjectsForText

**Database:** DBAUtility  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_SearchObjectsForText"]
    dbo_mat(["dbo.mat"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.mat |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDBA_SearchObjectsForText] (
	@LinkedServer	NVARCHAR(128), -- leave empty or NULL if not using
	@DBName			NVARCHAR(128), -- which DB to search in (only one)
	@ObjectName		NVARCHAR(128) = NULL, -- object to search in (for ALL use: NULL, '', or '%')
	@Search			NVARCHAR(2000) = NULL, -- string to search for (for Just Display use: NULL, '', or '%')
	@Query			NVARCHAR(4000) = NULL, -- optional query to use instead of default that uses @Search
	@IncludeJobs	BIT = 1,
	@IgnoreComments	BIT = 1,
	@IgnoreStrings	BIT = 0,
	@Action VARCHAR(20) = 'Process'

)
AS
-- =============================================================================================================
-- Name: spDBA_SearchObjectsForText
--
--	Input:		@LinkedServer VARCHAR(256) -- optional (can be empty '' or NULL)
--				@DBName VARCHAR(256) -- the only required parameter
--				@Object VARCHAR(256)
--				@Search VARCHAR(1000)
--				@Query VARCHAR(8000)
--	Output:		depends on value of @Query
-- 
-- Available actions:
--@LinkedServer is optional and can be left as empty ''. If specified, it needs to be an exact LinkedServer name defined on your server. It cannot contain wildcards (% or _) and most likely should be enclosed in square-brackets ([ and ]) to avoid problems. 
--@DBName is required. It needs to be an exact database name on your server or on the LinkedServer. It cannot contain wildcards (% or _). 
--@ObjectName is optional and can be left as empty ''. If specified, the search will only look at objects with names that match the pattern. It can be an exact object name or it can include wildcards (% and _). Default = '%'. 
--@Search is optional and can be left as empty ''. If specified, the search will only return results that match the pattern. It can be an exact string or it can include wildcards (% and _). Default = '%'. 
--@Query is optional and can be left as empty ''. If specified, you have full access to the temp tables holding the search data so you can do custom queries. For example, you can create your own temp tables to hold the results of several searches before doing an analysis. The three tables are: 
--		#Matches ([DBId] INT NOT NULL, [ObjectId] INT NOT NULL, [LineNum] SMALLINT, [ObjectType] CHAR(2), [Code] NVARCHAR(4000)) 
--		#MatchesFiltered ([DBId] INT NOT NULL, [ObjectId] INT NOT NULL, [LineNum] SMALLINT, [ObjectType] CHAR(2), [CodeFiltered] NVARCHAR(4000)) -- only available if ignoring comments or strings 
--		#ObjectNames ([DBId] INT NOT NULL, [ObjectId] INT NOT NULL, [DBName] SYSNAME NOT NULL, [ObjectName] NVARCHAR(260) NOT NULL) 
--@IncludeJobs is optional. If set to 1 (true), it will search job steps as well as standard DB objects. Default = 1. 
--@IgnoreComments is optional. If set to 1 (true), it will remove all comments (both single-line and block comments) and put the filtered code into the #MatchesFiltered temp table. Default = 1. 
--@IgnoreStrings is optional. If set to 1 (true), it will remove all text within single-quotes (including the single-quotes) except for anything that is part of a comment. Keep in mind when using this option that Dynamic SQL will also be removed. Default = 0. 

--Display all code in a DB on the local server including Job Steps and ignoring comments:
--EXEC dbo.spSearchObjectsForText '', 'foundation'

--Display all code in a DB on another server NOT including Job Steps: */
--EXEC dbo.spSearchObjectsForText '[SomeServer\SomeInstance]', 'SQL#', '', '', '', 0

--Display all code containing a "string" on the local server: */
--EXEC DBAUtility.dbo.spSearchObjectsForText '', 'auditorks', '', '%GAAP%'

-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	08/12/2010		Created based on the article Searching Objects for Text (http://www.sqlservercentral.com/articles/Stored+Procedures/62975/)
--		Mike Pelikan	08/27/2012		Added versioning
-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '08/27/2012'

SET NOCOUNT ON
----------------------------------------------------------------------------------------------------
--// Revision                                                                                  //--
----------------------------------------------------------------------------------------------------
IF @Action = 'ReturnVersion'
BEGIN
	GOTO EndHere
END

BEGIN
	DECLARE	@CRLF				CHAR(2), -- line break
			@ObjectNum			INT,
			@DBId				INT,
			@ObjectId			INT,
			@Text				NVARCHAR(4000),
			@XType				CHAR(2),
			@Name				sysname,
			@ObjectIdOld		INT,
			@CurrentLineNum		SMALLINT,
			@TextStart			SMALLINT,
			@TextStop			SMALLINT,
			@TempText			NVARCHAR(4000),
			@Continue			BIT,
			@SQL				NVARCHAR(500),
			@LinkedServerName	sysname

	CREATE TABLE #Objects ([ObjectNum] INT IDENTITY(1,1) NOT NULL PRIMARY KEY, [DBId] INT NOT NULL,
		ObjectId INT NOT NULL, [XType] CHAR(2), [Text] NVARCHAR(4000), [ColId] SMALLINT NULL)

	-- not enough room left in #Objects after storing "text" NVARCHAR(4000) field
	CREATE TABLE #ObjectNames ([DBId] INT NOT NULL, [ObjectId] INT NOT NULL,
		[DBName] sysname NOT NULL, [ObjectName] NVARCHAR(260) NOT NULL)

	CREATE TABLE #Matches ([DBId] INT NOT NULL, [ObjectId] INT NOT NULL, [LineNum] SMALLINT,
		[ObjectType] CHAR(2), [Code] NVARCHAR(4000))

	CREATE TABLE #MatchesFiltered ([DBId] INT NOT NULL, [ObjectId] INT NOT NULL, [LineNum] SMALLINT,
		[ObjectType] CHAR(2), [CodeFiltered] NVARCHAR(4000))

	-- Initialize variables
	SET @CRLF = (CHAR(13) + CHAR(10))
	SET @LinkedServerName = ''

	IF (@ObjectName IS NULL OR RTRIM(@ObjectName) = '')
	BEGIN
		SET @ObjectName = '%'
	END

	IF ((@LinkedServer IS NOT NULL) AND (LTRIM(@LinkedServer) <> ''))
	BEGIN
		SET @LinkedServerName = @LinkedServer + '.'
	END


	-- Check to make sure the @DBName parameter is a real database
	-- and Get the ID of the database we are searching
	SET @SQL = 'SELECT @DBId = sd.dbid FROM '
	SET @SQL = @SQL + @LinkedServerName
	SET @SQL = @SQL + 'master.dbo.sysdatabases sd WHERE sd.name = @DBName'

	EXEC sp_executesql @SQL, N'@DBName sysname, @DBId INT OUTPUT', @DBName = @DBName, @DBId = @DBId OUTPUT

	IF (@DBId IS NULL)
	BEGIN
		RAISERROR('Invalid Database Name: %s%sPlease try again.%s', 16, 1, @SQL, @CRLF, @CRLF)
		RETURN
	END


	-- Check to make sure that if @Query was passed in that is contains the temp table "#Matches"
	-- to help prevent random (i.e. unrelated) queries from being passed in
	IF ((@Query IS NOT NULL) AND (RTRIM(@Query) <> '') AND ((@Query + ' ' NOT LIKE '% #Matches %') AND (@Query + ' ' NOT LIKE '% #MatchesFiltered %')))
	BEGIN
		RAISERROR('@Query MUST contain at least one reference to either the #Matches or #MatchesFiltered temp table.%s%s%s', 16, 1, @CRLF, @CRLF, @Query)
		RETURN
	END


	--Get all of the objects from the specified DB into a temp table
	INSERT
	INTO #Objects ([DBId], [ObjectId], [Text], [XType], [ColId])
		EXEC ('
			SELECT ' + @DBId + ', so.id AS ''ObjectId'', sc.text AS ''text'', so.xtype, sc.colid
			FROM ' + @LinkedServerName + @DBName + '.dbo.syscomments sc --WITH (NOLOCK)
			INNER JOIN ' + @LinkedServerName + @DBName + '.dbo.sysobjects so --WITH (NOLOCK)
			ON so.id = sc.id
			AND so.name LIKE ''' + @ObjectName + '''
			WHERE sc.encrypted = 0
			AND so.xtype NOT IN (''S'', ''X'')
			ORDER BY so.xtype, so.id, sc.number, sc.colid')


	-- get column info
	INSERT
	INTO #Objects ([DBId], [ObjectId], [Text], [XType], [ColId])
		EXEC ('
			SELECT ' + @DBId + ' AS ''DBId'', sc.id AS ''ObjectId'', sc.name + CHAR(13) + CHAR(10) AS ''Text'', so.xtype, sc.colid
			FROM ' + @LinkedServerName + @DBName + '.dbo.syscolumns sc
			INNER JOIN ' + @LinkedServerName + @DBName + '.dbo.sysobjects so
			ON so.id = sc.id
			AND so.name LIKE ''' + @ObjectName + '''
			AND so.xtype = ''U''
--			AND sc.name LIKE ''' + @ObjectName + '''
			ORDER BY so.id, sc.colid')


	-- store the names of the objects
	INSERT
	INTO #ObjectNames ([DBId], [ObjectId], [DBName], [ObjectName])
		EXEC ('
			SELECT DISTINCT ' + @DBId + ', obj.ObjectId, ''' + @DBName + ''', so.name
			FROM ' + @LinkedServerName + @DBName + '.dbo.sysobjects so --WITH (NOLOCK)
			INNER JOIN #Objects obj
			ON obj.ObjectId = so.id')




	IF (@IncludeJobs = 1)
	BEGIN
		INSERT
		INTO #Objects ([DBId], [ObjectId], [Text], [XType], [ColId])
			EXEC ('
					SELECT sd.dbid, ((CONVERT(INT, CONVERT(VARBINARY(50), LEFT(CONVERT(VARCHAR(36), sj.job_id), 3))) * 100) + sjs.step_id) AS ''ObjectId'', command AS ''Text'', ''JS'' AS ''XType'', 1 AS ''ColId''
					FROM '  + @LinkedServerName + 'msdb.dbo.sysjobs sj
					INNER JOIN ' + @LinkedServerName + 'msdb.dbo.sysjobsteps sjs
							ON sjs.job_id = sj.job_id
					INNER JOIN ' + @LinkedServerName + 'master.dbo.sysdatabases sd
							ON sd.[name] = ''msdb''
							AND sj.name LIKE ''' + @ObjectName + '''
					ORDER BY sj.name, sjs.step_id
				')

		INSERT
		INTO #ObjectNames ([DBId], [ObjectId], [DBName], [ObjectName])
			EXEC ('
					SELECT DISTINCT sd.dbid, ((CONVERT(INT, CONVERT(VARBINARY(50), LEFT(CONVERT(VARCHAR(36), sj.job_id), 3))) * 100) + sjs.step_id) AS ''ObjectId'', sd.name AS ''DBName'', sj.name + '' :: '' + sjs.step_name AS ''ObjectName''
					FROM '  + @LinkedServerName + 'msdb.dbo.sysjobs sj
					INNER JOIN ' + @LinkedServerName + 'msdb.dbo.sysjobsteps sjs
							ON sjs.job_id = sj.job_id
					INNER JOIN ' + @LinkedServerName + 'master.dbo.sysdatabases sd
							ON sd.[name] = ''msdb''
							AND sj.name LIKE ''' + @ObjectName + '''
--					ORDER BY sj.name, sjs.step_id
				') 
	END

	SET @ObjectIdOld = -1

	--Use a cursor to step through the objects so we can reconstrunct them
	DECLARE crsObjects CURSOR LOCAL FAST_FORWARD
	FOR		SELECT		obj.[DBId], obj.[ObjectId], obj.[Text], obj.XType
			FROM		#Objects obj
			ORDER BY	obj.[ObjectId], obj.[ColId]

	OPEN crsObjects

	FETCH	NEXT
	FROM	crsObjects
	INTO	@DBId, @ObjectId, @Text, @XType

	WHILE (@@FETCH_STATUS = 0)
	BEGIN
		SET @TextStart = 1 -- initialize the value
		SET @TextStop = 1 -- set this to anything NOT zero just to get the WHILE loop started

		IF (@ObjectId <> @ObjectIdOld)
		BEGIN
			SET @ObjectIdOld = @ObjectId
			SET @CurrentLineNum = 0
			SET @Continue = 0 -- do NOT continue; start a new line
		END

		WHILE @TextStop <> 0
		BEGIN
			SET @TextStop = CHARINDEX(@CRLF, @Text, @TextStart)

			IF @TextStop > 0
			BEGIN
				SET @TempText = SUBSTRING(@Text, @TextStart, (@TextStop - @TextStart)) -- get from the start until the character BEFORE the CRLF
			END
			ELSE
			BEGIN
				SET @TempText = SUBSTRING(@Text, @TextStart, DATALENGTH(@Text)) -- get from the start until the end of the string
			END
			--print '[' + @Name + ' / ' + @NameOld + '] ' + convert(varchar, @textstart) + ' - ' + convert(varchar, @textstop) + ': ' + CONVERT(VARCHAR, @Continue) + ': ' + @TempText

			IF @Continue = 0
			BEGIN
				SET @CurrentLineNum = @CurrentLineNum + 1

				INSERT
				INTO	#Matches ([DBId], [ObjectId], LineNum, Code, ObjectType)
				VALUES	(@DBId, @ObjectId, @CurrentLineNum, @TempText, @XType)
			END
			ELSE
			BEGIN
				UPDATE	mat
				SET		mat.Code = mat.Code + @TempText
				FROM	#Matches mat
				WHERE	mat.[DBId] = @DBId
				AND		mat.[ObjectId] = @ObjectId
				AND		mat.[LineNum] = @CurrentLineNum
			END


			IF @TextStop > 0
			BEGIN
				SET @Continue = 0 -- do NOT continue; start a new line
				SET @TextStart = (@TextStop + 2) -- skip the CRLF to start at the next real char
			END
			ELSE
			BEGIN
				SET @Continue = 1 -- continue this line with the next one; do NOT start a new line for the next record
			END
		END -- WHILE

		FETCH	NEXT
		FROM	crsObjects
		INTO	@DBId, @ObjectId, @Text, @XType
	END

	-- Clean Up
	CLOSE crsObjects
	DEALLOCATE crsObjects
	DELETE FROM #Objects -- future use if multiple DB search capability is added to this proc

	-- clean up Column info that leaves an extraneous empty line
	DELETE	mat
	FROM	#Matches mat
	WHERE	mat.ObjectType = 'U'
	AND		mat.Code = ''

	-- Now output the matching rows
	IF (@Search IS NULL OR RTRIM(@Search) = '')
	BEGIN
		SET @Search = '%'
	END


	-- if @Search = something, IGNORE quotes / string; if @Search is empty, remove quotes / strings
	IF (@IgnoreComments = 1 OR @IgnoreStrings = 1)
	BEGIN
		-- Flags to help indicate how to handle the row or a series of rows
		DECLARE @CommentBlockFlag BIT
		DECLARE @StringLiteralFlag BIT

		SET @CommentBlockFlag = 0
		SET @StringLiteralFlag = 0

		-- Indexes to keep position on the line itself
		DECLARE @StopIndex SMALLINT
		DECLARE @WhereCommentBlock SMALLINT
		DECLARE @WhereInlineComment SMALLINT
		DECLARE @WhereStringLiteral SMALLINT

		SET @StopIndex = 0
		SET @WhereCommentBlock = 0
		SET @WhereInlineComment = 0
		SET @WhereStringLiteral = 0

		-- Temporary holder of the updated line
		DECLARE @TempLine NVARCHAR(4000)
		DECLARE @FixedLine NVARCHAR(4000)
		DECLARE @LineSegment NVARCHAR(4000)

		SET @LineSegment = ''


		DECLARE crsMatches CURSOR LOCAL FAST_FORWARD
		FOR		SELECT		obj.[DBId], obj.[ObjectId], obj.[LineNum], obj.[ObjectType], obj.[Code]
				FROM		#Matches obj
				ORDER BY	obj.[DBId], obj.[ObjectId], obj.[LineNum]

		OPEN crsMatches

		FETCH	NEXT
		FROM	crsMatches
		INTO	@DBId, @ObjectId, @CurrentLineNum, @XType, @TempLine

		-- Repeat section for each line of code / text
		WHILE (@@FETCH_STATUS = 0)
		BEGIN
			SET @FixedLine = ''

			WHILE (LEN(@TempLine) > 0)
			BEGIN
				SET @StopIndex = 0
				SET @LineSegment = ''

				IF (@IgnoreComments = 1)
				BEGIN
					SET @WhereCommentBlock = PATINDEX('%/*%', @TempLine)
					SET @WhereInlineComment = PATINDEX('%--%', @TempLine)
				END

				IF (@IgnoreStrings = 1)
				BEGIN
					SET @WhereStringLiteral = PATINDEX('%''%', @TempLine)
--					@WhereStringLiteral = match(@TempLine, /(^|[^'])'([^']|$)/)
				END

				IF (@CommentBlockFlag = 1)
				BEGIN	---- We are in a Comment Block
					SET @StopIndex = PATINDEX('%*/%', @TempLine)

					IF (@StopIndex > 0)
					BEGIN	---- The Comment Block ends in this line
						SET @CommentBlockFlag = 0
						SET @StopIndex = @StopIndex + 1	-- take an additional character since */ is two chars yet the match catches the first
						
						SET @TempLine = SUBSTRING(@TempLine, (@StopIndex + 1), 4000)
						CONTINUE	-- line might not be over so continue the While loop
					END
					ELSE
					BEGIN	-- The Comment Block does NOT end so take the rest of the line
						BREAK	-- line is over so just exit the loop
					END
				END

				IF (@StringLiteralFlag = 1)
				BEGIN	-- We are in a String Literal
					IF (@WhereStringLiteral > 0)
					BEGIN	-- The String Literal ends in this line
						IF (SUBSTRING(@TempLine, @WhereStringLiteral, 1) <> '''')
						BEGIN
							SET @WhereStringLiteral = @WhereStringLiteral + 1
						END

						SET @StringLiteralFlag = 0
						SET @TempLine = SUBSTRING(@TempLine, (@WhereStringLiteral + 1), 4000)
						CONTINUE	-- line might not be over so continue the While loop
					END
					ELSE
					BEGIN	-- The String does NOT end
						BREAK	-- line is over so just exit the loop
					END
				END

				IF (@WhereInlineComment > 0 AND (@WhereCommentBlock = 0 OR @WhereInlineComment < @WhereCommentBlock) AND (@WhereStringLiteral = 0 OR @WhereInlineComment < @WhereStringLiteral))
				BEGIN  -- There is an Inline comment on this line
					IF (@WhereInlineComment = 1)
					BEGIN	-- The Inline Comment is the entire line
						BREAK	-- line is over so just exit the loop
					END
					ELSE
					BEGIN	-- We have an Inline comment somewhere in the line
						SET @LineSegment = SUBSTRING(@TempLine, 1, (@WhereInlineComment - 1))
						SET @FixedLine = @FixedLine + @LineSegment	-- Append the LineSegment to the existing FixedLine
						BREAK	-- line is over so just exit the loop
					END
				END
				
				
				IF (@WhereCommentBlock > 0 AND (@WhereStringLiteral = 0 OR @WhereCommentBlock < @WhereStringLiteral))
				BEGIN
					-- There is a Block Comment on this line
					SET @CommentBlockFlag = 1
					IF (@WhereCommentBlock = 1)
					BEGIN	-- The Comment Block starts the line so there is nothing to the left to process
						SET @TempLine = SUBSTRING(@TempLine, 3, 4000)	-- skip the /*
						CONTINUE	---- line might not be over so continue the While loop
					END
					ELSE
					BEGIN	-- We have a comment block somewhere in the line
						SET @LineSegment = SUBSTRING(@TempLine, 1, (@WhereCommentBlock - 1))	-- Grab from beginning to char BEFORE the / *
						SET @TempLine = SUBSTRING(@TempLine, (@WhereCommentBlock + 2), 4000)	-- Grab from char AFTER the / * to end of line
						
						SET @FixedLine = @FixedLine + @LineSegment	-- Append the LineSegment to the existing FixedLine
						CONTINUE	-- line might not be over so continue the While loop
					END
				END

				
				IF (@WhereStringLiteral > 0)
				BEGIN
					-- There is a String Literal on this line
					SET @StringLiteralFlag = 1
					IF (SUBSTRING(@TempLine, @WhereStringLiteral, 1) <> '''')
					BEGIN
						SET @WhereStringLiteral = @WhereStringLiteral + 1
					END
					
					IF (@WhereStringLiteral = 1)
					BEGIN	-- The String Literal starts the line so there is nothing to the left to process
--						SET @FixedLine = @FixedLine + ''''
						SET @TempLine = SUBSTRING(@TempLine, 2, 4000)	-- skip the '
						CONTINUE	---- line might not be over so continue the While loop
					END
					ELSE
					BEGIN	-- We have a String Literal somewhere in the line
						SET @LineSegment = SUBSTRING(@TempLine, 1, (@WhereStringLiteral - 1))	-- Grab from beginning to char BEFORE the '
						SET @TempLine = SUBSTRING(@TempLine, (@WhereStringLiteral + 1), 4000)	-- Grab from char AFTER the ' to end of line
						
						SET @FixedLine = @FixedLine + @LineSegment-- + ''''	-- Append the updated LineSegment to the existing FixedLine
						CONTINUE	-- line might not be over so continue the While loop
					END
				END

				SET @FixedLine = @FixedLine + @TempLine	-- Append the TempLine to the existing FixedLine
				BREAK	-- since there are no BlockComments, InlineComments, or StringLiterals left, the entire line has been processed so exit the loop
			END

			INSERT
			INTO	#MatchesFiltered ([DBId], [ObjectId], [LineNum], [ObjectType], [CodeFiltered])
			VALUES	(@DBId, @ObjectId, @CurrentLineNum, @XType, @FixedLine)

			FETCH	NEXT
			FROM	crsMatches
			INTO	@DBId, @ObjectId, @CurrentLineNum, @XType, @TempLine

		END /* WHILE (@@FETCH_STATUS) */

	CLOSE crsMatches
	DEALLOCATE crsMatches

	END /* IF (Ignore vars) */




	IF (@Query IS NULL OR RTRIM(@Query) = '')
	BEGIN
		IF (@IgnoreComments = 1 OR @IgnoreStrings = 1)
		BEGIN
			SELECT		mat.LineNum, mat.Code, objnm.DBName, objnm.ObjectName, mat.ObjectType, fltr.CodeFiltered
			FROM		#Matches mat
			INNER JOIN	#ObjectNames objnm
					ON	objnm.[DBId] = mat.[DBId]
					AND	objnm.[ObjectId] = mat.[ObjectId]
			INNER JOIN	#MatchesFiltered fltr
					ON	fltr.[DBId] = mat.[DBId]
					AND	fltr.[ObjectId] = mat.[ObjectId]
					AND	fltr.[LineNum] = mat.[LineNum]
			WHERE		fltr.CodeFiltered LIKE @Search
			ORDER BY	objnm.DBName, mat.ObjectType, objnm.ObjectName, mat.LineNum
		END
		ELSE
		BEGIN
			SELECT		mat.LineNum, mat.Code, objnm.DBName, objnm.ObjectName, mat.ObjectType, CONVERT(NVARCHAR(4000), N'') AS 'CodeFiltered'
			FROM		#Matches mat
			INNER JOIN	#ObjectNames objnm
					ON	objnm.[DBId] = mat.[DBId]
					AND	objnm.[ObjectId] = mat.[ObjectId]
			WHERE	mat.Code LIKE @Search
			ORDER BY	objnm.DBName, mat.ObjectType, objnm.ObjectName, mat.LineNum
		END
	END
	ELSE
	BEGIN
		DELETE	mat
		FROM	#Matches mat
		WHERE	mat.Code NOT LIKE @Search

		DELETE	mat
		FROM	#MatchesFiltered mat
		WHERE	mat.CodeFiltered NOT LIKE @Search

		EXEC (@Query)
	END
END

EndHere:
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END

dbo,spDBA_SearchThroughAllCode,CREATE PROCEDURE [dbo].[spDBA_SearchThroughAllCode]
	@SearchStringIn varchar(255),
	@Action VARCHAR(20) = 'Process'
AS
-- =============================================================================================================
-- Name: spDBA_SearchThroughAllCode
--
--	Input:		@SearchStringIn VARCHAR(255)
--	Output:		search results
-- 
-- Available actions:
--@SearchStringIn -the search will only return results that match the pattern. It can be an exact string or it can include wildcards (% and _). Default = '%'. 

-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Mike Pelikan	08/27/2012		Added versioning
-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '08/27/2012'

SET NOCOUNT ON
----------------------------------------------------------------------------------------------------
--// Revision                                                                                  //--
----------------------------------------------------------------------------------------------------
IF @Action = 'ReturnVersion'
BEGIN
	GOTO EndHere
END

BEGIN
  DECLARE @SQL VARCHAR(2000)

  SET @SQL = 'USE ?; 
  SELECT ''?'' AS DATABASE_NAME, 
    sys.schemas.name AS [Schema Name],
    sys.objects.name AS [Object Name] ,
    type_desc AS [Object Type],
    substring(definition,CHARINDEX(''' + @SearchStringIn + ''',
      definition)-30, 60)
    AS [Text Context]
  FROM sys.objects
  JOIN sys.sql_modules
    ON sys.objects.object_id = sys.sql_modules.object_id
  JOIN sys.schemas
    ON sys.objects.schema_id = sys.schemas.schema_id
  WHERE CHARINDEX(''' + @SearchStringIn + ''',definition)>0'

  CREATE TABLE #SEARCH_RESULTS
   ( DATABASE_NAME NVARCHAR(128),
    [SCHEMA_NAME] VARCHAR(128),
    [OBJECT_NAME] VARCHAR(128),
    [OBJECT_TYPE] VARCHAR(20),
    TEXT_CONTEXT VARCHAR(60) )
    
  INSERT INTO #SEARCH_RESULTS EXEC sp_MSforeachdb @SQL
 

  SELECT * FROM #SEARCH_RESULTS
  ORDER BY DATABASE_NAME, [SCHEMA_NAME], [OBJECT_NAME]

END

EndHere:
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END

dbo,spDBA_SecurityReport,CREATE PROCEDURE [dbo].[spDBA_SecurityReport]
	@Databases nvarchar(2000)= 'SYSTEM_DATABASES, USER_DATABASES', 
	@bolOutputToTable BIT = 0,
	@Action VARCHAR(20) = 'Process'
AS
-- =============================================================================================================
-- Name: spDBA_SecurityReport
--
-- Description:	Reports objects and permissions that have been explicitly granted.
--  If a user has permissions on a object via sysadmin, the user will not be listed.
--
-- Output: error logging.
-- 
-- Available actions:
--	@Databases:
--	E.g. SYSTEM_DATABASES
--	E.g. USER_DATABASES
--	E.g. Database1
--	E.g. Database1, Database2
--	E.g. USER_DATABASES, master
--	E.g. SYSTEM_DATABASES, -master
--	E.g. %Database%
--	E.g. %Database%, -Database1
--
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	07/20/2009		Create initial version
--		Gary Derikito	07/23/2009		Added 3 part naming to remaining tables.
--		Mike Pelikan	02/23/2012		Added output to reporting table logic
--		Mike Pelikan	06/27/2012		Modified for versioning
--										Added Comments

-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '06/27/2012'

/*
exec spDBA_SecurityReport @Databases = DBAUtility
exec spDBA_SecurityReport @Databases = 'SYSTEM_DATABASES, USER_DATABASES'

*/
-- =============================================================================================================

----------------------------------------------------------------------------------------------------
--// Set options                                                                                //--
----------------------------------------------------------------------------------------------------
SET NOCOUNT ON

----------------------------------------------------------------------------------------------------
--// Revision                                                                                  //--
----------------------------------------------------------------------------------------------------
IF @Action = 'ReturnVersion'
BEGIN
	GOTO EndHere
END

----------------------------------------------------------------------------------------------------
--// Declare variables                                                                          //--
----------------------------------------------------------------------------------------------------

--  DECLARE @StartMessage nvarchar(max)
  DECLARE @EndMessage nvarchar(2000)
  DECLARE @DatabaseMessage nvarchar(2000)
  DECLARE @ErrorMessage nvarchar(2000)
  DECLARE @CurrentID int
  DECLARE @CurrentDatabase nvarchar(2000)
  DECLARE @CurrentTable nvarchar(2000)
  DECLARE @CurrentSchema nvarchar(128)
  DECLARE @CurrentCommand01 nvarchar(2000)
  DECLARE @CurrentCommandOutput01 int
  DECLARE @CreateDate datetime
  DECLARE @CurrentDate CHAR(8)
  DECLARE @tmpDatabases TABLE (ID int IDENTITY PRIMARY KEY,
                               DatabaseName nvarchar(2000),
                               Completed bit)

  DECLARE @Error int
  DECLARE @RowCount int
  DECLARE @ProductVersion	NVARCHAR(20) 
  DECLARE @SQL nvarchar(1000)
 
  SET @Error = 0
  SET @ProductVersion =  CAST(SERVERPROPERTY('productversion') AS VARCHAR)
  SET @CurrentDate = CONVERT(CHAR(8), GETDATE(), 112)


  IF object_id('tempdb..#ObjectSecurity') IS NOT NULL
	DROP TABLE #ObjectSecurity

  CREATE TABLE #ObjectSecurity (pk int IDENTITY PRIMARY KEY,
								dbname nvarchar(128),
                               username nvarchar(128),
                               gid smallint,
								objectname nvarchar(128),
								type char(2),
								id int,
								s varchar(15),
								i varchar(15),
								u varchar(15),
								d varchar(15),
								e varchar(15))
  
  ----------------------------------------------------------------------------------------------------
  --// Log initial information                                                                    //--
  ----------------------------------------------------------------------------------------------------

--  SET @StartMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Server: ' + CAST(SERVERPROPERTY('ServerName') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Version: ' + CAST(SERVERPROPERTY('ProductVersion') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Edition: ' + CAST(SERVERPROPERTY('Edition') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Procedure: ' + QUOTENAME(DB_NAME(DB_ID())) + '.' + QUOTENAME(OBJECT_SCHEMA_NAME(@@PROCID)) + '.' + QUOTENAME(OBJECT_NAME(@@PROCID)) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Parameters: @Databases = ' + ISNULL('''' + REPLACE(@Databases,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + ', @PhysicalOnly = ' + ISNULL('''' + REPLACE(@PhysicalOnly,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + ', @NoIndex = ' + ISNULL('''' + REPLACE(@NoIndex,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + CHAR(13) + CHAR(10)
--  SET @StartMessage = REPLACE(@StartMessage,'%','%%')
--  RAISERROR(@StartMessage,10,1) WITH NOWAIT

  ----------------------------------------------------------------------------------------------------
  --// Select databases                                                                           //--
  ----------------------------------------------------------------------------------------------------

  IF @Databases IS NULL OR @Databases = ''
  BEGIN
    SET @ErrorMessage = 'The value for parameter @Databases is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END


  IF SUBSTRING(@ProductVersion, 1, 1) = '8' --2000
	BEGIN
		INSERT INTO @tmpDatabases (DatabaseName, Completed)
		SELECT DatabaseName AS DatabaseName, 0 AS Completed
		FROM dbo.fnDBA_DatabaseSelect2000 (@Databases)
		ORDER BY DatabaseName ASC
		SET @RowCount = @@RowCount
	END
	ELSE --2005
	BEGIN
		INSERT INTO @tmpDatabases (DatabaseName, Completed)
		SELECT DatabaseName AS DatabaseName, 0 AS Completed
		FROM dbo.fnDBA_DatabaseSelect (@Databases)
		ORDER BY DatabaseName ASC
		SET @RowCount = @@RowCount
	END

  IF @@ERROR <> 0 OR (@RowCount = 0 AND @Databases <> 'USER_DATABASES')
  BEGIN
    SET @ErrorMessage = 'Error selecting databases.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END

  ----------------------------------------------------------------------------------------------------
  --// Check input parameters                                                                     //--
  ----------------------------------------------------------------------------------------------------

  
  ----------------------------------------------------------------------------------------------------
  --// Check error variable                                                                       //--
  ----------------------------------------------------------------------------------------------------

  IF @Error <> 0 GOTO Crash

  ----------------------------------------------------------------------------------------------------
  --// Execute commands                                                                           //--
  ----------------------------------------------------------------------------------------------------

  WHILE EXISTS (SELECT * FROM @tmpDatabases WHERE Completed = 0)
  BEGIN --loop through databases

--select * from @tmpDatabases return

    SELECT TOP 1 @CurrentID = ID,
                 @CurrentDatabase = DatabaseName
    FROM @tmpDatabases
    WHERE Completed = 0
    ORDER BY ID ASC


    -- Set database message
    SET @DatabaseMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = @DatabaseMessage + 'Database: ' + QUOTENAME(@CurrentDatabase) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = @DatabaseMessage + 'Status: ' + CAST(DATABASEPROPERTYEX(@CurrentDatabase,'status') AS nvarchar) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = REPLACE(@DatabaseMessage,'%','%%')
--    RAISERROR(@DatabaseMessage,10,1) WITH NOWAIT

    IF DATABASEPROPERTYEX(@CurrentDatabase,'status') = 'ONLINE'
    BEGIN

		INSERT INTO #ObjectSecurity(dbname, username, gid, objectname, type, id, s, i, u, d, e)
		EXEC(

				'select ' + '''' + @CurrentDatabase + '''' + ',sysusers_0.name as username,
				sysusers_0.gid,
				sysobjects_0.name as objectname, type,
				sysobjects_0.id,
				CASE WHEN sysprotects_1.action is null
					 THEN CASE WHEN sysobjects_0.xtype = '''+ 'P' + ''' THEN ''' + 'N/A' + '''
							   ELSE ' + '''' + 'No' + ''''
						  + ' END'
					 + ' ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'SELECT' + '''' + ',
				CASE WHEN sysprotects_2.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'P' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END 
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'INSERT' + '''' + ',
				CASE WHEN sysprotects_3.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'P' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END 
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'UPDATE' + '''' + ',
				CASE WHEN sysprotects_4.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'P' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'DELETE' + '''' + ',
				CASE WHEN sysprotects_5.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'U' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'EXECUTE' + ''''
		+ ' from [' + @CurrentDatabase + '].dbo.sysusers sysusers_0
				full join [' + @CurrentDatabase + '].dbo.sysobjects sysobjects_0 on ( sysobjects_0.xtype in ( '  + '''' + 'P' + '''' + ', ' + '''' + 'U' + '''' + ')
										  and sysobjects_0.name NOT LIKE ' + '''' + 'dt%' + ''''
										+ ')
				left join [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_1 on sysprotects_1.uid = sysusers_0.uid
														  and sysprotects_1.id = sysobjects_0.id
														  and sysprotects_1.action = 193
														  and sysprotects_1.protecttype in (
														  204, 205 )
				left join [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_2 on sysprotects_2.uid = sysusers_0.uid
														  and sysprotects_2.id = sysobjects_0.id
														  and sysprotects_2.action = 195
														  and sysprotects_2.protecttype in (
														  204, 205 )
				left join  [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_3 on sysprotects_3.uid = sysusers_0.uid
														  and sysprotects_3.id = sysobjects_0.id
														  and sysprotects_3.action = 197
														  and sysprotects_3.protecttype in (
														  204, 205 )
				left join  [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_4 on sysprotects_4.uid = sysusers_0.uid
														  and sysprotects_4.id = sysobjects_0.id
														  and sysprotects_4.action = 196
														  and sysprotects_4.protecttype in (
														  204, 205 )
				left join  [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_5 on sysprotects_5.uid = sysusers_0.uid
														  and sysprotects_5.id = sysobjects_0.id
														  and sysprotects_5.action = 224
														  and sysprotects_5.protecttype in (
														  204, 205 )
		where   ( sysprotects_1.action is not null
				  or sysprotects_2.action is not null
				  or sysprotects_3.action is not null
				  or sysprotects_4.action is not null
				  or sysprotects_5.action is not null
				)
		order by sysusers_0.name,
				sysobjects_0.name'
			)


	END


	-- Update that the database is completed
    UPDATE @tmpDatabases
    SET Completed = 1
    WHERE ID = @CurrentID

    -- Clear variables
    SET @CurrentID = NULL
    SET @CurrentDatabase = NULL

    SET @CurrentCommand01 = NULL

    SET @CurrentCommandOutput01 = NULL
 
	
  END--loop through databases end

  --return the results
  IF @bolOutputToTable = 0 
	  SELECT dbname, username, gid, objectname, type, id, s AS 'SELECT', i AS 'INSERT', u AS 'UPDATE', d AS 'DELETE', e AS 'EXECUTE' 
	  FROM #ObjectSecurity 
	  ORDER BY dbname, objectname, id
  ELSE
	  INSERT INTO COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_SecurityReport (InstanceName, DatabaseName, UserName, gid, ObjectName, ObjectType, ObjectID, [SELECT], [INSERT], [UPDATE], [DELETE], [EXECUTE])
	  SELECT @@ServerName InstanceName, dbname DatabaseName, username UserName, gid, objectname ObjectName, type ObjectType, id ObjectID, s AS 'SELECT', i AS 'INSERT', u AS 'UPDATE', d AS 'DELETE', e AS 'EXECUTE' 
	  FROM #ObjectSecurity 
	  ORDER BY dbname, objectname, id
		 
  RETURN 0


  ----------------------------------------------------------------------------------------------------
  --// Log completing information                                                                 //--
  ----------------------------------------------------------------------------------------------------

  Crash:
  SET @EndMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + ' Error with ' + OBJECT_NAME(@@PROCID)
  SET @EndMessage = REPLACE(@EndMessage,'%','%%')
  RAISERROR(@EndMessage,10,1) WITH Log

  ----------------------------------------------------------------------------------------------------
EndHere:
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END


dbo,spDBA_SecurityReport_DBRoleMembers,CREATE PROCEDURE [dbo].[spDBA_SecurityReport_DBRoleMembers] 
	@Databases nvarchar(2000) = 'SYSTEM_DATABASES, USER_DATABASES', 
	@bolOutputToTable BIT = 0,
	@Action VARCHAR(20) = 'Process'
AS
-- =============================================================================================================
-- Name: spDBA_SecurityReport_DBRoleMembers
--
-- Description:	Returns database role membership.  Null membership indicates a role has no members.
--
-- Output: error logging.
-- 
-- Available actions:
--	@Databases:
--	E.g. SYSTEM_DATABASES
--	E.g. USER_DATABASES
--	E.g. Database1
--	E.g. Database1, Database2
--	E.g. USER_DATABASES, master
--	E.g. SYSTEM_DATABASES, -master
--	E.g. %Database%
--	E.g. %Database%, -Database1
--
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	07/20/2009		Create initial version
--		Gary Derikito	07/23/2009		Added 3 part naming to remaining tables.
--		Mike Pelikan	02/23/2012		Changed Logic to write to consolidated server reporting table
--		Mike Pelikan	06/27/2012		Modified for versioning
--										Added Comments
--
-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '06/27/2012'

/*
exec spDBA_SecurityReport_DBRoleMembers @Databases = DBAUtility
exec spDBA_SecurityReport_DBRoleMembers @Databases = 'SYSTEM_DATABASES, USER_DATABASES'

*/
-- =============================================================================================================

----------------------------------------------------------------------------------------------------
--// Set options                                                                                //--
----------------------------------------------------------------------------------------------------
SET NOCOUNT ON

----------------------------------------------------------------------------------------------------
--// Revision                                                                                  //--
----------------------------------------------------------------------------------------------------
IF @Action = 'ReturnVersion'
BEGIN
	GOTO EndHere
END

----------------------------------------------------------------------------------------------------
--// Declare variables                                                                          //--
----------------------------------------------------------------------------------------------------

--  DECLARE @StartMessage nvarchar(max)
  DECLARE @EndMessage nvarchar(2000)
  DECLARE @DatabaseMessage nvarchar(2000)
  DECLARE @ErrorMessage nvarchar(2000)
  DECLARE @CurrentID int
  DECLARE @CurrentDatabase nvarchar(2000)
  DECLARE @CurrentTable nvarchar(2000)
  DECLARE @CurrentSchema nvarchar(128)
  DECLARE @CurrentCommand01 nvarchar(2000)
  DECLARE @CurrentCommandOutput01 int
  DECLARE @CreateDate datetime
  DECLARE @CurrentDate CHAR(8)
  DECLARE @tmpDatabases TABLE (ID int IDENTITY PRIMARY KEY,
                               DatabaseName nvarchar(2000),
                               Completed bit)

  DECLARE @Error int
  DECLARE @RowCount int
  DECLARE @ProductVersion	NVARCHAR(20) 
  DECLARE @SQL nvarchar(1000)
 
  SET @Error = 0
  SET @ProductVersion =  CAST(SERVERPROPERTY('productversion') AS VARCHAR)
  SET @CurrentDate = CONVERT(CHAR(8), GETDATE(), 112)


  IF object_id('tempdb..#RoleMembers') IS NOT NULL
	DROP TABLE #RoleMembers

  CREATE TABLE #RoleMembers (pk int IDENTITY PRIMARY KEY,
								dbname nvarchar(128),
								dbrolename nvarchar(128),
                               membername nvarchar(128),
                               membersid nvarchar(128))
  
  ----------------------------------------------------------------------------------------------------
  --// Log initial information                                                                    //--
  ----------------------------------------------------------------------------------------------------

--  SET @StartMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Server: ' + CAST(SERVERPROPERTY('ServerName') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Version: ' + CAST(SERVERPROPERTY('ProductVersion') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Edition: ' + CAST(SERVERPROPERTY('Edition') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Procedure: ' + QUOTENAME(DB_NAME(DB_ID())) + '.' + QUOTENAME(OBJECT_SCHEMA_NAME(@@PROCID)) + '.' + QUOTENAME(OBJECT_NAME(@@PROCID)) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Parameters: @Databases = ' + ISNULL('''' + REPLACE(@Databases,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + ', @PhysicalOnly = ' + ISNULL('''' + REPLACE(@PhysicalOnly,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + ', @NoIndex = ' + ISNULL('''' + REPLACE(@NoIndex,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + CHAR(13) + CHAR(10)
--  SET @StartMessage = REPLACE(@StartMessage,'%','%%')
--  RAISERROR(@StartMessage,10,1) WITH NOWAIT

  ----------------------------------------------------------------------------------------------------
  --// Select databases                                                                           //--
  ----------------------------------------------------------------------------------------------------

  IF @Databases IS NULL OR @Databases = ''
  BEGIN
    SET @ErrorMessage = 'The value for parameter @Databases is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END


  IF SUBSTRING(@ProductVersion, 1, 1) = '8' --2000
	BEGIN
		INSERT INTO @tmpDatabases (DatabaseName, Completed)
		SELECT DatabaseName AS DatabaseName, 0 AS Completed
		FROM dbo.fnDBA_DatabaseSelect2000 (@Databases)
		ORDER BY DatabaseName ASC
		SET @RowCount = @@RowCount
	END
	ELSE --2005
	BEGIN
		--GOTO Crash---comment out because VS is checking for existence of object
		INSERT INTO @tmpDatabases (DatabaseName, Completed)
		SELECT DatabaseName AS DatabaseName, 0 AS Completed
		FROM dbo.fnDBA_DatabaseSelect (@Databases)
		ORDER BY DatabaseName ASC
		SET @RowCount = @@RowCount
	END

  IF @@ERROR <> 0 OR (@RowCount = 0 AND @Databases <> 'USER_DATABASES')
  BEGIN
    SET @ErrorMessage = 'Error selecting databases.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END

  ----------------------------------------------------------------------------------------------------
  --// Check input parameters                                                                     //--
  ----------------------------------------------------------------------------------------------------

  
  ----------------------------------------------------------------------------------------------------
  --// Check error variable                                                                       //--
  ----------------------------------------------------------------------------------------------------

  IF @Error <> 0 GOTO Crash

  ----------------------------------------------------------------------------------------------------
  --// Execute commands                                                                           //--
  ----------------------------------------------------------------------------------------------------

  WHILE EXISTS (SELECT * FROM @tmpDatabases WHERE Completed = 0)
  BEGIN --loop through databases

--select * from @tmpDatabases return

    SELECT TOP 1 @CurrentID = ID,
                 @CurrentDatabase = DatabaseName
    FROM @tmpDatabases
    WHERE Completed = 0
    ORDER BY ID ASC


    -- Set database message
    SET @DatabaseMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = @DatabaseMessage + 'Database: ' + QUOTENAME(@CurrentDatabase) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = @DatabaseMessage + 'Status: ' + CAST(DATABASEPROPERTYEX(@CurrentDatabase,'status') AS nvarchar) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = REPLACE(@DatabaseMessage,'%','%%')
--    RAISERROR(@DatabaseMessage,10,1) WITH NOWAIT

    IF DATABASEPROPERTYEX(@CurrentDatabase,'status') = 'ONLINE'
    BEGIN

		INSERT INTO #RoleMembers(dbname, dbrolename, membername, membersid)
		EXEC(

				'select ' + '''' + @CurrentDatabase + '''' + ', DbRole = g.name, MemberName = u.name, MemberSID = u.sid'
		+ ' from [' + @CurrentDatabase + '].dbo.sysusers g 
				left join [' + @CurrentDatabase + '].dbo.sysmembers m on (g.uid = m.groupuid)
				left join [' + @CurrentDatabase + '].dbo.sysusers u on (u.uid = m.memberuid)
		where   (g.issqlrole = 1)
				order by 1, 2'
			)


	END


	-- Update that the database is completed
    UPDATE @tmpDatabases
    SET Completed = 1
    WHERE ID = @CurrentID

    -- Clear variables
    SET @CurrentID = NULL
    SET @CurrentDatabase = NULL

    SET @CurrentCommand01 = NULL

    SET @CurrentCommandOutput01 = NULL
 
	
  END--loop through databases end

IF @bolOutputToTable = 1
	INSERT INTO COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_SecurityReport_DBRoleMembers (InstanceName, DatabaseName, DBRoleName, MemberName)
	SELECT @@ServerName, dbname, DBRoleName, MemberName 
	FROM #RoleMembers 
	WHERE membername is not null
	ORDER BY dbname, dbrolename, membername
ELSE
	SELECT dbname, DBRoleName, MemberName 
	FROM #RoleMembers 
	WHERE membername is not null
	ORDER BY dbname, dbrolename, membername


  RETURN 0


  ----------------------------------------------------------------------------------------------------
  --// Log completing information                                                                 //--
  ----------------------------------------------------------------------------------------------------

  Crash:
  SET @EndMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + ' Error with ' + OBJECT_NAME(@@PROCID)
  SET @EndMessage = REPLACE(@EndMessage,'%','%%')
  RAISERROR(@EndMessage,10,1) WITH Log

  ----------------------------------------------------------------------------------------------------
EndHere:
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END


dbo,spDBA_SecurityReport_ServerReadModExec,CREATE PROCEDURE [dbo].[spDBA_SecurityReport_ServerReadModExec] 
	@Databases nvarchar(2000) = 'SYSTEM_DATABASES, USER_DATABASES', 
	@bolOutputToTable BIT = 0,
	@Action VARCHAR(20) = 'Process'
AS
-- =============================================================================================================
-- Name: spDBA_SecurityReport
--
-- Description:	Reports objects and permissions that have been explicitly granted.
--  If a user has permissions on a object via sysadmin, the user will not be listed.
--
-- Output: error logging.
-- 
-- Available actions:
--	@Databases:
--	E.g. SYSTEM_DATABASES
--	E.g. USER_DATABASES
--	E.g. Database1
--	E.g. Database1, Database2
--	E.g. USER_DATABASES, master
--	E.g. SYSTEM_DATABASES, -master
--	E.g. %Database%
--	E.g. %Database%, -Database1
--
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	07/20/2009		Create initial version
--		Gary Derikito	07/23/2009		Added 3 part naming to remaining tables.
--		Mike Pelikan	02/23/2012		Added output to reporting table logic
--		Mike Pelikan	06/27/2012		Modified for versioning
--										Added Comments
--
-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '06/27/2012'


/*
exec spDBA_SecurityReportV2 @Databases = DBAUtility
exec spDBA_SecurityReport_ServerReadModExec @Databases = 'SYSTEM_DATABASES, USER_DATABASES'

*/
-- =============================================================================================================
----------------------------------------------------------------------------------------------------
--// Set options                                                                                //--
----------------------------------------------------------------------------------------------------
SET NOCOUNT ON

----------------------------------------------------------------------------------------------------
--// Revision                                                                                  //--
----------------------------------------------------------------------------------------------------
IF @Action = 'ReturnVersion'
BEGIN
	GOTO EndHere
END

----------------------------------------------------------------------------------------------------
--// Declare variables                                                                          //--
----------------------------------------------------------------------------------------------------

--  DECLARE @StartMessage nvarchar(max)
  DECLARE @EndMessage nvarchar(2000)
  DECLARE @DatabaseMessage nvarchar(2000)
  DECLARE @ErrorMessage nvarchar(2000)
  DECLARE @CurrentID int
  DECLARE @CurrentDatabase nvarchar(2000)
  DECLARE @CurrentTable nvarchar(2000)
  DECLARE @CurrentSchema nvarchar(128)
  DECLARE @CurrentCommand01 nvarchar(2000)
  DECLARE @CurrentCommandOutput01 int
  DECLARE @CreateDate datetime
  DECLARE @CurrentDate CHAR(8)
  DECLARE @tmpDatabases TABLE (ID int IDENTITY PRIMARY KEY,
                               DatabaseName nvarchar(2000),
                               Completed bit)

  DECLARE @Error int
  DECLARE @RowCount int
  DECLARE @ProductVersion	NVARCHAR(20) 
  DECLARE @SQL nvarchar(1000)
 
  SET @Error = 0
  SET @ProductVersion =  CAST(SERVERPROPERTY('productversion') AS VARCHAR)
  SET @CurrentDate = CONVERT(CHAR(8), GETDATE(), 112)


  IF object_id('tempdb..#ObjectSecurity') IS NOT NULL
	DROP TABLE #ObjectSecurity

  CREATE TABLE #ObjectSecurity (pk int IDENTITY PRIMARY KEY,
								dbname nvarchar(128),
                               username nvarchar(128),
                               gid smallint,
								objectname nvarchar(128),
								type char(2),
								id int,
								s varchar(15),
								i varchar(15),
								u varchar(15),
								d varchar(15),
								e varchar(15))
  
  ----------------------------------------------------------------------------------------------------
  --// Log initial information                                                                    //--
  ----------------------------------------------------------------------------------------------------

--  SET @StartMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Server: ' + CAST(SERVERPROPERTY('ServerName') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Version: ' + CAST(SERVERPROPERTY('ProductVersion') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Edition: ' + CAST(SERVERPROPERTY('Edition') AS nvarchar) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Procedure: ' + QUOTENAME(DB_NAME(DB_ID())) + '.' + QUOTENAME(OBJECT_SCHEMA_NAME(@@PROCID)) + '.' + QUOTENAME(OBJECT_NAME(@@PROCID)) + CHAR(13) + CHAR(10)
--  SET @StartMessage = @StartMessage + 'Parameters: @Databases = ' + ISNULL('''' + REPLACE(@Databases,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + ', @PhysicalOnly = ' + ISNULL('''' + REPLACE(@PhysicalOnly,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + ', @NoIndex = ' + ISNULL('''' + REPLACE(@NoIndex,'''','''''') + '''','NULL')
--  SET @StartMessage = @StartMessage + CHAR(13) + CHAR(10)
--  SET @StartMessage = REPLACE(@StartMessage,'%','%%')
--  RAISERROR(@StartMessage,10,1) WITH NOWAIT

  ----------------------------------------------------------------------------------------------------
  --// Select databases                                                                           //--
  ----------------------------------------------------------------------------------------------------

  IF @Databases IS NULL OR @Databases = ''
  BEGIN
    SET @ErrorMessage = 'The value for parameter @Databases is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END


  IF SUBSTRING(@ProductVersion, 1, 1) = '8' --2000
	BEGIN
		INSERT INTO @tmpDatabases (DatabaseName, Completed)
		SELECT DatabaseName AS DatabaseName, 0 AS Completed
		FROM dbo.fnDBA_DatabaseSelect2000 (@Databases)
		ORDER BY DatabaseName ASC
		SET @RowCount = @@RowCount
	END
	ELSE --2005
	BEGIN
--		GOTO Crash---comment out because VS is checking for existence of object
		INSERT INTO @tmpDatabases (DatabaseName, Completed)
		SELECT DatabaseName AS DatabaseName, 0 AS Completed
		FROM dbo.fnDBA_DatabaseSelect (@Databases)
		ORDER BY DatabaseName ASC
		SET @RowCount = @@RowCount
	END

  IF @@ERROR <> 0 OR (@RowCount = 0 AND @Databases <> 'USER_DATABASES')
  BEGIN
    SET @ErrorMessage = 'Error selecting databases.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END

  ----------------------------------------------------------------------------------------------------
  --// Check input parameters                                                                     //--
  ----------------------------------------------------------------------------------------------------

  
  ----------------------------------------------------------------------------------------------------
  --// Check error variable                                                                       //--
  ----------------------------------------------------------------------------------------------------

  IF @Error <> 0 GOTO Crash

  ----------------------------------------------------------------------------------------------------
  --// Execute commands                                                                           //--
  ----------------------------------------------------------------------------------------------------

  WHILE EXISTS (SELECT * FROM @tmpDatabases WHERE Completed = 0)
  BEGIN --loop through databases

--select * from @tmpDatabases return

    SELECT TOP 1 @CurrentID = ID,
                 @CurrentDatabase = DatabaseName
    FROM @tmpDatabases
    WHERE Completed = 0
    ORDER BY ID ASC


    -- Set database message
    SET @DatabaseMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = @DatabaseMessage + 'Database: ' + QUOTENAME(@CurrentDatabase) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = @DatabaseMessage + 'Status: ' + CAST(DATABASEPROPERTYEX(@CurrentDatabase,'status') AS nvarchar) + CHAR(13) + CHAR(10)
    SET @DatabaseMessage = REPLACE(@DatabaseMessage,'%','%%')
--    RAISERROR(@DatabaseMessage,10,1) WITH NOWAIT

    IF DATABASEPROPERTYEX(@CurrentDatabase,'status') = 'ONLINE'
    BEGIN

		INSERT INTO #ObjectSecurity(dbname, username, gid, objectname, type, id, s, i, u, d, e)
		EXEC(

				'select ' + '''' + @CurrentDatabase + '''' + ',sysusers_0.name as username,
				sysusers_0.gid,
				sysobjects_0.name as objectname, type,
				sysobjects_0.id,
				CASE WHEN sysprotects_1.action is null
					 THEN CASE WHEN sysobjects_0.xtype = '''+ 'P' + ''' THEN ''' + 'N/A' + '''
							   ELSE ' + '''' + 'No' + ''''
						  + ' END'
					 + ' ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'SELECT' + '''' + ',
				CASE WHEN sysprotects_2.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'P' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END 
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'INSERT' + '''' + ',
				CASE WHEN sysprotects_3.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'P' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END 
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'UPDATE' + '''' + ',
				CASE WHEN sysprotects_4.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'P' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'DELETE' + '''' + ',
				CASE WHEN sysprotects_5.action is null
					 THEN CASE WHEN sysobjects_0.xtype = ' + '''' + 'U' + '''' + ' THEN ' + '''' + 'N/A' + ''''
							   + ' ELSE ' + '''' + 'No' + ''''
						  + ' END
					 ELSE ' + '''' + 'Yes' + ''''
				+ ' END as ' + '''' + 'EXECUTE' + ''''
		+ ' from [' + @CurrentDatabase + '].dbo.sysusers sysusers_0
				full join [' + @CurrentDatabase + '].dbo.sysobjects sysobjects_0 on ( sysobjects_0.xtype in ( '  + '''' + 'P' + '''' + ', ' + '''' + 'U' + '''' + ')
										  and sysobjects_0.name NOT LIKE ' + '''' + 'dt%' + ''''
										+ ')
				left join [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_1 on sysprotects_1.uid = sysusers_0.uid
														  and sysprotects_1.id = sysobjects_0.id
														  and sysprotects_1.action = 193
														  and sysprotects_1.protecttype in (
														  204, 205 )
				left join [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_2 on sysprotects_2.uid = sysusers_0.uid
														  and sysprotects_2.id = sysobjects_0.id
														  and sysprotects_2.action = 195
														  and sysprotects_2.protecttype in (
														  204, 205 )
				left join  [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_3 on sysprotects_3.uid = sysusers_0.uid
														  and sysprotects_3.id = sysobjects_0.id
														  and sysprotects_3.action = 197
														  and sysprotects_3.protecttype in (
														  204, 205 )
				left join  [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_4 on sysprotects_4.uid = sysusers_0.uid
														  and sysprotects_4.id = sysobjects_0.id
														  and sysprotects_4.action = 196
														  and sysprotects_4.protecttype in (
														  204, 205 )
				left join  [' + @CurrentDatabase + '].dbo.sysprotects as sysprotects_5 on sysprotects_5.uid = sysusers_0.uid
														  and sysprotects_5.id = sysobjects_0.id
														  and sysprotects_5.action = 224
														  and sysprotects_5.protecttype in (
														  204, 205 )
		where   ( sysprotects_1.action is not null
				  or sysprotects_2.action is not null
				  or sysprotects_3.action is not null
				  or sysprotects_4.action is not null
				  or sysprotects_5.action is not null
				)
		order by sysusers_0.name,
				sysobjects_0.name'
			)


	END


	-- Update that the database is completed
    UPDATE @tmpDatabases
    SET Completed = 1
    WHERE ID = @CurrentID

    -- Clear variables
    SET @CurrentID = NULL
    SET @CurrentDatabase = NULL

    SET @CurrentCommand01 = NULL

    SET @CurrentCommandOutput01 = NULL
 
	
  END--loop through databases end

--select * from #ObjectSecurity order by username return

--SELECT TOP 1 'Yes' FROM #ObjectSecurity c WHERE c.username = 'TargetServersRole' AND ((c.i = 'Yes' ) OR (c.u = 'Yes' ) OR (c.d = 'Yes' )) return

IF @bolOutputToTable = 0
	SELECT 
	a.username UserName
	,COALESCE((SELECT TOP 1 b.s FROM #ObjectSecurity b WHERE b.username = a.username AND b.s = 'Yes')
		,(SELECT TOP 1 'No' FROM #ObjectSecurity b WHERE b.username = a.username AND (b.s = 'No') OR (b.s = 'N/A')) )
	 AS 'Read'
	,COALESCE((SELECT TOP 1 'Yes' FROM #ObjectSecurity c WHERE c.username = a.username AND ((c.i = 'Yes' ) OR (c.u = 'Yes' ) OR (c.d = 'Yes' )))
		,(SELECT TOP 1 'No' FROM #ObjectSecurity c WHERE c.username = a.username AND ((c.i = 'No') OR (c.u = 'No' ) OR (c.d = 'No' ) OR (c.i = 'N/A') OR (c.u = 'N/A' ) OR (c.d = 'N/A' ))) )
	 AS 'Modify'
	,COALESCE((SELECT TOP 1 d.e FROM #ObjectSecurity d WHERE d.username = a.username AND d.e = 'Yes')
		,(SELECT TOP 1 'No' FROM #ObjectSecurity d WHERE d.username = a.username AND (d.e = 'No') OR (d.e = 'N/A')  ))
	 AS 'Exec'
	FROM #ObjectSecurity a
	GROUP BY a.username 
	ORDER BY a.username
ELSE
	INSERT INTO COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_SecurityReport_ServerReadModExec (InstanceName, UserName, [Read], [Modify], [Exec])
	SELECT @@SERVERNAME, 
	a.username 
	,COALESCE((SELECT TOP 1 b.s FROM #ObjectSecurity b WHERE b.username = a.username AND b.s = 'Yes')
		,(SELECT TOP 1 'No' FROM #ObjectSecurity b WHERE b.username = a.username AND (b.s = 'No') OR (b.s = 'N/A')) )
	 AS 'Read'
	,COALESCE((SELECT TOP 1 'Yes' FROM #ObjectSecurity c WHERE c.username = a.username AND ((c.i = 'Yes' ) OR (c.u = 'Yes' ) OR (c.d = 'Yes' )))
		,(SELECT TOP 1 'No' FROM #ObjectSecurity c WHERE c.username = a.username AND ((c.i = 'No') OR (c.u = 'No' ) OR (c.d = 'No' ) OR (c.i = 'N/A') OR (c.u = 'N/A' ) OR (c.d = 'N/A' ))) )
	 AS 'Modify'
	,COALESCE((SELECT TOP 1 d.e FROM #ObjectSecurity d WHERE d.username = a.username AND d.e = 'Yes')
		,(SELECT TOP 1 'No' FROM #ObjectSecurity d WHERE d.username = a.username AND (d.e = 'No') OR (d.e = 'N/A')  ))
	 AS 'Exec'
	 from #ObjectSecurity a
	GROUP BY a.username 
	ORDER BY a.username

  RETURN 0


  ----------------------------------------------------------------------------------------------------
  --// Log completing information                                                                 //--
  ----------------------------------------------------------------------------------------------------

  Crash:
  SET @EndMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + ' Error with ' + OBJECT_NAME(@@PROCID)
  SET @EndMessage = REPLACE(@EndMessage,'%','%%')
  RAISERROR(@EndMessage,10,1) WITH Log

  ----------------------------------------------------------------------------------------------------

EndHere:
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END


dbo,spDBA_SendEmail,CREATE PROCEDURE [dbo].[spDBA_SendEmail]
@recipients NVARCHAR(2000),
@copy_recipients NVARCHAR(2000) = NULL,
@subject NVARCHAR(1000) = 'DBA Maintenance Procedure Email',
@MessageTxt NVARCHAR(2000) = NULL

AS
-- =============================================================================================================
-- Name: spDBA_SendEmail
--
-- Description:	Use to send email from remote servers.  The procedure is intended to run
-- on a repository server.  Using this procedure allows a remote server that does not have
-- email functionality to send email via the repository server. 
--
-- Output: error logging.
-- 
-- Available actions:
--	@recipients =  recipient of email
--	@copy_recipients = email address of those copied.
--	@subject = subject of email passed in from calling procedure.
--  @MessageTxt = message text of email passed in by calling procedure.
--	@AttachedHistFile = Allowable values are 'JOB_HIST', ...  If this is provided, the procedure will query the table and return the results as an attachment.

-- Dependencies: 
--	Papamart.dw.dbo.usp_delete_old_files
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	05/12/2009		Created initial version.
--		Gary Derikito	05/13/2009		Add optional file attaching capability
--		Mike Pelikan	04/02/2012		Removed File Attaching capablitiy - this will be re added at a later time.
--										Added logic to return version date of backup script if @Databases = 'ReturnVersion'
--		Mike Pelikan	05/29/2012		Added logic to use dbmail or xp_sendmail depending on server version
--										
DECLARE @Revision DATETIME
SET @Revision = '5/29/2012'
 	
/*
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com'
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com', @subject = 'Test'
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com', @subject = 'Test', @MessageTxt = 'Test message body...'
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com', @subject = 'Test', @MessageTxt = 'Test message body...', @AttachedHistFile = 'JOB_HIST'

exec spDBA_SendEmail @recipients = 'badnewsBear'

 
*/
-- =============================================================================================================

BEGIN

  ----------------------------------------------------------------------------------------------------
  --// Set options                                                                                //--
  ----------------------------------------------------------------------------------------------------

  SET NOCOUNT ON

  ----------------------------------------------------------------------------------------------------
  --// Declare variables                                                                          //--
  ----------------------------------------------------------------------------------------------------
	


DECLARE @outputsql VARCHAR(4000),
        @bcpsql VARCHAR(4000),
		@cmd VARCHAR(4000),
		@filename VARCHAR(100),
		@ErrorMessage nvarchar(4000),
		@Error int,
		@EndMessage nvarchar(4000)

	----------------------------------------------------------------------------------------------------
	--// Revision Return		                                                                    //--
	----------------------------------------------------------------------------------------------------
IF @recipients = 'ReturnVersion' GOTO Logging

  ----------------------------------------------------------------------------------------------------
  --// Check input parameters                                                                     //--
  ----------------------------------------------------------------------------------------------------

  IF @recipients NOT LIKE '%@%' OR @recipients IS NULL
  BEGIN
    SET @ErrorMessage = 'The value for parameter @recipients is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END

  IF @copy_recipients NOT LIKE '%@%'
  BEGIN
    SET @ErrorMessage = 'The value for parameter @copy_recipients is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END


  ----------------------------------------------------------------------------------------------------
  --// Check error variable                                                                       //--
  ----------------------------------------------------------------------------------------------------

  IF @Error <> 0 GOTO Logging

  ----------------------------------------------------------------------------------------------------
  --// Execute commands                                                                           //--
  ----------------------------------------------------------------------------------------------------
IF (SELECT COUNT(*) from msdb.dbo.sysobjects where name = 'sp_send_dbmail') > 0 
BEGIN
      EXEC msdb.dbo.sp_send_dbmail @recipients = @recipients, @copy_recipients = @copy_recipients, @subject = @subject, @body = @MessageTxt

END
ELSE
BEGIN
      EXEC master.dbo.xp_sendmail @recipients = @recipients, @copy_recipients = @copy_recipients, @subject = @subject, @message = @MessageTxt
END      
	
RETURN 0

Logging:
	IF @recipients = 'ReturnVersion'
	BEGIN
		SELECT @Revision 
	END
	ELSE
	BEGIN
		SET @EndMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + ' Error with ' + OBJECT_NAME(@@PROCID)
		SET @EndMessage = REPLACE(@EndMessage,'%','%%')
		RAISERROR(@EndMessage,10,1) WITH LOG
	END
	
END

dbo,spDBA_SendEmail_FixMe,CREATE PROCEDURE [dbo].[spDBA_SendEmail_FixMe]

@recipients NVARCHAR(MAX),
@copy_recipients NVARCHAR(MAX) = NULL,
@subject NVARCHAR(MAX) = 'DBA Maintenance Procedure Email',
@MessageTxt NVARCHAR(MAX) = NULL,
@AttachedHistFile VARCHAR(50) = NULL


AS
-- =============================================================================================================
-- Name: spDBA_SendEmail
--
-- Description:	Use to send email from remote servers.  The procedure is intended to run
-- on a repository server.  Using this procedure allows a remote server that does not have
-- email functionality to send email via the repository server. 
--
-- Output: error logging.
-- 
-- Available actions:
--	@recipients =  recipient of email
--	@copy_recipients = email address of those copied.
--	@subject = subject of email passed in from calling procedure.
--  @MessageTxt = message text of email passed in by calling procedure.
--	@AttachedHistFile = Allowable values are 'JOB_HIST', ...  If this is provided, the procedure will query the table and return the results as an attachment.

-- Dependencies: 
--	Papamart.dw.dbo.usp_delete_old_files
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	05/12/2009		Created initial version.
--		Gary Derikito	05/13/2009		Add optional file attaching capability
 	
/*
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com'
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com', @subject = 'Test'
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com', @subject = 'Test', @MessageTxt = 'Test message body...'
exec spDBA_SendEmail @recipients = 'garyd@buildabear.com', @subject = 'Test', @MessageTxt = 'Test message body...', @AttachedHistFile = 'JOB_HIST'

exec spDBA_SendEmail @recipients = 'badnewsBear'

 
*/
-- =============================================================================================================

BEGIN

  ----------------------------------------------------------------------------------------------------
  --// Set options                                                                                //--
  ----------------------------------------------------------------------------------------------------

  SET NOCOUNT ON

  ----------------------------------------------------------------------------------------------------
  --// Declare variables                                                                          //--
  ----------------------------------------------------------------------------------------------------

 declare     @ac_path VARCHAR(100)

SET @ac_path = 'I:\Temp\Accounting\'

DECLARE @outputsql VARCHAR(4000),
        @bcpsql VARCHAR(4000),
		@cmd VARCHAR(4000),
		@filename VARCHAR(100),
		@ErrorMessage nvarchar(max),
		@Error int,
		@EndMessage nvarchar(max)


--select @recipients
--return
  
  ----------------------------------------------------------------------------------------------------
  --// Check input parameters                                                                     //--
  ----------------------------------------------------------------------------------------------------

  IF @recipients NOT LIKE '%@%' OR @recipients IS NULL
  BEGIN
    SET @ErrorMessage = 'The value for parameter @recipients is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END

  IF @copy_recipients NOT LIKE '%@%'
  BEGIN
    SET @ErrorMessage = 'The value for parameter @copy_recipients is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END

  IF @AttachedHistFile NOT IN ('JOB_HIST')
  BEGIN
    SET @ErrorMessage = 'The value for parameter @AttachedHistFile is not supported.' + CHAR(13) + CHAR(10)
    RAISERROR(@ErrorMessage,16,1) WITH LOG
    SET @Error = @@ERROR
  END

  
  ----------------------------------------------------------------------------------------------------
  --// Check error variable                                                                       //--
  ----------------------------------------------------------------------------------------------------

  IF @Error <> 0 GOTO Crash

  ----------------------------------------------------------------------------------------------------
  --// Execute commands                                                                           //--
  ----------------------------------------------------------------------------------------------------

IF @AttachedHistFile = 'JOB_HIST'
BEGIN
	SET @outputsql =
	+ ' select '  
	+ '  SERVER_NM' 
	+ ' , JOB_NM'
	+ ' , STEP_NM'
	+ ' , CAST(STEP_ID AS varchar(20))'
	+ ' , STEP_NM_HIST'
	+ ' , CAST(RUN_DT AS varchar(20))'
	+ ' , CAST(RUN_TM AS varchar(20))'
	+ ' , SQL_SEVERITY'
	+ ' , MESSAGE_TXT'
	+ ' , CAST(INSERT_DT as varchar(20))'
	+ ' from DBAUtility.dbo.JOB_HIST' 
	+ ' where datediff(day, INSERT_DT, getdate()) between -7 and 0'
	--select @outputsql

	SELECT  @filename = 'JOG_HIST' + '.txt'

	--select @filename
	--DELETE OLD FILES
	/*******************/
	-- set db name for production
	    EXEC [dw].dbo.usp_delete_old_files @path = @ac_path, @filemask = '*.txt',
	        @retention = 1
	/*******************/        

		SET @bcpsql = 'bcp "' + @outputsql + '" queryout "' + @ac_path + @filename
			+ '" -t "," -T -c'
		SET @bcpsql = 'bcp "' + @outputsql + '" queryout "' + @ac_path + @filename
			+ '" -t -T -c'

		EXEC master..xp_cmdshell @bcpsql
END

DECLARE @filelocation VARCHAR(100)
		
SET @filelocation = @ac_path + @filename
		
exec msdb.dbo.sp_send_dbmail 
@recipients=@recipients
,@copy_recipients=@copy_recipients
,@subject = @subject
,@query_result_separator = ','
,@file_attachments =  @filelocation
--,@ansi_attachment='TRUE'
,@body = @MessageTxt--'Message ...'

RETURN 0

  Crash:
  SET @EndMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120) + ' Error with ' + OBJECT_NAME(@@PROCID)
  SET @EndMessage = REPLACE(@EndMessage,'%','%%')
  RAISERROR(@EndMessage,10,1) WITH LOG

END

dbo,spDBA_StartAgentJobAndWait,CREATE procedure [dbo].[spDBA_StartAgentJobAndWait](@job nvarchar(128), @maxwaitmins int = 32767) --, @result int output)
AS
-- =============================================================================================================
-- Name: spDBA_StartAgentJobAndWait
--
-- Description:	Starts a SQLAgent Job and waits for it to finish or until a specified wait period elapsed
--
-- @Job: The SQL Server Agent Job to be run
-- @maxwaitmins: (Optional) The maximum number of minutes to wait.
--
-- @result: 1 -> OK
--          0 -> still running after maxwaitmins
--
-- Dependency: None
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Murrish	7/18/2013		Created based upon http://stackoverflow.com/questions/10648475/need-to-start-agent-job-and-wait-until-completes-and-get-success-or-failure

DECLARE @Revision DATETIME
SET @Revision = '07/18/2013'

-- =============================================================================================================

set NOCOUNT ON;
set XACT_ABORT ON;

    BEGIN TRY

    declare @running as int
    declare @seccount as int
    declare @maxseccount as int
    declare @start_job as bigint
    declare @run_status as int

    set @start_job = cast(convert(varchar, getdate(), 112) as bigint) * 1000000 + datepart(hour, getdate()) * 10000 + datepart(minute, getdate()) * 100 + datepart(second, getdate())

    set @maxseccount = 60*@maxwaitmins
    set @seccount = 0
    set @running = 0

    declare @job_owner sysname
    declare @job_id UNIQUEIDENTIFIER

    set @job_owner = SUSER_SNAME()

    -- get job id
    select @job_id=job_id
    from msdb.dbo.sysjobs sj
    where sj.name=@job

    -- invalid job name then exit with an error
    if @job_id is null
        RAISERROR (N'Unknown job: %s.', 16, 1, @job)

    -- output from stored procedure xp_sqlagent_enum_jobs is captured in the following table
    declare @xp_results TABLE ( job_id                UNIQUEIDENTIFIER NOT NULL,
                                last_run_date         INT              NOT NULL,
                                last_run_time         INT              NOT NULL,
                                next_run_date         INT              NOT NULL,
                                next_run_time         INT              NOT NULL,
                                next_run_schedule_id  INT              NOT NULL,
                                requested_to_run      INT              NOT NULL, -- BOOL
                                request_source        INT              NOT NULL,
                                request_source_id     sysname          COLLATE database_default NULL,
                                running               INT              NOT NULL, -- BOOL
                                current_step          INT              NOT NULL,
                                current_retry_attempt INT              NOT NULL,
                                job_state             INT              NOT NULL)

    -- start the job
    declare @r as int
    exec @r = msdb..sp_start_job @job

    -- quit if unable to start
    if @r<>0
        RAISERROR (N'Could not start job: %s.', 16, 2, @job)

    -- start with an initial delay to allow the job to appear in the job list (maybe I am missing something ?)
    WAITFOR DELAY '0:0:01';
    set @seccount = 1

    -- check job run state
    insert into @xp_results
    execute master.dbo.xp_sqlagent_enum_jobs 1, @job_owner, @job_id

    set @running= (SELECT top 1 running from @xp_results)

    while @running<>0 and @seccount < @maxseccount
    begin
        WAITFOR DELAY '0:1:0';	-- Wait for 1 minute
        set @seccount = @seccount + 1

        delete from @xp_results

        insert into @xp_results
        execute master.dbo.xp_sqlagent_enum_jobs 1, @job_owner, @job_id

        set @running= (SELECT top 1 running from @xp_results)
    end

    -- result: not ok (=1) if still running

    if @running <> 0 begin
        -- still running
        return 0
    end
    else begin

        -- did it finish ok ?
        set @run_status = 0

        select @run_status=run_status
        from msdb.dbo.sysjobhistory
        where job_id=@job_id
          and cast(run_date as bigint) * 1000000 + run_time >= @start_job

        if @run_status=1
            return 1  --finished ok
        else  --error
            RAISERROR (N'job %s did not finish successfully.', 16, 2, @job)

    end

    END TRY
    BEGIN CATCH

    DECLARE
        @ErrorMessage    NVARCHAR(4000),
        @ErrorNumber     INT,
        @ErrorSeverity   INT,
        @ErrorState      INT,
        @ErrorLine       INT,
        @ErrorProcedure  NVARCHAR(200);

    SELECT
        @ErrorNumber = ERROR_NUMBER(),
        @ErrorSeverity = ERROR_SEVERITY(),
        @ErrorState = ERROR_STATE(),
        @ErrorLine = ERROR_LINE(),
        @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

    SELECT @ErrorMessage =
        N'Error %d, Level %d, State %d, Procedure %s, Line %d, ' +
            'Message: '+ ERROR_MESSAGE();

    RAISERROR
        (
        @ErrorMessage,
        @ErrorSeverity,
        1,
        @ErrorNumber,    -- original error number.
        @ErrorSeverity,  -- original error severity.
        @ErrorState,     -- original error state.
        @ErrorProcedure, -- original error procedure name.
        @ErrorLine       -- original error line number.
        );

    END CATCH
```

