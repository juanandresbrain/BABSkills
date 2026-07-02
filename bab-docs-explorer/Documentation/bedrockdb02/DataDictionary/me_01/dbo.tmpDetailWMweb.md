# dbo.tmpDetailWMweb

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 25 | 1 |  |  |  |
| distribution_no | varchar | 6 | 1 |  |  |  |
| carton_nbr | varchar | 38 | 1 |  |  |  |
| upc_no | varchar | 14 | 1 |  |  |  |
| sent_units | numeric | 17 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputWMshipmentsWeb](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWMshipmentsWeb.md)

