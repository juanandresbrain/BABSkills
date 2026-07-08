# dbo.MSpub_identity_range

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| objid | int | 4 | 0 |  |  |  |
| range | bigint | 8 | 0 |  |  |  |
| pub_range | bigint | 8 | 0 |  |  |  |
| current_pub_range | bigint | 8 | 0 |  |  |  |
| threshold | int | 4 | 0 |  |  |  |
| last_seed | bigint | 8 | 1 |  |  |  |
