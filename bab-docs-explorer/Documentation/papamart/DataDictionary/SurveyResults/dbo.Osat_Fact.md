# dbo.Osat_Fact

**Database:** SurveyResults  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| osat_facts_key | int | 4 | 0 | YES |  |  |
| store_key | int | 4 | 0 |  |  |  |
| call_date_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| time_key | int | 4 | 0 |  |  |  |
| visit_type_dim_key | int | 4 | 0 |  |  |  |
| question_dim_key | int | 4 | 0 |  |  |  |
| calc_type_dim_key | int | 4 | 0 |  |  |  |
| raw_score | int | 4 | 0 |  |  |  |
| calc_score | int | 4 | 0 |  |  |  |
| unique_id | varchar | 30 | 0 |  |  |  |
| password | varchar | 30 | 1 |  |  |  |
| source | varchar | 30 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  |  |
| UPDT_DT | datetime | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| src_type | varchar | 1 | 1 |  |  | Indicates whether this is associated with a (T)ransaction, (R)egistration or (?)Unknown |
| transaction_id | int | 4 | 1 |  |  | Points to the Transaction_Facts or Trn_Ksk_Facts depending upon src_type. |
| CLNSD_GST_ID | int | 4 | 0 |  |  |  |
