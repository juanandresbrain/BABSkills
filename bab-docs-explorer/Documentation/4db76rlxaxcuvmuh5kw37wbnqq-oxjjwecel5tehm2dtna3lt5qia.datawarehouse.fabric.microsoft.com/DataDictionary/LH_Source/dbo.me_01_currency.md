# dbo.me_01_currency

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_id | decimal | 9 | 1 |  |  |  |
| currency_code | varchar | 8000 | 1 |  |  |  |
| currency_description | varchar | 8000 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
| create_date | datetime2 | 8 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| currency_symbol | varchar | 8000 | 1 |  |  |  |
