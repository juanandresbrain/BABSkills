# WEB.InventoryFactWebArchive

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 0 |  |  |  |
| GTIN | varchar | 20 | 0 |  |  |  |
| StyleCode | varchar | 6 | 0 |  |  |  |
| QTY | int | 4 | 0 |  |  |  |
| PreviousQTY | int | 4 | 1 |  |  |  |
| SellingGeography | varchar | 2 | 1 |  |  |  |
| UnbufferedQty | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CheckDate | datetime | 8 | 0 |  |  |  |

