# Azure.FranchiseeTSPA

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WeekEndingDate | date | 3 | 1 |  |  |  |
| FranchiseeCountry | varchar | 50 | 1 |  |  |  |
| Dept | varchar | 20 | 1 |  |  |  |
| DptRnk | bigint | 8 | 1 |  |  |  |
| DptRnkPW | bigint | 8 | 1 |  |  |  |
| CGrpRnk | bigint | 8 | 1 |  |  |  |
| CGrpRnkPW | bigint | 8 | 1 |  |  |  |
| YTDRnk | bigint | 8 | 1 |  |  |  |
| KeyStory | nvarchar | 60 | 1 |  |  |  |
| ConsGrp | varchar | 20 | 1 |  |  |  |
| Style# | varchar | 6 | 1 |  |  |  |
| StyleDesc | varchar | 20 | 1 |  |  |  |
| NonPromoRtl | decimal | 9 | 1 |  |  |  |
| MSTAT | varchar | 6 | 1 |  |  |  |
| SlsULW | int | 4 | 1 |  |  |  |
| SlsUPW | int | 4 | 0 |  |  |  |
| SlsU2PW | int | 4 | 0 |  |  |  |
| SlsUYTD | int | 4 | 1 |  |  |  |
| SlsR$ | numeric | 17 | 1 |  |  |  |
| AUR | numeric | 5 | 1 |  |  |  |
| Velcty | numeric | 5 | 1 |  |  |  |
| InStrST | numeric | 5 | 1 |  |  |  |
| StoreOnHand | int | 4 | 1 |  |  |  |
| WebStoresOnHand | int | 4 | 1 |  |  |  |
| WarehouseOnHand | int | 4 | 1 |  |  |  |
| TotalOnHand | int | 4 | 1 |  |  |  |
| WeeksOfSupply | int | 4 | 1 |  |  |  |
| DueByJAN | int | 4 | 0 |  |  |  |
| DueByFEB | int | 4 | 0 |  |  |  |
| DueByMAR | int | 4 | 0 |  |  |  |
| DueByAPR | int | 4 | 0 |  |  |  |
| DueByMAY | int | 4 | 0 |  |  |  |
| DueByJUN | int | 4 | 0 |  |  |  |
| DueByJUL | int | 4 | 0 |  |  |  |
| DueByAUG | int | 4 | 0 |  |  |  |
| DueBySEP | int | 4 | 0 |  |  |  |
| DueByOCT | int | 4 | 0 |  |  |  |
| DueByNOV | int | 4 | 0 |  |  |  |
| DueByDEC | int | 4 | 0 |  |  |  |
