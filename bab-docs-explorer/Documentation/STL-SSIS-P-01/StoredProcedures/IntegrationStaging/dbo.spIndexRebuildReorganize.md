# dbo.spIndexRebuildReorganize

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spIndexRebuildReorganize"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc spIndexRebuildReorganize

as

set nocount on

IF (Object_ID('tempdb..#Indexes') IS NOT NULL) DROP TABLE #Indexes;
with
IndexData as
	(
		SELECT 
			dbschemas.[name] as 'SchemaName',
			dbtables.[name] as 'TableName',
			dbindexes.[name] as 'IndexName',
			indexstats.avg_fragmentation_in_percent,
			indexstats.page_count,
			case 
				when avg_fragmentation_in_percent between 5 AND 30 then 'Reorganize'
				when avg_fragmentation_in_percent > 30	then 'Rebuild'
				else 'No Action'
			end as ActionRequired
		FROM sys.dm_db_index_physical_stats (DB_ID(), NULL, NULL, NULL, NULL) AS indexstats
		INNER JOIN sys.tables dbtables on dbtables.[object_id] = indexstats.[object_id]
		INNER JOIN sys.schemas dbschemas on dbtables.[schema_id] = dbschemas.[schema_id]
		INNER JOIN sys.indexes AS dbindexes ON dbindexes.[object_id] = indexstats.[object_id]
		AND indexstats.index_id = dbindexes.index_id
		WHERE 1=1
		and indexstats.database_id = DB_ID()
		and dbschemas.[name] in ('WEB','ERP')
		and dbindexes.[name] is not null --these would be the heap
	)
select 
	SchemaName,
	TableName,
	'ALTER INDEX ' + IndexName + ' ON ' + SchemaName + '.' + TableName + ' ' + ActionRequired as IndexCommand,
	'Update Statistics ' + SchemaName + '.' + TableName + ' with fullscan' as StatisticsCommand
into #Indexes
from IndexData 
where ActionRequired in ('Rebuild', 'Reorganize')
order by 1,2 

if (select count(*) from #Indexes) > 0
begin
	declare 
		@count int,
		@IndexCommand varchar(1000),
		@StatisticsCommand varchar(1000)
		
	select @count = count(*) from #Indexes

	while @count > 0
		begin
			select @Count = count(*) from #Indexes
		
			select @IndexCommand = max(IndexCommand) from #Indexes 
			select @StatisticsCommand = StatisticsCommand from #Indexes where IndexCommand = @IndexCommand

			exec(@IndexCommand)

			exec(@StatisticsCommand)
			
			delete from #Indexes
			where IndexCommand = @IndexCommand
		
			select @Count = count(*) from #Indexes

			if @Count = 0
				break
			else
				continue
		end
end
```

