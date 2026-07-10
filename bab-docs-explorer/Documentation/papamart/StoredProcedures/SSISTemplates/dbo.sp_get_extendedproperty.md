# dbo.sp_get_extendedproperty

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_get_extendedproperty"]
    D(["D"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| D |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_get_extendedproperty]
@databasename varchar(128) = NULL
as

BEGIN
SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED


IF @databasename IS NULL
SET @databasename = db_name()

DECLARE @sqltext nvarchar(4000)

IF object_id(N'tempdb.dbo.##temp___DataDictionary') IS NOT NULL
DROP TABLE ##temp___DataDictionary

IF object_id(N'tempdb.dbo.##temp___DataDictionary_schema') IS NOT NULL
DROP TABLE ##temp___DataDictionary_schema


CREATE TABLE ##temp___DataDictionary(
[tableschema] varchar(128) NULL,
[tablename] varchar(128) NULL,
[columnname] varchar(128) NULL,
[xtype] varchar(8) NULL,
[description] nvarchar(4000) NULL
) 

CREATE TABLE ##temp___DataDictionary_schema(
[tableschema] varchar(128),
[tablename] varchar(128) NULL,
)

-- Deploy Database Property
SET @sqltext = 'INSERT INTO ##temp___DataDictionary ([description], [xtype]) SELECT cast(value as nvarchar(4000)), ''D'' FROM '
+ @databasename + '.sys.fn_listextendedproperty(default, default, default, default, default, default, default)'

EXECUTE (@sqltext)

-- Get table level data dictionary

SET @sqltext = 'INSERT INTO ##temp___DataDictionary_schema SELECT DISTINCT TABLE_SCHEMA, TABLE_NAME FROM ' 
+ @databasename + '.INFORMATION_SCHEMA.TABLES'
EXECUTE(@sqltext)

DECLARE table_cursor CURSOR FOR 
SELECT DISTINCT [tableschema] FROM ##temp___DataDictionary_schema

DECLARE @TABLE_SCHEMA VARCHAR(128)

OPEN table_cursor
FETCH NEXT FROM table_cursor INTO @TABLE_SCHEMA

WHILE @@FETCH_STATUS = 0
BEGIN

SET @sqltext = 'INSERT INTO ##temp___DataDictionary ([tableschema], [tablename],[description], [xtype]) SELECT ' 
+ '''' + @TABLE_SCHEMA + '''' + + ', objname, cast(value as nvarchar(4000)), ''U'' FROM '
+ @databasename + '.sys.fn_listextendedproperty (NULL, ''schema'', ' 
+ '''' + @TABLE_SCHEMA + ''''+ ', ''table'', default, NULL, NULL)'

EXECUTE(@sqltext)

FETCH NEXT FROM table_cursor INTO @TABLE_SCHEMA
END

CLOSE table_cursor
DEALLOCATE table_cursor

CREATE TABLE ##temp___DataDictionary_keys(
[tableschema] varchar(128) NULL,
[tablename] varchar(128) NULL,
[columnname] varchar(128) NULL,
[xtype] varchar(8) NULL
) 

-- Populate all the key types
SET @sqltext = 'INSERT INTO ##temp___DataDictionary_keys SELECT U.TABLE_SCHEMA,U.TABLE_NAME, U.COLUMN_NAME, xtype '
+ 'FROM ' + @databasename + '.INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE U '
+ 'JOIN ' + @databasename + '.sys.sysobjects O ON U.CONSTRAINT_NAME = O.name WHERE O.xtype in (''F'',''PK'')'
EXECUTE(@sqltext)

-- Get column level 
DECLARE @TABLE_NAME varchar(128)

DECLARE column_cursor CURSOR FAST_FORWARD FOR 
SELECT [tableschema], [tablename] FROM ##temp___DataDictionary_schema

OPEN column_cursor
FETCH NEXT FROM column_cursor INTO @TABLE_SCHEMA, @TABLE_NAME

WHILE @@FETCH_STATUS = 0
BEGIN
-- display all columns under MyTable
SET @sqltext = 'INSERT INTO ##temp___DataDictionary ([tableschema], [tablename],[columnname], [description]) SELECT '
+ '''' + @TABLE_SCHEMA + '''' + ',' 
+ '''' + @TABLE_NAME + '''' + ', objname, cast(value as nvarchar(4000))'
+ ' FROM ' + @databasename + '.sys.fn_listextendedproperty (NULL, ''schema'', '
+ '''' + @TABLE_SCHEMA + '''' + ', ''table'', '
+ '''' + @TABLE_NAME + '''' + ', ''column'', default)'

EXECUTE(@sqltext)

FETCH NEXT FROM column_cursor INTO @TABLE_SCHEMA, @TABLE_NAME
END

CLOSE column_cursor
DEALLOCATE column_cursor

UPDATE D
SET D.[xtype] = K.[xtype]
FROM ##temp___DataDictionary D JOIN ##temp___DataDictionary_keys K
ON D.tableschema = K.tableschema AND D.tablename = K.tablename AND D.columnname = K.columnname

SELECT @@servername as servername,@databasename as dbname,tableschema,tablename,columnname,[xtype],[description] 
FROM ##temp___DataDictionary
ORDER BY @@servername ,dbname,tableschema,tablename,columnname,[xtype] asc

DROP TABLE ##temp___DataDictionary

DROP TABLE ##temp___DataDictionary_keys

END
```

