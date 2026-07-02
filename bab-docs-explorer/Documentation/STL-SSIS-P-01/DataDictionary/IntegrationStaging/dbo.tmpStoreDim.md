# dbo.tmpStoreDim

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | varchar | 30 | 1 |  |  |  |
| StoreNumber | varchar | 10 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| PermCloseStatus | int | 4 | 0 |  |  |  |
| StoreNameAbbr | varchar | 100 | 1 |  |  |  |
| StoreNameFull | varchar | 255 | 1 |  |  |  |
| StorePhoneNumber | varchar | 100 | 1 |  |  |  |
| StoreFaxNumber | varchar | 255 | 1 |  |  |  |
| StoreEmail | varchar | 255 | 1 |  |  |  |
| TimeZoneDesc | varchar | 30 | 1 |  |  |  |
| StateProvinceNameAbbr | varchar | 10 | 1 |  |  |  |
| StateProvinceNameFull | varchar | 255 | 1 |  |  |  |
| StoreLocator | varchar | 8000 | 1 |  |  |  |
| StoreMallWebsiteURL | varchar | 255 | 1 |  |  |  |
| StoreLongitude | numeric | 9 | 1 |  |  |  |
| StoreLatitude | numeric | 9 | 1 |  |  |  |
| StoreLegalDescription | varchar | 50 | 1 |  |  |  |
| Channel | varchar | 8 | 0 |  |  |  |
| TradingGroup | varchar | 62 | 1 |  |  |  |
| CountryNameAbbr | nvarchar | 100 | 1 |  |  |  |
| CountryNameFull | varchar | 50 | 1 |  |  |  |
| SubChannel | nvarchar | 114 | 1 |  |  |  |
| Zone | varchar | 100 | 0 |  |  |  |
| Area | varchar | 100 | 0 |  |  |  |
| District | varchar | 100 | 0 |  |  |  |
| CompanyLevel | varchar | 11 | 0 |  |  |  |
| BearRange | varchar | 50 | 1 |  |  |  |
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
| isBRFstore | int | 4 | 0 |  |  |  |
| WebOrStore | varchar | 5 | 0 |  |  |  |

