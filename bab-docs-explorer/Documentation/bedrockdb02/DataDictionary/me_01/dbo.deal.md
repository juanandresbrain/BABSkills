# dbo.deal

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| deal_id | int | 4 | 0 | YES |  |  |
| deal_no | nvarchar | 40 | 0 |  |  |  |
| name | nvarchar | 100 | 1 |  |  |  |
| description | nvarchar | 500 | 1 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_to_date | smalldatetime | 4 | 0 |  |  |  |
| register_status | nvarchar | 8 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| status_date | smalldatetime | 4 | 0 |  |  |  |
| issue_date | smalldatetime | 4 | 0 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| location_grouping | smallint | 2 | 0 |  |  |  |
| requires_cancel_send_flag | bit | 1 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| promotional_event_flag | bit | 1 | 0 |  |  |  |
| approval_status | smallint | 2 | 0 |  |  |  |
| submitted_by_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_location_to_deals_$sp](../../StoredProcedures/me_01/dbo.copy_location_to_deals_$sp.md)

