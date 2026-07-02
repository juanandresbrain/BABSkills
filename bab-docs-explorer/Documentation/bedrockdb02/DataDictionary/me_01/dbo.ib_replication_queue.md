# dbo.ib_replication_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_replication_queue_id | decimal | 9 | 0 | YES |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | nvarchar | 4 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| other_entity_id | decimal | 9 | 1 |  |  |  |
| primary_entity_key | nvarchar | 40 | 1 |  |  |  |
| secondary_entity_key | nvarchar | 40 | 1 |  |  |  |
| replication_data | nvarchar | 210 | 0 |  |  |  |
| posted_flag | bit | 1 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)

