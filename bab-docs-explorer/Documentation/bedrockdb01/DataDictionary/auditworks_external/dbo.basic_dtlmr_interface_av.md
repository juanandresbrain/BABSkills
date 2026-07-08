# dbo.basic_dtlmr_interface_av

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | char | 8 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| seq | tinyint | 1 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| entry_time | char | 4 | 0 |  |  |  |
| transaction_code | char | 1 | 0 |  |  |  |
| subcode | char | 3 | 0 |  |  |  |
| identifier | char | 20 | 0 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| extended_amount | int | 4 | 0 |  |  |  |
| tender_total | int | 4 | 0 |  |  |  |
| subsystem | char | 15 | 0 |  |  |  |
| swap_flag | tinyint | 1 | 1 |  |  |  |
