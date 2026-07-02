# dbo.eom_interface_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_utc | datetime | 8 | 0 |  |  |  |
| endpoint | nvarchar | -1 | 0 |  |  |  |
| request | nvarchar | -1 | 0 |  |  |  |
| response | nvarchar | -1 | 1 |  |  |  |
| exception | nvarchar | -1 | 1 |  |  |  |
| code | smallint | 2 | 1 |  |  |  |

