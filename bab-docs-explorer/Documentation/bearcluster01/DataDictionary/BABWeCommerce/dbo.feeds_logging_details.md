# dbo.feeds_logging_details

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DetailsId | int | 4 | 0 | YES |  |  |
| LoggingId | int | 4 | 0 |  |  |  |
| DateStamp | datetime | 8 | 1 |  |  |  |
| Source | varchar | 1024 | 1 |  |  |  |
| Details | varchar | 2048 | 1 |  |  |  |

