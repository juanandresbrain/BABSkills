# dbo.recordyourvoice_orders

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderID | int | 4 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderDate | datetime2 | 8 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| AudioRecordedDate | datetime2 | 8 | 1 |  |  |  |
| AudioTransferDate | datetime2 | 8 | 1 |  |  |  |
| ChipRecordedDate | datetime2 | 8 | 1 |  |  |  |
