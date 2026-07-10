# Queries.TMP_SB_All_guest_with_address_2018H1

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| unique_guest_id | int | 4 | 0 |  |  |  |
| address | varchar | 121 | 0 |  |  |  |
| city | varchar | 60 | 1 |  |  |  |
| st | varchar | 5 | 1 |  |  |  |
| zip | varchar | 10 | 1 |  |  |  |
| country | varchar | 5 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| store_name | varchar | 255 | 1 |  |  |  |
| num_trans | int | 4 | 1 |  |  |  |
| sales | decimal | 17 | 1 |  |  |  |
