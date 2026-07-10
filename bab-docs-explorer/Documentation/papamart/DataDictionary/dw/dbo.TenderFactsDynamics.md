# dbo.TenderFactsDynamics

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TenderFactsDynamics_Key | int | 4 | 0 | YES |  |  |
| transaction_id | int | 4 | 0 |  |  |  |
| tender_key | int | 4 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| tender_amt | numeric | 9 | 1 |  |  |  |
| tender_count | int | 4 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  |  |
| UPDT_DT | datetime | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
