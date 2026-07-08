# dbo.TRNSCTN_EVNT

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TRNSCTN_TYPE_ID | int | 4 | 0 |  |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| RFRNC_NUM | smallint | 2 | 0 |  |  |  |
| RFRNC_NUM_DESC | varchar | 255 | 0 |  |  |  |
| RVRSL | tinyint | 1 | 0 |  |  |  |
| LAST_MDFD | datetime | 8 | 0 |  |  |  |
| ROW_ID | int | 4 | 0 | YES |  |  |
