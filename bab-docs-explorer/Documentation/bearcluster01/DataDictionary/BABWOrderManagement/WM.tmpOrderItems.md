# WM.tmpOrderItems

**Database:** BABWOrderManagement  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderItemID | int | 4 | 0 |  |  |  |
| OrderId | int | 4 | 0 |  |  |  |
| sku | varchar | 50 | 0 |  |  |  |
| qty | int | 4 | 0 |  |  |  |
| ItemDescription | varchar | 100 | 1 |  |  |  |
| Price | money | 8 | 1 |  |  |  |
| DiscountedPrice | money | 8 | 1 |  |  |  |
| PreviousQTY | int | 4 | 1 |  |  |  |
| PreviousOriginalPrice | money | 8 | 1 |  |  |  |
| PreviousDiscountedPrice | money | 8 | 1 |  |  |  |
| GuestSatisfactionRefund | money | 8 | 1 |  |  |  |
| GiftCardNumber | varchar | 20 | 1 |  |  |  |
| Note | varchar | 50 | 1 |  |  |  |
| RecordYourVoiceOrder | varchar | 20 | 1 |  |  |  |
| EmbroideryCode | varchar | 32 | 1 |  |  |  |
| DateofBirth | smalldatetime | 4 | 1 |  |  |  |
| FullName | varchar | 50 | 1 |  |  |  |
| Height | decimal | 9 | 1 |  |  |  |
| Weight | decimal | 9 | 1 |  |  |  |
| FurColor | varchar | 20 | 1 |  |  |  |
| EyeColor | varchar | 10 | 1 |  |  |  |
| BelongsTo | varchar | 50 | 1 |  |  |  |
| StuffedBy | varchar | 50 | 1 |  |  |  |
| idNum | varchar | 20 | 1 |  |  |  |
| tmpItemID | int | 4 | 1 |  |  |  |
| ParentItem | int | 4 | 1 |  |  |  |
| ItemId | varchar | 20 | 1 |  |  |  |
| TrackingNumber | varchar | 30 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |

