# dbo.Household_Activity_Facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Household_key | int | 4 | 0 |  |  |  |
| Number_Of_Visits | int | 4 | 1 |  |  |  |
| First_Visit_date_key | int | 4 | 1 |  |  |  |
| Last_Visit_date_key | int | 4 | 1 |  |  |  |
| Recency_in_Months | int | 4 | 1 |  |  |  |
| Nearest_store | int | 4 | 1 |  |  | uses store_key |
| Distinace_To_Nearest_Store | float | 8 | 1 |  |  |  |
| trade_area_group_key | int | 4 | 1 |  |  |  |
