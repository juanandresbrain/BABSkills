# ERP.DistributionDetail

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PICKLISTID | varchar | 20 | 1 |  |  |  |
| ITEMDESCRIPTION | varchar | 75 | 1 |  |  |  |
| ITEMNUMBER | varchar | 7 | 1 |  |  |  |
| MODEOFDELIVERY | varchar | 10 | 1 |  |  |  |
| ORDERID | varchar | 20 | 1 |  |  |  |
| QUANTITY | numeric | 17 | 1 |  |  |  |
| QUANTITYUNITOFMEASURE | varchar | 5 | 1 |  |  |  |
| SALESPRICE | numeric | 17 | 1 |  |  |  |
| TRANSACTIONDATETIME | datetime | 8 | 1 |  |  |  |
| Warehouse | varchar | 5 | 1 |  |  |  |
| Location | varchar | 5 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| ReleaseDate | datetime | 8 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| UOM | varchar | 10 | 1 |  |  |  |
| OrderLineNumber | numeric | 17 | 1 |  |  |  |
| BABAptosDistroLineNumber | nvarchar | 100 | 1 |  |  |  |
| BABAptosDistroNumber | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spDistributionsReadyToRelease](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease.md)
- [IntegrationStaging: ERP.spDistributionsReadyToRelease_Bak20231205](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease_Bak20231205.md)
- [IntegrationStaging: ERP.spMergeDistributiondDetail](../../StoredProcedures/IntegrationStaging/ERP.spMergeDistributiondDetail.md)
- [IntegrationStaging: ERP.spMergeDistributiondDetail_BAK20231117](../../StoredProcedures/IntegrationStaging/ERP.spMergeDistributiondDetail_BAK20231117.md)

