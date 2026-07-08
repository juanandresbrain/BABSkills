# dbo.DBUpgradeHistory

**Database:** ReportServerSATempDB  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UpgradeID | bigint | 8 | 0 | YES |  |  |
| DbVersion | nvarchar | 50 | 1 |  |  |  |
| User | nvarchar | 256 | 1 |  |  |  |
| DateTime | datetime | 8 | 1 |  |  |  |
