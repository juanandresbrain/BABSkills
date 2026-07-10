# dbo.s_SpaceUsed

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.s_SpaceUsed"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
Create procedure s_SpaceUsed
@SourceDB	varchar(128)
as
/*
exec s_SpaceUsed 'mydb'
*/

set nocount on

declare @sql varchar(128)
	create table #tables(name varchar(128))
	
	select @sql = 'insert #tables select TABLE_NAME from ' + @SourceDB + '.INFORMATION_SCHEMA.TABLES where TABLE_TYPE = ''BASE TABLE'''
	exec (@sql)
	
	create table #SpaceUsed (name varchar(128), rows varchar(11), reserved varchar(18), data varchar(18), index_size varchar(18), unused varchar(18))
	declare @name varchar(128)
	select @name = ''
	while exists (select * from #tables where name > @name)
	begin
		select @name = min(name) from #tables where name > @name
		select @sql = 'exec ' + @SourceDB + '..sp_executesql N''insert #SpaceUsed exec sp_spaceused ' + @name + ''''
		exec (@sql)
	end
	select * from #SpaceUsed
	drop table #tables
	drop table #SpaceUsed
```

