# dbo.possellingcontextstage

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | varchar | 8000 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| LocationID | varchar | 8000 | 1 |  |  |  |
| TaxJurisdictionCode | varchar | 8000 | 1 |  |  |  |
| DefaultCurrencyCode | varchar | 8000 | 1 |  |  |  |
| StoreKey | varchar | 8000 | 1 |  |  |  |
| PermCloseStatus | int | 4 | 1 |  |  |  |
| StoreNameAbbr | varchar | 8000 | 1 |  |  |  |
| StoreNameFull | varchar | 8000 | 1 |  |  |  |
| StorePhoneNumber | varchar | 8000 | 1 |  |  |  |
| StoreEmail | varchar | 8000 | 1 |  |  |  |
| TimeZoneDesc | varchar | 8000 | 1 |  |  |  |
| Address1 | varchar | 8000 | 1 |  |  |  |
| Address2 | varchar | 8000 | 1 |  |  |  |
| City | varchar | 8000 | 1 |  |  |  |
| StateProvinceNameAbbr | varchar | 8000 | 1 |  |  |  |
| StateProvinceNameFull | varchar | 8000 | 1 |  |  |  |
| Zip | varchar | 8000 | 1 |  |  |  |
| StoreLocator | varchar | 8000 | 1 |  |  |  |
| StoreMallWebsiteURL | varchar | 8000 | 1 |  |  |  |
| StoreLongitude | decimal | 9 | 1 |  |  |  |
| StoreLatitude | decimal | 9 | 1 |  |  |  |
| StoreLegalDescription | varchar | 8000 | 1 |  |  |  |
| Channel | varchar | 8000 | 1 |  |  |  |
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| CountryNameAbbr | varchar | 8000 | 1 |  |  |  |
| CountryNameFull | varchar | 8000 | 1 |  |  |  |
| SubChannel | varchar | 8000 | 1 |  |  |  |
| Zone | varchar | 8000 | 1 |  |  |  |
| Area | varchar | 8000 | 1 |  |  |  |
| District | varchar | 8000 | 1 |  |  |  |
| CompanyLevel | varchar | 8000 | 1 |  |  |  |
| BearRange | varchar | 8000 | 1 |  |  |  |
| bearea | varchar | 8000 | 1 |  |  |  |
| bearritory | varchar | 8000 | 1 |  |  |  |
| DCSource | varchar | 8000 | 1 |  |  |  |
| DistroDay | varchar | 8000 | 1 |  |  |  |
| DeliveryDay | varchar | 8000 | 1 |  |  |  |
| SoundStore | varchar | 8000 | 1 |  |  |  |
| StoreConcept | varchar | 8000 | 1 |  |  |  |
| FocusFifty | varchar | 8000 | 1 |  |  |  |
| LocationType | varchar | 8000 | 1 |  |  |  |
| StoreOpenStatus | varchar | 8000 | 1 |  |  |  |
| StoreDesign | varchar | 8000 | 1 |  |  |  |
| isBRFstore | bit | 1 | 1 |  |  |  |
| WebOrStore | varchar | 8000 | 1 |  |  |  |
| isEndlessAisleEligible | int | 4 | 1 |  |  |  |
| WarehouseLegalEntity | varchar | 8000 | 1 |  |  |  |
| OperatingUnitNumber | varchar | 8000 | 1 |  |  |  |
