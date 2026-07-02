# dbo.tmpHeaderCN

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fromLocation | varchar | 4 | 1 |  |  |  |
| document_no | varchar | 10 | 1 |  |  |  |
| date_shipped | varchar | 10 | 1 |  |  |  |
| expected_receipt_date | varchar | 10 | 1 |  |  |  |
| location_code | varchar | 10 | 1 |  |  |  |
| external_system_name | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputCNshipments](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNshipments.md)

