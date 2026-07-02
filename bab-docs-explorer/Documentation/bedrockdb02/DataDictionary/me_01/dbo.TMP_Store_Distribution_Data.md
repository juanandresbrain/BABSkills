# dbo.TMP_Store_Distribution_Data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store Shipment Number | decimal | 9 | 1 |  |  |  |
| Store | varchar | 10 | 0 |  |  |  |
| Rec Type Label | varchar | 20 | 1 |  |  |  |
| Style Code | varchar | 20 | 0 |  |  |  |
| Style Short Description | varchar | 8000 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| Exported to Warehouse Date | datetime | 8 | 1 |  |  |  |
| Exported | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CN](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CN.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406.md)

