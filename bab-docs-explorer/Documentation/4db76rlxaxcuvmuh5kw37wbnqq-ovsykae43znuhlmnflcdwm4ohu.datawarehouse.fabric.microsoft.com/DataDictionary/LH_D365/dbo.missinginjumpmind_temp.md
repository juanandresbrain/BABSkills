# dbo.missinginjumpmind_temp

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| DeviceId | varchar | 8000 | 1 |  |  |  |
| BusinessDate | int | 4 | 1 |  |  |  |
| SequenceNumber | int | 4 | 1 |  |  |  |
| Barcode | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionIdText | varchar | 8000 | 1 |  |  |  |
| CreateDate | date | 3 | 1 |  |  |  |
| ES_Flag | int | 4 | 1 |  |  |  |
| PIPO_Flag | int | 4 | 1 |  |  |  |
| DiscountTotal | decimal | 17 | 1 |  |  |  |
| SubTotal | decimal | 17 | 1 |  |  |  |
| TaxTotal | decimal | 17 | 1 |  |  |  |
| Total | decimal | 17 | 1 |  |  |  |
