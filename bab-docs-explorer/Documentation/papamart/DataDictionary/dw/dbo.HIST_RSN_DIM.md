# dbo.HIST_RSN_DIM

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HIST_RSN_ID | int | 4 | 0 | YES |  | The unique identifier of a record in the History Reason dimension table.  This is a surrogate key that it used within all of the history table to identfiy the reason that each particular History record was created. |
| HIST_RSN_CD | varchar | 20 | 1 |  |  | The code identifying the reason that a record was loaded into a history table.  Valid values include: UPDATE and DELETE. |
| HIST_RSN_DESCR | varchar | 50 | 1 |  |  | The description of the code identifying the reason that a record was loaded into a history table.  Valid values include: UPDATE and DELETE. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
