# dbo.tblPLM_Merchandising

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleCode | varchar | 20 | 1 |  |  |  |
| MerchandiseGroupCode | varchar | 20 | 0 |  |  |  |
| LongDescription | varchar | 120 | 1 |  |  |  |
| ShortDescription | varchar | 20 | 1 |  |  |  |
| SeasonCode | varchar | 2 | 0 |  |  |  |
| Year | smallint | 2 | 0 |  |  |  |
| PLUDescription | varchar | 40 | 1 |  |  |  |
| OrderMultiple | int | 4 | 1 |  |  |  |
| DistributionMultiple | int | 4 | 1 |  |  |  |
| OriginalSellingRetail | decimal | 17 | 1 |  |  |  |
| PrimaryVendorCode | varchar | 20 | 1 |  |  |  |
| PrimaryVendorStyleCode | varchar | 40 | 1 |  |  |  |
| PrimaryVendorCurrentCost | decimal | 9 | 1 |  |  |  |
| CurrentSellingRetail | decimal | 17 | 1 |  |  |  |
| StyleStatus | smallint | 2 | 0 |  |  |  |
| LastReceiptDate | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)

