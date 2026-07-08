# dbo.EVNT_500223

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EVNT_ID | int | 4 | 0 | YES |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| SRVR_NAME | nvarchar | 100 | 0 |  |  |  |
| APP_ID | decimal | 9 | 0 |  |  |  |
| PRDCT_ID | nvarchar | 60 | 0 |  |  |  |
| INSTNC_NUM | smallint | 2 | 0 |  |  |  |
| USER_ID | decimal | 9 | 0 |  |  |  |
| EVNT_POST_DTM | datetime | 8 | 0 |  |  |  |
| EVNT_CRTN_DTM | datetime | 8 | 0 |  |  |  |
| STRG_MCHNSM | nvarchar | 60 | 0 |  |  |  |
| FLD_821 | smallint | 2 | 1 |  |  |  |
| FLD_1 | smallint | 2 | 1 |  |  |  |
| FLD_2 | smallint | 2 | 1 |  |  |  |
| FLD_3 | smallint | 2 | 1 |  |  |  |
| FLD_824 | smallint | 2 | 1 |  |  |  |
| FLD_825 | nvarchar | 128 | 1 |  |  |  |
| FLD_826 | nvarchar | 256 | 1 |  |  |  |
| FLD_822 | nvarchar | 64 | 1 |  |  |  |
| FLD_823 | nvarchar | 1024 | 1 |  |  |  |
