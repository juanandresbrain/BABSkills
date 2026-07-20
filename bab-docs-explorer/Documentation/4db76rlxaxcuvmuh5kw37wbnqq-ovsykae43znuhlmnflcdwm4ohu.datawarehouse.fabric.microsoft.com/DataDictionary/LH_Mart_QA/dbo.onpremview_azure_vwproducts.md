# dbo.onpremview_azure_vwproducts

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| StyleDescription | varchar | 8000 | 1 |  |  |  |
| Color | varchar | 8000 | 1 |  |  |  |
| Concept | varchar | 8000 | 1 |  |  |  |
| Chain | varchar | 8000 | 1 |  |  |  |
| Division | varchar | 8000 | 1 |  |  |  |
| Department | varchar | 8000 | 1 |  |  |  |
| Class | varchar | 8000 | 1 |  |  |  |
| SubClass | varchar | 8000 | 1 |  |  |  |
| DeptCode | varchar | 8000 | 1 |  |  |  |
| SubClassCode | varchar | 8000 | 1 |  |  |  |
| ScorecardCategory | varchar | 8000 | 1 |  |  |  |
| PrimaryVendorCode | varchar | 8000 | 1 |  |  |  |
| PrimaryVendorName | varchar | 8000 | 1 |  |  |  |
| AltPrimaryVendorCode | varchar | 8000 | 1 |  |  |  |
| CurrentRetail | decimal | 9 | 1 |  |  |  |
| OriginalRetail | decimal | 9 | 1 |  |  |  |
| CurrentSellingRetailHome | decimal | 9 | 1 |  |  |  |
| PriceWithVat | decimal | 9 | 1 |  |  |  |
| EuroValue | decimal | 9 | 1 |  |  |  |
| CanValue | decimal | 9 | 1 |  |  |  |
| MerchStatus | varchar | 8000 | 1 |  |  |  |
| JurisdictionCode | varchar | 8000 | 1 |  |  |  |
| Gender | varchar | 8000 | 1 |  |  |  |
| CoreFashCode | varchar | 8000 | 1 |  |  |  |
| InlineCode | varchar | 8000 | 1 |  |  |  |
| ActivationDate | date | 3 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| IDATE | date | 3 | 1 |  |  |  |
| ODATE | date | 3 | 1 |  |  |  |
| ONOTE | varchar | 8000 | 1 |  |  |  |
| OUTLET | varchar | 8000 | 1 |  |  |  |
| OMSTAT | varchar | 8000 | 1 |  |  |  |
| altKeyStory | varchar | 8000 | 1 |  |  |  |
| HomeCurrentRetail | decimal | 9 | 1 |  |  |  |
| HomeOriginalRetail | decimal | 9 | 1 |  |  |  |
| IECurrentRetail | decimal | 9 | 1 |  |  |  |
| IEOriginalRetail | decimal | 9 | 1 |  |  |  |
| DKCurrentRetail | decimal | 9 | 1 |  |  |  |
| DKOriginalRetail | decimal | 9 | 1 |  |  |  |
| LicenseCode | varchar | 8000 | 1 |  |  |  |
| LicenseDescription | varchar | 8000 | 1 |  |  |  |
| FactoryCode | varchar | 8000 | 1 |  |  |  |
| FactoryName | varchar | 8000 | 1 |  |  |  |
| Primary_Vendor_Cur_Cost | decimal | 5 | 1 |  |  |  |
| MSTAT | varchar | 8000 | 1 |  |  |  |
| BufferQTY | int | 4 | 1 |  |  |  |
| WebActiveDate | date | 3 | 1 |  |  |  |
| RoyaltyStyle | varchar | 8000 | 1 |  |  |  |
| WebStatus | varchar | 8000 | 1 |  |  |  |
| WholeSaleStatus | varchar | 8000 | 1 |  |  |  |
| ChainAverageOnHandCost | decimal | 9 | 1 |  |  |  |
| ChainAverageOnHandCostGBP | decimal | 9 | 1 |  |  |  |
| isBRFstyle | bit | 1 | 1 |  |  |  |
| WebInventory | int | 4 | 1 |  |  |  |
