# dbo.CRDM_PRMTRS_DPNDNCY

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PRMTR_NAME | nvarchar | 60 | 0 |  |  |  |
| PRMTR_VAL | nvarchar | 510 | 0 |  |  |  |
| DPNDNT_PRMTR_NAME | nvarchar | 60 | 0 |  |  |  |
| DPNDNT_PRMTR_DRP_DWN_QRY | nvarchar | 4000 | 1 |  |  |  |
