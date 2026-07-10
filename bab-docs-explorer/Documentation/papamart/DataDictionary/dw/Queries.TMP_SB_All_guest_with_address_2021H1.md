# Queries.TMP_SB_All_guest_with_address_2021H1

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| unique_guest_id | numeric | 13 | 0 |  |  |  |
| address | nvarchar | 162 | 0 |  |  |  |
| city | nvarchar | 80 | 1 |  |  |  |
| st | nvarchar | 80 | 1 |  |  |  |
| zip | nvarchar | 40 | 1 |  |  |  |
| country | nchar | 6 | 0 |  |  |  |
| store_id | int | 4 | 0 |  |  |  |
| store_name | nvarchar | 60 | 0 |  |  |  |
| num_trans | int | 4 | 1 |  |  |  |
| sales | money | 8 | 1 |  |  |  |
