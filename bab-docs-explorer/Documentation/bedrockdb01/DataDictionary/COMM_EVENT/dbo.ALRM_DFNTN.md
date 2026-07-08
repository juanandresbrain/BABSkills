# dbo.ALRM_DFNTN

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ALRM_DFNTN_ID | int | 4 | 0 |  |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| SVRTY | tinyint | 1 | 0 |  |  |  |
| ENBLD | decimal | 5 | 0 |  |  |  |
| TRGR_TYPE | tinyint | 1 | 0 |  |  |  |
| TEST_FRQNCY_MNT | smallint | 2 | 1 |  |  |  |
| TEST_BCKT_LVL | tinyint | 1 | 0 |  |  |  |
| NUM_DAYS_KEEP_ALRM | smallint | 2 | 0 |  |  |  |
| ALRM_QNTY | smallint | 2 | 0 |  |  |  |
| ALRM_DRTN | smallint | 2 | 0 |  |  |  |
| ALRM_QRY | nvarchar | 2000 | 0 |  |  |  |
| LAST_MDFD_DTM | datetime | 8 | 0 |  |  |  |
| LAST_EVNT_ID | int | 4 | 1 |  |  |  |
| LAST_ALRM_DTM | datetime | 8 | 1 |  |  |  |
