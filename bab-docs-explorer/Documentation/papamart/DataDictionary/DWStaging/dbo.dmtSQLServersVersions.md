# dbo.dmtSQLServersVersions

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Team | nvarchar | 100 | 0 |  |  |  |
| Environment | nvarchar | 100 | 0 |  |  |  |
| Device_Name | nvarchar | 100 | 0 |  |  |  |
| SQL_Version | nvarchar | 100 | 0 |  |  |  |
| Edition | nvarchar | 100 | 0 |  |  |  |
| Service_Pack | nvarchar | 100 | 0 |  |  |  |
| Max_Service_Pack | tinyint | 1 | 1 |  |  |  |
| UpdatedTo | nvarchar | 100 | 1 |  |  |  |
| What_is_Needed_to_Retire | nvarchar | 200 | 1 |  |  |  |
