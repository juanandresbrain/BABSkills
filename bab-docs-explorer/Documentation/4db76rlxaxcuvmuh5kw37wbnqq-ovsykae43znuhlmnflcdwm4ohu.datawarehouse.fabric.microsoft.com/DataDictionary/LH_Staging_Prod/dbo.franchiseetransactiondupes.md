# dbo.franchiseetransactiondupes

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 8000 | 1 |  |  |  |
| TransactionID | varchar | 8000 | 1 |  |  |  |
| HeaderRecords | int | 4 | 1 |  |  |  |
| PaymentRecords | int | 4 | 1 |  |  |  |
| MerchandiseRecords | int | 4 | 1 |  |  |  |
| GiftCardRecords | int | 4 | 1 |  |  |  |
