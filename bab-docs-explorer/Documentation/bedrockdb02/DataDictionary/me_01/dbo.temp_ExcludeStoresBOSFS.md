# dbo.temp_ExcludeStoresBOSFS

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ExStore | nvarchar | 40 | 1 |  |  |  |
| InsertDate | smalldatetime | 4 | 0 |  |  |  |
| Comment | nvarchar | 400 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmail1DaysPastERDWarning](../../StoredProcedures/me_01/dbo.spMerchandisingEmail1DaysPastERDWarning.md)
- [me_01: dbo.spMerchandisingEmail1DaysPastERDWarning_BAK](../../StoredProcedures/me_01/dbo.spMerchandisingEmail1DaysPastERDWarning_BAK.md)
- [me_01: dbo.spMerchandisingEmail2DaysPastERDWarning_BAK](../../StoredProcedures/me_01/dbo.spMerchandisingEmail2DaysPastERDWarning_BAK.md)

