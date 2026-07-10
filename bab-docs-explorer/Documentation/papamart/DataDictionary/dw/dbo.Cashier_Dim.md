# dbo.Cashier_Dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cashier_key | int | 4 | 0 | YES |  | Surrogate Key |
| cashier_code | varchar | 50 | 0 |  |  | BK: (Optionally) Store _ and Cashier No to identify the cashier. |
| INS_DT | datetime | 8 | 0 |  |  | Date record Inserted |
