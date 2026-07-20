# dbo.dim_store

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store_Key | int | 4 | 1 |  |  |  |
| store_id | varchar | 8000 | 1 |  |  |  |
| StoreRanking | varchar | 8000 | 1 |  |  |  |
| store_name | varchar | 8000 | 1 |  |  |  |
| storeNameNum | varchar | 8000 | 1 |  |  |  |
| bearea | varchar | 8000 | 1 |  |  |  |
| bearritory | varchar | 8000 | 1 |  |  |  |
| RankedBearritory | varchar | 8000 | 1 |  |  |  |
| region | varchar | 8000 | 1 |  |  |  |
| RankedRegion | varchar | 8000 | 1 |  |  |  |
| GeographyRegion | varchar | 8000 | 1 |  |  |  |
| ParentCountry | varchar | 8000 | 1 |  |  |  |
| ChildCountry | varchar | 8000 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| country_name | varchar | 8000 | 1 |  |  |  |
| country_display | varchar | 8000 | 1 |  |  |  |
| state_province | varchar | 8000 | 1 |  |  |  |
| state_province_key | varchar | 8000 | 1 |  |  |  |
| city | varchar | 8000 | 1 |  |  |  |
| postal_code | varchar | 8000 | 1 |  |  |  |
| latitude | decimal | 9 | 1 |  |  |  |
| longitude | decimal | 9 | 1 |  |  |  |
| dma_name | varchar | 8000 | 1 |  |  |  |
| opening_date | datetime2 | 8 | 1 |  |  |  |
| opening_date_id | int | 4 | 1 |  |  |  |
| comp_week_id | int | 4 | 1 |  |  |  |
| open_fp_id | int | 4 | 1 |  |  |  |
| open_week_id | int | 4 | 1 |  |  |  |
| comp_date_key | int | 4 | 1 |  |  |  |
| ReportFlag | int | 4 | 1 |  |  |  |
| ClubMaxFlag | int | 4 | 1 |  |  |  |
| BearRange | varchar | 8000 | 1 |  |  |  |
| RankedBearRange | varchar | 8000 | 1 |  |  |  |
| CompanyLevel | varchar | 8000 | 1 |  |  |  |
| RankedCompanyLevel | varchar | 8000 | 1 |  |  |  |
| IsClosed | bit | 1 | 1 |  |  |  |
| closing_date_key | int | 4 | 1 |  |  |  |
| closing_date | datetime2 | 8 | 1 |  |  |  |
| closing_max_comp_date_key | int | 4 | 1 |  |  |  |
| closing_max_comp_date | datetime2 | 8 | 1 |  |  |  |
| closing_max_ly_comp_date_key | int | 4 | 1 |  |  |  |
| closing_max_ly_comp_date | datetime2 | 8 | 1 |  |  |  |
| MerchCompanyLevel | varchar | 8000 | 1 |  |  |  |
| MerchBearRange | varchar | 8000 | 1 |  |  |  |
| MerchCountry | varchar | 8000 | 1 |  |  |  |
| MerchRegion | varchar | 8000 | 1 |  |  |  |
| MerchBearritory | varchar | 8000 | 1 |  |  |  |
| isHispanicStore | bit | 1 | 1 |  |  |  |
| HispanicStoreGroup | varchar | 8000 | 1 |  |  |  |
| MerchBearRangeKey | varchar | 8000 | 1 |  |  |  |
| MerchCountryKey | varchar | 8000 | 1 |  |  |  |
| MerchRegionKey | varchar | 8000 | 1 |  |  |  |
| MerchBearitoryKey | varchar | 8000 | 1 |  |  |  |
| CountryKey | varchar | 8000 | 1 |  |  |  |
| RankedCompanyLevelKey | varchar | 8000 | 1 |  |  |  |
| RankedBearRangeKey | varchar | 8000 | 1 |  |  |  |
| RankedRegionKey | varchar | 8000 | 1 |  |  |  |
| RankedBearitoryKey | varchar | 8000 | 1 |  |  |  |
| BearRangeKey | varchar | 8000 | 1 |  |  |  |
| RegionKey | varchar | 8000 | 1 |  |  |  |
| BearitoryKey | varchar | 8000 | 1 |  |  |  |
| city_key | varchar | 8000 | 1 |  |  |  |
| city_display | varchar | 8000 | 1 |  |  |  |
| postal_code_key | varchar | 8000 | 1 |  |  |  |
| postal_code_display | varchar | 8000 | 1 |  |  |  |
| GeographyParentCountryKey | varchar | 8000 | 1 |  |  |  |
| GeographyRegionKey | varchar | 8000 | 1 |  |  |  |
| LocationType | varchar | 8000 | 1 |  |  |  |
| JurisdictionCode | varchar | 8000 | 1 |  |  |  |
| isFocusStore | varchar | 8000 | 1 |  |  |  |
| isNewSoundStore | varchar | 8000 | 1 |  |  |  |
| isShopperTrakStore | varchar | 8000 | 1 |  |  |  |
| plainCountry | varchar | 8000 | 1 |  |  |  |
| isWebStore | varchar | 8000 | 1 |  |  |  |
| Area | varchar | 8000 | 1 |  |  |  |
| AreaKey | varchar | 8000 | 1 |  |  |  |
