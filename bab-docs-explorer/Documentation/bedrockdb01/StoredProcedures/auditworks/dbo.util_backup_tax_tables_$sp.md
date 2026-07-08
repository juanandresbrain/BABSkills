# dbo.util_backup_tax_tables_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_backup_tax_tables_$sp"]
    vc_category(["vc_category"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| vc_category |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[util_backup_tax_tables_$sp]

AS

/*
Comment
	This stored procedure can be used to backup all tax master tables currently populated.
	The backup table name will be named similarly as the source, but include a _BK_YYYYMMDDHHmiss extension.
	Ex. tax_rate will be backup up as tax_rate_BK_20151007083059
	All tables backed up will contain similar extension per execution of procedure. 		


Author:			
Stephen M.						
*/

DECLARE 
@tablename varchar(40),
@extension varchar(16) ,
@sqlstring nvarchar(2000)

SELECT @extension = REPLACE(CONVERT(VARCHAR(8), GETDATE(), 112)+CONVERT(VARCHAR(8), GETDATE(), 114), ':','')

DECLARE tax_table_list CURSOR
  FOR
    SELECT tb_name FROM vc_category
	WHERE tb_name LIKE '%tax%'
	AND UPPER(tb_type) IN ('USER','COMBO')
FOR READ ONLY

OPEN tax_table_list

FETCH tax_table_list
INTO @tablename

WHILE @@FETCH_STATUS = 0
BEGIN
	SET @sqlstring = N'IF EXISTS (SELECT 1 FROM ' + @tablename +') BEGIN SELECT * INTO ' + @tablename + '_BK_' + @extension + ' FROM ' + @tablename + ' END'

	EXEC sp_executesql @sqlstring

	FETCH NEXT FROM tax_table_list into @tablename

END
CLOSE tax_table_list
DEALLOCATE tax_table_list
```

