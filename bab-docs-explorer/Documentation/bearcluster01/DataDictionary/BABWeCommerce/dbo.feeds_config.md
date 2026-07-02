# dbo.feeds_config

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ConfigKey | varchar | 150 | 0 |  |  |  |
| ConfigDescription | varchar | 150 | 1 |  |  |  |
| ConfigValue | varchar | 250 | 0 |  |  |  |
| ConfigEnvironment | varchar | 50 | 0 |  |  |  |
| FeedType | varchar | 50 | 1 |  |  |  |
| LastAccessed | datetime | 8 | 1 |  |  |  |

