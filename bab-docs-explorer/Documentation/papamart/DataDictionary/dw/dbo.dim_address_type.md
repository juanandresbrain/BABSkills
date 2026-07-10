# dbo.dim_address_type

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| addr_type_key | int | 4 | 0 | YES |  |  |
| addr_type_code | char | 2 | 1 |  |  |  |
| addr_type_desc | varchar | 50 | 1 |  |  |  |
| apt_unit | char | 1 | 1 |  |  |  |
