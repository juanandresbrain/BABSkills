# dbo.WebDemandTrackingCommerceCloud

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 50 | 1 |  |  |  |
| OrderStatus | varchar | 50 | 1 |  |  |  |
| OrderDateUTC | datetime | 8 | 1 |  |  |  |
| OrderNetTotal | numeric | 9 | 1 |  |  |  |
| OrderCustom1 | varchar | 500 | 1 |  |  |  |
| OrderCustom2 | varchar | 500 | 1 |  |  |  |
| OrderCustom3 | varchar | 500 | 1 |  |  |  |
| OrderCustom4 | varchar | 500 | 1 |  |  |  |
| OrderCustom5 | varchar | 500 | 1 |  |  |  |
| DeckSKU | varchar | 50 | 1 |  |  |  |
| UPC | varchar | 50 | 1 |  |  |  |
| ItemPrice | numeric | 9 | 1 |  |  |  |
| OrderItemCustom1 | varchar | 500 | 1 |  |  |  |
| OrderItemCustom2 | varchar | 500 | 1 |  |  |  |
| OrderItemCustom3 | varchar | 500 | 1 |  |  |  |
| OrderItemCustom4 | varchar | 500 | 1 |  |  |  |
| OrderItemCustom5 | varchar | 500 | 1 |  |  |  |
| OrderItemStatusChangeDateUTC | datetime | 8 | 1 |  |  |  |
| ItemStatus | varchar | 50 | 1 |  |  |  |
| OrderItemTypeName | varchar | 50 | 1 |  |  |  |
| OrderDiscount | numeric | 9 | 1 |  |  |  |
| ItemDiscount | numeric | 9 | 1 |  |  |  |
| Amount | numeric | 9 | 1 |  |  |  |
| ItemSubtotal | numeric | 9 | 1 |  |  |  |
| ItemTotal | numeric | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 50 | 1 |  |  |  |
| GiftCardTypeName | varchar | 50 | 1 |  |  |  |
| ToName | varchar | 100 | 1 |  |  |  |
| ToEmail | varchar | 100 | 1 |  |  |  |
| FromName | varchar | 100 | 1 |  |  |  |
| FromEmail | varchar | 100 | 1 |  |  |  |
| Message | nvarchar | 8000 | 1 |  |  |  |
| GiftCardActivatedAmount | numeric | 9 | 1 |  |  |  |
| Channel | varchar | 50 | 1 |  |  |  |
| FileName | nvarchar | 1000 | 1 |  |  |  |
| SiteCode | varchar | 2 | 1 |  |  |  |
