# dbo.template_header

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| template_id | tran_id_datatype | 9 | 0 | YES |  |  |
| template_description | nvarchar | 510 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| created_by | int | 4 | 1 |  |  |  |
| modified_by | int | 4 | 1 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_remark | nvarchar | 2000 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
