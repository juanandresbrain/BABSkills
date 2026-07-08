# dbo.MSsubscriber_info

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher | sysname | 256 | 0 |  |  |  |
| subscriber | sysname | 256 | 0 |  |  |  |
| type | tinyint | 1 | 0 |  |  |  |
| login | sysname | 256 | 1 |  |  |  |
| password | nvarchar | 1048 | 1 |  |  |  |
| description | nvarchar | 1020 | 1 |  |  |  |
| security_mode | int | 4 | 0 |  |  |  |
