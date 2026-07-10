# dbo.FlashTrafficStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| storeID | int | 4 | 1 |  |  |  |
| exits | int | 4 | 1 |  |  |  |
| enters | int | 4 | 1 |  |  |  |
| startTime | varchar | 128 | 1 |  |  |  |
| insert_datetime | datetime | 8 | 1 |  |  |  |
| HTTPString | varchar | 3000 | 1 |  |  |  |
