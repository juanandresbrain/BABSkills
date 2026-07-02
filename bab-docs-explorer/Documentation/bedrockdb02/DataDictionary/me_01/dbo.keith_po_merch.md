# dbo.keith_po_merch

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 20 | 0 |  |  |  |
| OrderLine | int | 4 | 0 |  |  |  |
| ItemAttr1 | varchar | 14 | 0 |  |  |  |
| ItemId | varchar | 20 | 0 |  |  |  |
| ColorCode | varchar | 3 | 0 |  |  |  |
| SupplierItemDesc | varchar | 8000 | 1 |  |  |  |
| CurrQty | int | 4 | 1 |  |  |  |
| StartShipDate | smalldatetime | 4 | 0 |  |  |  |
| EndDeliverDateTime | smalldatetime | 4 | 1 |  |  |  |
| CancelDate | smalldatetime | 4 | 0 |  |  |  |
| OrderDate | smalldatetime | 4 | 1 |  |  |  |

