# dbo.z_save_user_pref_01282011

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CNTXT_ID | varchar | 255 | 0 |  |  |  |
| USER_ID | int | 4 | 1 |  |  |  |
| GRP_LBL | varchar | 255 | 1 |  |  |  |
| PREF_DFNTN | text | 16 | 1 |  |  |  |
| UPDTD_DATE_TIME | datetime | 8 | 1 |  |  |  |
| UPDTD_BY | int | 4 | 1 |  |  |  |
| SSN_ID | T_ID | 16 | 1 |  |  |  |
