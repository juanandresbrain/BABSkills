# dbo.tmpAllStorePRICE

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| location_name | varchar | 52 | 1 |  |  |  |
| style | varchar | 6 | 1 |  |  |  |
| description | varchar | 52 | 1 |  |  |  |
| price | decimal | 9 | 1 |  |  |  |
| promotion_no | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailMerchToStorePriceValidation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMerchToStorePriceValidation.md)

