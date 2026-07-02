# dbo.ERP_DistributionDataLookupStage

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 20 | 1 |  |  |  |
| OrderID | varchar | 20 | 1 |  |  |  |
| PickListID | varchar | 20 | 1 |  |  |  |
| OrderType | varchar | 20 | 1 |  |  |  |
| SequenceNumber | int | 4 | 1 |  |  |  |
| ItemNumber | varchar | 20 | 1 |  |  |  |
| UnconvertedQty | int | 4 | 1 |  |  |  |
| ConvertedQty | int | 4 | 1 |  |  |  |
| SalePrice | numeric | 17 | 1 |  |  |  |
| MerchOrSupply | varchar | 6 | 1 |  |  |  |
| DistributionMultiple | int | 4 | 1 |  |  |  |
| ColorCode | varchar | 2 | 1 |  |  |  |
| VendorStyle | varchar | 6 | 1 |  |  |  |
| ShortDescription | varchar | 52 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spERP_MergeDistributionDataLookup](../../StoredProcedures/me_01/dbo.spERP_MergeDistributionDataLookup.md)

