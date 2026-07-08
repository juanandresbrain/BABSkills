# dbo.ADT_TRL_DTL

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ENTRY_ID | T_ID | 16 | 0 |  |  |  |
| SEQ_NUM | T_LONG_INTEGER | 4 | 0 | YES |  |  |
| TBL_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| TBL_KEY | T_DESCRIPTION | 255 | 0 |  |  |  |
| TBL_KEY_RSRC_NAME | T_LONG_DATA | 255 | 0 |  |  |  |
| TBL_KEY_RSRC_PRMS | T_DESCRIPTION | 255 | 0 |  |  |  |
| ACTN_CODE | T_SYSTEM_CODE | 4 | 0 |  |  |  |
| CLMN_NAME | T_AUDIT_TRAIL_COLUMNS | 512 | 1 |  |  |  |
| OLD_VAL | T_AUDIT_TRAIL_TEXT | 3000 | 1 |  |  |  |
| NEW_VAL | T_AUDIT_TRAIL_TEXT | 3000 | 1 |  |  |  |
