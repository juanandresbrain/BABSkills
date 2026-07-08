# dbo.IHcolumns

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| column_id | int | 4 | 0 | YES |  |  |
| publishercolumn_id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| article_id | int | 4 | 0 |  |  |  |
| column_ordinal | int | 4 | 0 |  |  |  |
| mapped_type | tinyint | 1 | 0 |  |  |  |
| mapped_length | bigint | 8 | 1 |  |  |  |
| mapped_prec | int | 4 | 1 |  |  |  |
| mapped_scale | int | 4 | 1 |  |  |  |
| mapped_nullable | bit | 1 | 1 |  |  |  |
