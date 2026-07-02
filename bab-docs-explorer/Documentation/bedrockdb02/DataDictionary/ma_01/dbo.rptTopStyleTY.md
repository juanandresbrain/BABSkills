# dbo.rptTopStyleTY

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Department | nvarchar | 80 | 1 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| style_desc | nvarchar | 240 | 1 |  |  |  |
| NetSalesUnits1WeekAgo | int | 4 | 0 |  |  |  |
| NetSalesRetailTe1WeekAgo | decimal | 17 | 0 |  |  |  |
| EOPOnHandUnitsTotal1WeekAgo | int | 4 | 0 |  |  |  |
| OnOrderUnitsPastDuePeriods | int | 4 | 0 |  |  |  |
| OnOrderUnitsThisPeriod | int | 4 | 0 |  |  |  |
| OnOrderUnitsNext1Period | int | 4 | 0 |  |  |  |
| OnOrderUnitsNext2Period | int | 4 | 0 |  |  |  |
| OnOrderUnitsNext3Period | int | 4 | 0 |  |  |  |
| OnOrderUnitsNext4Period | int | 4 | 0 |  |  |  |
| OnOrderUnitsNext5Period | int | 4 | 0 |  |  |  |
| OutDate | nvarchar | 60 | 1 |  |  |  |
| OutDateNote | nvarchar | 60 | 0 |  |  |  |
| PastPlusCurrOO | int | 4 | 0 |  |  |  |
| Plus1Period | int | 4 | 0 |  |  |  |
| Plus2And3Periods | int | 4 | 0 |  |  |  |
| Plus4And5Periods | int | 4 | 0 |  |  |  |
| MerchandiseStatus | nvarchar | 12 | 0 |  |  |  |
| NetSalesUnitsLast1WeekLY | int | 4 | 0 |  |  |  |
| NetSalesRetailTELast1WeekLY | decimal | 17 | 0 |  |  |  |
| EOPOnHandUnitsTotalLast1WeekLY | int | 4 | 0 |  |  |  |
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
| EOPOnHandStrUnitsTotal1WeekAgo | int | 4 | 0 |  |  |  |
| EOPOnHandWHUnitsTotal1WeekAgo | int | 4 | 0 |  |  |  |
| EOPOnHandStrUnitsTotalLast1WeekLY | int | 4 | 0 |  |  |  |
| EOPOnHandWHUnitsTotalLast1WeekLY | int | 4 | 0 |  |  |  |
| EOPOnHandCostTotalLast1Week | decimal | 17 | 0 |  |  |  |
| EOPOnHandCostTotalLast1WeekLY | decimal | 17 | 0 |  |  |  |
| NetSalesUnits2WeeksAgo | int | 4 | 0 |  |  |  |
| NetSalesUnits3WeeksAgo | int | 4 | 0 |  |  |  |
| NetSalesUnitsLast2WeeksLY | int | 4 | 0 |  |  |  |
| NetSalesUnitsLast3WeeksLY | int | 4 | 0 |  |  |  |
| NetSalesUnitsThisYear | int | 4 | 0 |  |  |  |
| NetSalesUnitsyeartoDateWeeksLY | int | 4 | 0 |  |  |  |
| KeyStory | nvarchar | 60 | 0 |  |  |  |
| OutletStyles | nvarchar | 12 | 0 |  |  |  |
| InDate | nvarchar | 60 | 0 |  |  |  |
| WMSTAT | nvarchar | 12 | 0 |  |  |  |
| OMSTAT | nvarchar | 12 | 0 |  |  |  |
| USWebNetSalesUnits1WeekAgo | int | 4 | 0 |  |  |  |
| USWebNetSalesRetailTe1WeekAgo | decimal | 17 | 0 |  |  |  |
| USWebNetSalesUnits2WeeksAgo | int | 4 | 0 |  |  |  |
| USWebNetSalesUnits3WeeksAgo | int | 4 | 0 |  |  |  |
| USWebNetSalesUnitsThisYear | int | 4 | 0 |  |  |  |
| UKWebNetSalesUnits1WeekAgo | int | 4 | 0 |  |  |  |
| UKWebNetSalesRetailTe1WeekAgo | decimal | 17 | 0 |  |  |  |
| UKWebNetSalesUnits2WeeksAgo | int | 4 | 0 |  |  |  |
| UKWebNetSalesUnits3WeeksAgo | int | 4 | 0 |  |  |  |
| UKWebNetSalesUnitsThisYear | int | 4 | 0 |  |  |  |
| USWebNetSalesRetailTELast1WeekLY | decimal | 17 | 0 |  |  |  |
| USWebNetSalesUnitsLast1WeekLY | int | 4 | 0 |  |  |  |
| UKWebNetSalesRetailTELast1WeekLY | decimal | 17 | 0 |  |  |  |
| UKWebNetSalesUnitsLast1WeekLY | int | 4 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| MerchWeek | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.spMerchandisingTopStyleStage](../../StoredProcedures/ma_01/dbo.spMerchandisingTopStyleStage.md)

