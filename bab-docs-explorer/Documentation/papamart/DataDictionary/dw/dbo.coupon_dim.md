# dbo.coupon_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| coupon_key | int | 4 | 0 | YES |  | Surrogate key, IDENTITY column |
| Retail_Pro | int | 4 | 1 |  |  | Natural key: business key.  Populated by SSIS with reference number. |
| coupon_desc | varchar | 50 | 1 |  |  |  |
| start_date | datetime | 8 | 1 |  |  |  |
| stop_date | datetime | 8 | 1 |  |  |  |
| qty_distributed | int | 4 | 1 |  |  |  |
| event_id | int | 4 | 1 |  |  |  |
| event_name | varchar | 200 | 1 |  |  |  |
| category_id | int | 4 | 1 |  |  |  |
| category | varchar | 200 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| dmDiscountID | int | 4 | 0 |  |  |  |
| categoryTypeID | int | 4 | 0 |  |  |  |
