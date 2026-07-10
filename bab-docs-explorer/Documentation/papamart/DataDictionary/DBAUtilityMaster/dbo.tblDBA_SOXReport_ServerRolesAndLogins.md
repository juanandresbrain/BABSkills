# dbo.tblDBA_SOXReport_ServerRolesAndLogins

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RLID | int | 4 | 0 | YES |  |  |
| InstanceName | nvarchar | 256 | 1 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| dbname | sysname | 256 | 1 |  |  |  |
| sysadmin | varchar | 3 | 0 |  |  |  |
| securityadmin | varchar | 3 | 0 |  |  |  |
| serveradmin | varchar | 3 | 0 |  |  |  |
| setupadmin | varchar | 3 | 0 |  |  |  |
| processadmin | varchar | 3 | 0 |  |  |  |
| diskadmin | varchar | 3 | 0 |  |  |  |
| dbcreator | varchar | 3 | 0 |  |  |  |
| bulkadmin | varchar | 3 | 0 |  |  |  |
| RunYear | char | 4 | 1 |  |  |  |
| RunQuarter | char | 2 | 1 |  |  |  |
| RunDate | datetime | 8 | 0 |  |  |  |
