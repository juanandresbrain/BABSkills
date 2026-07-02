# dbo.DistroImportArchive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DestID | varchar | 52 | 1 |  |  |  |
| style_code | varchar | 52 | 1 |  |  |  |
| quantity | varchar | 52 | 1 |  |  |  |
| InvType | varchar | 52 | 1 |  |  |  |
| Sourceid | varchar | 52 | 1 |  |  |  |
| ImportFile | varchar | 1000 | 1 |  |  |  |
| DocumentNumber | varchar | 52 | 1 |  |  |  |
| ImportTime | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingDistroImport](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport.md)
- [me_01: dbo.spMerchandisingDistroImport_BAK_20181119](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport_BAK_20181119.md)
- [me_01: dbo.spMerchandisingDistroImportBACKUP20150909](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportBACKUP20150909.md)
- [me_01: dbo.spMerchandisingDistroImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportValidation.md)

