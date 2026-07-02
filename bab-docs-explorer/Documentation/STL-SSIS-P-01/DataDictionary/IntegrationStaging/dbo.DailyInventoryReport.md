# dbo.DailyInventoryReport

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Style_Code | varchar | 6 | 1 |  |  |  |
| DisplayName | nvarchar | 300 | 1 |  |  |  |
| HierarchyGroupCode | nvarchar | 40 | 1 |  |  |  |
| keyStory | nvarchar | 60 | 1 |  |  |  |
| mstat | nvarchar | 12 | 1 |  |  |  |
| OrderMultiple | int | 4 | 1 |  |  |  |
| MerchInDate | datetime | 8 | 1 |  |  |  |
| PreviousWeekSales | int | 4 | 1 |  |  |  |
| WTDSales | int | 4 | 1 |  |  |  |
| YesterdaySales | int | 4 | 1 |  |  |  |
| Inventory | int | 4 | 1 |  |  |  |
| Purchased | int | 4 | 1 |  |  |  |
| InventoryBuffer | int | 4 | 1 |  |  |  |
| ProductSellingGeography | char | 2 | 1 |  |  |  |
| AllocatedQTY | int | 4 | 1 |  |  |  |
| YesterdayEnterpriseSales | int | 4 | 1 |  |  |  |
| WTDEnterpriseSales | int | 4 | 1 |  |  |  |
| MTDSales | int | 4 | 1 |  |  |  |
| MTDEnterpriseSales | int | 4 | 1 |  |  |  |
| InTransit | int | 4 | 1 |  |  |  |
| AvailableToDist | int | 4 | 1 |  |  |  |
| LatWeekEnterpriseSales | int | 4 | 1 |  |  |  |

