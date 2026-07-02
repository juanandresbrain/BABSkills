# dbo.tmpHearMe

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 20 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailNonUnivSoundStores](../../StoredProcedures/me_01/dbo.spMerchandisingEmailNonUnivSoundStores.md)

