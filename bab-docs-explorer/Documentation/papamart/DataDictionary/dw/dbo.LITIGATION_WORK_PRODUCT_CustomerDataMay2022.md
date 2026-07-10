# dbo.LITIGATION_WORK_PRODUCT_CustomerDataMay2022

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_id | int | 4 | 0 |  |  |  |
| customer_no | numeric | 13 | 0 |  |  |  |
| telephone_no | nvarchar | 32 | 0 |  |  |  |
| PhoneCreateDate | datetime | 8 | 0 |  |  |  |
| PhoneCreateStore | int | 4 | 1 |  |  |  |
| PhoneCreateUserName | nvarchar | 100 | 1 |  |  |  |
| PhoneCreateEmployeeNumber | int | 4 | 1 |  |  |  |
| PhoneModifyDate | datetime | 8 | 0 |  |  |  |
| PhoneModifyStore | int | 4 | 1 |  |  |  |
| PhoneModifyUserName | nvarchar | 100 | 1 |  |  |  |
| PhoneModifyEmployeeNumber | int | 4 | 1 |  |  |  |
| PhoneModifySourceCode | nvarchar | 40 | 1 |  |  |  |
| PhoneModifySourceName | varchar | 255 | 1 |  |  |  |
| PhoneDivisionCreateDate | datetime | 8 | 0 |  |  |  |
| PhoneDivisionCreateStoreNumber | int | 4 | 1 |  |  |  |
| PhoneDivisionCreateSourceCode | nvarchar | 40 | 1 |  |  |  |
| PhoneDivisionCreateSourceName | varchar | 255 | 1 |  |  |  |
| text_opt_in_flag | tinyint | 1 | 0 |  |  |  |
| text_opt_in_date | smalldatetime | 4 | 1 |  |  |  |
| TextModifyUserName | nvarchar | 100 | 1 |  |  |  |
| TextModifyEmployeeNumber | int | 4 | 1 |  |  |  |
| PhoneDivisionModifyDate | datetime | 8 | 0 |  |  |  |
| text_modify_store_no | int | 4 | 1 |  |  |  |
| TextModifySourceCode | nvarchar | 40 | 1 |  |  |  |
| TextCreateSourceName | varchar | 255 | 1 |  |  |  |
