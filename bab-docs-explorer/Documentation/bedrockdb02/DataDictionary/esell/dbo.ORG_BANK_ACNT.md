# dbo.ORG_BANK_ACNT

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BANK_ACNT_ID | T_INTEGER | 2 | 0 | YES |  |  |
| BANK_BRNCH_ID | T_ID | 16 | 0 |  | YES |  |
| BANK_ID | T_ID | 16 | 0 |  | YES |  |
| BANK_ACNT_NUM | nvarchar | 50 | 0 |  |  |  |
| BANK_ACNT_DESC | nvarchar | 510 | 0 |  |  |  |
| GL_RFRNC_NUM | nvarchar | 50 | 1 |  |  |  |
| CRNCY_CODE | nchar | 6 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| SYS_CODE | nvarchar | 8 | 0 |  |  |  |

