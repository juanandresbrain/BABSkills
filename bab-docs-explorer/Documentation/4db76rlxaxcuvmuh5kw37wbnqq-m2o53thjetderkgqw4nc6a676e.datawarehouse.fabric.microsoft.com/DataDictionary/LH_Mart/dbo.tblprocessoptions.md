# dbo.tblprocessoptions

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_name | varchar | 8000 | 1 |  |  |  |
| process_string | varchar | 8000 | 1 |  |  |  |
| process_active | bit | 1 | 1 |  |  |  |
| process_datetime | datetime2 | 8 | 1 |  |  |  |
| Process_start_range | int | 4 | 1 |  |  |  |
| process_end_range | int | 4 | 1 |  |  |  |
| process_guest_activity_key | int | 4 | 1 |  |  |  |
| process_id | int | 4 | 1 |  |  |  |
