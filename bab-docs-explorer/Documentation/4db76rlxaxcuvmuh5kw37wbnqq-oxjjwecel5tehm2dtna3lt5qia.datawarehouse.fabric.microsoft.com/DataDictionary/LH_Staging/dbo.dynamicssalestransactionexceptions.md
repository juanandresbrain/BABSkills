# dbo.dynamicssalestransactionexceptions

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| Reason | varchar | 8000 | 1 |  |  |  |
| ItemId | varchar | 8000 | 1 |  |  |  |
| Price | decimal | 9 | 1 |  |  |  |
| LineObject | int | 4 | 1 |  |  |  |
| LineObjectDescription | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| IsCurrent | varchar | 8000 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| VarianceValue | decimal | 9 | 1 |  |  |  |
