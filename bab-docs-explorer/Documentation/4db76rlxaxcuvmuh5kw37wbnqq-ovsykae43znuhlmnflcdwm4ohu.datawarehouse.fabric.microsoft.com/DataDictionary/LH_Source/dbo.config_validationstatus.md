# dbo.config_validationstatus

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BatchID | int | 4 | 1 |  |  |  |
| SourceTableName | varchar | 8000 | 1 |  |  |  |
| TargetTableName | varchar | 8000 | 1 |  |  |  |
| PrimaryKeyList | varchar | 8000 | 1 |  |  |  |
| SourceRowCount | int | 4 | 1 |  |  |  |
| TargetRowCount | int | 4 | 1 |  |  |  |
| ExtraKeysCount | int | 4 | 1 |  |  |  |
| MissingKeysCount | int | 4 | 1 |  |  |  |
| ColumnWiseMisMatchesCount | int | 4 | 1 |  |  |  |
| DataTypeMismatches | int | 4 | 1 |  |  |  |
| SourceDuplicateRecords | int | 4 | 1 |  |  |  |
| TgtDuplicateRecords | int | 4 | 1 |  |  |  |
