# dbo.imat_process_header

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_process_header_id | decimal | 9 | 0 | YES |  |  |
| process_no | nvarchar | 32 | 0 |  |  |  |
| process_desc | nvarchar | 240 | 1 |  |  |  |
| matching_process_used | tinyint | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| invoice_qty | smallint | 2 | 0 |  |  |  |
| invoice_qty_matched | smallint | 2 | 0 |  |  |  |
| start_date_time | smalldatetime | 4 | 1 |  |  |  |
| end_date_time | smalldatetime | 4 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| trace_processing | bit | 1 | 0 |  |  |  |
| gl_posting_date | smalldatetime | 4 | 1 |  |  |  |
| user_id | numeric | 9 | 1 |  |  |  |

