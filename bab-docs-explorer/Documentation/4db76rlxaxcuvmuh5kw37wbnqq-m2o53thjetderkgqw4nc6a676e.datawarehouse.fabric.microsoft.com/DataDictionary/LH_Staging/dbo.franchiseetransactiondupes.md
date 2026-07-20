# dbo.franchiseetransactiondupes

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 8000 | 1 |  |  |  |
| TransactionID | varchar | 8000 | 1 |  |  |  |
| HeaderRecords | int | 4 | 1 |  |  |  |
| PaymentRecords | int | 4 | 1 |  |  |  |
| MerchandiseRecords | int | 4 | 1 |  |  |  |
| GiftCardRecords | int | 4 | 1 |  |  |  |
