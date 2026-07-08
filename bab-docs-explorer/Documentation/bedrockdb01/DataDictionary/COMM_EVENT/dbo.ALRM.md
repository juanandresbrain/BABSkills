# dbo.ALRM

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_ID | int | 4 | 0 | YES |  |  |
| ALRM_DTM | datetime | 8 | 0 |  |  |  |
| ACKNWLDGMNT_DTM | datetime | 8 | 1 |  |  |  |
| ACKNWLDGMNT_USER_ID | int | 4 | 1 |  |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| ALRM_DFNTN_ID | int | 4 | 0 |  |  |  |
| ALRM_KEY | nvarchar | 4000 | 0 |  |  |  |
| EVNT_ID | int | 4 | 1 |  |  |  |
| EVNT_STSTC_ID | int | 4 | 1 |  |  |  |
| EVNT_STSTC_HSTRY_ID | int | 4 | 1 |  |  |  |
