# dbo.tmpDistribution_splitBAK20150720

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | bigint | 8 | 0 |  |  |  |
| sourceid | varchar | 20 | 0 |  |  |  |
| destid | varchar | 21 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| rec_type | varchar | 6 | 0 |  |  |  |
| sequencenbr | bigint | 8 | 0 |  |  |  |
| distribution_number | varchar | 20 | 0 |  |  |  |
| ref_field_1 | int | 4 | 0 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| active_pick_flag | varchar | 1 | 0 |  |  |  |
| released | bit | 1 | 1 |  |  |  |
| exported_date | datetime | 8 | 1 |  |  |  |

