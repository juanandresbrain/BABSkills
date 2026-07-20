# dbo.tmpdynamicsretailtransaction

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaId | varchar | 8000 | 1 |  |  |  |
| RreceiptId | varchar | 8000 | 1 |  |  |  |
| TransactionNumber | varchar | 8000 | 1 |  |  |  |
| TransactionDate | datetime2 | 8 | 1 |  |  |  |
| DiscountAmount | float | 8 | 1 |  |  |  |
| DiscountAmountWithoutTax | float | 8 | 1 |  |  |  |
| GrossAmount | float | 8 | 1 |  |  |  |
| NetAmount | float | 8 | 1 |  |  |  |
| NetPrice | float | 8 | 1 |  |  |  |
| NumberOfItems | float | 8 | 1 |  |  |  |
| NumberOfPaymentLines | int | 4 | 1 |  |  |  |
| NumberOfItemLines | float | 8 | 1 |  |  |  |
| OperatingUnitNumber | varchar | 8000 | 1 |  |  |  |
| PaymentAmount | float | 8 | 1 |  |  |  |
