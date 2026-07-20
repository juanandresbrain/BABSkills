# dbo.giftcard_batchtransactioncode

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transactionId | int | 4 | 1 |  |  |  |
| transactionCode | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| isActive | bit | 1 | 1 |  |  |  |
