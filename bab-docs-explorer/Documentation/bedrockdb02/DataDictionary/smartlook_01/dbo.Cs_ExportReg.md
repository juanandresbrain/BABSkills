# dbo.Cs_ExportReg

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cs_file_id | int | 4 | 0 | YES |  |  |
| object_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| service_id | int | 4 | 0 |  |  |  |
| cs_interval | smallint | 2 | 0 |  |  |  |
| reset_flag | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Cs_GetCsFileID](../../StoredProcedures/fn_01/dbo.Cs_GetCsFileID.md)
- [fn_01: dbo.Cs_TransmissionResults](../../StoredProcedures/fn_01/dbo.Cs_TransmissionResults.md)
- [fn_01: dbo.Cs_TransmissionStart](../../StoredProcedures/fn_01/dbo.Cs_TransmissionStart.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Cs_GetCsFileID](../../StoredProcedures/smartlook_01/dbo.Cs_GetCsFileID.md)
- [smartlook_01: dbo.Cs_TransmissionResults](../../StoredProcedures/smartlook_01/dbo.Cs_TransmissionResults.md)
- [smartlook_01: dbo.Cs_TransmissionStart](../../StoredProcedures/smartlook_01/dbo.Cs_TransmissionStart.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

