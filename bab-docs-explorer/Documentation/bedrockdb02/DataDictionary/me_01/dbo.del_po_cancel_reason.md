# dbo.del_po_cancel_reason

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_cancellation_reason_id | decimal | 5 | 0 | YES |  |  |
| reason_code | nvarchar | 6 | 0 |  |  |  |
| description | nvarchar | 120 | 0 |  |  |  |
| responsibility_type | smallint | 2 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| deleted_date | smalldatetime | 4 | 0 |  |  |  |

