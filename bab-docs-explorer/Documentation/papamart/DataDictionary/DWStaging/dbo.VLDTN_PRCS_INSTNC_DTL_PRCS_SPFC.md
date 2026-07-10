# dbo.VLDTN_PRCS_INSTNC_DTL_PRCS_SPFC

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 0 | YES |  | The unique identifier of a validation process instance detail record.  These records show the detail results of the execution of a validation process.  Exactly what detail data is shown depends on the type of validation.  In some instances (e.g. REC_CNT) all validations, regardless of pass/fail will have entries in the detail table.  In other instances (e.g. MISS_KEY, REF_INTGRTY, etc.) the detail data for those records failing the validation will be inserted. |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 0 |  |  | A numeric sequence identifying a particular detail record within a Validation Process Instance.  This differentiates between each of the detail records for a given Validation Process Instance. |
| HSH_KEY_DTA_SET_CD | varchar | 20 | 1 |  |  | The code identifying the set of data from which this hash key came.  The primary data sets used in these validation processes are 'SRC' and 'TGT'. |
| HSH_KEY_COL_NM | varchar | 500 | 1 |  |  | The name of the fields that make up the hash key for this record.  Each field name should be separated by a delimiter, typically a pipe '\|'. |
| HSH_KEY_TXT | varchar | 500 | 1 |  |  | The textual representation of the key fields that make up this natural key, separated by a delimiter.  The delimiter should typically be a pipe '\|'. |
| VLDTD_TBL_NM | varchar | 500 | 1 |  |  | The name of the table on which a process specific validation is being performed.  For example, if this record was validating the ssgender column on the source table tblCustomerRecipient, this column would contain 'TBLCUSTOMERRECIPIENT'. |
| VLDTD_COL_NM | varchar | 500 | 1 |  |  | The name of the column on which a process specific validation is being performed.  For example, if this record was validating the ssgender column on the source table tblCustomerRecipient, this column would contain 'SSGENDER'. |
| VLDTD_COL_VAL_AMT | decimal | 9 | 1 |  |  | The value in the validated column, if that value is numeric amount.  If the value is textual or datetime, it will be displayed in a different column. |
| VLDTD_COL_VAL_TXT | varchar | 500 | 1 |  |  | The value in the validated column, if that value is textual.  If the value is numeric or datetime, it will be displayed in a different column. |
| VLDTD_COL_VAL_DT | datetime | 8 | 1 |  |  | The value in the validated column, if that value is a datetime.  If the value is numeric or textual, it will be displayed in a different column. |
| INS_DT | datetime | 8 | 0 |  |  | The date and time at which the record was originally inserted into the table. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date and time at which the record was most recently updated in the table. |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
