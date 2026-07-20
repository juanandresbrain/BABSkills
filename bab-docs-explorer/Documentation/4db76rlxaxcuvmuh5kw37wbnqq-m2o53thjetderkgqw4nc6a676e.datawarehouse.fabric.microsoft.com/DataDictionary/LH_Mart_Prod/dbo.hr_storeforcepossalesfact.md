# dbo.hr_storeforcepossalesfact

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreCode | varchar | 8000 | 1 |  |  |  |
| Date | varchar | 8000 | 1 |  |  |  |
| Slot | varchar | 8000 | 1 |  |  |  |
| SaleTrans | int | 4 | 1 |  |  |  |
| SaleValue | decimal | 9 | 1 |  |  |  |
| SaleUnits | decimal | 17 | 1 |  |  |  |
| RefundTrans | decimal | 17 | 1 |  |  |  |
| RefundValue | decimal | 9 | 1 |  |  |  |
| RefundUnits | decimal | 17 | 1 |  |  |  |
| PartySaleValue | decimal | 9 | 1 |  |  |  |
| PartyTrans | int | 4 | 1 |  |  |  |
| PartyBookings | int | 4 | 1 |  |  |  |
| PartyCount | int | 4 | 1 |  |  |  |
| StufferTrans | int | 4 | 1 |  |  |  |
| SkinsTrans | int | 4 | 1 |  |  |  |
| StuffersUnits | decimal | 17 | 1 |  |  |  |
| SkinsUnits | decimal | 17 | 1 |  |  |  |
| BackpackTrans | int | 4 | 1 |  |  |  |
| BackpackUnits | decimal | 17 | 1 |  |  |  |
| BonusClubTrans | int | 4 | 1 |  |  |  |
| GiftCardValue | decimal | 9 | 1 |  |  |  |
| GiftCardUnits | decimal | 17 | 1 |  |  |  |
| EnterpriseSellingValue | decimal | 9 | 1 |  |  |  |
| EnterpriseSellingTrans | int | 4 | 1 |  |  |  |
| EnterpriseSellingUnits | decimal | 17 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| StoreIDRaw | int | 4 | 1 |  |  |  |
| DateRaw | date | 3 | 1 |  |  |  |
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
| MobileCaptureCount | int | 4 | 1 |  |  |  |
| MobileEmailOptInCount | int | 4 | 1 |  |  |  |
