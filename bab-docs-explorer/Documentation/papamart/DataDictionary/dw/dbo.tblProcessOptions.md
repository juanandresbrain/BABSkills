# dbo.tblProcessOptions

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_name | varchar | 250 | 0 |  |  |  |
| process_string | varchar | 5000 | 1 |  |  |  |
| process_active | bit | 1 | 1 |  |  |  |
| process_datetime | datetime | 8 | 1 |  |  |  |
| Process_start_range | int | 4 | 1 |  |  |  |
| process_end_range | int | 4 | 1 |  |  |  |
| process_guest_activity_key | int | 4 | 1 |  |  |  |
| process_id | int | 4 | 0 | YES |  |  |
