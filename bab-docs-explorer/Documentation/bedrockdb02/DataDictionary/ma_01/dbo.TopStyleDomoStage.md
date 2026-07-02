# dbo.TopStyleDomoStage

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TradingGroup | varchar | 2 | 1 |  |  |  |
| Department | nvarchar | 80 | 0 |  |  |  |
| DepartmentRank | bigint | 8 | 0 |  |  |  |
| DepartmentRankPreviousWeek | bigint | 8 | 0 |  |  |  |
| ConsumerGroupRank | bigint | 8 | 0 |  |  |  |
| ConsumerGroupRankPreviousWeek | bigint | 8 | 0 |  |  |  |
| YearToDateRank | bigint | 8 | 0 |  |  |  |
| KeyStory | nvarchar | 60 | 0 |  |  |  |
| ConsumerGroup | nvarchar | 80 | 0 |  |  |  |
| Style | nvarchar | 40 | 1 |  |  |  |
| StyleDescription | nvarchar | 240 | 1 |  |  |  |
| Non_PromoRetail_US_CA | decimal | 9 | 1 |  |  |  |
| MSTAT | nvarchar | 12 | 0 |  |  |  |
| SalesUnits1WeekAgo | int | 4 | 0 |  |  |  |
| SalesUnits2WeeksAgo | int | 4 | 0 |  |  |  |
| SalesUnits3WeeksAgo | int | 4 | 0 |  |  |  |
| SalesUnitsThisYear | int | 4 | 0 |  |  |  |
| SalesRetailTE1WeekAgo | decimal | 17 | 0 |  |  |  |
| AvgUnitRetail | decimal | 9 | 0 |  |  |  |
| AvgNonCLR_Markdown | decimal | 9 | 0 |  |  |  |
| Velocity | decimal | 9 | 1 |  |  |  |
| InStoreSellThroughPercentage | decimal | 9 | 0 |  |  |  |
| ChainInventory | int | 4 | 1 |  |  |  |
| OutletInventory | int | 4 | 1 |  |  |  |
| WebInventory | int | 4 | 1 |  |  |  |
| Ohio980Inventory | int | 4 | 1 |  |  |  |
| OhioLocked1000Inventory | int | 4 | 1 |  |  |  |
| WC960Inventory | int | 4 | 1 |  |  |  |
| UK2970Inventory | int | 4 | 1 |  |  |  |
| DoorCount | int | 4 | 1 |  |  |  |
| PastDuePlusCurrent | int | 4 | 1 |  |  |  |
| OnOrderNextPeriod | int | 4 | 0 |  |  |  |
| OnOrderNextPeriod2 | int | 4 | 0 |  |  |  |
| OnOrderNextPeriod3 | int | 4 | 0 |  |  |  |
| OnOrderNextPeriod4n5 | int | 4 | 1 |  |  |  |
| Aged | varchar | 1 | 1 |  |  |  |
| InDate | nvarchar | 60 | 0 |  |  |  |
| OutDate | nvarchar | 60 | 1 |  |  |  |
| OutDateNote | nvarchar | 60 | 0 |  |  |  |
| MerchWeek | int | 4 | 1 |  |  |  |
| ChainCode | nvarchar | 40 | 0 |  |  |  |
| ChainLabel | nvarchar | 80 | 0 |  |  |  |
| DivisionCode | nvarchar | 40 | 0 |  |  |  |
| DivisionLabel | nvarchar | 80 | 0 |  |  |  |
| DepartmentCode | nvarchar | 40 | 0 |  |  |  |
| DepartmentLabel | nvarchar | 80 | 0 |  |  |  |
| ClassCode | nvarchar | 40 | 0 |  |  |  |
| ClassLabel | nvarchar | 80 | 0 |  |  |  |
| SubClassCode | nvarchar | 40 | 0 |  |  |  |
| SubClassLabel | nvarchar | 80 | 0 |  |  |  |
| OutletStyles | nvarchar | 12 | 0 |  |  |  |
| OutletMerchandiseStatus | nvarchar | 12 | 0 |  |  |  |
| WholesaleMerchandiseStatus | nvarchar | 12 | 0 |  |  |  |
| UnitCost | decimal | 17 | 0 |  |  |  |
| WebUSAvgUnitRetail | decimal | 9 | 0 |  |  |  |
| WebUKAvgUnitRetail | decimal | 9 | 0 |  |  |  |
| USWebNetSalesUnits1WeekAgo | int | 4 | 0 |  |  |  |
| USWebNetSalesUnits2WeeksAgo | int | 4 | 0 |  |  |  |
| USWebNetSalesUnits3WeeksAgo | int | 4 | 0 |  |  |  |
| USWebNetSalesRetailTe1WeekAgo | decimal | 17 | 0 |  |  |  |
| USWebNetSalesUnitsThisYear | int | 4 | 0 |  |  |  |
| UKWebNetSalesUnits1WeekAgo | int | 4 | 0 |  |  |  |
| UKWebNetSalesUnits2WeeksAgo | int | 4 | 0 |  |  |  |
| UKWebNetSalesUnits3WeeksAgo | int | 4 | 0 |  |  |  |
| UKWebNetSalesRetailTe1WeekAgo | decimal | 17 | 0 |  |  |  |
| UKWebNetSalesUnitsThisYear | int | 4 | 0 |  |  |  |

