# dbo.FNDTN_DSHBRD_NTFCTN

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| NTFCTN_ID | int | 4 | 0 | YES |  |  |
| SCHDL_OTPT_ID | binary | 16 | 0 |  | YES |  |
| DATA_VIEW_INSTNC_ID | binary | 16 | 0 |  | YES |  |
| DSHBRD_OTPT_ID | binary | 16 | 1 |  | YES |  |
| CRTD_DATE_TIME | datetime | 8 | 0 |  |  |  |
| NTFCTN_TEXT | nvarchar | 100 | 0 |  |  |  |
| MSG_TEXT | nvarchar | 8000 | 1 |  |  |  |

