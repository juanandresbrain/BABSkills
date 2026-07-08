# dbo.Cs_FileStat_1002

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transmission_id | int | 4 | 0 |  |  |  |
| cs_file_id | int | 4 | 0 |  |  |  |
| status_id | smallint | 2 | 0 |  |  |  |
| found_datafile_datetime | datetime | 8 | 0 |  |  |  |
| number_of_files | tinyint | 1 | 0 |  |  |  |
| sent_to_polling_datetime | datetime | 8 | 1 |  |  |  |
| sent_to_polling_filename | varchar | 30 | 1 |  |  |  |
| polling_results_datetime | datetime | 8 | 1 |  |  |  |
| polling_results_code | int | 4 | 1 |  |  |  |
| polling_results_message | varchar | 255 | 1 |  |  |  |
| service_confirmation_datetime | datetime | 8 | 1 |  |  |  |
| service_confirmation_contents | text | 16 | 1 |  |  |  |
| from_execution_id | int | 4 | 0 |  |  |  |
| to_execution_id | int | 4 | 0 |  |  |  |
| retransmitted_datetime | datetime | 8 | 1 |  |  |  |
| validated_datetime | datetime | 8 | 1 |  |  |  |
| validated_user_id | int | 4 | 1 |  |  |  |
| backup_still_exists | smallint | 2 | 1 |  |  |  |
