# dbo.VLDTN_PRCS_INSTNC_DTL_TRN_SUM

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 0 | YES |  | The unique identifier of a validation process instance detail record.  These records show the detail results of the execution of a validation process.  Exactly what detail data is shown depends on the type of validation.  In some instances (e.g. REC_CNT) all validations, regardless of pass/fail will have entries in the detail table.  In other instances (e.g. MISS_KEY, REF_INTGRTY, etc.) the detail data for those records failing the validation will be inserted. |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 0 |  |  | A numeric sequence identifying a particular detail record within a Validation Process Instance.  This differentiates between each of the detail records for a given Validation Process Instance. |
| HASH_KEY_COL_NM | varchar | 500 | 1 |  |  | The name of the columns that make up the aggregate hash key.  These are the columns that are used in the aggregation of the transactional sum amount.  For example, if the transaction sum amount is total sales, this could be aggregated by both store and product, in which case this would contain 'STORE_KEY\|PRODUCT_KEY'. |
| HSH_KEY_TXT | varchar | 500 | 1 |  |  | The actual value from the columns that make up the aggregate hash key.  These are the columns that are used in the aggregation of the transactional sum amount.  For example, if the transaction sum amount is total sales, this could be aggregated by both store and product, in which case this would contain a particular store key and product key.  For example,  '125\|10'. |
| SRC_TBL_NM | varchar | 500 | 1 |  |  | The name of the source table containing the transactional summary amount that is being validated. |
| SRC_COL_NM | varchar | 500 | 1 |  |  | The name of the column from the source data set that contains the transaction summary amount. |
| SRC_TRN_SUM_AMT | decimal | 9 | 1 |  |  | The aggregated sum of the transaction amount from the source data. |
| TGT_TBL_NM | varchar | 500 | 1 |  |  | The name of the target table containing the transactional summary amount that is being validated. |
| TGT_COL_NM | varchar | 500 | 1 |  |  | The name of the column from the target data set that contains the transaction summary amount. |
| TGT_TRN_SUM_AMT | decimal | 9 | 1 |  |  | The aggregated sum of the transaction amount from the target data. |
| INS_DT | datetime | 8 | 0 |  |  | The date and time at which the record was originally inserted into the table. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date and time at which the record was most recently updated in the table. |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
