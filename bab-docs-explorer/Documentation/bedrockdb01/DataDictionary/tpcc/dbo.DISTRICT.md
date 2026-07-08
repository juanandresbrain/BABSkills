# dbo.DISTRICT

**Database:** tpcc  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| d_id | tinyint | 1 | 0 |  |  |  |
| d_w_id | int | 4 | 0 |  |  |  |
| d_ytd | money | 8 | 0 |  |  |  |
| d_next_o_id | int | 4 | 1 |  |  |  |
| d_tax | smallmoney | 4 | 1 |  |  |  |
| d_name | char | 10 | 1 |  |  |  |
| d_street_1 | char | 20 | 1 |  |  |  |
| d_street_2 | char | 20 | 1 |  |  |  |
| d_city | char | 20 | 1 |  |  |  |
| d_state | char | 2 | 1 |  |  |  |
| d_zip | char | 9 | 1 |  |  |  |
| padding | char | 6000 | 0 |  |  |  |
