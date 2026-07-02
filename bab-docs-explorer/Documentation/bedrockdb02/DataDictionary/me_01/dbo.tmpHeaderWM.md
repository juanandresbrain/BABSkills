# dbo.tmpHeaderWM

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 50 | 1 |  |  |  |
| date_shipped | varchar | 30 | 1 |  |  |  |
| expected_receipt_date | varchar | 30 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| external_system_name | nvarchar | 510 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputWMshipments](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWMshipments.md)

