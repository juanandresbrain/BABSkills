# dbo.stock_status_adjustment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| stock_status_adjustment_id | decimal | 9 | 0 | YES |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| submit_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_ss_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_ss_adj_documents_$sp.md)

