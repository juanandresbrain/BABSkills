# dbo.import_vendor_tran_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_vendor_tran_set_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| edi_transaction_set_code | nvarchar | 20 | 0 |  |  |  |
| live_edi_version | nvarchar | 100 | 1 |  |  |  |
| test_edi_version | nvarchar | 100 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |

