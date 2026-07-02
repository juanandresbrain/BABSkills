# dbo.tmpDistroTestStage

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sourceid | varchar | 20 | 0 |  |  |  |
| destid | varchar | 20 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| rec_type | varchar | 6 | 1 |  |  |  |
| sequencenbr | bigint | 8 | 0 |  |  |  |
| distribution_number | varchar | 20 | 0 |  |  |  |
| ref_field_1 | int | 4 | 0 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| active_pick_flag | varchar | 1 | 0 |  |  |  |
| released | int | 4 | 0 |  |  |  |
| exported_date | datetime | 8 | 0 |  |  |  |

