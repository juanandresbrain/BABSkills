# dbo.reservation

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reservation_id | decimal | 9 | 0 | YES |  |  |
| transaction_type | smallint | 2 | 0 |  |  |  |
| document_type | smallint | 2 | 0 |  |  |  |
| number | nvarchar | 128 | 1 |  |  |  |
| customer_order_number | nvarchar | 128 | 1 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| action_date_utc | datetime | 8 | 0 |  |  |  |
| action_date | datetime | 8 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.update_reservation_details_$sp](../../StoredProcedures/me_01/dbo.update_reservation_details_$sp.md)

