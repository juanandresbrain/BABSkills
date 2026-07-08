# dbo.customer_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| customer_role | smallint | 2 | 0 |  |  |  |
| customer_info_type | smallint | 2 | 0 |  |  |  |
| customer_info | nvarchar | 6000 | 0 |  |  |  |
