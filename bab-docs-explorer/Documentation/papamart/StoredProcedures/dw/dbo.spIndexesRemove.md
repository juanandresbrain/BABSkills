# dbo.spIndexesRemove

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spIndexesRemove"]
    IndexSnapshot(["IndexSnapshot"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| IndexSnapshot |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.spIndexesRemove (
	@username varchar(200),
	@tablename varchar(200)
)
 AS

set nocount on

-- drop table IndexSnapshot
-- create table IndexSnapshot (
-- 	username	varchar(500),
-- 	tablename	varchar(500),
-- 	indexname	varchar(500),
-- 	datestamp	datetime,
-- 	createscript	varchar(8000)
-- )

/*
declare @tablename varchar(100)
declare @username varchar(100)
set @tablename = 'QXXX_VALENTINES2008_MAILER_UK_SUMMARY_CONSOLIDATED'
set @username = 'dbo'
*/

declare @index varchar(500)
declare @now datetime
set @now = getdate()

IF (Object_ID('tempdb..#TMP') IS NOT NULL) DROP TABLE #TMP
SELECT 
	REPLICATE(' ',4000) AS COLNAMES ,
	u.name as tableownername,
	OBJECT_NAME(I.ID) AS TABLENAME,
	I.ID AS TABLEID,
	I.INDID AS INDEXID,
	I.NAME AS INDEXNAME,
	I.STATUS,
	INDEXPROPERTY (I.ID,I.NAME,'ISUNIQUE') AS ISUNIQUE,
	INDEXPROPERTY (I.ID,I.NAME,'ISCLUSTERED') AS ISCLUSTERED,
	INDEXPROPERTY (I.ID,I.NAME,'INDEXFILLFACTOR') AS INDEXFILLFACTOR
INTO #TMP
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
	--uncomment below to eliminate PK or UNIQUE indexes;
	--what i call 'normal' indexes
--	AND   INDEXPROPERTY (I.ID,I.NAME,'ISUNIQUE')       =0
--	AND   INDEXPROPERTY (I.ID,I.NAME,'ISCLUSTERED') =0


DECLARE
  @ISQL VARCHAR(4000),
  @TABLEID INT,
  @INDEXID INT,
  @MAXTABLELENGTH INT,
  @MAXINDEXLENGTH INT
  --USED FOR FORMATTING ONLY
    SELECT @MAXTABLELENGTH=MAX(LEN(TABLENAME)) FROM #TMP
    SELECT @MAXINDEXLENGTH=MAX(LEN(INDEXNAME)) FROM #TMP

    DECLARE C1 CURSOR FOR
      SELECT TABLEID,INDEXID FROM #TMP  
    OPEN C1
      FETCH NEXT FROM C1 INTO @TABLEID,@INDEXID
        WHILE @@FETCH_STATUS <> -1
          BEGIN
	SET @ISQL = ''
	SELECT @ISQL=@ISQL + ISNULL(SYSCOLUMNS.NAME,'') + ',' FROM SYSINDEXES I
	INNER JOIN SYSINDEXKEYS ON I.ID=SYSINDEXKEYS.ID AND I.INDID=SYSINDEXKEYS.INDID
	INNER JOIN SYSCOLUMNS ON SYSINDEXKEYS.ID=SYSCOLUMNS.ID AND SYSINDEXKEYS.COLID=SYSCOLUMNS.COLID
	WHERE I.INDID > 0 
	AND I.INDID < 255 
	AND (I.STATUS & 64)=0
	AND I.ID=@TABLEID AND I.INDID=@INDEXID
	ORDER BY SYSCOLUMNS.COLID
	UPDATE #TMP SET COLNAMES=@ISQL WHERE TABLEID=@TABLEID AND INDEXID=@INDEXID

	FETCH NEXT FROM C1 INTO @TABLEID,@INDEXID
         END
      CLOSE C1
      DEALLOCATE C1
  --AT THIS POINT, THE 'COLNAMES' COLUMN HAS A TRAILING COMMA
  UPDATE #TMP SET COLNAMES=LEFT(COLNAMES,LEN(COLNAMES) -1)

insert into IndexSnapshot (username, tablename, indexname, datestamp, createscript)
select @username, @tablename, indexname, getdate(),
	'CREATE ' 
    + CASE WHEN ISUNIQUE     = 1 THEN ' UNIQUE ' ELSE '' END 
    + CASE WHEN ISCLUSTERED = 1 THEN ' CLUSTERED ' ELSE '' END 
    + ' INDEX [' + INDEXNAME + ']' 
    +' ON [' + tableownername + '].[' + TABLENAME + '] '
    + '(' + COLNAMES + ')' 
    + CASE WHEN INDEXFILLFACTOR = 0 THEN ''  ELSE  ' WITH FILLFACTOR = ' + CONVERT(VARCHAR(10),INDEXFILLFACTOR)   END
    FROM #TMP
order by tablename

-- *************************************************************************************************
-- *************************************************************************************************
-- *************************************************************************************************

-- CREATE  INDEX [IX_MAILERS_2007SUMMER_MAIN_ADDRESS] ON [DBO].[MAILERS_2007SUMMER_MAIN] (ADDRESS1,POSTAL_CODE) WITH FILLFACTOR = 51
-- CREATE  INDEX [IX_MAILERS_2007SUMMER_MAIN_PROMOCODE] ON [DBO].[MAILERS_2007SUMMER_MAIN] (PROMOCODE) WITH FILLFACTOR = 51
-- CREATE  INDEX [IX_MAILERS_2007SUMMER_MAIN_CUSTOMER_NUM_CRM] ON [DBO].[MAILERS_2007SUMMER_MAIN] (CUSTOMER_NUM_CRM) WITH FILLFACTOR = 51


-- declare @username varchar(100)
-- declare @tablename varchar(100)
-- set @tablename = 'MAILERS_2007SUMMER_MAIN'
-- set @username = 'dbo'

declare @indexname varchar(500)
declare @sql varchar(8000)

declare curIndex cursor
for	
	select i.username, i.tablename, i.indexname 
	from IndexSnapshot i
		join (
			select username, tablename, indexname, max(datestamp) datestamp
			from IndexSnapshot s
			where datestamp > @now
			group by username, tablename, indexname
		) d
		on d.username = i.username
		and d.tablename = i.tablename
		and d.indexname = i.indexname
		and d.datestamp = i.datestamp
	where i.tablename = @tablename 
		and i.username = @username
open curIndex

fetch next from curIndex into @username, @tablename, @indexname
while (@@fetch_STATUS <> -1)
begin
	set @SQL = 'drop index [' + @username + '].[' + @tablename + '].[' + @indexname + ']'
 	print @sql
  	exec (@SQL)

	fetch next from curIndex into @username, @tablename, @indexname
end
close curIndex
deallocate curIndex

-- -- *************************************************************************************************
-- -- *************************************************************************************************
-- -- *************************************************************************************************
-- -- CREATE  INDEX [IX_MAILERS_2007SUMMER_MAIN_ADDRESS] ON [DBO].[MAILERS_2007SUMMER_MAIN] (ADDRESS1,POSTAL_CODE) WITH FILLFACTOR = 51
-- -- CREATE  INDEX [IX_MAILERS_2007SUMMER_MAIN_PROMOCODE] ON [DBO].[MAILERS_2007SUMMER_MAIN] (PROMOCODE) WITH FILLFACTOR = 51
-- -- CREATE  INDEX [IX_MAILERS_2007SUMMER_MAIN_CUSTOMER_NUM_CRM] ON [DBO].[MAILERS_2007SUMMER_MAIN] (CUSTOMER_NUM_CRM) WITH FILLFACTOR = 51
-- 
-- -- select * from IndexSnapshot
-- 
-- -- declare @username varchar(100)
-- -- declare @tablename varchar(100)
-- -- set @tablename = 'MAILERS_2007SUMMER_MAIN'
-- -- set @username = 'dbo'
-- -- declare @sql varchar(8000)
-- 
-- declare @createscript varchar(8000)
-- 
-- declare curIndex cursor
-- for	
-- 	select i.createscript
-- 	from IndexSnapshot i
-- 		join (
-- 			select username, tablename, max(datestamp) datestamp
-- 			from IndexSnapshot s
-- 			group by username, tablename
-- 		) d
-- 		on d.username = i.username
-- 		and d.tablename = i.tablename
-- 		and d.datestamp = i.datestamp
-- 	where i.tablename = @tablename 
-- 		and i.username = @username
-- open curIndex
-- 
-- fetch next from curIndex into @createscript
-- while (@@fetch_STATUS <> -1)
-- begin
-- 	set @SQL = @createscript
--  	print @sql
--   	exec (@SQL)
-- 
-- 	fetch next from curIndex into @createscript
-- end
-- close curIndex
-- deallocate curIndex
-- 

-- select * from IndexSnapshot

--SELECT * FROM #TMP


-- SELECT top 100 
-- 	REPLICATE(' ',4000) AS COLNAMES ,
-- 	u.name as tableownername,
-- 	OBJECT_NAME(I.ID) AS TABLENAME,
-- 	I.ID AS TABLEID,
-- 	I.INDID AS INDEXID,
-- 	I.NAME AS INDEXNAME,
-- 	I.STATUS,
-- 	INDEXPROPERTY (I.ID,I.NAME,'ISUNIQUE') AS ISUNIQUE,
-- 	INDEXPROPERTY (I.ID,I.NAME,'ISCLUSTERED') AS ISCLUSTERED,
-- 	INDEXPROPERTY (I.ID,I.NAME,'INDEXFILLFACTOR') AS INDEXFILLFACTOR
-- INTO #TMP
-- FROM
-- 	sysobjects o
-- 	join SYSINDEXES I
-- 	on i.id = o.id
-- 	join sysusers u
-- 	on u.uid = o.uid
-- WHERE I.INDID > 0 
-- 	AND I.INDID < 255 
-- 	AND (I.STATUS & 64)=0
-- --uncomment below to eliminate PK or UNIQUE indexes;
-- --what i call 'normal' indexes
-- AND   INDEXPROPERTY (I.ID,I.NAME,'ISUNIQUE')       =0
-- AND   INDEXPROPERTY (I.ID,I.NAME,'ISCLUSTERED') =0
-- 
-- 
-- DECLARE
--   @ISQL VARCHAR(4000),
--   @TABLEID INT,
--   @INDEXID INT,
--   @MAXTABLELENGTH INT,
--   @MAXINDEXLENGTH INT
--   --USED FOR FORMATTING ONLY
--     SELECT @MAXTABLELENGTH=MAX(LEN(TABLENAME)) FROM #TMP
--     SELECT @MAXINDEXLENGTH=MAX(LEN(INDEXNAME)) FROM #TMP
-- 
--     DECLARE C1 CURSOR FOR
--       SELECT TABLEID,INDEXID FROM #TMP  
--     OPEN C1
--       FETCH NEXT FROM C1 INTO @TABLEID,@INDEXID
--         WHILE @@FETCH_STATUS <> -1
--           BEGIN
-- 	SET @ISQL = ''
-- 	SELECT @ISQL=@ISQL + ISNULL(SYSCOLUMNS.NAME,'') + ',' FROM SYSINDEXES I
-- 	INNER JOIN SYSINDEXKEYS ON I.ID=SYSINDEXKEYS.ID AND I.INDID=SYSINDEXKEYS.INDID
-- 	INNER JOIN SYSCOLUMNS ON SYSINDEXKEYS.ID=SYSCOLUMNS.ID AND SYSINDEXKEYS.COLID=SYSCOLUMNS.COLID
-- 	WHERE I.INDID > 0 
-- 	AND I.INDID < 255 
-- 	AND (I.STATUS & 64)=0
-- 	AND I.ID=@TABLEID AND I.INDID=@INDEXID
-- 	ORDER BY SYSCOLUMNS.COLID
-- 	UPDATE #TMP SET COLNAMES=@ISQL WHERE TABLEID=@TABLEID AND INDEXID=@INDEXID
-- 
-- 	FETCH NEXT FROM C1 INTO @TABLEID,@INDEXID
--          END
--       CLOSE C1
--       DEALLOCATE C1
--   --AT THIS POINT, THE 'COLNAMES' COLUMN HAS A TRAILING COMMA
--   UPDATE #TMP SET COLNAMES=LEFT(COLNAMES,LEN(COLNAMES) -1)
-- 
-- -- SELECT  'CREATE ' 
-- --     + CASE WHEN ISUNIQUE     = 1 THEN ' UNIQUE ' ELSE '' END 
-- --     + CASE WHEN ISCLUSTERED = 1 THEN ' CLUSTERED ' ELSE '' END 
-- --     + ' INDEX [' + UPPER(INDEXNAME) + ']' 
-- --     +' ON [' + UPPER(TABLENAME) + '] '
-- --     + '(' + UPPER(COLNAMES) + ')' 
-- --     + CASE WHEN INDEXFILLFACTOR = 0 THEN ''  ELSE  ' WITH FILLFACTOR = ' + CONVERT(VARCHAR(10),INDEXFILLFACTOR)   END
-- --     FROM #TMP
-- -- order by tablename
-- 
-- SELECT  'CREATE ' 
--     + CASE WHEN ISUNIQUE     = 1 THEN ' UNIQUE ' ELSE '        ' END 
--     + CASE WHEN ISCLUSTERED = 1 THEN ' CLUSTERED ' ELSE '           ' END 
--     + ' INDEX [' + UPPER(INDEXNAME) + ']' 
--     + SPACE(@MAXINDEXLENGTH - LEN(INDEXNAME))
--     +' ON [' + UPPER(tableownername) + '].[' + UPPER(TABLENAME) + '] '
--     + SPACE(@MAXTABLELENGTH - LEN(TABLENAME)) 
--     + '(' + UPPER(COLNAMES) + ')' 
--     + CASE WHEN INDEXFILLFACTOR = 0 THEN ''  ELSE  ' WITH FILLFACTOR = ' + CONVERT(VARCHAR(10),INDEXFILLFACTOR)   END
--     FROM #TMP
-- order by tablename
-- 
-- --SELECT * FROM #TMP
-- DROP TABLE #TMP
--
```

