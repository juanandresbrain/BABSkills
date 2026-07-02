# dbo.Cs_ReTransmission

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transmission_id | int | 4 | 0 | YES |  |  |
| user_id | int | 4 | 0 |  |  |  |
| request_datetime | datetime | 8 | 0 |  |  |  |
| new_transmission_id | int | 4 | 1 |  |  |  |
| status_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Cs_ResubmitTransmission](../../StoredProcedures/fn_01/dbo.Cs_ResubmitTransmission.md)
- [fn_01: dbo.Cs_ReTransmissionStart](../../StoredProcedures/fn_01/dbo.Cs_ReTransmissionStart.md)
- [fn_01: dbo.Cs_ValidateTransmission](../../StoredProcedures/fn_01/dbo.Cs_ValidateTransmission.md)
- [smartlook_01: dbo.Cs_ResubmitTransmission](../../StoredProcedures/smartlook_01/dbo.Cs_ResubmitTransmission.md)
- [smartlook_01: dbo.Cs_ReTransmissionStart](../../StoredProcedures/smartlook_01/dbo.Cs_ReTransmissionStart.md)
- [smartlook_01: dbo.Cs_ValidateTransmission](../../StoredProcedures/smartlook_01/dbo.Cs_ValidateTransmission.md)

