# dbo.spDBA_CheckBackups

**Database:** DBAUtility  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_CheckBackups"]
    backupset(["backupset"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| backupset |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDBA_CheckBackups]
AS	

SET NOCOUNT ON
select 	'Databases and backups on server ' + @@servername
select 	SUBSTRING(s.name,1,40)			AS	'Database',
	CAST(b.backup_start_date AS char(11)) 	AS 	'Backup Date  ',
	CASE WHEN b.backup_start_date > DATEADD(dd,-1,getdate())
		THEN 'Backup is current within a day'
	     WHEN b.backup_start_date > DATEADD(dd,-7,getdate())
		THEN 'Backup is current within a week'
	     ELSE '*****CHECK BACKUP!!!*****'
		END
						AS 'Comment'

from 	master..sysdatabases	s
LEFT OUTER JOIN	msdb..backupset b
	ON s.name = b.database_name
	AND b.backup_start_date = (SELECT MAX(backup_start_date)
					FROM msdb..backupset
					WHERE database_name = b.database_name
						AND type = 'D')		-- full database backups only, not log backups
WHERE	s.name <> 'tempdb'

ORDER BY 	s.name
```

