# dbo.spIndexesReadd

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spIndexesReadd"]
    IndexSnapshot(["IndexSnapshot"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| IndexSnapshot |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.spIndexesReadd (
	@username varchar(200),
	@tablename varchar(200)
)
AS

set nocount on


/*
-- declare @username varchar(100)
-- declare @tablename varchar(100)
-- set @tablename = 'MAILERS_2007SUMMER_MAIN'
-- set @username = 'dbo'
*/


declare @sql varchar(8000)

declare @createscript varchar(8000)

declare curIndex cursor
for	
	select i.createscript
	from IndexSnapshot i
		join (
			select username, tablename, max(datestamp) datestamp
			from IndexSnapshot s
			group by username, tablename
		) d
		on d.username = i.username
		and d.tablename = i.tablename
		and d.datestamp = i.datestamp
	where i.tablename = @tablename 
		and i.username = @username
		and i.indexname not in (
			select i.name
			FROM
				sysobjects o
				join SYSINDEXES I
				on i.id = o.id
				join sysusers u
				on u.uid = o.uid
			WHERE I.INDID > 0 
				AND I.INDID < 255 
				AND (I.STATUS & 64)=0
				and o.name = @tablename
				and u.name = @username
		)
open curIndex

fetch next from curIndex into @createscript
while (@@fetch_STATUS <> -1)
begin
	set @SQL = @createscript
 	print @sql
  	exec (@SQL)

	fetch next from curIndex into @createscript
end
close curIndex
deallocate curIndex
```

