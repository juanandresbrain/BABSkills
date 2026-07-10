# dbo.HR_StoreForcePosSalesStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreCode | varchar | 4 | 1 |  |  |  |
| Date | varchar | 30 | 1 |  |  |  |
| Slot | varchar | 5 | 1 |  |  |  |
| SaleTrans | int | 4 | 1 |  |  |  |
| SaleValue | money | 8 | 1 |  |  |  |
| SaleUnits | int | 4 | 1 |  |  |  |
| RefundTrans | int | 4 | 1 |  |  |  |
| RefundValue | money | 8 | 1 |  |  |  |
| RefundUnits | int | 4 | 1 |  |  |  |
| PartySaleValue | money | 8 | 1 |  |  |  |
| PartyTrans | int | 4 | 1 |  |  |  |
| PartyBookings | int | 4 | 1 |  |  |  |
| PartyCount | int | 4 | 1 |  |  |  |
| StufferTrans | int | 4 | 1 |  |  |  |
| SkinsTrans | int | 4 | 1 |  |  |  |
| StuffersUnits | int | 4 | 1 |  |  |  |
| SkinsUnits | int | 4 | 1 |  |  |  |
| BackpackTrans | int | 4 | 1 |  |  |  |
| BackpackUnits | int | 4 | 1 |  |  |  |
| BonusClubTrans | int | 4 | 1 |  |  |  |
| GiftCardValue | money | 8 | 1 |  |  |  |
| GiftCardUnits | int | 4 | 1 |  |  |  |
| EnterpriseSellingValue | money | 8 | 1 |  |  |  |
| EnterpriseSellingTrans | int | 4 | 1 |  |  |  |
| EnterpriseSellingUnits | int | 4 | 1 |  |  |  |
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
| StoreCodeRaw | int | 4 | 1 |  |  |  |
| TransactionDateRaw | date | 3 | 1 |  |  |  |
| MobileCaptureCount | int | 4 | 1 |  |  |  |
| MobileEmailOptInCount | int | 4 | 1 |  |  |  |
