# dbo.tmpMerchToStorePriceVariance

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | nvarchar | 40 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| CurrentSellingRetail | decimal | 9 | 1 |  |  |  |
| OWNRSP | nvarchar | 12 | 0 |  |  |  |
| price | decimal | 9 | 1 |  |  |  |
| promotion_no | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailMerchToStorePriceValidation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMerchToStorePriceValidation.md)

