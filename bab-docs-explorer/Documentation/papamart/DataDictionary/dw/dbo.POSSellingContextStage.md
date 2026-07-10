# dbo.POSSellingContextStage

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | varchar | 30 | 1 |  |  |  |
| StoreNumber | varchar | 4 | 1 |  |  |  |
| LocationID | nvarchar | 40 | 0 |  |  |  |
| TaxJurisdictionCode | nchar | 10 | 1 |  |  |  |
| DefaultCurrencyCode | nchar | 6 | 1 |  |  |  |
| StoreKey | varchar | 30 | 1 |  |  |  |
| PermCloseStatus | int | 4 | 0 |  |  |  |
| StoreNameAbbr | varchar | 50 | 0 |  |  |  |
| StoreNameFull | varchar | 255 | 0 |  |  |  |
| StorePhoneNumber | varchar | 100 | 1 |  |  |  |
| StoreEmail | varchar | 255 | 1 |  |  |  |
| TimeZoneDesc | varchar | 30 | 1 |  |  |  |
| Address1 | varchar | 255 | 1 |  |  |  |
| Address2 | varchar | 255 | 1 |  |  |  |
| City | varchar | 50 | 1 |  |  |  |
| StateProvinceNameAbbr | varchar | 10 | 1 |  |  |  |
| StateProvinceNameFull | varchar | 255 | 1 |  |  |  |
| Zip | varchar | 50 | 1 |  |  |  |
| StoreLocator | varchar | 8000 | 1 |  |  |  |
| StoreMallWebsiteURL | varchar | 255 | 1 |  |  |  |
| StoreLongitude | numeric | 9 | 1 |  |  |  |
| StoreLatitude | numeric | 9 | 1 |  |  |  |
| StoreLegalDescription | varchar | 50 | 1 |  |  |  |
| Channel | varchar | 6 | 0 |  |  |  |
| TradingGroup | varchar | 13 | 1 |  |  |  |
| CountryNameAbbr | varchar | 50 | 1 |  |  |  |
| CountryNameFull | varchar | 50 | 1 |  |  |  |
| SubChannel | varchar | 57 | 1 |  |  |  |
| Zone | varchar | 100 | 0 |  |  |  |
| Area | varchar | 100 | 0 |  |  |  |
| District | varchar | 100 | 0 |  |  |  |
| CompanyLevel | varchar | 7 | 0 |  |  |  |
| BearRange | varchar | 13 | 0 |  |  |  |
| bearea | varchar | 100 | 1 |  |  |  |
| bearritory | varchar | 103 | 1 |  |  |  |
| DCSource | nvarchar | 12 | 1 |  |  |  |
| DistroDay | nvarchar | 12 | 1 |  |  |  |
| DeliveryDay | nvarchar | 12 | 1 |  |  |  |
| SoundStore | nvarchar | 12 | 1 |  |  |  |
| StoreConcept | nvarchar | 12 | 1 |  |  |  |
| FocusFifty | nvarchar | 12 | 1 |  |  |  |
| LocationType | nvarchar | 12 | 1 |  |  |  |
| StoreOpenStatus | varchar | 6 | 0 |  |  |  |
| StoreDesign | varchar | 255 | 1 |  |  |  |
| isBRFstore | bit | 1 | 0 |  |  |  |
| WebOrStore | varchar | 5 | 0 |  |  |  |
| isEndlessAisleEligible | int | 4 | 1 |  |  |  |
| WarehouseLegalEntity | nvarchar | 8000 | 1 |  |  |  |
| OperatingUnitNumber | nvarchar | 8000 | 1 |  |  |  |
