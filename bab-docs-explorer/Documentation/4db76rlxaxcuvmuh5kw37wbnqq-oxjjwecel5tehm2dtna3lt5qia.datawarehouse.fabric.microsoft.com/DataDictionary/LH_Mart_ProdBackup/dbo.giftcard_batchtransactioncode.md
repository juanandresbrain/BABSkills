# dbo.giftcard_batchtransactioncode

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transactionId | int | 4 | 1 |  |  |  |
| transactionCode | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| isActive | bit | 1 | 1 |  |  |  |
