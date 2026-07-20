# dbo.weborderprocessing_wm_orderitems

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderItemID | int | 4 | 1 |  |  |  |
| OrderId | int | 4 | 1 |  |  |  |
| sku | varchar | 8000 | 1 |  |  |  |
| qty | int | 4 | 1 |  |  |  |
| ItemDescription | varchar | 8000 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| DiscountedPrice | decimal | 9 | 1 |  |  |  |
| PreviousQTY | int | 4 | 1 |  |  |  |
| PreviousOriginalPrice | decimal | 9 | 1 |  |  |  |
| PreviousDiscountedPrice | decimal | 9 | 1 |  |  |  |
| GuestSatisfactionRefund | decimal | 9 | 1 |  |  |  |
| GiftCardNumber | varchar | 8000 | 1 |  |  |  |
| Note | varchar | 8000 | 1 |  |  |  |
| RecordYourVoiceOrder | varchar | 8000 | 1 |  |  |  |
| EmbroideryCode | varchar | 8000 | 1 |  |  |  |
| DateofBirth | datetime2 | 8 | 1 |  |  |  |
| FullName | varchar | 8000 | 1 |  |  |  |
| Height | decimal | 9 | 1 |  |  |  |
| Weight | decimal | 9 | 1 |  |  |  |
| FurColor | varchar | 8000 | 1 |  |  |  |
| EyeColor | varchar | 8000 | 1 |  |  |  |
| BelongsTo | varchar | 8000 | 1 |  |  |  |
| StuffedBy | varchar | 8000 | 1 |  |  |  |
| idNum | varchar | 8000 | 1 |  |  |  |
| tmpItemID | int | 4 | 1 |  |  |  |
| ParentItem | int | 4 | 1 |  |  |  |
| ItemId | varchar | 8000 | 1 |  |  |  |
| TrackingNumber | varchar | 8000 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
