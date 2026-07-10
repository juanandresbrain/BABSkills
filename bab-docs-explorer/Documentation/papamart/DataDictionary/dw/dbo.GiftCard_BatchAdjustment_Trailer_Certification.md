# dbo.GiftCard_BatchAdjustment_Trailer_Certification

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| batch_id | int | 4 | 0 |  |  |  |
| trailer_id | int | 4 | 0 | YES |  |  |
| format | char | 1 | 1 |  |  |  |
| record_count | char | 10 | 1 |  |  |  |
| filler | char | 288 | 1 |  |  |  |
