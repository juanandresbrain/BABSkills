# dbo.NTFCTN_STS

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_ID | int | 4 | 0 |  |  |  |
| NTFCTN_SBSCRPTN_ID | int | 4 | 0 |  |  |  |
| ATMPT_CNT | tinyint | 1 | 0 |  |  |  |
| LAST_DTM | datetime | 8 | 0 |  |  |  |
| STS | tinyint | 1 | 0 |  |  |  |
| FRMTD_ALRM_TEXT | nvarchar | 8000 | 0 |  |  |  |
