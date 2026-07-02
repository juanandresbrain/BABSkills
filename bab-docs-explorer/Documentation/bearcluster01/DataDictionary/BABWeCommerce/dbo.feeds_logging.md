# dbo.feeds_logging

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LoggingId | int | 4 | 0 | YES |  |  |
| DateStamp | datetime | 8 | 1 |  |  |  |
| Source | varchar | 255 | 1 |  |  |  |
| Message | varchar | 255 | 1 |  |  |  |
| LogLevelId | int | 4 | 1 |  | YES |  |

