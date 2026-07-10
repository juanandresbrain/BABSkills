# dbo.VLDTN_PRCS

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_ID | int | 4 | 0 | YES |  | The unique identifier of a record in the Validation Process table.  This is an identity column that acts as a surrogate key for Validation Process records. |
| VLDTN_PRCS_NM | varchar | 50 | 1 |  |  | This is the name used to identify a particular validation process. |
| VLDTN_PRCS_DESCR | varchar | 100 | 1 |  |  | A textual description of the validation, including the sources, targets, and a general idea of the anticipated results. |
| FREQ_CD | varchar | 20 | 1 |  |  | The code identifying the frequency with which this validation will be executed.  Typical frequencies include Daily, Weekly, Monthly, Annually, etc. |
| FREQ_DESCR | varchar | 50 | 1 |  |  | The description of the code identifying the frequency with which this validation will be executed.  Typical frequencies include Daily, Weekly, Monthly, Annually, etc. |
| CLS_CD | varchar | 20 | 1 |  |  | The code representing the class of validation.  Validations are separated into four primary classes: Record Count, Missing Record (Source vs. Target), Missing Record (Target vs. Source), and Dimension Specific Audit. |
| CLS_DESCR | varchar | 50 | 1 |  |  | The description of the code representing the class of validation.  Validations are separated into four primary classes: Record Count, Missing Record (Source vs. Target), Missing Record (Target vs. Source), and Dimension Specific Audit. |
| ACTV_STRT_DT | datetime | 8 | 1 |  |  | The date on which execution of this particular validation process first started.  This is populated when the Validation Status Code is 'Active'. |
| ACTV_END_DT | datetime | 8 | 1 |  |  | The date on which execution of this validation process ceased.  This will be populated when the Validation Status Code = 'Inactive' |
| ACTV_STAT_CD | varchar | 20 | 1 |  |  | The code identifying the status of the validation process.  Validation processes can either be Active (currently executing), Inactive (execution terminated) or Suspended (execution temporarily stopped). |
| INACTV_RSN_TXT | varchar | 500 | 1 |  |  | The text describing the reason for changing the Validation Process Active Status Code to Inactive.  This provides a historical view of why the change in status was made. |
| THRSHLD_QTY | decimal | 9 | 1 |  |  | If a threshold makes sense for this particular validation process, it will be stored here.  Thresholds quantities are numeric and define the minimum level of matching between the source and target data involved in the validation.  For example, assume that the validation is comparing the total sales dollars from the Point of Sale (POS) system to the Data Warehouse.  Assume further that it is known that dollar value rounding may cause minor differences between the two total dollar values, then, this value may be set to 0.99, since there should be a 99% match between the source dollar values and those in the Data Warehouse. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which the record was originally inserted into the table. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which the record was most recently updated in the table. |
| BEG_EFF_DT | datetime | 8 | 0 |  |  | The date on which this record became effective within the Data Warehouse.  This would be used for tracking Type II slowly changing dimension (SCD) records. |
| END_EFF_DT | datetime | 8 | 0 |  |  | The date on which this record was no longer effective within the Data Warehouse.  This would be used for tracking Type II slowly changing dimension (SCD) records. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This record tracks the execution of an overall ETL process.  Logs, which are the high level processes, contain events, which are the detailed tasks. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Event record.  This record tracks the execution of one task within the overall ETL process.  Logs, which are the high level processes, contain events, which are the detailed tasks. |
