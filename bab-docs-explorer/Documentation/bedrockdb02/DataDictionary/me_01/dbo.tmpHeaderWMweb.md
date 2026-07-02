# dbo.tmpHeaderWMweb

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 25 | 1 |  |  |  |
| date_shipped | varchar | 30 | 1 |  |  |  |
| expected_receipt_date | varchar | 30 | 1 |  |  |  |
| location_code | varchar | 4 | 0 |  |  |  |
| external_system_name | varchar | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputWMshipmentsWeb](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWMshipmentsWeb.md)

