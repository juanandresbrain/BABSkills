# dbo.azure_franchisee_monthly_royalty

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| CountryNameFull | varchar | 8000 | 1 |  |  |  |
| TotalSales | decimal | 9 | 1 |  |  |  |
| FootwareSales | decimal | 17 | 1 |  |  |  |
| SoundSales | decimal | 17 | 1 |  |  |  |
| UnstuffedSales | decimal | 17 | 1 |  |  |  |
| PartySales | decimal | 9 | 1 |  |  |  |
| GiftCardSales | decimal | 17 | 1 |  |  |  |
| AccessoriesSales | decimal | 17 | 1 |  |  |  |
| ClothesSales | decimal | 17 | 1 |  |  |  |
| SportsSales | decimal | 17 | 1 |  |  |  |
| PrestuffedSales | decimal | 17 | 1 |  |  |  |
| GiftCardsRedeemed | decimal | 17 | 1 |  |  |  |
| FriendSales | decimal | 9 | 1 |  |  |  |
| HumanSales | decimal | 9 | 1 |  |  |  |
| PetSales | decimal | 9 | 1 |  |  |  |
| StuffersSales | decimal | 9 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| ExchangeRate | float | 8 | 1 |  |  |  |
| RoyltyRate | varchar | 8000 | 1 |  |  |  |
| week_of_period | int | 4 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| StoreNameAbbr | varchar | 8000 | 1 |  |  |  |
| TaxRate | decimal | 9 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| to_currency_code | varchar | 8000 | 1 |  |  |  |
| GaapSalesUSD | float | 8 | 1 |  |  |  |
| RoyaltyRate | float | 8 | 1 |  |  |  |
| TotalRoyalty | float | 8 | 1 |  |  |  |
| TaxWitholding | float | 8 | 1 |  |  |  |
| TotalRoyaltyDue | float | 8 | 1 |  |  |  |
| ExchangeRates | float | 8 | 1 |  |  |  |
