# dbo.tpm_po_create_line_1_

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 |  |  |  |
| po_no | varchar | 20 | 1 |  |  |  |
| Type | int | 4 | 1 |  |  |  |
| EventCode | varchar | 4 | 1 |  |  |  |
| EventLocationInternalId | varchar | 6 | 1 |  |  |  |
| EventSourceLocationInternalId | varchar | 6 | 1 |  |  |  |
| InternalStatus | int | 4 | 1 |  |  |  |
| FulFillFlag | int | 4 | 1 |  |  |  |
| AcceptRqdMode | int | 4 | 1 |  |  |  |
| AcceptedFlag | int | 4 | 1 |  |  |  |
| OwnerID | varchar | 4 | 1 |  |  |  |
| ShipToldRef | varchar | 4 | 1 |  |  |  |
| ShipTo | varchar | 4 | 1 |  |  |  |
| ShipFromId | varchar | 20 | 1 |  |  |  |
| SupplierId | varchar | 20 | 1 |  |  |  |
| Hub1Id | varchar | 1 | 1 |  |  |  |
| BillTold | varchar | 6 | 1 |  |  |  |
| TypeCode | varchar | 1 | 1 |  |  |  |
| CurrencyDesc | varchar | 50 | 1 |  |  |  |
| OrderDate | smalldatetime | 4 | 1 |  |  |  |
| PayTermsDesc | varchar | 50 | 1 |  |  |  |
| TransportMethodDesc | varchar | 50 | 1 |  |  |  |
| FOBDesc | varchar | 20 | 1 |  |  |  |
| COOCode | varchar | 5 | 1 |  |  |  |
| Rep1Id | varchar | 30 | 1 |  |  |  |
| OrderLine | smallint | 2 | 1 |  |  |  |
| AltDetailKey | int | 4 | 1 |  |  |  |
| ItemId | varchar | 20 | 1 |  |  |  |
| ItemDesc | varchar | 20 | 1 |  |  |  |
| AcceptedItemFlag | int | 4 | 1 |  |  |  |
| CurrQty | int | 4 | 1 |  |  |  |
| UOMCode | varchar | 1 | 1 |  |  |  |
| StartShipDate | smalldatetime | 4 | 1 |  |  |  |
| EndDeliverDateTime | smalldatetime | 4 | 1 |  |  |  |
| CancelDate | smalldatetime | 4 | 1 |  |  |  |
| UnitCost | decimal | 9 | 1 |  |  |  |
| RetailPrice | decimal | 9 | 1 |  |  |  |
| ColorCode | varchar | 3 | 1 |  |  |  |
| ColorDesc | varchar | 8 | 1 |  |  |  |
| ItemAttr1 | varchar | 14 | 1 |  |  |  |
| SupplierItemId | varchar | 25 | 1 |  |  |  |
| SupplierItemDesc | varchar | 40 | 1 |  |  |  |
| ShipToId | varchar | 4 | 1 |  |  |  |
| StdPackQty | int | 4 | 1 |  |  |  |
| StdCaseQty | int | 4 | 1 |  |  |  |
| CatchWeightFlag | int | 4 | 1 |  |  |  |
| Rep2Id | varchar | 30 | 1 |  |  |  |
| InternalStatusDetail | int | 4 | 1 |  |  |  |
| line_no | int | 4 | 1 |  |  |  |
| TransactionDate | smalldatetime | 4 | 1 |  |  |  |
| TransactionType | varchar | 50 | 1 |  |  |  |

