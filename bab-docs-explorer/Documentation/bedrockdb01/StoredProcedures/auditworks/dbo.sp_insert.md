# dbo.sp_insert

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_insert"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
create proc [dbo].[sp_insert] @table_name varchar(30),
@include_identity_col tinyint = 1
AS

DECLARE @last int, @first int, @identity_column varchar(50), @rows int
SET nocount ON
SELECT @last = max(colorder), @first = min(colorder), @identity_column = max(CASE WHEN COLUMNPROPERTY(t.id,c.name,'IsIdentity') = 1 AND @include_identity_col = 1 THEN c.name ELSE ' ' END)
from sysobjects t, syscolumns c
where t.type IN ('U', 'V') and t.name = @table_name
and t.id = c.id
and (@include_identity_col = 1 OR COLUMNPROPERTY(t.id,c.name,'IsIdentity') <> 1)
AND c.autoval IS NULL


SELECT 'SET IDENTITY_INSERT ' + @table_name + ' ON
GO'
WHERE @identity_column <> ' ' 

select substring('INSERT into ' + @table_name + '(
       ', 1, 255 * (1-(sign(colorder - @first))))
	+
       substring(substring('       ', 1, 13 + len(@table_name)), 1, 255 * sign(colorder - @first)) +
c.name + Substring(') , ', 1 + 2*sign(@last - colorder), 2)
from sysobjects t, syscolumns c
where t.type IN ('U', 'V') and t.name = @table_name
and t.id = c.id
and (@include_identity_col = 1 OR COLUMNPROPERTY(t.id,c.name,'IsIdentity') <> 1)
AND c.autoval IS NULL
order by colorder

SELECT CASE WHEN @identity_column <> ' ' THEN 'SET IDENTITY_INSERT ' + @table_name + ' OFF
GO' ELSE 'GO' END


return
```

