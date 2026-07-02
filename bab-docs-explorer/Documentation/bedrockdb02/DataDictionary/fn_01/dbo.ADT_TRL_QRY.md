# dbo.ADT_TRL_QRY

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ENTRY_ID | T_ID | 16 | 0 | YES | YES |  |
| SEQ_NUM | T_LONG_INTEGER | 4 | 0 | YES |  |  |
| QRY_KEY_NUM | T_LONG_INTEGER | 4 | 0 |  | YES |  |
| KEY_PART_VAL_1 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_2 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_3 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_4 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_5 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_6 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_7 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_8 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_9 | T_DESCRIPTION | 255 | 1 |  |  |  |
| KEY_PART_VAL_10 | T_DESCRIPTION | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [esell: dbo.mass_create_store_location_$sp](../../StoredProcedures/esell/dbo.mass_create_store_location_$sp.md)

