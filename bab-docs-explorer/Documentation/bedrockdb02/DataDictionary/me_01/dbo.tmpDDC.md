# dbo.tmpDDC

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Type | varchar | 14 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| document_no | varchar | 20 | 0 |  |  |  |
| carton_no | varchar | 20 | 1 |  |  |  |
| shipFrom | varchar | 20 | 0 |  |  |  |
| shipto | varchar | 20 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| units_sent | int | 4 | 1 |  |  |  |
| units_received | int | 4 | 1 |  |  |  |

