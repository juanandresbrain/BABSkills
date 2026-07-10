# dbo.VLDTN_PRCS_INSTNC_DTL_REF_INTGRTY

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 0 | YES |  | The unique identifier of a validation process instance detail record.  These records show the detail results of the execution of a validation process.  Exactly what detail data is shown depends on the type of validation.  In some instances (e.g. REC_CNT) all validations, regardless of pass/fail will have entries in the detail table.  In other instances (e.g. MISS_KEY, REF_INTGRTY, etc.) the detail data for those records failing the validation will be inserted. |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 0 |  |  | A numeric sequence identifying a particular detail record within a Validation Process Instance.  This differentiates between each of the detail records for a given Validation Process Instance. |
| PARNT_TBL_NM | varchar | 500 | 1 |  |  | The name of the parent table for the record that failed the referential integrity validation.  For records failing this validation, this should contain the Key value, but does not. |
| CHILD_TBL_NM | varchar | 500 | 1 |  |  | The name of the childtable for the record that failed the referential integrity validation.  For records failing this validation, this contains the Key value that does not exist in the other table. |
| CHILD_COL_NM | varchar | 500 | 1 |  |  | The name of the column on the child table that contains the key which is missing from the parent table based on the Referential Integrity validation. |
| MISS_CHILD_ID | int | 4 | 1 |  |  | The identifier on the record that failed the validation which exists in the child table, but not in the parent table.  This is the orphaned identifier and needs to be resolved in the parent table in order for the record to pass the validation. |
| INS_DT | datetime | 8 | 0 |  |  | The date and time at which the record was originally inserted into the table. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date and time at which the record was most recently updated in the table. |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
