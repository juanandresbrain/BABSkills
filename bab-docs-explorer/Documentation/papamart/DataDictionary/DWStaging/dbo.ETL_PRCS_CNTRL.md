# dbo.ETL_PRCS_CNTRL

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETL_PRCS_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Process.  This is used to identify the ETL process throughout all of the loads. |
| ETL_PRCS_NM | varchar | 50 | 1 |  |  | The name of the ETL process.  This name describes the process that this record controls. |
| LAST_TS | datetime | 8 | 1 |  |  | This is the maximum timestamp loaded in the most recent ETL process.  This is stored in a datetime data type.  Each record will store the last timestamp or the last identifier, depending on which is used for extracting data from the source system. |
| LAST_ID | int | 4 | 1 |  |  | This is the maximum identifier loaded in the most recent ETL process.  This is stored in an integer data type.  Each record will store the last timestamp or the last identifier, depending on which is used for extracting data from the source system. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the INS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| STAT_CD | varchar | 10 | 1 |  |  |  |
