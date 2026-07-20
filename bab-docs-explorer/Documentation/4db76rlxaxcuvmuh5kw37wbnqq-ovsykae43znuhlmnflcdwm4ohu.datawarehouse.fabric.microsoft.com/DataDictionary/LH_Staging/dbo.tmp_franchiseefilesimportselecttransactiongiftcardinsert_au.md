# dbo.tmp_franchiseefilesimportselecttransactiongiftcardinsert_au

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FranchiseeTransactionHeaderID | int | 4 | 1 |  |  |  |
| FranchiseeTransactionGiftCardID | int | 4 | 1 |  |  |  |
| TransactionID | varchar | 8000 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| GiftCardAmount | decimal | 5 | 1 |  |  |  |
| Discount | decimal | 5 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| Franchisee | varchar | 8000 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
