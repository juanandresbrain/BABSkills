# dbo.PMSOrderNumberExport

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pms_no | varchar | 7 | 1 |  |  |  |
| es_no | varchar | 20 | 1 |  |  |  |
| entry_date | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingProcessPMSOrderNumberExportFile](../../StoredProcedures/me_01/dbo.spMerchandisingProcessPMSOrderNumberExportFile.md)

