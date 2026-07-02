# dbo.tmpTransferImport

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sourceid | varchar | 52 | 1 |  |  |  |
| style_code | varchar | 52 | 1 |  |  |  |
| quantity | varchar | 52 | 1 |  |  |  |
| destid | varchar | 52 | 1 |  |  |  |
| invType | varchar | 52 | 1 |  |  |  |
| ImportFile | varchar | 1000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingDistroImport](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport.md)
- [me_01: dbo.spMerchandisingDistroImport_BAK_20181119](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport_BAK_20181119.md)
- [me_01: dbo.spMerchandisingDistroImportBACKUP20150909](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportBACKUP20150909.md)
- [me_01: dbo.spMerchandisingSelectPoolPointTransfer](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPoolPointTransfer.md)

