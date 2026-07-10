# dbo.tmp_wbi_rawdata_summary

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 0 |  |  |  |
| store_id | varchar | 8000 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| gaapsales | decimal | 17 | 1 |  |  |  |
| merchandiseunits | int | 4 | 1 |  |  |  |
| animalunits | int | 4 | 1 |  |  |  |
| partyflag | int | 4 | 0 |  |  |  |
| division | varchar | 20 | 1 |  |  |  |
| hour | int | 4 | 1 |  |  |  |
| half_hour_id | int | 4 | 1 |  |  |  |
