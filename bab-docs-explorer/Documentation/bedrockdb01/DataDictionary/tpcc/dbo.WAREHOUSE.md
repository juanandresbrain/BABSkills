# dbo.WAREHOUSE

**Database:** tpcc  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| w_id | int | 4 | 0 |  |  |  |
| w_ytd | money | 8 | 0 |  |  |  |
| w_tax | smallmoney | 4 | 0 |  |  |  |
| w_name | char | 10 | 1 |  |  |  |
| w_street_1 | char | 20 | 1 |  |  |  |
| w_street_2 | char | 20 | 1 |  |  |  |
| w_city | char | 20 | 1 |  |  |  |
| w_state | char | 2 | 1 |  |  |  |
| w_zip | char | 9 | 1 |  |  |  |
| padding | char | 4000 | 0 |  |  |  |
