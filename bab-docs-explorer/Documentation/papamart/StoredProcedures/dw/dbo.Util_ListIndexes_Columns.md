# dbo.Util_ListIndexes_Columns

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Util_ListIndexes_Columns"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
/**
*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
Util_ListIndexes_Columns
By Jesse Roberge - YeshuaAgapao@Yahoo.com
Update - Fixed existance check for drop

Databears -- use this to investigate index consolidation.

Lists details for all indexes on one or more tables / schemas, including row count and size.
If you want one row per index instead of one row per member column at the expense of data type and other column information,
  then use Util_ListIndexes instead.

Required Input Parameters
	none

Optional Input Parameters
	@SchemaName sysname=''		Filters to a single schema.  Can use LIKE wildcards.  All schemas if blank.  Accepts LIKE Wildcards.
	@TableName sysname=''		Filters to a single table.  Can use LIKE wildcards.  All tables if blank.  Accepts LIKE Wildcards.

Usage
	EXECUTE Util_ListIndexes_Columns 'dbo', 'Cart'

Copyright:
	Licensed under the L-GPL - a weak copyleft license - you are permitted to use this as a component of a proprietary database and call this from proprietary software.
	Copyleft lets you do anything you want except plagarize, conceal the source, proprietarize modifications, or prohibit copying & re-distribution of this script/proc.

	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    see <http://www.fsf.org/licensing/licenses/lgpl.html> for the license text.

*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
**/

CREATE PROCEDURE dbo.Util_ListIndexes_Columns
	@SchemaName sysname='',
	@TableName sysname=''
AS

SELECT
	sys.schemas.schema_id, sys.schemas.name AS schema_name,
	sys.objects.object_id, sys.objects.name AS object_name,
	sys.indexes.index_id, sys.indexes.name AS index_name,
	sys.indexes.type, sys.indexes.type_desc,
	partitions.Rows, partitions.SizeMB,
	sys.indexes.is_unique, sys.indexes.is_primary_key, sys.indexes.is_unique_constraint,
	sys.index_columns.index_column_id, sys.index_columns.key_ordinal, sys.index_columns.partition_ordinal,
	sys.columns.column_id, sys.columns.name AS column_name,
	sys.index_columns.is_included_column, sys.index_columns.is_descending_key,
	sys.columns.system_type_id, sys.types.name AS type_name,
	sys.columns.max_length, sys.columns.precision, sys.columns.scale,
	sys.columns.is_nullable, sys.columns.is_identity, sys.columns.is_computed
FROM
	sys.objects
	JOIN sys.schemas ON sys.objects.schema_id=sys.schemas.schema_id
	JOIN sys.indexes ON sys.objects.object_id=sys.indexes.object_id
	JOIN (
		SELECT
			object_id, index_id, SUM(row_count) AS Rows,
			CONVERT(numeric(19,3), CONVERT(numeric(19,3), SUM(in_row_reserved_page_count+lob_reserved_page_count+row_overflow_reserved_page_count))/CONVERT(numeric(19,3), 128)) AS SizeMB
		FROM sys.dm_db_partition_stats
		GROUP BY object_id, index_id
	) AS partitions ON sys.indexes.object_id=partitions.object_id AND sys.indexes.index_id=partitions.index_id
	JOIN sys.index_columns ON sys.indexes.object_id=sys.index_columns.object_id AND sys.indexes.index_id=sys.index_columns.index_id
	JOIN sys.columns ON sys.index_columns.column_id=sys.columns.column_id AND sys.index_columns.object_id=sys.columns.object_id
	JOIN sys.types ON sys.columns.system_type_id=sys.types.user_type_id
WHERE
	sys.schemas.name LIKE CASE WHEN @SchemaName='' THEN sys.schemas.name ELSE @SchemaName END
	AND sys.objects.name LIKE CASE WHEN @TableName='' THEN sys.objects.name ELSE @TableName END
ORDER BY
	sys.schemas.name, sys.objects.name, sys.indexes.name,
	sys.index_columns.is_included_column, sys.index_columns.key_ordinal, sys.index_columns.index_column_id
```

