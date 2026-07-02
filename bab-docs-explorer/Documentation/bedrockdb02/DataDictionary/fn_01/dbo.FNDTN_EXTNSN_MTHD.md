# dbo.FNDTN_EXTNSN_MTHD

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MTHD_ID | T_ID | 16 | 0 | YES |  |  |
| APP_ID | int | 4 | 0 |  |  |  |
| PROD_ID | varchar | 30 | 0 |  |  |  |
| ON_BFR | bit | 1 | 0 |  |  |  |
| ON_AFTR | bit | 1 | 0 |  |  |  |
| ON_STEP | bit | 1 | 0 |  |  |  |
| CLS_NAME | varchar | 255 | 0 |  |  |  |
| MTHD_NAME | varchar | 255 | 0 |  |  |  |
| MTHD_DESC | varchar | 255 | 1 |  |  |  |

