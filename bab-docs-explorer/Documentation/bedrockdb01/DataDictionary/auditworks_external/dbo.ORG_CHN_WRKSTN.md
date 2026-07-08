# dbo.ORG_CHN_WRKSTN

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WRKSTN_ID | T_ID | 16 | 0 |  |  |  |
| WRKSTN_NUM | T_INTEGER | 2 | 0 |  |  |  |
| TRMNL_MDL_NUM | nvarchar | 100 | 1 |  |  |  |
| CMPTR_NAME | nvarchar | 126 | 1 |  |  |  |
| DRWR_CNT | T_INTEGER | 2 | 0 |  |  |  |
| MNFCTR_NAME | nvarchar | 100 | 1 |  |  |  |
| IP_ADRS | nvarchar | 40 | 1 |  |  |  |
| PLNG_IDNTFR | T_INTEGER | 2 | 1 |  |  |  |
| PLNG_LINE_NUM | nvarchar | 120 | 1 |  |  |  |
| TRNG_MODE | T_BOOLEAN | 5 | 0 |  |  |  |
| ACTBLTY_TYPE | nvarchar | 8 | 0 |  |  |  |
| BSNS_DAY_END_RNG_START_TIME | T_DATETIME | 8 | 1 |  |  |  |
| BSNS_DAY_END_RNG_END_TIME | T_DATETIME | 8 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| LOC_ID | T_ID | 16 | 0 |  |  |  |
| ORG_CHN_NUM | T_LONG_INTEGER | 4 | 0 |  |  |  |
| PRNT_WRKSTN_ID | T_ID | 16 | 1 |  |  |  |
| CMR_A | nvarchar | 510 | 1 |  |  |  |
| FDN_CSTMZTN_DATA | nvarchar | 4000 | 1 |  |  |  |
