# dbo.tmpsmscrmphonejoin

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Mobile | varchar | 8000 | 1 |  |  |  |
| SubscriberKey | varchar | 8000 | 1 |  |  |  |
| phone_create_store_no | int | 4 | 1 |  |  |  |
| phone_opt_in_date | datetime2 | 8 | 1 |  |  |  |
| text_opt_in_flag | int | 4 | 1 |  |  |  |
| text_modify_store_no | int | 4 | 1 |  |  |  |
