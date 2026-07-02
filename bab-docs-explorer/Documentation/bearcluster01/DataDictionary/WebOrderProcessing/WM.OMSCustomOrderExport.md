# WM.OMSCustomOrderExport

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomOrderExportID | int | 4 | 0 | YES |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| OrderNumber | varchar | 50 | 0 |  |  |  |
| OrderStatus | varchar | 50 | 1 |  |  |  |
| OrderDateUTC | datetime | 8 | 1 |  |  |  |
| OrderNetTotal | decimal | 9 | 1 |  |  |  |
| OrderCustom1 | varchar | 255 | 1 |  |  |  |
| OrderCustom2 | varchar | 255 | 1 |  |  |  |
| OrderCustom3 | varchar | 255 | 1 |  |  |  |
| OrderCustom4 | varchar | 255 | 1 |  |  |  |
| OrderCustom5 | varchar | 255 | 1 |  |  |  |
| DeckSKU | varchar | 100 | 1 |  |  |  |
| UPC | varchar | 50 | 1 |  |  |  |
| ItemPrice | decimal | 9 | 1 |  |  |  |
| OrderItemCustom1 | varchar | 255 | 1 |  |  |  |
| OrderItemCustom2 | varchar | 255 | 1 |  |  |  |
| OrderItemCustom3 | varchar | 255 | 1 |  |  |  |
| OrderItemCustom4 | varchar | 255 | 1 |  |  |  |
| OrderItemCustom5 | varchar | 255 | 1 |  |  |  |
| OrderItemStatusChangeDateUTC | varchar | 50 | 1 |  |  |  |
| ItemStatus | varchar | 50 | 1 |  |  |  |
| OrderItemTypeName | varchar | 255 | 1 |  |  |  |
| OrderDiscount | decimal | 9 | 1 |  |  |  |
| ItemDiscount | decimal | 9 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| ItemSubtotal | decimal | 9 | 1 |  |  |  |
| ItemTotal | decimal | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 50 | 1 |  |  |  |
| GiftCardTypeName | varchar | 50 | 1 |  |  |  |
| ToName | varchar | 255 | 1 |  |  |  |
| ToEmail | varchar | 100 | 1 |  |  |  |
| FromName | varchar | 255 | 1 |  |  |  |
| FromEmail | varchar | 100 | 1 |  |  |  |
| Message | varchar | -1 | 1 |  |  |  |
| GiftCardActivatedAmount | decimal | 5 | 1 |  |  |  |
| ImportFileName | nvarchar | 800 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SiteCode | varchar | 2 | 1 |  |  |  |
| Channel | varchar | 100 | 1 |  |  |  |

