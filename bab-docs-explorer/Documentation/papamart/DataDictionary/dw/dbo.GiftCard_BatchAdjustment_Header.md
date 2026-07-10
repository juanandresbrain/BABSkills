# dbo.GiftCard_BatchAdjustment_Header

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| batch_id | int | 4 | 0 | YES |  |  |
| record_format_indicator | char | 1 | 0 |  |  |  |
| version | char | 2 | 0 |  |  |  |
| revision | char | 2 | 0 |  |  |  |
| processed_date | char | 13 | 0 |  |  |  |
| period_start_date | char | 13 | 0 |  |  |  |
| period_end_date | char | 13 | 0 |  |  |  |
| file_number | char | 4 | 0 |  |  |  |
| number_of_files | char | 4 | 0 |  |  |  |
| file_data_type | char | 3 | 0 |  |  |  |
| reserved_flag | char | 4 | 0 |  |  |  |
| record_length | char | 4 | 0 |  |  |  |
| sequence_number | char | 4 | 0 |  |  |  |
| prev_sequence_number | char | 4 | 0 |  |  |  |
| relative_post_date | char | 1 | 0 |  |  |  |
| filler | char | 227 | 0 |  |  |  |
