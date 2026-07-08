# dbo.interface_loopback

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| interface_id | int | 4 | 0 |  |  |  |
| loopback_type | int | 4 | 0 |  |  |  |
| loopback_code | int | 4 | 0 |  |  |  |
| loopback_text | nvarchar | 510 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
