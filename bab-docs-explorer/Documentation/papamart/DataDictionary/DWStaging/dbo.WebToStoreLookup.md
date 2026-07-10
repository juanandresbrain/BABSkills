# dbo.WebToStoreLookup

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| OrderNum | varchar | 10 | 1 |  |  |  |
| isPickupFromStore | int | 4 | 0 |  |  |  |
| isCurbside | int | 4 | 0 |  |  |  |
| isShipFromStore | int | 4 | 0 |  |  |  |
| isSameDay | int | 4 | 0 |  |  |  |
| LineNote | varchar | 10 | 1 |  |  |  |
