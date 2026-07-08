# dbo.NTFCTN_SBSCRPTN

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| NTFCTN_SBSCRPTN_ID | int | 4 | 0 |  |  |  |
| ALRM_DFNTN_ID | int | 4 | 0 |  |  |  |
| NTFCTN_TYPE | tinyint | 1 | 0 |  |  |  |
| LOG_NTFCTN | tinyint | 1 | 0 |  |  |  |
| ENBLD | tinyint | 1 | 0 |  |  |  |
| NTFCTN_DATA | nvarchar | 4000 | 1 |  |  |  |
| ALRM_TEXT | nvarchar | 8000 | 0 |  |  |  |
| LANG_ID | smallint | 2 | 0 |  |  |  |
