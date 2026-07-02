# WEB.GoogleAdsPricebookStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PriceBookName | nvarchar | 510 | 1 |  |  |  |
| Currency | nvarchar | 510 | 1 |  |  |  |
| OnlineFlag | bit | 1 | 1 |  |  |  |
| ProductNumber | nvarchar | 510 | 1 |  |  |  |
| OnlineFrom | datetime | 8 | 1 |  |  |  |
| OnlineTo | datetime | 8 | 1 |  |  |  |
| Quantity | tinyint | 1 | 1 |  |  |  |
| Price | decimal | 13 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spGoogleAdsInventoryLoad](../../StoredProcedures/IntegrationStaging/WEB.spGoogleAdsInventoryLoad.md)

