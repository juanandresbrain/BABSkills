# dbo.VW_tmpSysObjects

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.VW_tmpSysObjects"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql
create view VW_tmpSysObjects

as

---sql 2005
SELECT DISTINCT o.name AS Object_Name, 
replace(replace(substring(m.definition, charindex('Description:', m.definition, 0), 100), '
', ' '), '	', ' ') description,
convert(varchar, o.create_date, 101) create_date, 
convert(varchar, o.modify_date, 101) modify_date, 
m.definition
FROM sys.sql_modules m (nolock)
INNER JOIN sys.objects o (nolock) ON m.object_id=o.object_id
where o.type_desc = 'SQL_STORED_PROCEDURE'
and o.name not like '%bak%'
and o.name not like '%back%'
and o.name not like '%$%'
```

