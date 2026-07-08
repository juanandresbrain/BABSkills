# dbo.interface

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| interface_id | int | 4 | 0 |  |  |  |
| interface_name | nvarchar | 50 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
| interface_type | int | 4 | 0 |  |  |  |
| OUT_INTRLAV | int | 4 | 0 |  |  |  |
| OUT_ACKNWLDG_TYPE | int | 4 | 0 |  |  |  |
| OUT_ACKNWLDG_TMT | int | 4 | 0 |  |  |  |
| OUT_ACKNWLDG_RTRY | int | 4 | 0 |  |  |  |
| IN_ACKNWLDG_TYPE | int | 4 | 0 |  |  |  |
| OWNR | int | 4 | 0 |  |  |  |
