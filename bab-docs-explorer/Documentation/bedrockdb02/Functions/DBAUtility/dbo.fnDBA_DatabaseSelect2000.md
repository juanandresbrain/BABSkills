# dbo.fnDBA_DatabaseSelect2000

**Database:** DBAUtility  
**Server:** bedrockdb02  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDBA_DatabaseSelect2000"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @DatabaseList | nvarchar | 2000 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[fnDBA_DatabaseSelect2000] (@DatabaseList nvarchar(1000))

RETURNS @Database TABLE(DatabaseName nvarchar(1000) NOT NULL )

AS
BEGIN
-- =============================================================================================================
-- Name: fnDBA_DatabaseSelect2000
--
-- Description:	Parses a list of database names.  Used with index maintenance procedures.
-- This version is for use with SQL Server 2000
-- 
-- Output: List of database names.
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Derikito	05/21/2009		Created based on fnDatabaseSelect
--		Mike Pelikan	06/27/2012		Modified for versioning report only

-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '06/27/2012'
 	 
 	
/*
select * from fnDBA_DatabaseSelect2000('DBAUtility')
select * from fnDBA_DatabaseSelect2000('USER_DATABASES, -DBAUtility')
select * from fnDBA_DatabaseSelect2000('trecs, UPCS')
select * from fnDBA_DatabaseSelect2000('USER_DATABASES, -DBAUtility, -pubs')

select * from fnDBA_DatabaseSelect2000('SYSTEM_DATABASES')
select * from fnDBA_DatabaseSelect2000('SYSTEM_DATABASES, -msdb')

select * from fnDBA_DatabaseSelect2000('SYSTEM_DATABASES, USER_DATABASES, -DBAUtility, -pubs')

*/
-- =============================================================================================================

  DECLARE @Database01 TABLE(DatabaseName nvarchar(1000),
                            DatabaseStatus bit)

  DECLARE @Database02 TABLE(DatabaseName nvarchar(1000),
                            DatabaseStatus bit)

  DECLARE @DatabaseItem nvarchar(1000)
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
    FROM master..sysdatabases
    WHERE dbid > 4
  END

  IF EXISTS (SELECT * FROM @Database01 WHERE DatabaseName = 'USER_DATABASES' AND DatabaseStatus = 1)
  BEGIN
    INSERT INTO @Database02 (DatabaseName, DatabaseStatus)
    SELECT [name], 1
    FROM master..sysdatabases
    WHERE dbid > 4
  END

  INSERT INTO @Database (DatabaseName)
  SELECT DISTINCT d1.[name] 
  FROM
  (SELECT [name] FROM master..sysdatabases WHERE [name] <> 'tempdb') d1
  INNER JOIN
  (SELECT DatabaseName FROM @Database02 WHERE DatabaseStatus = 1) d2
  ON (d1.[name] COLLATE database_default = d2.DatabaseName COLLATE database_default)
  LEFT JOIN
  (SELECT DatabaseName FROM @Database02 WHERE DatabaseStatus = 0) d0
  ON (d2.DatabaseName COLLATE database_default = d0.DatabaseName COLLATE database_default)
  WHERE d0.DatabaseName IS NULL   

/*
  INSERT INTO @Database (DatabaseName)
  SELECT [name]
  FROM sys.databases
  WHERE [name] <> 'tempdb'
  AND source_database_id IS NULL
  INTERSECT
  SELECT DatabaseName
  FROM @Database02
  WHERE DatabaseStatus = 1
  EXCEPT
  SELECT DatabaseName
  FROM @Database02
  WHERE DatabaseStatus = 0
*/
  RETURN

END
```
