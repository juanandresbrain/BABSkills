# dbo.EMPLY_ORG_CHN_PSTN_A_HSTRY

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EMPLY_NUM | T_LONG_INTEGER | 4 | 0 | YES | YES |  |
| EFCTV_DATE | T_DATE | 8 | 0 |  |  |  |
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 | YES | YES |  |
| PSTN_CODE | nchar | 8 | 0 | YES | YES |  |
| EXPRTN_DATE | T_DATE | 8 | 1 |  |  |  |
| EMPLY_SHRT_NUM | T_INTEGER | 2 | 1 |  |  |  |
| ACNTBLTY | nvarchar | 8 | 1 |  |  |  |
| PRMRY_LOC_ID | T_ID | 16 | 1 |  |  |  |
| PRMRY_LOC_A | T_BOOLEAN | 5 | 0 |  |  |  |
| EMPLY_ORG_CHN_PSTN_A_HSTRY_ID | numeric | 9 | 0 | YES |  |  |
| PRMRY_DISP_FNCTN_NUM | T_LONG_INTEGER | 4 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

