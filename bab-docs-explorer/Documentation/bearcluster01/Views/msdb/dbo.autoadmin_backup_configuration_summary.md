# dbo.autoadmin_backup_configuration_summary

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.autoadmin_backup_configuration_summary"]
    dbo_autoadmin_backup_configurations(["dbo.autoadmin_backup_configurations"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.autoadmin_backup_configurations |

## View Code

```sql
----------------------------------------------------------------------------------------------------
--                              autoadmin_backup_configuration_summary
--
-- Contains a summarized version of autoadmin_backup_configurations
-- This removes db_ids and outputs only count of databases with each configuration
--
CREATE VIEW autoadmin_backup_configuration_summary
as
SELECT 
	ManagedBackupVersion,
	IsAlwaysOn,
	IsDropped,
	IsEnabled,
	RetentionPeriod,
	EncryptionAlgorithm,
	SchedulingOption,
	DayOfWeek,
	COUNT(*) AS DatabaseCount
FROM autoadmin_backup_configurations
GROUP BY
	ManagedBackupVersion,
	IsAlwaysOn,
	IsDropped,
	IsEnabled,
	RetentionPeriod,
	EncryptionAlgorithm,
	SchedulingOption,
	DayOfWeek
```

