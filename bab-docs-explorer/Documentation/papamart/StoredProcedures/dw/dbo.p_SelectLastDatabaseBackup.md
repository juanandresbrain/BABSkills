# dbo.p_SelectLastDatabaseBackup

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.p_SelectLastDatabaseBackup"]
    backupset(["backupset"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| backupset |

## Stored Procedure Code

```sql
Create proc p_SelectLastDatabaseBackup 
As
select max(isnull(datediff(dd,b.backup_start_date,getdate()),0)) 
as 'Number of Days since last backup',
b.type as  'Backup type (D-database,L-log)', b.backup_size, d.name 
as database_name
from  master..sysdatabases d with (nolock)
left join msdb..backupset b  with (nolock) 
on d.name = b.database_name 
and b.backup_start_date = (select max(backup_start_date) 
                                         from msdb..backupset b2 
                                         where b.database_name = b2.database_name
                                        and b2.type = b.type)
where d.name != 'tempdb'
group by d.name, b.type, b.backup_size
```

