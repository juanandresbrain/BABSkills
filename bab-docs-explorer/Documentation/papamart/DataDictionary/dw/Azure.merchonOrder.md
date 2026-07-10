# Azure.merchonOrder

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_ID | numeric | 9 | 0 |  |  |  |
| Location_id | smallint | 2 | 0 |  |  |  |
| Fiscal_Year | varchar | 4 | 1 |  |  |  |
| Fiscal_Period | varchar | 2 | 1 |  |  |  |
| On_Order | int | 4 | 1 |  |  |  |
| DateKey | datetime | 8 | 1 |  |  |  |
| PeriodKey | int | 4 | 1 |  |  |  |
| TotalFlag | int | 4 | 1 |  |  |  |
