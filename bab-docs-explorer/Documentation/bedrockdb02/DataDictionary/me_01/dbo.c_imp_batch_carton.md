# dbo.c_imp_batch_carton

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| c_imp_batch_carton_id | decimal | 9 | 0 |  |  |  |
| entity_type | varchar | 2 | 0 |  |  |  |
| action_type | char | 1 | 0 |  |  |  |
| carton_no | varchar | 20 | 0 |  |  |  |
| location_code | varchar | 20 | 0 |  |  |  |
| employee_code | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectCBRSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCBRSummary.md)

