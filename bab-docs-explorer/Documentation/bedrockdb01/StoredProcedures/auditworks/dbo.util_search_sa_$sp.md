# dbo.util_search_sa_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_search_sa_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[util_search_sa_$sp] 


AS
DECLARE
@erno               int

/************************************************************************************
   Name: util_search_sa_$sp
   Author: Paul
   Description: To search for column names and strings.
                logic is for SQL2005 and higher
                
**************************************************************************************

Jan12,15 Paul  added search script to find procs and tables referenced by a proc (SQL 2008 and up)
Feb12,14 Paul  added scripts to find column names used by unique indices including PK and unique key constraints
Sep10,13 Paul

*/


/* Search for a column name in all tables */

SELECT t.name AS table_name,
c.user_type_id, c.max_length
-- SCHEMA_NAME(schema_id) AS schema_name,
-- c.name AS column_name
FROM sys.tables AS t
INNER JOIN sys.columns c ON t.OBJECT_ID = c.OBJECT_ID
WHERE c.name LIKE 'tax_level%'
ORDER BY table_name; 


-- Search for columns with user_type_id 48 (tinyint)

select t.name as table_name
-- c.user_type_id, c.max_length
-- schema_name(schema_id) as schema_name,
-- c.name as column_name
from sys.tables as t
inner join sys.columns c on t.object_id = c.object_id
where c.name like 'tax_level%'
and c.user_type_id = 48
and t.name not like 'vicci%'
order by table_name; 


-- Simple script to identify all the columns with datatype TEXT in specific database
SELECT OBJECT_NAME(c.OBJECT_ID) TableName, c.name ColumnName
FROM sys.columns AS c
JOIN sys.types AS t ON c.user_type_id=t.user_type_id
WHERE t.name = 'text' --you can change text to other datatypes
ORDER BY c.OBJECT_ID;


/* search for varchar datatypes in tables (excludes nvarchar).
   also excluding some obsolete objects from this search */

SELECT OBJECT_NAME(c.OBJECT_ID) as TableName, c.name as ColumnName -- , t.name
-- INTO #util_column_list
FROM sys.columns AS c
JOIN sys.types AS t ON c.user_type_id=t.user_type_id
WHERE t.name = 'varchar' --you can change text to other datatypes
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'bk%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'db%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'export_info%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'export_reg%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'export_format%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'export_store%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'Ex_Q%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'flash%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'lg_%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'nsb%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'SA_EV%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'util%'
AND OBJECT_NAME(c.OBJECT_ID) NOT LIKE 'vc_cat%'
ORDER BY OBJECT_NAME(c.OBJECT_ID);

/* other examples for CRDM datatypes .
  Note: The datatypes in these queries are no longer used by CRDM as of CRDM 5.1 Mssql */

/*
SELECT OBJECT_NAME(c.OBJECT_ID) TableName, c.name ColumnName
FROM sys.columns AS c
JOIN sys.types AS t ON c.user_type_id=t.user_type_id
WHERE t.name IN ('T_CODE', 'T_CODE2', 'T_CODE3', 'T_CODE4', 'T_CODE5', 'T_CODE6','T_COMPUTER_NAME') 
ORDER BY c.OBJECT_ID;

SELECT OBJECT_NAME(c.OBJECT_ID) TableName, c.name ColumnName
FROM sys.columns AS c
JOIN sys.types AS t ON c.user_type_id=t.user_type_id
WHERE t.name IN ('T_ALPHANUM_VALUE', 'T_DESCRIPTION', 'T_ENCRYPTED_CREDIT_CARD_NUMBER', 'T_LONG_CODE',
   'T_NAME', 'T_POSTCODE','T_SHORT_DESC', 'T_SHORT_NAME', 'T_SYSTEM_CODE') 
ORDER BY c.OBJECT_ID;

*/



/* Search procs, triggers and view definitions for a string, list the object names only */

SELECT DISTINCT obj.name AS Object_Name, obj.Type -- , obj.type_desc 
FROM sys.sql_modules sm 
    INNER JOIN sys.objects obj ON sm.object_id = obj.object_id 
WHERE sm.definition LIKE '%media_reconciliation%'
AND obj.Type IN ('P', 'TR', 'V')
ORDER BY Object_Name

/* Search procs only */

SELECT OBJECT_NAME(object_id) as object_name
FROM sys.procedures
WHERE OBJECT_DEFINITION(object_id) LIKE '%media_reconciliation%'
ORDER BY object_name

/* same as above but capture proc definition (need to use grid for capture in gui) */

SELECT OBJECT_NAME(object_id) as object_name, OBJECT_DEFINITION(object_id)
FROM sys.procedures
WHERE OBJECT_DEFINITION(object_id) LIKE '%media_reconciliation%'
ORDER BY object_name


/* Search only view definitions for a string, e.g. Foundation db name, and list the object names only */

SELECT DISTINCT obj.name AS Object_Name -- , sm.definition , obj.Type , obj.type_desc 
FROM sys.sql_modules sm 
    INNER JOIN sys.objects obj ON sm.object_id = obj.object_id 
WHERE sm.definition LIKE '%fn8%'
AND obj.Type IN ('V')
ORDER BY Object_Name


/* show objects referenced by a proc, including other procs and user tables , SQL 2008 and up */

--SELECT * 
--FROM sys.dm_sql_referenced_entities('dbo.edit_header_$sp', 'OBJECT');

