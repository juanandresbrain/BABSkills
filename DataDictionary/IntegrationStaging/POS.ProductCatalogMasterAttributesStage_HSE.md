# POS.ProductCatalogMasterAttributesStage_HSE

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleCode | varchar | 100 | 1 |  |  |  |
| AVAILB | varchar | 4 | 1 |  |  |  |
| UPC | varchar | 100 | 1 |  |  |  |
| ItemDescription | varchar | 1000 | 1 |  |  |  |
| ProductDescription | varchar | 1000 | 1 |  |  |  |
| ItemName | varchar | 1000 | 1 |  |  |  |
| ItemType | varchar | 10 | 1 |  |  |  |
| SellingStatus | varchar | 10 | 1 |  |  |  |
| Stuffable | varchar | 10 | 1 |  |  |  |
| isEndlessAisleEligible | varchar | 5 | 1 |  |  |  |
| isEmployeeDiscountEligible | varchar | 5 | 1 |  |  |  |
| isreturneligible | int | 4 | 1 |  |  |  |
| iscashierentersprice | int | 4 | 1 |  |  |  |
| isqtyrestricted | int | 4 | 1 |  |  |  |
| isloyaltyrewardsdiscounteligible | int | 4 | 1 |  |  |  |
| giftCardType | varchar | 5 | 1 |  |  |  |
| Department | varchar | 100 | 1 |  |  |  |
| SubClass | varchar | 100 | 1 |  |  |  |
| ClassCode | varchar | 100 | 1 |  |  |  |
| subClassCode | varchar | 100 | 1 |  |  |  |
| departmenthierarchygroupid | int | 4 | 1 |  |  |  |
| classhierarchygroupid | int | 4 | 1 |  |  |  |
| subclasshierarchygroupid | int | 4 | 1 |  |  |  |
| productsellinggeography | varchar | 5 | 1 |  |  |  |
| productcountry | varchar | 5 | 1 |  |  |  |

