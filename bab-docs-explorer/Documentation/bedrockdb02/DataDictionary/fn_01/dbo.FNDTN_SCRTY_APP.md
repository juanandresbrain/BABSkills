# dbo.FNDTN_SCRTY_APP

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| APP_ID | smallint | 2 | 0 | YES |  |  |
| APP_NAME | varchar | 50 | 0 |  |  |  |
| APP_DESC | varchar | 255 | 1 |  |  |  |
| APP_HRCHY_LVL | tinyint | 1 | 0 |  |  |  |
| APP_LCNS | varchar | 255 | 1 |  |  |  |
| APP_USE_NSB_AUTH | bit | 1 | 0 |  |  |  |
| APP_CRT_SBS_ACT | bit | 1 | 0 |  |  |  |
| APP_ALW_MLTI_INSTNC | bit | 1 | 0 |  |  |  |
| APP_DSLW_L0_FULL_ACS | bit | 1 | 0 |  |  |  |
| ACTV | bit | 1 | 1 |  |  |  |
| APP_NAME_RSRC_NAME | varchar | 255 | 1 |  |  |  |

