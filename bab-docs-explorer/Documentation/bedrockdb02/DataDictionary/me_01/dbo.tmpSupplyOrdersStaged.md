# dbo.tmpSupplyOrdersStaged

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 1 |  |  |  |
| OrderDate | date | 3 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| OrderQty | numeric | 13 | 1 |  |  |  |
| ProductDescription | nvarchar | 200 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectStoreDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributions.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsWIP20220406.md)

