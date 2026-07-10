# dbo.transaction_detail_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 0 |  |  |  |
| currency_key | int | 4 | 0 |  |  |  |
| transaction_id | decimal | 9 | 0 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| Register_Num | int | 4 | 0 |  |  |  |
| cashier_id | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| party_y_n | char | 1 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| tdf_key | int | 4 | 0 | YES |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| vat_tax_amount | decimal | 5 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 1 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 1 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 1 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| upsell_disc_allocated | money | 8 | 1 |  |  | This is the amount of unit_disc_amount which is from the allocation of the upsell discounts. |
| ext_cost | money | 8 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
