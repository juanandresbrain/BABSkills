# dbo.FlashTrafficErrorLog

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 1 |  |  |  |
| insert_date | datetime | 8 | 1 |  |  |  |
| HTTPString | varchar | 1000 | 1 |  |  |  |
| ResponseText | varchar | 8000 | 1 |  |  |  |
