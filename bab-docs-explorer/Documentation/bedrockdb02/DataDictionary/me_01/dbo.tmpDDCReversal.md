# dbo.tmpDDCReversal

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 10 | 1 |  |  |  |
| date_shipped | varchar | 30 | 1 |  |  |  |
| expected_receipt_date | varchar | 30 | 1 |  |  |  |
| location_code | varchar | 1000 | 1 |  |  |  |
| external_system_name | nvarchar | 510 | 1 |  |  |  |
| distribution_no | varchar | 6 | 1 |  |  |  |
| carton_no | varchar | 20 | 1 |  |  |  |
| upc_no | varchar | 36 | 1 |  |  |  |
| sent_units | int | 4 | 1 |  |  |  |
| hierarchy | varchar | 2 | 1 |  |  |  |
| units_sent | int | 4 | 1 |  |  |  |
| reversal | int | 4 | 1 |  |  |  |
| units_received | int | 4 | 1 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |

