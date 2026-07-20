# dbo.gaap_salesreport

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionDate | date | 3 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| order_id | varchar | 8000 | 1 |  |  |  |
| TransactionHour | int | 4 | 1 |  |  |  |
| TransactionMinute | int | 4 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| Department | varchar | 8000 | 1 |  |  |  |
| ProductSellingGeography | varchar | 8000 | 1 |  |  |  |
| extended_discounted_amount | decimal | 17 | 1 |  |  |  |
| tax_amount | decimal | 17 | 1 |  |  |  |
| UnitsSold | decimal | 17 | 1 |  |  |  |
| Shlastupdatetime | datetime2 | 8 | 1 |  |  |  |
| Sllastupdatetime | datetime2 | 8 | 1 |  |  |  |
