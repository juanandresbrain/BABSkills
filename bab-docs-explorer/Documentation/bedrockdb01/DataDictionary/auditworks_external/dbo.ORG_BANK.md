# dbo.ORG_BANK

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BANK_ID | T_ID | 16 | 0 |  |  |  |
| BANK_NAME | nvarchar | 100 | 0 |  |  |  |
| BANK_SHRT_NAME | nvarchar | 50 | 0 |  |  |  |
| INSTN_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| GMT_OFST | T_QUANTITY_DECIMAL | 9 | 1 |  |  |  |
| DFLT_CRNCY_CODE | nchar | 6 | 1 |  |  |  |
| DFLT_ADRS_SEQ | T_SEQUENCE_NUMBER | 9 | 1 |  |  |  |
