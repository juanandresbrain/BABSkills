# dbo.GEOG_ADRS

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ADRS_ID | T_ID | 16 | 0 | YES |  |  |
| ADRS_LINE_1 | nvarchar | 100 | 1 |  |  |  |
| ADRS_LINE_2 | nvarchar | 100 | 1 |  |  |  |
| ADRS_LINE_3 | nvarchar | 100 | 1 |  |  |  |
| ADRS_LINE_4 | nvarchar | 100 | 1 |  |  |  |
| CITY | nvarchar | 100 | 1 |  |  |  |
| POST_CODE | nvarchar | 30 | 1 |  |  |  |
| ADRS_MTCH_KEY | nvarchar | 100 | 1 |  |  |  |
| CNTRY_CODE_ISO3 | nchar | 6 | 0 |  |  |  |
| TRTRY_CODE | nchar | 6 | 1 |  |  |  |
| ADRS_RULE_ID | T_ID | 16 | 1 |  |  |  |

