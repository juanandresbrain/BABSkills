# dbo.fnDBA_DatabaseSelect_BackupHistory

**Database:** DBAUtilityMaster  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDBA_DatabaseSelect_BackupHistory"]
    dbo_tblDBA_BackupHistoryRepository(["dbo.tblDBA_BackupHistoryRepository"]) --> FUNC
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @DatabaseList | nvarchar | -1 | NO |
| @InstanceName | varchar | 1000 | NO |

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_BackupHistoryRepository |

## Function Code

```sql
CREATE FUNCTION [dbo].[fnDBA_DatabaseSelect_BackupHistory] (@DatabaseList nvarchar(max), @InstanceName VARCHAR(1000) = NULL)

RETURNS @Database TABLE (InstanceName varchar(1000), DatabaseName nvarchar(max) NOT NULL)

AS

BEGIN

-- =============================================================================================================
-- Name: fnDBA_DatabaseSelect_BackupHistory
--
-- Description:	Parses a list of database names.  Used with index maintenance procedures.
--
-- Output: List of database names.
--
-- Dependencies: 
--		DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	01/02/2009		Created based on SQL Server article http://www.sqlmag.com/Articles/ArticleID/100178/pg/2/2.html
--		Mike Pelikan	20120210		Updated with most recent version from  http://ola.hallengren.com     
--		Mike Pelikan	20120305		Modified to include instance and only records from DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository
-- 	 
/*
*/

--DECLARE @Database TABLE (InstanceName varchar(1000), DatabaseName nvarchar(max) NOT NULL)

--DECLARE @DatabaseList nvarchar(max), @InstanceName VARCHAR(1000)
--SELECT @DatabaseList = 'DBAUtility', @InstanceName =''
-- =============================================================================================================

  ----------------------------------------------------------------------------------------------------
  --// Source: http://ola.hallengren.com                                                          //--
  ----------------------------------------------------------------------------------------------------

  DECLARE @DatabaseItem nvarchar(max)
  DECLARE @Position int

  DECLARE @CurrentID int
  DECLARE @CurrentDatabaseName nvarchar(max)
  DECLARE @CurrentDatabaseStatus bit

  DECLARE @Database01 TABLE (InstanceName varchar(1000),
								DatabaseName nvarchar(max))

  DECLARE @Database02 TABLE (ID int IDENTITY PRIMARY KEY,
								InstanceName varchar(1000),
								DatabaseName nvarchar(max),
								DatabaseStatus bit,
								Completed bit)

  DECLARE @Database03 TABLE (InstanceName varchar(1000),
								DatabaseName nvarchar(max),
								DatabaseStatus bit)

  DECLARE @Sysdatabases TABLE (InstanceName varchar(1000),
								DatabaseName nvarchar(max))

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
    IF @DatabaseItem <> '-' INSERT INTO @Database01 (InstanceName, DatabaseName) VALUES(@InstanceName, @DatabaseItem)
  END

  ----------------------------------------------------------------------------------------------------
  --// Handle database exclusions                                                                 //--
  ----------------------------------------------------------------------------------------------------

  INSERT INTO @Database02 (InstanceName, DatabaseName, DatabaseStatus, Completed)
  SELECT DISTINCT @InstanceName, DatabaseName = CASE WHEN DatabaseName LIKE '-%' THEN RIGHT(DatabaseName,LEN(DatabaseName) - 1) ELSE DatabaseName END,
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

	IF ISNULL(@InstanceName, '') <> ''
	BEGIN
		IF @CurrentDatabaseName = 'SYSTEM_DATABASES'
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName IN('master','model','msdb','tempdb') AND InstanceName = @InstanceName
		END
		ELSE IF @CurrentDatabaseName = 'USER_DATABASES'
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName NOT IN('master','model','msdb','tempdb') AND InstanceName = @InstanceName
		END
		ELSE IF @CurrentDatabaseName = 'ALL_DATABASES'
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE InstanceName = @InstanceName
		END
		ELSE IF CHARINDEX('%',@CurrentDatabaseName) > 0
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName LIKE REPLACE(PARSENAME(@CurrentDatabaseName,1),'_','[_]') AND InstanceName = @InstanceName
		END
		ELSE
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName = PARSENAME(@CurrentDatabaseName,1) AND InstanceName = @InstanceName
		END

		UPDATE @Database02
		SET Completed = 1
		WHERE ID = @CurrentID

	END
    ELSE
    BEGIN 
		IF @CurrentDatabaseName = 'SYSTEM_DATABASES'
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName IN('master','model','msdb','tempdb') 
		END
		ELSE IF @CurrentDatabaseName = 'USER_DATABASES'
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName NOT IN('master','model','msdb','tempdb')
		END
		ELSE IF @CurrentDatabaseName = 'ALL_DATABASES'
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
		END
		ELSE IF CHARINDEX('%',@CurrentDatabaseName) > 0
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName LIKE REPLACE(PARSENAME(@CurrentDatabaseName,1),'_','[_]')
		END
		ELSE
		BEGIN
			INSERT INTO @Database03 (InstanceName, DatabaseName, DatabaseStatus)
			SELECT InstanceName, DatabaseName, @CurrentDatabaseStatus
			FROM dbo.tblDBA_BackupHistoryRepository
			WHERE DatabaseName = @CurrentDatabaseName
		END

		UPDATE @Database02
		SET Completed = 1
		WHERE ID = @CurrentID

    END
    SET @CurrentID = NULL
    SET @CurrentDatabaseName = NULL
    SET @CurrentDatabaseStatus = NULL

  END

  ----------------------------------------------------------------------------------------------------
  --// Handle tempdb and database snapshots                                                       //--
  ----------------------------------------------------------------------------------------------------
IF ISNULL(@InstanceName, '') = '' 
BEGIN
  INSERT INTO @Sysdatabases (InstanceName, DatabaseName)
  SELECT InstanceName, DatabaseName 
  FROM DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository 
  WHERE DatabaseName IN (
	SELECT [name]
	FROM sys.databases
	WHERE [name] <> 'tempdb'
	AND source_database_id IS NULL)
END
ELSE
BEGIN
  INSERT INTO @Sysdatabases (InstanceName, DatabaseName)
  SELECT InstanceName, DatabaseName 
  FROM DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository 
  WHERE InstanceName = @InstanceName AND DatabaseName IN (
	SELECT [name]
	FROM sys.databases
	WHERE [name] <> 'tempdb'
	AND source_database_id IS NULL)
END
  ----------------------------------------------------------------------------------------------------
  --// Return results                                                                             //--
  ----------------------------------------------------------------------------------------------------


  INSERT INTO @Database (InstanceName, DatabaseName)
  SELECT InstanceName, DatabaseName
  FROM @Sysdatabases
  INTERSECT
  SELECT InstanceName, DatabaseName
  FROM @Database03
  WHERE DatabaseStatus = 1
  EXCEPT
  SELECT InstanceName, DatabaseName
  FROM @Database03
  WHERE DatabaseStatus = 0

  RETURN

  ----------------------------------------------------------------------------------------------------

END
```

