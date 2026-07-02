# dbo.FNDTN_SCRTY_NSB_USER_111414

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| USER_ID | numeric | 9 | 0 |  |  |  |
| USER_NAME | varchar | 50 | 0 |  |  |  |
| USER_FULL_NAME | varchar | 50 | 0 |  |  |  |
| USER_DESC | varchar | 255 | 1 |  |  |  |
| USER_PSWRD | varchar | 50 | 1 |  |  |  |
| USER_DMN | varchar | 255 | 1 |  |  |  |
| USER_LCKT | bit | 1 | 0 |  |  |  |
| USER_SID | varchar | 255 | 1 |  |  |  |
| USER_GUID | varchar | 255 | 1 |  |  |  |
| LGN_TYPE | int | 4 | 1 |  |  |  |
| CAN_ENCRYPT | bit | 1 | 1 |  |  |  |
| CAN_DCRYPT | bit | 1 | 1 |  |  |  |
| EXPRY_DATE | datetime | 8 | 1 |  |  |  |
| PRMPT_FRST_LGN | bit | 1 | 1 |  |  |  |
| MP_NVR_EXPR | bit | 1 | 1 |  |  |  |
| LAST_MP_RESET | datetime | 8 | 1 |  |  |  |
| CHNG_PSWRD | bit | 1 | 1 |  |  |  |
| DLTD | bit | 1 | 1 |  |  |  |
| USER_PSWRD_TYPE | T_SMALL_INTEGER | 1 | 0 |  |  |  |

