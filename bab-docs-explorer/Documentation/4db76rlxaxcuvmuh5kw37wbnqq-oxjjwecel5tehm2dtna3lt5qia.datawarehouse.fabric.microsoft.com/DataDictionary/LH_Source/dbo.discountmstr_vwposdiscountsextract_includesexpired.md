# dbo.discountmstr_vwposdiscountsextract_includesexpired

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| discountID | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| startDate | date | 3 | 1 |  |  |  |
| EndingDate | date | 3 | 1 |  |  |  |
| couponNumber | int | 4 | 1 |  |  |  |
| DiscountTitle | varchar | 8000 | 1 |  |  |  |
| discountMethod | varchar | 8000 | 1 |  |  |  |
| DiscountType | varchar | 8000 | 1 |  |  |  |
| rptDescription | varchar | 8000 | 1 |  |  |  |
| CalcMethod | varchar | 8000 | 1 |  |  |  |
| DiscountItemTierCalcMethod | varchar | 8000 | 1 |  |  |  |
| calcMethodAmount | decimal | 9 | 1 |  |  |  |
| DiscountAmount | decimal | 9 | 1 |  |  |  |
| buyAmount | decimal | 9 | 1 |  |  |  |
| buyValue | decimal | 5 | 1 |  |  |  |
| DiscountBuyType | varchar | 8000 | 1 |  |  |  |
| DiscountBuyTypeKeyWord | varchar | 8000 | 1 |  |  |  |
| buyType | varchar | 8000 | 1 |  |  |  |
| BuyTypeKeyWord | varchar | 8000 | 1 |  |  |  |
| AppliesTo | varchar | 8000 | 1 |  |  |  |
| AppliesToKeyword | varchar | 8000 | 1 |  |  |  |
| DiscountAppliesTo | varchar | 8000 | 1 |  |  |  |
| DiscountAppliesToKeyword | varchar | 8000 | 1 |  |  |  |
| isPartyDiscount | bit | 1 | 1 |  |  |  |
| itemGroupID | varchar | 8000 | 1 |  |  |  |
| itemProductID | decimal | 9 | 1 |  |  |  |
| quantity | decimal | 9 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
