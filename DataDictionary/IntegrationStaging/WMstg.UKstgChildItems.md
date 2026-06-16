# WMstg.UKstgChildItems

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderItemID | int | 4 | 1 |  |  |  |
| OrderId | int | 4 | 1 |  |  |  |
| sku | varchar | 50 | 1 |  |  |  |
| ItemStatus | varchar | 20 | 1 |  |  |  |
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
| EmbroideryCode | varchar | 32 | 1 |  |  |  |
| idNum | varchar | 20 | 1 |  |  |  |
| RecordYourVoiceOrderNumber | varchar | 20 | 1 |  |  |  |
| ParentItem | int | 4 | 1 |  |  |  |
| ItemId | varchar | 20 | 1 |  |  |  |

