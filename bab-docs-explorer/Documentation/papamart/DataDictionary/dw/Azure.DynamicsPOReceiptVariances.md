# Azure.DynamicsPOReceiptVariances

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReceiptDate | date | 3 | 1 |  |  |  |
| PurchaseOrderNumber | varchar | 20 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| ProductDescription | nvarchar | 8000 | 1 |  |  |  |
| Quantity | float | 8 | 1 |  |  |  |
| AptosReceiptQty | int | 4 | 1 |  |  |  |
| VarianceQty | float | 8 | 1 |  |  |  |
| ReceivingWarehouseID | nvarchar | 8 | 1 |  |  |  |
