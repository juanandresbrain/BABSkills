# dbo.fnDBA_DatabaseSelect

**Database:** DBAUtility_new  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDBA_DatabaseSelect"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @DatabaseList | nvarchar | -1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[fnDBA_DatabaseSelect] (@DatabaseList nvarchar(max))

RETURNS @Database TABLE (DatabaseName nvarchar(max) NOT NULL)

AS

BEGIN

-- =============================================================================================================
-- Name: [fnDBA_DatabaseSelect]
--
-- Description:	Parses a list of database names.  Used with index maintenance procedures.
--
-- Output: List of database names.
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	01/02/2009		Created based on SQL Server article http://www.sqlmag.com/Articles/ArticleID/100178/pg/2/2.html
--		Mike Pelikan	20120210		Updated with most recent version from  http://ola.hallengren.com     
--		Mike Pelikan	06/27/2012		Modified for versioning report only

-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '06/27/2012'
 	 
/*
*/
-- =============================================================================================================

  ----------------------------------------------------------------------------------------------------
  --// Source: http://ola.hallengren.com                                                          //--
  ----------------------------------------------------------------------------------------------------

  DECLARE @DatabaseItem nvarchar(max)
  DECLARE @Position int

  DECLARE @CurrentID int
  DECLARE @CurrentDatabaseName nvarchar(max)
  DECLARE @CurrentDatabaseStatus bit

  DECLARE @Database01 TABLE (DatabaseName nvarchar(max))

  DECLARE @Database02 TABLE (ID int IDENTITY PRIMARY KEY,
                             DatabaseName nvarchar(max),
                             DatabaseStatus bit,
                             Completed bit)

  DECLARE @Database03 TABLE (DatabaseName nvarchar(max),
                             DatabaseStatus bit)

  DECLARE @Sysdatabases TABLE (DatabaseName nvarchar(max))

  ----------------------------------------------------------------------------------------------------
  --// Split input string into elements                                                           //--
  ----------------------------------------------------------------------------------------------------

  WHILE CHARINDEX(', ',@DatabaseList) > 0 SET @DatabaseList = REPLACE(@DatabaseList,', ',',')
  WHILE CHARINDEX(' ,',@DatabaseList) > 0 SET @DatabaseList = REPLACE(@DatabaseList,' ,',',')
  WHILE CHARINDEX(',,',@DatabaseList) > 0 SET @DatabaseList = REPLACE(@DatabaseList,',,',',')

  IF RIGHT(@DatabaseList,1) = ',' SET @DatabaseList = LEFT(@DatabaseList,LEN(@DatabaseList) - 1)
  IF LEFT(@DatabaseList,1) = ','  SET @DatabaseList = RIGHT(@DatabaseList,LEN(@DatabaseList) - 1)

  SET @DatabaseList = LTRIM(RTRIM(@DatabaseList))

  WHILE LEN(@DatabaseList) > 0
  BEGIN
    SET @Position = CHARINDEX(',', @DatabaseList)
    IF @Position = 0
    BEGIN
      SET @DatabaseItem = @DatabaseList
      SET @DatabaseList = ''
    END
    ELSE
    BEGIN
      SET @DatabaseItem = LEFT(@DatabaseList, @Position - 1)
      SET @DatabaseList = RIGHT(@DatabaseList, LEN(@DatabaseList) - @Position)
    END
    IF @DatabaseItem <> '-' INSERT INTO @Database01 (DatabaseName) VALUES(@DatabaseItem)
  END

  ----------------------------------------------------------------------------------------------------
  --// Handle database exclusions                                                                 //--
  ----------------------------------------------------------------------------------------------------

  INSERT INTO @Database02 (DatabaseName, DatabaseStatus, Completed)
  SELECT DISTINCT DatabaseName = CASE WHEN DatabaseName LIKE '-%' THEN RIGHT(DatabaseName,LEN(DatabaseName) - 1) ELSE DatabaseName END,
                  DatabaseStatus = CASE WHEN DatabaseName LIKE '-%' THEN 0 ELSE 1 END,
                  0 AS Completed
  FROM @Database01

  ----------------------------------------------------------------------------------------------------
  --// Resolve elements                                                                           //--
  ----------------------------------------------------------------------------------------------------

  WHILE EXISTS (SELECT * FROM @Database02 WHERE Completed = 0)
  BEGIN

    SELECT TOP 1 @CurrentID = ID,
                 @CurrentDatabaseName = DatabaseName,
                 @CurrentDatabaseStatus = DatabaseStatus
    FROM @Database02
    WHERE Completed = 0
    ORDER BY ID ASC

    IF @CurrentDatabaseName = 'SYSTEM_DATABASES'
    BEGIN
      INSERT INTO @Database03 (DatabaseName, DatabaseStatus)
      SELECT [name], @CurrentDatabaseStatus
      FROM sys.databases
      WHERE [name] IN('master','model','msdb','tempdb')
    END
    ELSE IF @CurrentDatabaseName = 'USER_DATABASES'
    BEGIN
      INSERT INTO @Database03 (DatabaseName, DatabaseStatus)
      SELECT [name], @CurrentDatabaseStatus
      FROM sys.databases
      WHERE [name] NOT IN('master','model','msdb','tempdb')
    END
    ELSE IF @CurrentDatabaseName = 'ALL_DATABASES'
    BEGIN
      INSERT INTO @Database03 (DatabaseName, DatabaseStatus)
      SELECT [name], @CurrentDatabaseStatus
      FROM sys.databases
    END
    ELSE IF CHARINDEX('%',@CurrentDatabaseName) > 0
    BEGIN
      INSERT INTO @Database03 (DatabaseName, DatabaseStatus)
      SELECT [name], @CurrentDatabaseStatus
      FROM sys.databases
      WHERE [name] LIKE REPLACE(PARSENAME(@CurrentDatabaseName,1),'_','[_]')
    END
    ELSE
    BEGIN
      INSERT INTO @Database03 (DatabaseName, DatabaseStatus)
      SELECT [name], @CurrentDatabaseStatus
      FROM sys.databases
      WHERE [name] = PARSENAME(@CurrentDatabaseName,1)
    END

    UPDATE @Database02
    SET Completed = 1
    WHERE ID = @CurrentID

    SET @CurrentID = NULL
    SET @CurrentDatabaseName = NULL
    SET @CurrentDatabaseStatus = NULL

  END

  ----------------------------------------------------------------------------------------------------
  --// Handle tempdb and database snapshots                                                       //--
  ----------------------------------------------------------------------------------------------------

  INSERT INTO @Sysdatabases (DatabaseName)
  SELECT [name]
  FROM sys.databases
  WHERE [name] <> 'tempdb'
  AND source_database_id IS NULL

  ----------------------------------------------------------------------------------------------------
  --// Return results                                                                             //--
  ----------------------------------------------------------------------------------------------------

  INSERT INTO @Database (DatabaseName)
  SELECT DatabaseName
  FROM @Sysdatabases
  INTERSECT
  SELECT DatabaseName
  FROM @Database03
  WHERE DatabaseStatus = 1
  EXCEPT
  SELECT DatabaseName
  FROM @Database03
  WHERE DatabaseStatus = 0

  RETURN

  ----------------------------------------------------------------------------------------------------

END
```

