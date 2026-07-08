# dbo.FNDTN_SCRTY_APP_ATRBT

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| APP_ID | smallint | 2 | 0 |  |  |  |
| APP_ATRBT_ID | varchar | 10 | 0 |  |  |  |
| APP_ATRBT_NAME | varchar | 50 | 0 |  |  |  |
| APP_ATRBT_DESC | varchar | 255 | 1 |  |  |  |
| APP_ATRBT_MASK | varchar | 64 | 1 |  |  |  |
| APP_ATRBT_CLIP_TEXT | bit | 1 | 0 |  |  |  |
| APP_ATRBT_RQRD | bit | 1 | 0 |  |  |  |
| APP_ATRBT_ENCRPTD | bit | 1 | 0 |  |  |  |
