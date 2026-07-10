# dbo.fnDatabaseSelect

**Database:** DBAUtility  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDatabaseSelect"]
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
CREATE FUNCTION [dbo].[fnDatabaseSelect] (@DatabaseList nvarchar(max))

RETURNS @Database TABLE(DatabaseName nvarchar(max) NOT NULL)

AS
-- =============================================================================================================
-- Name: fnDatabaseSelect
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
--		Gary Derikito	06/16/2009		Add collate to allow for multiple databases with incompatible collations
 	
/*
*/
-- =============================================================================================================


BEGIN

  DECLARE @Database01 TABLE(DatabaseName nvarchar(max),
                            DatabaseStatus bit)

  DECLARE @Database02 TABLE(DatabaseName nvarchar(max),
                            DatabaseStatus bit)

  DECLARE @DatabaseItem nvarchar(max)
  DECLARE @Position int

  SET @DatabaseList = LTRIM(RTRIM(@DatabaseList))
  SET @DatabaseList = REPLACE(@DatabaseList,' ','')
  SET @DatabaseList = REPLACE(@DatabaseList,'[','')
  SET @DatabaseList = REPLACE(@DatabaseList,']','')
  SET @DatabaseList = REPLACE(@DatabaseList,'''','')
  SET @DatabaseList = REPLACE(@DatabaseList,'"','')

  WHILE CHARINDEX(',,',@DatabaseList) > 0 SET @DatabaseList = REPLACE(@DatabaseList,',,',',')

  IF RIGHT(@DatabaseList,1) = ',' SET @DatabaseList = LEFT(@DatabaseList,LEN(@DatabaseList) - 1)
  IF LEFT(@DatabaseList,1) = ','  SET @DatabaseList = RIGHT(@DatabaseList,LEN(@DatabaseList) - 1)

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
    INSERT INTO @Database01 (DatabaseName) VALUES(@DatabaseItem)
  END

  UPDATE @Database01
  SET DatabaseStatus = 1
  WHERE DatabaseName NOT LIKE '-%'

  UPDATE @Database01
  SET  DatabaseName = RIGHT(DatabaseName,LEN(DatabaseName) - 1), DatabaseStatus = 0
  WHERE DatabaseName LIKE '-%'

  INSERT INTO @Database02 (DatabaseName, DatabaseStatus)
  SELECT DISTINCT DatabaseName, DatabaseStatus
  FROM @Database01
  WHERE DatabaseName NOT IN('SYSTEM_DATABASES','USER_DATABASES')

  IF EXISTS (SELECT * FROM @Database01 WHERE DatabaseName = 'SYSTEM_DATABASES' AND DatabaseStatus = 0)
  BEGIN
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus) VALUES('master', 0)
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus) VALUES('model', 0)
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus) VALUES('msdb', 0)
  END

  IF EXISTS (SELECT * FROM @Database01 WHERE DatabaseName = 'SYSTEM_DATABASES' AND DatabaseStatus = 1)
  BEGIN
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus) VALUES('master', 1)
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus) VALUES('model', 1)
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus) VALUES('msdb', 1)
  END

  IF EXISTS (SELECT * FROM @Database01 WHERE DatabaseName = 'USER_DATABASES' AND DatabaseStatus = 0)
  BEGIN
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus)
    SELECT [name], 0
    FROM sys.databases
    WHERE database_id > 4
  END

  IF EXISTS (SELECT * FROM @Database01 WHERE DatabaseName = 'USER_DATABASES' AND DatabaseStatus = 1)
  BEGIN
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus)
    SELECT [name], 1
    FROM sys.databases
    WHERE database_id > 4
  END

  INSERT INTO @Database (DatabaseName)
  SELECT [name] COLLATE SQL_Latin1_General_CP1_CI_AS
  FROM sys.databases
  WHERE [name] <> 'tempdb'
  AND source_database_id IS NULL
  INTERSECT
  SELECT DatabaseName COLLATE SQL_Latin1_General_CP1_CI_AS
  FROM @Database02
  WHERE DatabaseStatus = 1
  EXCEPT
  SELECT DatabaseName COLLATE SQL_Latin1_General_CP1_CI_AS
  FROM @Database02
  WHERE DatabaseStatus = 0

  RETURN

END
```

