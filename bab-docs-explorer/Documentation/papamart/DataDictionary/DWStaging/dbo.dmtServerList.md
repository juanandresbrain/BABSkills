# dbo.dmtServerList

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Server_Name | nvarchar | 100 | 0 |  |  |  |
| Description | nvarchar | 300 | 0 |  |  |  |
| IP_Address | nvarchar | 100 | 0 |  |  |  |
| Team_Ownership | nvarchar | 100 | 0 |  |  |  |
| Buisiness_Object | nvarchar | 100 | 1 |  |  |  |
| Operating_System | nvarchar | 100 | 0 |  |  |  |
| Location | nvarchar | 100 | 0 |  |  |  |
| Production | bit | 1 | 0 |  |  |  |
| Status | nvarchar | 100 | 0 |  |  |  |
| Team_Email | nvarchar | 100 | 0 |  |  |  |
