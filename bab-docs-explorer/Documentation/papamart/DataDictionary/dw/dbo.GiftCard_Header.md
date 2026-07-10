# dbo.GiftCard_Header

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FileID | int | 4 | 0 | YES |  |  |
| file_name | varchar | 250 | 1 |  |  |  |
| dw_processed_date | datetime | 8 | 1 |  |  |  |
| version | varchar | 2 | 1 |  |  |  |
| processed_date | datetime | 8 | 1 |  |  |  |
| period_start_date | datetime | 8 | 1 |  |  |  |
| period_end_date | datetime | 8 | 1 |  |  |  |
| file_number | int | 4 | 1 |  |  |  |
| number_of_files | int | 4 | 1 |  |  |  |
| file_data_type | varchar | 3 | 1 |  |  |  |
| record_length | int | 4 | 1 |  |  |  |
| sequence_number | int | 4 | 1 |  |  |  |
| prev_sequence_number | int | 4 | 1 |  |  |  |
| rows_found | int | 4 | 1 |  |  |  |
| rows_expected | int | 4 | 1 |  |  |  |
| footer_found | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
