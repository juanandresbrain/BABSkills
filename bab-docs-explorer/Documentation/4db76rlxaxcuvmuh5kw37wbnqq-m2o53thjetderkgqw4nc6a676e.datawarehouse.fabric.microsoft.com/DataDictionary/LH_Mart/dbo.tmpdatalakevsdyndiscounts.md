# dbo.tmpdatalakevsdyndiscounts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| DataLakeRetailTransactionId | varchar | 8000 | 1 |  |  |  |
| DataLakeAmount | decimal | 9 | 1 |  |  |  |
| DatalakeDiscountOriginType | varchar | 8000 | 1 |  |  |  |
| DataLakePeriodicDiscountOfferId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| DiscountOriginType | varchar | 8000 | 1 |  |  |  |
| PeriodicDiscountOfferId | varchar | 8000 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| CurrentSentDate | datetime2 | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
