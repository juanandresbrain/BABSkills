# dbo.tmpDetailWM

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 50 | 1 |  |  |  |
| distribution_no | varchar | 20 | 1 |  |  |  |
| carton_nbr | varchar | 20 | 0 |  |  |  |
| upc_no | varchar | 14 | 1 |  |  |  |
| sent_units | numeric | 13 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputWMshipments](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWMshipments.md)

