# dbo.giftcard_header

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FileID | int | 4 | 1 |  |  |  |
| file_name | varchar | 8000 | 1 |  |  |  |
| dw_processed_date | datetime2 | 8 | 1 |  |  |  |
| version | varchar | 8000 | 1 |  |  |  |
| processed_date | datetime2 | 8 | 1 |  |  |  |
| period_start_date | datetime2 | 8 | 1 |  |  |  |
| period_end_date | datetime2 | 8 | 1 |  |  |  |
| file_number | int | 4 | 1 |  |  |  |
| number_of_files | int | 4 | 1 |  |  |  |
| file_data_type | varchar | 8000 | 1 |  |  |  |
| record_length | int | 4 | 1 |  |  |  |
| sequence_number | int | 4 | 1 |  |  |  |
| prev_sequence_number | int | 4 | 1 |  |  |  |
| rows_found | int | 4 | 1 |  |  |  |
| rows_expected | int | 4 | 1 |  |  |  |
| footer_found | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
