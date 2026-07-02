# dbo.EMPLY_ORG_CHN_PSTN_A

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EMPLY_NUM | T_LONG_INTEGER | 4 | 0 | YES | YES |  |
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 | YES | YES |  |
| PSTN_CODE | nchar | 8 | 0 | YES | YES |  |
| EFCTV_DATE | T_DATE | 8 | 0 |  |  |  |
| EXPRTN_DATE | T_DATE | 8 | 1 |  |  |  |
| EMPLY_SHRT_NUM | T_INTEGER | 2 | 1 |  |  |  |
| ACNTBLTY | nvarchar | 8 | 1 |  |  |  |
| PRMRY_LOC_ID | T_ID | 16 | 1 |  | YES |  |
| WORK_TLPHN_NUM | nvarchar | 120 | 1 |  |  |  |
| WORK_FAX_NUM | nvarchar | 120 | 1 |  |  |  |
| WORK_MBL_NUM | nvarchar | 120 | 1 |  |  |  |
| WORK_EML_ADRS | nvarchar | 100 | 1 |  |  |  |
| PRMRY_LOC_A | T_BOOLEAN | 5 | 0 |  |  |  |
| EMPLY_ORG_CHN_PSTN_A_ID | numeric | 9 | 0 | YES |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |

