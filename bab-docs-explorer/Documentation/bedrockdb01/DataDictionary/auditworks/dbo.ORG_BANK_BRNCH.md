# dbo.ORG_BANK_BRNCH

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BANK_BRNCH_ID | T_ID | 16 | 0 |  |  |  |
| BANK_ID | T_ID | 16 | 0 |  |  |  |
| BANK_BRNCH_NUM | nchar | 12 | 0 |  |  |  |
| BANK_BRNCH_NAME | nvarchar | 100 | 0 |  |  |  |
| BANK_BRNCH_SHRT_NAME | nvarchar | 50 | 0 |  |  |  |
| GMT_OFST | T_CONVERSION_FACTOR | 9 | 1 |  |  |  |
| DFLT_CRNCY_CODE | nchar | 6 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
