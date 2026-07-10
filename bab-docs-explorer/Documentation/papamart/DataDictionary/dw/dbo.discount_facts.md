# dbo.discount_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| coupon_key | int | 4 | 0 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| reference_no | varchar | 20 | 1 |  |  |  |
| process_name | varchar | 50 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
| uid | int | 4 | 0 | YES |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 1 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 1 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 1 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| categoryTypeID | int | 4 | 0 |  |  |  |
| isExpired | bit | 1 | 0 |  |  |  |
| lift_amount | money | 8 | 0 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
