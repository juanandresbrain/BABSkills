# dbo.VLDTN_PRCS_INSTNC

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_ID | int | 4 | 0 | YES |  | The unique identifier of a validation process instance record.  This identifies the execution of a particular instance of a validation process, including the timestamp, overall success/failure result of the process itself, along with a pass/fail indication for the data that went was validated. |
| VLDTN_PRCS_ID | int | 4 | 0 |  |  |  |
| EXEC_STRT_DTTM | datetime | 8 | 1 |  |  | The timestamp for the start of execution of a particular instance of a Validation process.  This identifies the date and time at which this validation process execution initiated. |
| EXEC_END_DTTM | datetime | 8 | 1 |  |  | The timestamp for the end of execution of a particular instance of a Validation process.  This identifies the date and time at which this validation process execution completed. |
| PASS_REC_CNT | int | 4 | 1 |  |  | The count of the number of records that passed the validation process during the execution of this particular validation process instance.  This value, along with the number of failed records and the threshold will be used in calculating whether the data passed the validation process overall. |
| FAIL_REC_CNT | int | 4 | 1 |  |  | The count of the number of records that failed the validation process during the execution of this particular validation process instance.  This value, along with the number of passed records and the threshold will be used in calculating whether the data passed the validation process overall. |
| THRSHLD_QTY | decimal | 9 | 1 |  |  | If a threshold makes sense for this particular validation process, it will be stored here.  Thresholds quantities are numeric and define the minimum level of matching between the source and target data involved in the validation.  For example, assume that the validation is comparing the total sales dollars from the Point of Sale (POS) system to the Data Warehouse.  Assume further that it is known that dollar value rounding may cause minor differences between the two total dollar values, then, this value may be set to 0.99, since there should be a 99% match between the source dollar values and those in the Data Warehouse. |
| PASS_IND | char | 1 | 1 |  |  | This indciates whether or not the execution of a particular validation process passed or failed.  The PASS/FAIL status of a particular validation process is built into the evaluation of the results and therefore each validation process sets this indicator at the time of execution based on the PASS/FAIL criteria defined for that process.  Valid values include Y (Yes), N (No), and U (Unknown). |
| INS_DT | datetime | 8 | 0 |  |  | The date and time at which this record was originally inserted into the table. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date and time at which this record was most recently updated in the table. |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
