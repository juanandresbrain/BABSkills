# ERP.tmpDistributionsReadyToRelease

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 20 | 1 |  |  |  |
| PICKLISTID | varchar | 20 | 1 |  |  |  |
| CUSTOMERREQUISITIONID | varchar | 50 | 1 |  |  |  |
| DELIVERYTERM | varchar | 200 | 1 |  |  |  |
| FROMWAREHOUSE | varchar | 10 | 1 |  |  |  |
| MODEOFDELIVERY | int | 4 | 1 |  |  |  |
| ORDERID | varchar | 12 | 1 |  |  |  |
| ORDERTYPE | varchar | 20 | 1 |  |  |  |
| SHIPTONAME | varchar | 100 | 1 |  |  |  |
| TOWAREHOUSE | varchar | 10 | 1 |  |  |  |
| TRANSACTIONDATETIME | datetime | 8 | 1 |  |  |  |
| ITEMDESCRIPTION | varchar | 75 | 1 |  |  |  |
| MerchOrSupply | varchar | 6 | 0 |  |  |  |
| ITEMNUMBER | varchar | 20 | 1 |  |  |  |
| QUANTITY | numeric | 17 | 1 |  |  |  |
| ConvertedQuantity | int | 4 | 1 |  |  |  |
| QUANTITYUNITOFMEASURE | varchar | 5 | 1 |  |  |  |
| SALESPRICE | numeric | 17 | 1 |  |  |  |
| RecType | int | 4 | 0 |  |  |  |
| ReasonCode | nvarchar | 510 | 1 |  |  |  |
| Priority | int | 4 | 1 |  |  |  |
| SequenceNumber | bigint | 8 | 1 |  |  |  |
| ref_field_1 | bigint | 8 | 1 |  |  |  |
| current_day | nvarchar | 60 | 1 |  |  |  |
| OrderAddressID | int | 4 | 1 |  |  |  |
| OrderLocationCode | int | 4 | 1 |  |  |  |
| SaleToStore | int | 4 | 0 |  |  |  |
| VendorStyle | varchar | 6 | 1 |  |  |  |
| ColorCode | varchar | 2 | 0 |  |  |  |
| ShortDesription | varchar | 52 | 1 |  |  |  |
| DistributionMultiple | int | 4 | 1 |  |  |  |
| OrderCreateSource | varchar | 10 | 1 |  |  |  |
| RecTypeMessage | nvarchar | 510 | 1 |  |  |  |
| BABAptosDistroNumber | nvarchar | 100 | 1 |  |  |  |
| BABAptosDistroLineNumber | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spDistributionsReadyToRelease](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease.md)
- [IntegrationStaging: ERP.spDistributionsReadyToRelease_Bak20231205](../../StoredProcedures/IntegrationStaging/ERP.spDistributionsReadyToRelease_Bak20231205.md)

