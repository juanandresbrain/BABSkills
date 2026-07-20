# dbo.rawtransdata

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JoinKey | varchar | 8000 | 1 |  |  |  |
| device_id | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| AssociateNumber | varchar | 8000 | 1 |  |  |  |
| AssociateName | varchar | 8000 | 1 |  |  |  |
| SumTotal | decimal | 17 | 1 |  |  |  |
| subtotal | decimal | 17 | 1 |  |  |  |
| business_unit_id | varchar | 8000 | 1 |  |  |  |
