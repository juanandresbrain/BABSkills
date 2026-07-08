# dbo.IHpublishercolumns

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publishercolumn_id | int | 4 | 0 | YES |  |  |
| table_id | int | 4 | 0 |  |  |  |
| publisher_id | smallint | 2 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| column_ordinal | int | 4 | 0 |  |  |  |
| type | varchar | 255 | 0 |  |  |  |
| length | bigint | 8 | 0 |  |  |  |
| prec | int | 4 | 1 |  |  |  |
| scale | int | 4 | 1 |  |  |  |
| isnullable | bit | 1 | 0 |  |  |  |
| iscaptured | bit | 1 | 0 |  |  |  |
