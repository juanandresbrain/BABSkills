# WMS.WholesaleOnOrder

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| PurchaseOrderLineStatus | nvarchar | 510 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| LineNumber | bigint | 8 | 1 |  |  |  |
| RemainPurchPhysical | int | 4 | 1 |  |  |  |
| OrderedPurchaseQuantity | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

