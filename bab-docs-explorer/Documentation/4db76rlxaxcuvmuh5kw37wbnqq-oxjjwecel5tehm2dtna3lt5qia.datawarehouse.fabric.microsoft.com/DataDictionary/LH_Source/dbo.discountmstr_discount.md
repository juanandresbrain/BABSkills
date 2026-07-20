# dbo.discountmstr_discount

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| discountID | int | 4 | 1 |  |  |  |
| eventID | int | 4 | 1 |  |  |  |
| Title | varchar | 8000 | 1 |  |  |  |
| budgetRegionID | int | 4 | 1 |  |  |  |
| countryID | int | 4 | 1 |  |  |  |
| startDate | date | 3 | 1 |  |  |  |
| endingDate | date | 3 | 1 |  |  |  |
| approvalNeededBy | date | 3 | 1 |  |  |  |
| estimatedDistributionQty | int | 4 | 1 |  |  |  |
| actualDistributionQty | int | 4 | 1 |  |  |  |
| estimatedDiscountValue | decimal | 9 | 1 |  |  |  |
| actualMarketingCost | decimal | 9 | 1 |  |  |  |
| discountMethodID | int | 4 | 1 |  |  |  |
| discountTypeID | int | 4 | 1 |  |  |  |
| discountValue | decimal | 5 | 1 |  |  |  |
| isPartyDiscount | bit | 1 | 1 |  |  |  |
| calcMethodID | int | 4 | 1 |  |  |  |
| isLimitedToStores | bit | 1 | 1 |  |  |  |
| couponNumber | int | 4 | 1 |  |  |  |
| appliesToID | int | 4 | 1 |  |  |  |
| buyTypeID | int | 4 | 1 |  |  |  |
| buyValue | decimal | 5 | 1 |  |  |  |
| isApproved | bit | 1 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_DT | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_DT | datetime2 | 8 | 1 |  |  |  |
| Notes | varchar | 8000 | 1 |  |  |  |
| isWebDiscount | bit | 1 | 1 |  |  |  |
| isSerializedCoupon | bit | 1 | 1 |  |  |  |
| isExported | bit | 1 | 1 |  |  |  |
| rptDescription | varchar | 8000 | 1 |  |  |  |
| estimatedQtyRedeemded | int | 4 | 1 |  |  |  |
| distroMethodID | int | 4 | 1 |  |  |  |
| isExportedToWeb | bit | 1 | 1 |  |  |  |
