# dbo.FNDTN_DSHBRD_DATA_VIEW_PRMPT

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DATA_VIEW_ID | T_ID | 16 | 0 | YES |  |  |
| SEQ_NUM | T_SMALL_INTEGER | 1 | 0 | YES |  |  |
| NAME_RES_NAME | nvarchar | 510 | 0 |  |  |  |
| DESC_RES_NAME | nvarchar | 510 | 1 |  |  |  |
| PRMPT_TYPE | T_CODE1 | 1 | 0 |  |  |  |
| PRMTR_TYPE_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
| DATA_TYPE_FULL_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| IS_RQRD | T_BOOLEAN | 5 | 0 |  |  |  |
| VLD_DSPL_VLS | nvarchar | 4000 | 1 |  |  |  |
| VLD_VLS | nvarchar | 4000 | 1 |  |  |  |