/* same query to show procs, but excluding user tables :

SELECT DISTINCT OBJECTPROPERTYEX(referenced_id, 'BASETYPE'), 
       referenced_database_name, referenced_schema_name, 
       referenced_entity_name 
FROM sys.dm_sql_referenced_entities('dbo.edit_header_$sp', 'OBJECT')
WHERE OBJECTPROPERTYEX(referenced_id, 'BASETYPE') <> 'U';

*/

/* SA 5.1 - list all triggers and procs that use a try catch,
   and exclude procs that do not require separate qa testing */

SELECT DISTINCT obj.name AS Object_Name, obj.Type -- , obj.type_desc 
FROM sys.sql_modules sm 
    INNER JOIN sys.objects obj ON sm.object_id = obj.object_id 
WHERE lower(sm.definition) LIKE '%begin try%'
and obj.name NOT LIKE 'test%'
and obj.name NOT LIKE 'vicci%'
and obj.name NOT LIKE 'util%'
and obj.name NOT LIKE 'trig%'
and obj.name NOT LIKE 'common%'
and obj.name NOT LIKE 'rprt%'
and obj.name NOT LIKE 'ENCR%'
and obj.name NOT LIKE 'scale%'
and obj.name NOT LIKE 'mew%'
and obj.name NOT LIKE 'partition%'
AND obj.Type IN ('P', 'TR', 'V')
ORDER BY obj.Type, Object_Name



/* List primary key columns */

SELECT
--  SCHEMA_NAME(T.schema_id) AS table_schema,
  T.name as TableName,
  KC.name AS constraint_name,
  COL_NAME(T.object_id, IC.column_id) AS column_name,
  IC.key_ordinal
--  , IC.is_descending_key
-- INTO #util_pk_column_list
FROM
  sys.tables AS T
  INNER JOIN
  sys.key_constraints AS KC
  ON KC.parent_object_id = T.object_id
  INNER JOIN
  sys.indexes AS I
  ON KC.unique_index_id = I.index_id
  AND KC.parent_object_id = I.object_id
  INNER JOIN
  sys.index_columns AS IC
  ON I.object_id = IC.object_id
  AND I.index_id = IC.index_id
WHERE
  T.type = 'U'
  AND IC.is_included_column = 0
ORDER BY
  T.object_id,
  IC.key_ordinal;


/* List all Foreign keys and the referenced column */

SELECT f.name AS ForeignKey,
OBJECT_NAME(f.parent_object_id) AS TableName,
COL_NAME(fc.parent_object_id,
fc.parent_column_id) AS ColumnName,
OBJECT_NAME (f.referenced_object_id) AS ReferenceTableName,
COL_NAME(fc.referenced_object_id,
fc.referenced_column_id) AS ReferenceColumnName
FROM sys.foreign_keys AS f
INNER JOIN sys.foreign_key_columns AS fc
ON f.OBJECT_ID = fc.constraint_object_id;



/* List all Unique indices including pk and unique key constraints.
    The list will include PK and unique key constraints as well as unique indices that are not constraints. */

/*
SELECT     obj.name as TableName, col.name as ColumnName, idx.name as IndexName
 INTO #util_uk_column_list
FROM         sys.objects AS obj INNER JOIN
                      sys.columns AS col ON col.object_id = obj.object_id INNER JOIN
                      sys.index_columns AS idx_cols ON idx_cols.column_id = col.column_id AND idx_cols.object_id = col.object_id INNER JOIN
                      sys.indexes AS idx ON idx_cols.index_id = idx.index_id AND idx.object_id = col.object_id
WHERE     (idx.is_unique = 1)
AND obj.name NOT LIKE 'sys%'
-- AND       (obj.name = 'pluginUsers')
ORDER BY obj.name, col.name;
*/

/* Example using temp tables created above.
    Find tables that have pk columns with datatypes = varchar */
/*
select distinct cl.TableName 
from #util_column_list cl, #util_pk_column_list pk 
where cl.TableName   = pk.TableName
and   cl. ColumnName = pk.column_name;
*/

/* Find tables that have unique key index on columns with datatypes = varchar.
   The list will include PK and unique key constraints as well as unique indices that are not constraints. */

/*
select distinct cl.TableName 
from #util_column_list cl, #util_uk_column_list pk 
where cl.TableName   = pk.TableName
and   cl. ColumnName = pk.ColumnName

*/


/* Find nolock hints

SELECT distinct o.name -- s.name, o.name, m.definition
  FROM sys.schemas AS s
  INNER JOIN sys.objects AS o
  ON s.[schema_id] = o.[schema_id]
  INNER JOIN sys.sql_modules AS m
  ON o.[object_id] = m.[object_id]
  WHERE UPPER(m.[definition]) LIKE N'%UPDATE%SET%FROM%NOLOCK%'
     OR UPPER(m.[definition]) LIKE N'%DELETE%FROM%NOLOCK%'
     OR UPPER(m.[definition]) LIKE N'%WITH%(%SELECT%NOLOCK%)%DELETE%'
     OR UPPER(m.[definition]) LIKE N'%WITH%(%SELECT%NOLOCK%)%UPDATE%';
*/



/* the following is for SQL2000 environments */

/*
SELECT x.name
FROM (
SELECT SO.name, SO.type, COUNT(1) as page_count
FROM sysobjects SO, syscomments SC
WHERE SO.id = SC.id
AND SC.text LIKE '%media_reconciliation%' 
-- AND SO.type = 'P' -- for procedures only
GROUP BY SO.name, SO.type ) x
ORDER BY x.name
*/


RETURN
```

