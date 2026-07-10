# dbo.CRM_POS_TRN_JOIN_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRM_POS_STG_ID | int | 4 | 0 |  |  | The unique identifier of a record within the CRM POS Staging table.  This is a surrogate key for the records in this table and will uniquely identify a record with the Staging environment.  It is not, however, connected to a record within the source system. |
| TRN_ID | int | 4 | 0 |  |  | Transaction_ID populated from transaction_detail_facts based on a join of store, date, POS number, and register number |
