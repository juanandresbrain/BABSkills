# dbo.franchiseetransactionorphans

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Franchisee | varchar | 8000 | 1 |  |  |  |
| TransactionID | varchar | 8000 | 1 |  |  |  |
| HeaderRecords | varchar | 8000 | 1 |  |  |  |
| PaymentRecords | varchar | 8000 | 1 |  |  |  |
| MerchandiseRecords | varchar | 8000 | 1 |  |  |  |
| GiftCardRecords | varchar | 8000 | 1 |  |  |  |
| OrphanMessage | varchar | 8000 | 1 |  |  |  |
| EmptyColumnsFound | varchar | 8000 | 1 |  |  |  |
