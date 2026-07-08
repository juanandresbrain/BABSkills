# dbo.CRDM_PRMTRS

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRMTR_NAME | nvarchar | 60 | 0 |  |  |  |
| PRMTR_DESC | nvarchar | 150 | 0 |  |  |  |
| PRMTR_CMNT | nvarchar | 510 | 1 |  |  |  |
| PRMTR_DATA_TYPE | nchar | 12 | 1 |  |  |  |
| PRMTR_VAL | nvarchar | 510 | 1 |  |  |  |
| PRMTR_VAL_BIN | T_ID | 16 | 1 |  |  |  |
| PRMTR_GRP_CODE | nvarchar | 40 | 1 |  |  |  |
| PRMTR_VAL_FRM_RNG | nvarchar | 100 | 1 |  |  |  |
| PRMTR_VAL_TO_RNG | nvarchar | 100 | 1 |  |  |  |
| DRP_DWN_QRY | nvarchar | 4000 | 1 |  |  |  |
| SEQ_NUM | smallint | 2 | 1 |  |  |  |
