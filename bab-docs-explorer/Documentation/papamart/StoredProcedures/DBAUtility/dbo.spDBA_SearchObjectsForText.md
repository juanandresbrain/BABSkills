# dbo.spDBA_SearchObjectsForText

**Database:** DBAUtility  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_SearchObjectsForText"]
    mat(["mat"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| mat |

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
```

