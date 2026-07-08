# dbo.FNDTN_DSHBRD_NTFCTN

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| NTFCTN_ID | int | 4 | 0 | YES |  |  |
| SCHDL_OTPT_ID | binary | 16 | 0 |  |  |  |
| DATA_VIEW_INSTNC_ID | binary | 16 | 0 |  |  |  |
| DSHBRD_OTPT_ID | binary | 16 | 1 |  |  |  |
| CRTD_DATE_TIME | datetime | 8 | 0 |  |  |  |
| NTFCTN_TEXT | nvarchar | 100 | 0 |  |  |  |
| MSG_TEXT | nvarchar | 8000 | 1 |  |  |  |
