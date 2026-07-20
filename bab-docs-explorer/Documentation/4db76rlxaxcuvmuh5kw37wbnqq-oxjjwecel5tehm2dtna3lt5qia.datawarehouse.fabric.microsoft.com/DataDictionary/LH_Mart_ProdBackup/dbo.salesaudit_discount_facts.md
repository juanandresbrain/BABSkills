# dbo.salesaudit_discount_facts

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| coupon_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| process_name | varchar | 8000 | 1 |  |  |  |
| process_date | datetime2 | 8 | 1 |  |  |  |
| uid | int | 4 | 1 |  |  |  |
| DW_AuditLoadDt | datetime2 | 8 | 1 |  |  |  |
