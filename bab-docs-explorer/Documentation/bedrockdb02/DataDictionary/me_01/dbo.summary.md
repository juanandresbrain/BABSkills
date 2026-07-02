# dbo.summary

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrder | nvarchar | 40 | 0 |  |  |  |
| SupplierName | nvarchar | 100 | 0 |  |  |  |
| ShipToCode | nvarchar | 40 | 1 |  |  |  |
| ShipToName | nvarchar | 120 | 1 |  |  |  |
| FactoryName | nvarchar | 8000 | 1 |  |  |  |
| FactoryCode | nvarchar | 8000 | 1 |  |  |  |
| StyleCode | nvarchar | 40 | 1 |  |  |  |
| StyleDescription | nvarchar | 240 | 1 |  |  |  |
| Units | decimal | 17 | 1 |  |  |  |
| ExpectedReceiptDate | varchar | 30 | 1 |  |  |  |
| EstimatedCartons | decimal | 17 | 1 |  |  |  |

