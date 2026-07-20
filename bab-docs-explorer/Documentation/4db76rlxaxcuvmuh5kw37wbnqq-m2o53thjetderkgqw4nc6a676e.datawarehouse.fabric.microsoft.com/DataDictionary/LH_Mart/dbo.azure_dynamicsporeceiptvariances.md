# dbo.azure_dynamicsporeceiptvariances

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReceiptDate | date | 3 | 1 |  |  |  |
| PurchaseOrderNumber | varchar | 8000 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| ProductDescription | varchar | 8000 | 1 |  |  |  |
| Quantity | float | 8 | 1 |  |  |  |
| AptosReceiptQty | int | 4 | 1 |  |  |  |
| VarianceQty | float | 8 | 1 |  |  |  |
| ReceivingWarehouseID | varchar | 8000 | 1 |  |  |  |
