# dbo.Labor_Employee_Dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| emp_key | int | 4 | 0 | YES |  | Surrogate Key |
| store_key | int | 4 | 0 |  |  | Store for this employee; FK to store_dim |
| emp_id | bigint | 8 | 0 |  |  | Internal Employee Number in the Source System |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPD_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
