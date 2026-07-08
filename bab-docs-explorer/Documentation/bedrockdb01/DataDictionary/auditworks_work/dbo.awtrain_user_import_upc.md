# dbo.awtrain_user_import_upc

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | char | 1 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| sku_id | numeric | 9 | 1 |  |  |  |
| pos_identifier | varchar | 20 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
