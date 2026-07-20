# dbo.hr_storeforcecustomermetricsstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreNo | int | 4 | 1 |  |  |  |
| StoreCode | int | 4 | 1 |  |  |  |
| StoreCodeRaw | int | 4 | 1 |  |  |  |
| Date | varchar | 8000 | 1 |  |  |  |
| TransactionDateRaw | date | 3 | 1 |  |  |  |
| Slot | varchar | 8000 | 1 |  |  |  |
| MobileCaptureCount | int | 4 | 1 |  |  |  |
| MobileEmailOptInCount | int | 4 | 1 |  |  |  |
