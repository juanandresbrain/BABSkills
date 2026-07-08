# dbo.ORG_CHN_WRKSTN_CNFG

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WRKSTN_CNFG_CODE | nchar | 8 | 0 |  |  |  |
| WRKSTN_CNFG_DESC | nvarchar | 510 | 0 |  |  |  |
| WRKSTN_CNFG_SHRT_DESC | nvarchar | 100 | 0 |  |  |  |
| TRAN_TRNSLT_VRSN_NUM | T_INTEGER | 2 | 1 |  |  |  |
| PLNG_FILE_NAME | nvarchar | 1020 | 1 |  |  |  |
| ACTV | T_BOOLEAN | 5 | 0 |  |  |  |
| RPRT_UNSD_WRKSTNS | T_FLAG | 5 | 1 |  |  |  |
