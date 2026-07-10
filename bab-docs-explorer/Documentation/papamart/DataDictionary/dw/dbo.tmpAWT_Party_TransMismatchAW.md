# dbo.tmpAWT_Party_TransMismatchAW

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EventID | int | 4 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| PT_Balance | money | 8 | 1 |  |  |  |
| AW_Balance | money | 8 | 1 |  |  |  |
| Voucher_Balance | money | 8 | 1 |  |  |  |
| Diff | money | 8 | 1 |  |  |  |
| dStart | smalldatetime | 4 | 1 |  |  |  |
| FirstTransDate | smalldatetime | 4 | 1 |  |  |  |
| LastTransDate | smalldatetime | 4 | 1 |  |  |  |
