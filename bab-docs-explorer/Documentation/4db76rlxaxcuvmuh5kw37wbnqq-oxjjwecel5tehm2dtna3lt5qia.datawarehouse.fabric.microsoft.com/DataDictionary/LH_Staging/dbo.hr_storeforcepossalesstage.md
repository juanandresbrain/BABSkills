# dbo.hr_storeforcepossalesstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreCode | varchar | 8000 | 1 |  |  |  |
| Date | varchar | 8000 | 1 |  |  |  |
| Slot | varchar | 8000 | 1 |  |  |  |
| SaleTrans | int | 4 | 1 |  |  |  |
| SaleValue | decimal | 9 | 1 |  |  |  |
| SaleUnits | int | 4 | 1 |  |  |  |
| RefundTrans | int | 4 | 1 |  |  |  |
| RefundValue | decimal | 9 | 1 |  |  |  |
| RefundUnits | int | 4 | 1 |  |  |  |
| PartySaleValue | decimal | 9 | 1 |  |  |  |
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
| GiftCardValue | decimal | 9 | 1 |  |  |  |
| GiftCardUnits | int | 4 | 1 |  |  |  |
| EnterpriseSellingValue | decimal | 9 | 1 |  |  |  |
| EnterpriseSellingTrans | int | 4 | 1 |  |  |  |
| EnterpriseSellingUnits | int | 4 | 1 |  |  |  |
| ShipFromStoreSales | decimal | 9 | 1 |  |  |  |
| ShipFromStoreTransactions | int | 4 | 1 |  |  |  |
| ShipFromStoreUnits | int | 4 | 1 |  |  |  |
| PickupFromStoreSales | decimal | 9 | 1 |  |  |  |
| PickupFromStoreTransactions | int | 4 | 1 |  |  |  |
| PickupFromStoreUnits | int | 4 | 1 |  |  |  |
| CurbsideSales | decimal | 9 | 1 |  |  |  |
| CurbsideTransactions | int | 4 | 1 |  |  |  |
| CurbsideUnits | int | 4 | 1 |  |  |  |
| GiftCardBonusSales | decimal | 9 | 1 |  |  |  |
| GiftCardBonusUnits | int | 4 | 1 |  |  |  |
| GiftCardBonusQualifying | int | 4 | 1 |  |  |  |
| StoreCodeRaw | int | 4 | 1 |  |  |  |
| TransactionDateRaw | date | 3 | 1 |  |  |  |
| MobileCaptureCount | int | 4 | 1 |  |  |  |
| MobileEmailOptInCount | int | 4 | 1 |  |  |  |
