# dbo.sp_help1

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_help1"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
create proc [dbo].[sp_help1] @table_name varchar(30)
AS
Set nocount on
DECLARE @type varchar(10)
SELECT @type = type
FROM sysobjects t
where t.name = @table_name
IF @type NOT IN ('U', 'V')
  SELECT 'Invalid type:  ' + @type
ELSE
  IF @type = 'V'
    SELECT 'View:  ' + @table_name
  ELSE
    SELECT 'Table:  ' + @table_name

SELECT convert(varchar(30), c.name) Column_Name, 
       convert(varchar(45), CASE WHEN type_name(c.xtype) like '%char%' OR type_name(c.xtype) like '%binary%' 
                     THEN type_name(c.xtype) + '(' + convert(varchar,c.prec) + ')'
                     ELSE CASE WHEN type_name(c.xtype) in ('numeric', 'decimal') 
                               THEN type_name(c.xtype) + '(' + convert(varchar,c.prec) + ',' + convert(varchar,c.scale) + ')'
                               ELSE type_name(c.xtype) END END + CASE WHEN c.xusertype <> c.xtype THEN ' ' + type_name(c.xusertype) ELSE ' ' END) Data_Type,
       c.isnullable Nullable,
       COLUMNPROPERTY(t.id,c.name,'IsIdentity') Is_Identity,  --revised
       convert(nvarchar(53), CASE WHEN SUBSTRING(d.text, 1, 1) = '(' THEN SUBSTRING(d.text, 2, len(d.text) - 2) ELSE d.text END) Default_Value
from sysobjects t
     INNER JOIN syscolumns c
        ON t.id = c.id
     LEFT OUTER JOIN syscomments d
        ON c.cdefault = d.id
where t.type IN ('U', 'V') and t.name = @table_name           

return
```

