# dbo.tmpStoreList

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| str_num | numeric | 5 | 0 |  |  |  |
| store_ip | varchar | 68 | 1 |  |  |  |
| StoreGroup | bigint | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailMerchToStorePriceValidation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMerchToStorePriceValidation.md)
- [me_01: dbo.spMerchandisingInactiveSkuPreWork](../../StoredProcedures/me_01/dbo.spMerchandisingInactiveSkuPreWork.md)

