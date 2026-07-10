# dbo.tmpDynamicsRetailTransaction

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| RreceiptId | nvarchar | 8000 | 1 |  |  |  |
| TransactionNumber | nvarchar | 8000 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 1 |  |  |  |
| DiscountAmount | float | 8 | 1 |  |  |  |
| DiscountAmountWithoutTax | float | 8 | 1 |  |  |  |
| GrossAmount | float | 8 | 1 |  |  |  |
| NetAmount | float | 8 | 1 |  |  |  |
| NetPrice | float | 8 | 1 |  |  |  |
| NumberOfItems | float | 8 | 1 |  |  |  |
| NumberOfPaymentLines | int | 4 | 1 |  |  |  |
| NumberOfItemLines | float | 8 | 1 |  |  |  |
| OperatingUnitNumber | nvarchar | 8000 | 1 |  |  |  |
| PaymentAmount | float | 8 | 1 |  |  |  |
