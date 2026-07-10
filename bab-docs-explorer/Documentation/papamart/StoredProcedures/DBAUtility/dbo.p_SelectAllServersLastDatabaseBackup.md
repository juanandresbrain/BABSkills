# dbo.p_SelectAllServersLastDatabaseBackup

**Database:** DBAUtility  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.p_SelectAllServersLastDatabaseBackup"]
    CentralTableForBackupInfo(["CentralTableForBackupInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CentralTableForBackupInfo |

## Stored Procedure Code

```sql
CREATE procedure p_SelectAllServersLastDatabaseBackup 
@p_NumOfDays smallint = 0
As
  
set nocount on
declare @InstanceName    varchar(400),
            @cmd                    varchar(4000),  -- holds the command to be run on each server
            @cmd2                  varchar(4000)   -- runs the command on the SQL SERVER 
                                                                   -- instance with OSQLS (xp_cmdshell)
DECLARE		@rowcount int,
			@counter int
 
If @p_NumOfDays > 0
          Delete from CentralTableForBackupInfo 
where InsertDate <= dateadd(dd,(-1)*@p_NumOfDays,getdate()) 

Create table #tmp (primkey int identity(1,1), InstanceName varchar(1000))
insert into #tmp
Exec master..xp_cmdshell 'osql -L'
delete from #tmp where InstanceName is null or InstanceName like 'Servers:%'

SET @rowcount = (SELECT MAX(primkey) FROM #tmp)
SET @counter = 0

SELECT * FROM #tmp

if exists (select 1 from #tmp where InstanceName  like '%-- NONE --%')
begin
            print ('Please connect to the LAN - no servers were encountered!') 
            return
end

-----------------------------------------------------------------------------------------------
--For each server - run the script and insert data into a centralized table
----------------------------------------------------------------------------------------------------- 

select @cmd = 'select  convert(varchar(40), max(isnull(datediff(dd,b.backup_start_date ,getdate()),0))) as Maxd,'+
'b.type,convert(varchar(40),b.backup_size) as backup_size,d.name ' +
'into #t from     master..sysdatabases d with (nolock) ' +
'left join msdb..backupset b  with (nolock) on d.name = b.database_name ' +
'where b.backup_start_date = (select max(backup_start_date) from msdb..backupset b2 ' +
'where b.database_name = b2.database_name and b2.type = b.type) ' +
'group by d.name, b.type, b.backup_size ;  ' + 
-- Since I am getting results from xp_cmdshell and OSQL - The results are returned in one
--line (no columns)
-- This is why I separate the values with '@^1^@','@^2^@' and so on, so I can later substring 
--the values
-- easily:
'select ''@^1^@''+Maxd+''@^2^@''+type+''@^3^@''+backup_size+''@^4^@''+name+''@^5^@'' from #t'
 
create table #tmp2 (a varchar(8000))
 
WHILE @counter < @rowcount
begin
			SET @counter = @counter + 1

			SET @InstanceName = (SELECT instancename FROM #tmp WHERE primkey = @counter)

            select @cmd2 = 'osql -E -S"' + @InstanceName + '" -Q "' + @cmd + '"' 
		SELECT @cmd2

            insert into #tmp2 (a) exec master..xp_cmdshell @cmd2

SELECT * FROM #tmp2
 
            delete from #tmp2 where a not like '%@^_^@%' or a is null
            update #tmp2 set a = rtrim(ltrim(a))

            insert into CentralTableForBackupInfo (InstanceName, DaysFromLastBackup,BackupType, 
			BackupSizeKB, DatabaseName) 
            select   @InstanceName,
                        substring(a,charindex('@^1^@',a)+5,charindex('@^2^@',a)-charindex('@^1^@',a)-5), 
                        substring(a,charindex('@^2^@',a)+5,charindex('@^3^@',a)-charindex('@^2^@',a)-5), 
                        substring(a,charindex('@^3^@',a)+5,charindex('@^4^@',a)-charindex('@^3^@',a)-5), 
                        substring(a,charindex('@^4^@',a)+5,charindex('@^5^@',a)-charindex('@^4^@',a)-5) 
            from #tmp2
            
	truncate table #tmp2
            
end
```

