# dbo.litigation_work_product_customerdatamay2022

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_id | int | 4 | 1 |  |  |  |
| customer_no | decimal | 13 | 1 |  |  |  |
| telephone_no | varchar | 8000 | 1 |  |  |  |
| PhoneCreateDate | datetime2 | 8 | 1 |  |  |  |
| PhoneCreateStore | int | 4 | 1 |  |  |  |
| PhoneCreateUserName | varchar | 8000 | 1 |  |  |  |
| PhoneCreateEmployeeNumber | int | 4 | 1 |  |  |  |
| PhoneModifyDate | datetime2 | 8 | 1 |  |  |  |
| PhoneModifyStore | int | 4 | 1 |  |  |  |
| PhoneModifyUserName | varchar | 8000 | 1 |  |  |  |
| PhoneModifyEmployeeNumber | int | 4 | 1 |  |  |  |
| PhoneModifySourceCode | varchar | 8000 | 1 |  |  |  |
| PhoneModifySourceName | varchar | 8000 | 1 |  |  |  |
| PhoneDivisionCreateDate | datetime2 | 8 | 1 |  |  |  |
| PhoneDivisionCreateStoreNumber | int | 4 | 1 |  |  |  |
| PhoneDivisionCreateSourceCode | varchar | 8000 | 1 |  |  |  |
| PhoneDivisionCreateSourceName | varchar | 8000 | 1 |  |  |  |
| text_opt_in_flag | int | 4 | 1 |  |  |  |
| text_opt_in_date | datetime2 | 8 | 1 |  |  |  |
| TextModifyUserName | varchar | 8000 | 1 |  |  |  |
| TextModifyEmployeeNumber | int | 4 | 1 |  |  |  |
| PhoneDivisionModifyDate | datetime2 | 8 | 1 |  |  |  |
| text_modify_store_no | int | 4 | 1 |  |  |  |
| TextModifySourceCode | varchar | 8000 | 1 |  |  |  |
| TextCreateSourceName | varchar | 8000 | 1 |  |  |  |
