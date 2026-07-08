# dbo.ALRM

**Database:** foundation_event  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_ID | T_LONG_INTEGER | 4 | 0 | YES |  |  |
| ALRM_DTM | T_DATETIME | 8 | 0 |  |  |  |
| FRMTD_ALRM_TEXT | T_SHORT_TEXT | 4000 | 1 |  |  |  |
| ACKNWLDGMNT_DTM | T_DATETIME | 8 | 1 |  |  |  |
| ACKNWLDGMNT_USER_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
| EVNT_TYPE_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ALRM_DFNTN_ID | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ALRM_KEY | T_FORMATTING_INSTRUCTION | 2000 | 0 |  |  |  |
| EVNT_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
| EVNT_STSTC_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
| EVNT_STSTC_HSTRY_ID | T_LONG_INTEGER | 4 | 1 |  |  |  |
