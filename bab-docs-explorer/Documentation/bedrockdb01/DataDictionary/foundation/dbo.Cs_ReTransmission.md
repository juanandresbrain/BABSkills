# dbo.Cs_ReTransmission

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transmission_id | int | 4 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| request_datetime | datetime | 8 | 0 |  |  |  |
| new_transmission_id | int | 4 | 1 |  |  |  |
| status_id | smallint | 2 | 0 |  |  |  |
