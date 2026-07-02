# dbo.promotion

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 0 |  |  |  |
| document_number | nvarchar | 40 | 0 |  |  |  |
| promotion_number | decimal | 9 | 0 | YES |  |  |
| cancel_date | smalldatetime | 4 | 1 |  |  |  |
| cancel_flag | decimal | 5 | 0 |  |  |  |

