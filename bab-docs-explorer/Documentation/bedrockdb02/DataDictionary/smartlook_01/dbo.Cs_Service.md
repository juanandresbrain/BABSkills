# dbo.Cs_Service

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| service_id | int | 4 | 0 | YES |  |  |
| label | varchar | 30 | 1 |  |  |  |
| file_name | varchar | 30 | 0 |  |  |  |
| allow_multiple_files | smallint | 2 | 0 |  |  |  |
| expect_confirmation | smallint | 2 | 0 |  |  |  |
| contact_info | varchar | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Cs_TransmissionResults](../../StoredProcedures/fn_01/dbo.Cs_TransmissionResults.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Cs_TransmissionResults](../../StoredProcedures/smartlook_01/dbo.Cs_TransmissionResults.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

