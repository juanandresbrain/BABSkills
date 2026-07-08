# dbo.EMPLY_ORG_CHN_PSTN_A_HSTRY

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EMPLY_NUM | int | 4 | 0 |  |  |  |
| EFCTV_DATE | datetime | 8 | 0 |  |  |  |
| ORG_CHN_NUM | int | 4 | 0 |  |  |  |
| PSTN_CODE | char | 4 | 0 |  |  |  |
| EXPRTN_DATE | datetime | 8 | 1 |  |  |  |
| EMPLY_SHRT_NUM | smallint | 2 | 1 |  |  |  |
| ACNTBLTY | varchar | 4 | 1 |  |  |  |
| PRMRY_LOC_ID | binary | 16 | 1 |  |  |  |
| PRMRY_LOC_A | numeric | 5 | 0 |  |  |  |
| EMPLY_ORG_CHN_PSTN_A_HSTRY_ID | numeric | 9 | 0 | YES |  |  |
| PRMRY_DISP_FNCTN_NUM | int | 4 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
