# dbo.tmpLoyaltyPrestage2

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| TransactionLineNumber | int | 4 | 1 |  |  |  |
| DiscountReference | varchar | 80 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | nvarchar | 160 | 1 |  |  |  |
| StoreNumber | nvarchar | 160 | 1 |  |  |  |
| Country | varchar | 80 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| PurchaseRevenue | decimal | 5 | 1 |  |  |  |
| LineItemPrice | decimal | 5 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 5 | 1 |  |  |  |
| ParentTransactionSubTotal | decimal | 17 | 1 |  |  |  |
| SKU | varchar | 255 | 1 |  |  |  |
| KeyStory | nvarchar | 160 | 1 |  |  |  |
| ConsumerGroup | varchar | 80 | 1 |  |  |  |
| Department | varchar | 255 | 1 |  |  |  |
| LicensedOrNot | bit | 1 | 1 |  |  |  |
| TaxTotal | decimal | 5 | 1 |  |  |  |
| ShippingPerLineItem | decimal | 5 | 1 |  |  |  |
| ShippingTotal | decimal | 5 | 1 |  |  |  |
| GiftCardTendered | decimal | 5 | 1 |  |  |  |
| stuffed | bit | 1 | 1 |  |  |  |
| unstuffed | bit | 1 | 1 |  |  |  |
| GroupedTendersCash | decimal | 5 | 1 |  |  |  |
| GroupedTendersCreditDebit | decimal | 5 | 1 |  |  |  |
| GroupedTendersGiftCard | decimal | 5 | 1 |  |  |  |
| GroupedTendersKlarna | decimal | 5 | 1 |  |  |  |
| GroupedTendersPayPal | decimal | 5 | 1 |  |  |  |
| GroupedTendersAmazon | decimal | 5 | 1 |  |  |  |
| GroupedTendersAliPay | decimal | 5 | 1 |  |  |  |
| GroupedTendersFacebook | decimal | 5 | 1 |  |  |  |
| GroupedTendersOther | decimal | 5 | 1 |  |  |  |
| GroupedTendersPartyDeposit | decimal | 5 | 1 |  |  |  |
| GroupedTendersPOParty | decimal | 5 | 1 |  |  |  |
| GroupedTendersWeChatPay | decimal | 5 | 1 |  |  |  |
| Class | varchar | 20 | 1 |  |  |  |
| SubClass | varchar | 20 | 1 |  |  |  |
| IsBundleOrSet | bit | 1 | 1 |  |  |  |
| FulfillmentDate | date | 3 | 1 |  |  |  |
| isPointsEligible | bit | 1 | 1 |  |  |  |
| OrderReference | varchar | 50 | 1 |  |  |  |
| EmployeeID | int | 4 | 1 |  |  |  |
| matchedByEmail | bit | 1 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
