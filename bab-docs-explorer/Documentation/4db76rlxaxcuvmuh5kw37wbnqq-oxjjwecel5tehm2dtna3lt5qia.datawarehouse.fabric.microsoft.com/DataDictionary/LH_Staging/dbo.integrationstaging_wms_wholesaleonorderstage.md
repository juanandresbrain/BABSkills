# dbo.integrationstaging_wms_wholesaleonorderstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderNumber | varchar | 8000 | 1 |  |  |  |
| PurchaseOrderLineStatus | varchar | 8000 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| LineNumber | bigint | 8 | 1 |  |  |  |
| RemainPurchPhysical | int | 4 | 1 |  |  |  |
| OrderedPurchaseQuantity | int | 4 | 1 |  |  |  |
