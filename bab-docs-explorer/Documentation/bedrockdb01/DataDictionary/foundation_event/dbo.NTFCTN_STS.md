# dbo.NTFCTN_STS

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| NTFCTN_SBSCRPTN_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ATMPT_CNT | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| LAST_DTM | T_DATETIME | 8 | 0 |  |  |  |
| STS | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| FRMTD_ALRM_TEXT | T_SHORT_TEXT | 4000 | 0 |  |  |  |
