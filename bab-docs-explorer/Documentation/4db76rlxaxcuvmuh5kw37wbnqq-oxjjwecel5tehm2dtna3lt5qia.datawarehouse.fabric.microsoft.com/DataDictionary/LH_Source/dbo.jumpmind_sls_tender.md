# dbo.jumpmind_sls_tender

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tender_code | varchar | 8000 | 1 |  |  |  |
| tender_type_code | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| cash_drawer_open_required | int | 4 | 1 |  |  |  |
| till_unit_count_required | int | 4 | 1 |  |  |  |
| till_amount_count_required | int | 4 | 1 |  |  |  |
| return_tender_type_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| check_number | varchar | 8000 | 1 |  |  |  |
