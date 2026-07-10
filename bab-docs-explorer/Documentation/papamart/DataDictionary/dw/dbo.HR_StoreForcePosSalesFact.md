# dbo.HR_StoreForcePosSalesFact

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreCode | varchar | 4 | 1 |  |  |  |
| Date | varchar | 30 | 1 |  |  |  |
| Slot | varchar | 5 | 1 |  |  |  |
| SaleTrans | int | 4 | 1 |  |  |  |
| SaleValue | money | 8 | 1 |  |  |  |
| SaleUnits | numeric | 17 | 1 |  |  |  |
| RefundTrans | numeric | 17 | 1 |  |  |  |
| RefundValue | money | 8 | 1 |  |  |  |
| RefundUnits | numeric | 17 | 1 |  |  |  |
| PartySaleValue | money | 8 | 1 |  |  |  |
| PartyTrans | int | 4 | 1 |  |  |  |
| PartyBookings | int | 4 | 1 |  |  |  |
| PartyCount | int | 4 | 1 |  |  |  |
| StufferTrans | int | 4 | 1 |  |  |  |
| SkinsTrans | int | 4 | 1 |  |  |  |
| StuffersUnits | numeric | 17 | 1 |  |  |  |
| SkinsUnits | numeric | 17 | 1 |  |  |  |
| BackpackTrans | int | 4 | 1 |  |  |  |
| BackpackUnits | numeric | 17 | 1 |  |  |  |
| BonusClubTrans | int | 4 | 1 |  |  |  |
| GiftCardValue | money | 8 | 1 |  |  |  |
| GiftCardUnits | numeric | 17 | 1 |  |  |  |
| EnterpriseSellingValue | money | 8 | 1 |  |  |  |
| EnterpriseSellingTrans | int | 4 | 1 |  |  |  |
| EnterpriseSellingUnits | numeric | 17 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| StoreIDRaw | int | 4 | 1 |  |  |  |
| DateRaw | date | 3 | 1 |  |  |  |
| ShipFromStoreSales | money | 8 | 1 |  |  |  |
| ShipFromStoreTransactions | int | 4 | 1 |  |  |  |
| ShipFromStoreUnits | int | 4 | 1 |  |  |  |
| PickupFromStoreSales | money | 8 | 1 |  |  |  |
| PickupFromStoreTransactions | int | 4 | 1 |  |  |  |
| PickupFromStoreUnits | int | 4 | 1 |  |  |  |
| CurbsideSales | money | 8 | 1 |  |  |  |
| CurbsideTransactions | int | 4 | 1 |  |  |  |
| CurbsideUnits | int | 4 | 1 |  |  |  |
| GiftCardBonusSales | money | 8 | 1 |  |  |  |
| GiftCardBonusUnits | int | 4 | 1 |  |  |  |
| GiftCardBonusQualifying | int | 4 | 1 |  |  |  |
| MobileCaptureCount | int | 4 | 1 |  |  |  |
| MobileEmailOptInCount | int | 4 | 1 |  |  |  |
