# Azure.vwSQLBackupsMostRecentDates

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwSQLBackupsMostRecentDates"]
    dbo_SQLBackupsMostRecentDates(["dbo.SQLBackupsMostRecentDates"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SQLBackupsMostRecentDates |

## View Code

```sql
CREATE view [Azure].[vwSQLBackupsMostRecentDates]

as 

select 
	ServerName,	
	DatabaseName,	
	DatabaseType,	
	FullBackupDate,	
	DifferentialBackupDate,
	SQLServerServiceAccount,
	SQLAgentServerAccount
from [stl-ssis-p-01].IntegrationStaging.dbo.SQLBackupsMostRecentDates
```

