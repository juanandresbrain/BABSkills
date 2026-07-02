# dbo.spDatabaseBackupOnDemand

**Database:** master  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDatabaseBackupOnDemand"]
    dbo_backupset(["dbo.backupset"]) --> SP
    dbo_CommandExecute(["dbo.CommandExecute"]) --> SP
    dbo_log_shipping_primary_databases(["dbo.log_shipping_primary_databases"]) --> SP
    dbo_log_shipping_secondary_databases(["dbo.log_shipping_secondary_databases"]) --> SP
    dbo_Queue(["dbo.Queue"]) --> SP
    dbo_QueueDatabase(["dbo.QueueDatabase"]) --> SP
    dbo_tmpDatabases(["dbo.tmpDatabases"]) --> SP
    sys_dm_db_log_stats(["sys.dm_db_log_stats"]) --> SP
    sys_dm_os_host_info(["sys.dm_os_host_info"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.backupset |
| dbo.CommandExecute |
| dbo.log_shipping_primary_databases |
| dbo.log_shipping_secondary_databases |
| dbo.Queue |
| dbo.QueueDatabase |
| dbo.tmpDatabases |
| sys.dm_db_log_stats |
| sys.dm_os_host_info |

## Stored Procedure Code

```sql
create proc spDatabaseBackupOnDemand
```

