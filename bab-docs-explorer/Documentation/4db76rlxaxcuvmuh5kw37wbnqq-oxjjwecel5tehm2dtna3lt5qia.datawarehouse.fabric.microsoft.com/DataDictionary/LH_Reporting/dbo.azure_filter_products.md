# dbo.azure_filter_products

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductKey | int | 4 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| StyleDescription | varchar | 8000 | 1 |  |  |  |
| FilterStyle-Desc | varchar | 8000 | 1 |  |  |  |
| Concept | varchar | 8000 | 1 |  |  |  |
| Filter_Chain | varchar | 8000 | 1 |  |  |  |
| Filter_Division | varchar | 8000 | 1 |  |  |  |
| Filter_Department | varchar | 8000 | 1 |  |  |  |
| Filter_Class | varchar | 8000 | 1 |  |  |  |
| Filter_SubClass | varchar | 8000 | 1 |  |  |  |
| Filter_KeyStory | varchar | 8000 | 1 |  |  |  |
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
| isBRFstyle | int | 4 | 1 |  |  |  |
| WebInventory | int | 4 | 1 |  |  |  |
