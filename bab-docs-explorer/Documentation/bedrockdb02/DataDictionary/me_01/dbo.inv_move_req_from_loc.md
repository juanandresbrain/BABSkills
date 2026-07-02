# dbo.inv_move_req_from_loc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inv_move_req_from_loc_id | decimal | 9 | 0 | YES |  |  |
| inventory_move_request_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| print_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)

