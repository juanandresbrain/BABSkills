# dbo.webdemandtrackingcommercecloud

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| OrderDateUTC | datetime2 | 8 | 1 |  |  |  |
| OrderNetTotal | decimal | 9 | 1 |  |  |  |
| OrderCustom1 | varchar | 8000 | 1 |  |  |  |
| OrderCustom2 | varchar | 8000 | 1 |  |  |  |
| OrderCustom3 | varchar | 8000 | 1 |  |  |  |
| OrderCustom4 | varchar | 8000 | 1 |  |  |  |
| OrderCustom5 | varchar | 8000 | 1 |  |  |  |
| DeckSKU | varchar | 8000 | 1 |  |  |  |
| UPC | varchar | 8000 | 1 |  |  |  |
| ItemPrice | decimal | 9 | 1 |  |  |  |
| OrderItemCustom1 | varchar | 8000 | 1 |  |  |  |
| OrderItemCustom2 | varchar | 8000 | 1 |  |  |  |
| OrderItemCustom3 | varchar | 8000 | 1 |  |  |  |
| OrderItemCustom4 | varchar | 8000 | 1 |  |  |  |
| OrderItemCustom5 | varchar | 8000 | 1 |  |  |  |
| OrderItemStatusChangeDateUTC | datetime2 | 8 | 1 |  |  |  |
| ItemStatus | varchar | 8000 | 1 |  |  |  |
| OrderItemTypeName | varchar | 8000 | 1 |  |  |  |
| OrderDiscount | decimal | 9 | 1 |  |  |  |
| ItemDiscount | decimal | 9 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| ItemSubtotal | decimal | 9 | 1 |  |  |  |
| ItemTotal | decimal | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 8000 | 1 |  |  |  |
| GiftCardTypeName | varchar | 8000 | 1 |  |  |  |
| ToName | varchar | 8000 | 1 |  |  |  |
| ToEmail | varchar | 8000 | 1 |  |  |  |
| FromName | varchar | 8000 | 1 |  |  |  |
| FromEmail | varchar | 8000 | 1 |  |  |  |
| Message | varchar | 8000 | 1 |  |  |  |
| GiftCardActivatedAmount | decimal | 9 | 1 |  |  |  |
| Channel | varchar | 8000 | 1 |  |  |  |
| FileName | varchar | 8000 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
