# dbo.NTFCTN_SBSCRPTN

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| NTFCTN_SBSCRPTN_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ALRM_DFNTN_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| NTFCTN_TYPE | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| LOG_NTFCTN | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| ENBLD | T_SMALL_INTEGER | 1 | 0 |  |  |  |
| NTFCTN_DATA | T_FORMATTING_INSTRUCTION | 2000 | 1 |  |  |  |
| ALRM_TEXT | T_SHORT_TEXT | 4000 | 0 |  |  |  |
| LANG_ID | T_INTEGER | 2 | 0 |  |  |  |
