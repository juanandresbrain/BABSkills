# dbo.VLDTN_PRCS_INSTNC_DTL_REC_CNT

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VLDTN_PRCS_INSTNC_DTL_ID | int | 4 | 0 | YES |  | The unique identifier of a validation process instance detail record.  These records show the detail results of the execution of a validation process.  Exactly what detail data is shown depends on the type of validation.  In some instances (e.g. REC_CNT) all validations, regardless of pass/fail will have entries in the detail table.  In other instances (e.g. MISS_KEY, REF_INTGRTY, etc.) the detail data for those records failing the validation will be inserted. |
| VLDTN_PRCS_INSTNC_ID | int | 4 | 1 |  |  |  |
| SEQ_NBR | int | 4 | 0 |  |  | A numeric sequence identifying a particular detail record within a Validation Process Instance.  This differentiates between each of the detail records for a given Validation Process Instance. |
| HSH_KEY_COL_NM | varchar | 500 | 1 |  |  | The name of the columns that make up the aggregate hash key.  These are the columns that are used in the aggregation of the transactional sum amount.  For example, if the transaction sum amount is total sales, this could be aggregated by both store and product, in which case this would contain 'STORE_KEY\|PRODUCT_KEY'. |
| HSH_KEY_TXT | varchar | 500 | 1 |  |  | The actual value from the columns that make up the aggregate hash key.  These are the columns that are used in the aggregation of the transactional sum amount.  For example, if the transaction sum amount is total sales, this could be aggregated by both store and product, in which case this would contain a particular store key and product key.  For example,  '125\|10'. |
| SRC_TBL_NM | varchar | 500 | 1 |  |  | The name of the source table from which the record count was obtained. |
| SRC_REC_CNT | int | 4 | 1 |  |  | The count of records from the source table.  This is the same number of records as should have been loaded into the target table.  Some sources are true external sources for the data warehouse and some sources are tables within the data warehouse that act as a source for other tables in the data warehouse. |
| TGT_TBL_NM | varchar | 500 | 1 |  |  | The name of the target table from which the record count was obtained. |
| TGT_REC_CNT | int | 4 | 1 |  |  | The count of records from the target table.  This is the same number of records as should have been loaded into the target table.  Some sources are true external sources for the data warehouse and some sources are tables within the data warehouse that act as a source for other tables in the data warehouse. |
| INS_DT | datetime | 8 | 0 |  |  | The date and time at which the record was originally inserted into the table. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date and time at which the record was most recently updated in the table. |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
