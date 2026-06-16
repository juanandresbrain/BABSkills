# ERP.PurchaseOrderHeaderStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderNumber | varchar | 50 | 1 |  |  |  |
| ConfirmationNumber | varchar | 50 | 1 |  |  |  |
| TransportMethodDesc | varchar | 50 | 1 |  |  |  |
| FOBDesc | varchar | 50 | 1 |  |  |  |
| ShipFromId | varchar | 50 | 1 |  |  |  |
| Rep2Id | varchar | 50 | 1 |  |  |  |
| CurrencyDesc | varchar | 50 | 1 |  |  |  |
| OrderCreateDate | datetime | 8 | 1 |  |  |  |
| PaymentTerms | varchar | 50 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergePurchaseOrderHeader_Bak20210125](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderHeader_Bak20210125.md)

