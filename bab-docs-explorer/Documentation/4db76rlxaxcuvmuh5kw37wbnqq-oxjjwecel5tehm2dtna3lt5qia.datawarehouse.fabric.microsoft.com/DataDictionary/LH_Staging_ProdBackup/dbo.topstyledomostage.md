# dbo.topstyledomostage

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TradingGroup | varchar | 8000 | 1 |  |  |  |
| Department | varchar | 8000 | 1 |  |  |  |
| DepartmentRank | bigint | 8 | 1 |  |  |  |
| DepartmentRankPreviousWeek | bigint | 8 | 1 |  |  |  |
| ConsumerGroupRank | bigint | 8 | 1 |  |  |  |
| ConsumerGroupRankPreviousWeek | bigint | 8 | 1 |  |  |  |
| YearToDateRank | bigint | 8 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| ConsumerGroup | varchar | 8000 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| StyleDescription | varchar | 8000 | 1 |  |  |  |
| Non_PromoRetail_US_CA | decimal | 9 | 1 |  |  |  |
| MSTAT | varchar | 8000 | 1 |  |  |  |
| SalesUnits1WeekAgo | int | 4 | 1 |  |  |  |
| SalesUnits2WeeksAgo | int | 4 | 1 |  |  |  |
| SalesUnits3WeeksAgo | int | 4 | 1 |  |  |  |
| SalesUnitsThisYear | int | 4 | 1 |  |  |  |
| SalesRetailTE1WeekAgo | decimal | 17 | 1 |  |  |  |
| AvgUnitRetail | decimal | 9 | 1 |  |  |  |
| AvgNonCLR_Markdown | decimal | 9 | 1 |  |  |  |
| Velocity | decimal | 9 | 1 |  |  |  |
| InStoreSellThroughPercentage | decimal | 9 | 1 |  |  |  |
| ChainInventory | int | 4 | 1 |  |  |  |
| OutletInventory | int | 4 | 1 |  |  |  |
| WebInventory | int | 4 | 1 |  |  |  |
| Ohio980Inventory | int | 4 | 1 |  |  |  |
| OhioLocked1000Inventory | int | 4 | 1 |  |  |  |
| WC960Inventory | int | 4 | 1 |  |  |  |
| UK2970Inventory | int | 4 | 1 |  |  |  |
| DoorCount | int | 4 | 1 |  |  |  |
| PastDuePlusCurrent | int | 4 | 1 |  |  |  |
| OnOrderNextPeriod | int | 4 | 1 |  |  |  |
| OnOrderNextPeriod2 | int | 4 | 1 |  |  |  |
| OnOrderNextPeriod3 | int | 4 | 1 |  |  |  |
| OnOrderNextPeriod4n5 | int | 4 | 1 |  |  |  |
| Aged | varchar | 8000 | 1 |  |  |  |
| InDate | varchar | 8000 | 1 |  |  |  |
| OutDate | varchar | 8000 | 1 |  |  |  |
| OutDateNote | varchar | 8000 | 1 |  |  |  |
| MerchWeek | int | 4 | 1 |  |  |  |
| ChainCode | varchar | 8000 | 1 |  |  |  |
| ChainLabel | varchar | 8000 | 1 |  |  |  |
| DivisionCode | varchar | 8000 | 1 |  |  |  |
| DivisionLabel | varchar | 8000 | 1 |  |  |  |
| DepartmentCode | varchar | 8000 | 1 |  |  |  |
| DepartmentLabel | varchar | 8000 | 1 |  |  |  |
| ClassCode | varchar | 8000 | 1 |  |  |  |
| ClassLabel | varchar | 8000 | 1 |  |  |  |
| SubClassCode | varchar | 8000 | 1 |  |  |  |
| SubClassLabel | varchar | 8000 | 1 |  |  |  |
| OutletStyles | varchar | 8000 | 1 |  |  |  |
| OutletMerchandiseStatus | varchar | 8000 | 1 |  |  |  |
| WholesaleMerchandiseStatus | varchar | 8000 | 1 |  |  |  |
| UnitCost | decimal | 17 | 1 |  |  |  |
| WebUSAvgUnitRetail | decimal | 9 | 1 |  |  |  |
| WebUKAvgUnitRetail | decimal | 9 | 1 |  |  |  |
| USWebNetSalesUnits1WeekAgo | int | 4 | 1 |  |  |  |
| USWebNetSalesUnits2WeeksAgo | int | 4 | 1 |  |  |  |
| USWebNetSalesUnits3WeeksAgo | int | 4 | 1 |  |  |  |
| USWebNetSalesRetailTe1WeekAgo | decimal | 17 | 1 |  |  |  |
| USWebNetSalesUnitsThisYear | int | 4 | 1 |  |  |  |
| UKWebNetSalesUnits1WeekAgo | int | 4 | 1 |  |  |  |
| UKWebNetSalesUnits2WeeksAgo | int | 4 | 1 |  |  |  |
| UKWebNetSalesUnits3WeeksAgo | int | 4 | 1 |  |  |  |
| UKWebNetSalesRetailTe1WeekAgo | decimal | 17 | 1 |  |  |  |
| UKWebNetSalesUnitsThisYear | int | 4 | 1 |  |  |  |
