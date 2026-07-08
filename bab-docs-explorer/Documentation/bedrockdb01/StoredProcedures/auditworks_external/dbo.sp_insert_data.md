# dbo.sp_insert_data

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_insert_data"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[sp_insert_data] @table_name varchar(30),
@include_identity_col tinyint = 1
AS
DECLARE @sql_command nvarchar(max),
        @sql_prefix nvarchar(max),
        @column_name nvarchar(50), 
        @col_value nvarchar(max), @last int, @first int,
        @identity_column varchar(50), @rows int

SET NOCOUNT ON 
SELECT @last = max(colorder), @first = min(colorder), @identity_column = max(CASE WHEN COLUMNPROPERTY(t.id,c.name,'IsIdentity') = 1 AND @include_identity_col = 1 THEN c.name ELSE ' ' END), @sql_command = ' ', @sql_prefix = ' '
 FROM sysobjects t, syscolumns c
WHERE t.type = 'U' and t.name = @table_name
  AND t.id = c.id
  AND lower(type_name(c.xusertype)) <> 'image'
  AND (@include_identity_col = 1 OR COLUMNPROPERTY(t.id,c.name,'IsIdentity') <> 1)  
  AND c.autoval IS NULL
  
IF @last IS NULL
BEGIN
  PRINT 'Invalid table name'
  RETURN
END

SELECT @sql_prefix = ' SELECT ''INSERT INTO ' + @table_name + '(' -- VALUES('' + '

DECLARE processing_cursor CURSOR
    FOR
 SELECT CASE WHEN lower(type_name(c.xtype)) NOT LIKE '%char%' AND lower(type_name(c.xtype)) NOT LIKE '%date%' 
             THEN 'CASE WHEN ' + c.name + ' IS NOT NULL THEN CONVERT(nvarchar(4000), ' + c.name + ') ELSE ''NULL'' END' 
             ELSE CASE WHEN lower(type_name(c.xtype)) LIKE '%date%'
                       THEN 'CASE WHEN ' + c.name + ' IS NOT NULL THEN  '''''''' + CONVERT(nvarchar(4000), ' + c.name + ', 101)  + '' '' + CONVERT(nvarchar(4000), ' + c.name + ',108) + '''''''' ELSE ''NULL'' END'  
                       ELSE 'CASE WHEN ' + c.name + ' IS NOT NULL THEN '''''''' + REPLACE(' + c.name  + ', '''''''', '''''''''''') + '''''''' ELSE ''NULL'' END' 
                  END  END
        + CASE WHEN colorder <> @last
        THEN ' + '', '' + '  ELSE ' + '')'' FROM ' + @table_name END,
        CASE WHEN colorder <> @first THEN ', ' ELSE '' END + c.name + CASE WHEN colorder = @last THEN ') VALUES('' + ' ELSE '' END 
   FROM sysobjects t, syscolumns c
  WHERE t.type = 'U' and t.name = @table_name
    AND t.id = c.id
    AND lower(type_name(c.xusertype)) NOT IN ('image', 'timestamp')
    AND (@include_identity_col = 1 OR COLUMNPROPERTY(t.id,c.name,'IsIdentity')<> 1)  
    AND c.autoval IS NULL
  ORDER by colorder

OPEN processing_cursor

 FETCH processing_cursor
  INTO @col_value, @column_name

 WHILE @@fetch_status = 0 
 BEGIN
   SELECT @sql_command = @sql_command + @col_value,
          @sql_prefix = @sql_prefix + @column_name
	
  FETCH processing_cursor
  INTO @col_value, @column_name
 END /* while not end of processing_cursor */

CLOSE processing_cursor
DEALLOCATE processing_cursor

SELECT @sql_command = @sql_prefix + @sql_command
PRINT @sql_command

IF @identity_column <> ' ' 
  SELECT 'SET IDENTITY_INSERT ' + @table_name + ' ON
GO'

EXEC sp_executesql @sql_command

IF @identity_column <> ' ' 
  SELECT 'SET IDENTITY_INSERT ' + @table_name + ' OFF
GO'

RETURN
```

