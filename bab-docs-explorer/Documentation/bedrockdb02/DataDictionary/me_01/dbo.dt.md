# dbo.dt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| sourceid | int | 4 | 0 |  |  |  |
| destid | int | 4 | 0 |  |  |  |
| upc_number | int | 4 | 0 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| groupinglabel | varchar | 20 | 1 |  |  |  |
| description | varchar | 20 | 1 |  |  |  |
| rec_type | int | 4 | 0 |  |  |  |
| loaded_date | datetime | 8 | 0 |  |  |  |
| documentnumber | varchar | 9 | 1 |  |  |  |
| linenumber | int | 4 | 1 |  |  |  |
| reasoncode | varchar | 5 | 1 |  |  |  |
| exported_date | datetime | 8 | 1 |  |  |  |
| tpm_exported_date | datetime | 8 | 1 |  |  |  |

