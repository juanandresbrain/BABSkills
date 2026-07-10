# dbo.Labor_Hours_Fact

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 0 | YES |  | Surrogate Key |
| store_key | int | 4 | 0 |  |  | FK to Store_Dim |
| date_key | int | 4 | 0 |  |  | Payroll Date for this record; FK to Date_Dim |
| emp_key | int | 4 | 0 |  |  | Employee Key; FK to Labor_Employee_Dim |
| job_key | int | 4 | 0 |  |  | Job for this transaction (I.E. BB, CWM); FK to Labor_Job_Dim |
| HOURTYPE_KEY | int | 4 | 0 |  |  | Indicates the hourly type  for this transaction. I.E. Regular, Double Time, etc; FK to Labor_HourType_Dim |
| timecode_key | int | 4 | 0 |  |  | Indicates the activity for this transaction. I.E. Work, Paid time off; FK to Labor_Timecode_Dim |
| start_Time | datetime | 8 | 0 |  |  | Relative starting time for this transaction. ex: 1/1/1900 14.26 |
| end_Time | datetime | 8 | 0 |  |  | Relative starting time for this transaction. ex: 1/1/1901 2.26 means 2:26 the next day. |
| wrkd_minutes | int | 4 | 0 |  |  | Number of minutes worked |
| source_system | tinyint | 1 | 0 |  |  | Source of this record 1-Workbrain, 2-Can/UK extract |
| INS_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| wrkd_id | int | 4 | 1 |  |  |  |
